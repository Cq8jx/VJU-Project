#!/bin/bash
set -euo pipefail

INPUT_DIR="./pdf-to-md"
OUTPUT_DIR="./pdf-to-md-md"
DEFAULT_INPUT_USED=false
CHUNK_SIZE=${PDF2MD_CHUNK_SIZE:-20}
MAX_RETRY=${PDF2MD_MAX_RETRY:-3}
RETRY_DELAY=${PDF2MD_RETRY_DELAY:-5}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "必要なコマンド '$1' が見つかりません。インストールしてから再実行してください。" >&2
    exit 1
  fi
}

require_command gemini

PDFINFO_AVAILABLE=true
if ! command -v pdfinfo >/dev/null 2>&1; then
  PDFINFO_AVAILABLE=false
  echo "警告: pdfinfo が見つかりません。ページ数を取得できないため PDF を分割できません。" >&2
fi

GS_AVAILABLE=true
if ! command -v gs >/dev/null 2>&1; then
  GS_AVAILABLE=false
  echo "警告: Ghostscript (gs) が見つかりません。PDF の分割が行えないため、ファイル単位で処理します。" >&2
fi

if [[ ! -d "$INPUT_DIR" ]]; then
  if compgen -G "*.pdf" > /dev/null; then
    INPUT_DIR="."
    DEFAULT_INPUT_USED=true
  else
    mkdir -p "$INPUT_DIR"
    echo "PDF を処理するには $INPUT_DIR に配置してください。" >&2
    exit 1
  fi
fi

mkdir -p "$OUTPUT_DIR"

# nullglob により一致しない場合は空配列とする
shopt -s nullglob
pdf_files=("$INPUT_DIR"/*.pdf)
shopt -u nullglob

if (( ${#pdf_files[@]} == 0 )); then
  if [[ "$DEFAULT_INPUT_USED" == "true" ]]; then
    echo "現在のディレクトリに PDF ファイルがありません。" >&2
  else
    echo "$INPUT_DIR 内に PDF ファイルが見つかりません。" >&2
  fi
  exit 0
fi

PROMPT_TEXT="$(cat <<'EOF'
アップロードされた資料をmarkdownにしてください。要約や翻訳などはせずに元の内容全文、元の言語のままで、一括でダウンロードできるようにしてください。

* アップロード済みの PDF ファイルを直接読み取り、ローカルでコマンドを実行しようとしないでください。
* Markdown を編集した場合は、報告前にテーブル列数と列揃えを確認し、表やリストが崩れていないかレンダリングを点検する。
* Markdown 内の用語は正式名称表（https://docs.google.com/spreadsheets/d/1kfRklEPr2MbZJeKY8Me0lTO68-8G4EtZlviktDpR1pA/edit?gid=962055076#gid=962055076）で照合し、表記揺れを防ぐ。
* 変換プロセスに関する説明や注意書き、確認メッセージなどは出力せず、PDF 本文のみを Markdown で返してください。
* 最初の行から本文を出力し、挨拶や了解・承知などの応答文は含めないでください。
EOF
)"

declare -a TEMP_DIRS=()
cleanup() {
  local dir
  for dir in "${TEMP_DIRS[@]}"; do
    [[ -d "$dir" ]] && rm -rf "$dir"
  done
}
trap cleanup EXIT

process_chunk() {
  local chunk_pdf="$1" chunk_output="$2" chunk_prompt="$3" start_page="$4" end_page="$5"
  local attachment retries status first_line size

  attachment="@$(basename "$chunk_pdf")"
  retries=0
  status=1

  while (( retries < MAX_RETRY )); do
    if gemini "$chunk_prompt" "$attachment" > "$chunk_output"; then
      first_line=$(grep -m1 -v '^[[:space:]]*$' "$chunk_output" || true)
      size=$(wc -c < "$chunk_output")

      if grep -q "Error when talking to Gemini API" "$chunk_output"; then
        echo "gemini API がエラーを返しました: $(basename "$chunk_pdf")" >&2
        cat "$chunk_output" >&2
        status=1
      elif grep -q "Error executing tool" "$chunk_output"; then
        echo "gemini の実行中にツール呼び出しエラーが発生しました: $(basename "$chunk_pdf")" >&2
        status=1
      elif [[ -z "$first_line" ]]; then
        echo "出力が空でした。" >&2
        status=1
      elif [[ "$first_line" =~ ^(了解しました|了解です|承知いたしました|承知しました) ]]; then
        echo "本文ではなく応答文が返されました。再試行します。" >&2
        status=1
      elif grep -Eq '了解しました|承知いたしました|用語集|Googleスプレッドシート|変換します' "$chunk_output"; then
        echo "本文以外の説明が含まれていました。再試行します。" >&2
        status=1
      else
        if (( size < 500 )) && (( end_page == 0 || end_page - start_page >= 1 )); then
          echo "警告: 生成結果が想定より短い可能性があります (${chunk_output})。" >&2
        fi
        status=0
        break
      fi
    else
      status=$?
    fi

    (( retries++ ))
    if (( retries < MAX_RETRY )); then
      echo "再試行します (${retries}/${MAX_RETRY})..." >&2
      sleep "$RETRY_DELAY"
    fi
  done

  return "$status"
}

for file in "${pdf_files[@]}"; do
  filename="$(basename "$file" .pdf)"
  output_path="$OUTPUT_DIR/$filename.md"
  echo "Converting $file → $output_path"

  temp_dir="$(mktemp -d "${TMPDIR:-/tmp}/pdf2md.XXXXXX")"
  TEMP_DIRS+=("$temp_dir")
  temp_output="$temp_dir/output.md"
  : > "$temp_output"

  page_count=0
  if [[ "$PDFINFO_AVAILABLE" == "true" ]]; then
    page_count=$(pdfinfo "$file" 2>/dev/null | awk '/^Pages:/ {print $2}') || page_count=0
  fi

  if ! [[ "$page_count" =~ ^[0-9]+$ ]]; then
    page_count=0
  fi

  chunk_index=0
  start_page=1

  if (( page_count == 0 )) || [[ "$GS_AVAILABLE" != "true" ]]; then
    chunk_index=$((chunk_index + 1))
    chunk_label=$(printf "%03d" "$chunk_index")
    chunk_pdf="$temp_dir/${filename}_chunk_${chunk_label}.pdf"
    cp "$file" "$chunk_pdf"

    chunk_prompt="$PROMPT_TEXT\n\n対象 PDF 全体を処理してください。手順の説明は出力しないでください。"
    chunk_output="$temp_dir/${filename}_chunk_${chunk_label}.md"

    if ! process_chunk "$chunk_pdf" "$chunk_output" "$chunk_prompt" 0 0; then
      echo "chunk ${chunk_label} の処理に失敗しました。" >&2
      exit 1
    fi

    cat "$chunk_output" >> "$temp_output"
    rm -f "$chunk_output"
  else
    while (( start_page <= page_count )); do
      chunk_index=$((chunk_index + 1))
      end_page=$((start_page + CHUNK_SIZE - 1))
      if (( end_page > page_count )); then
        end_page=$page_count
      fi

      chunk_label=$(printf "%03d" "$chunk_index")
      chunk_pdf="$temp_dir/${filename}_chunk_${chunk_label}.pdf"

      if ! gs -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -dFirstPage="$start_page" -dLastPage="$end_page" -sOutputFile="$chunk_pdf" "$file" >/dev/null 2>&1; then
        echo "Ghostscript による PDF 分割に失敗しました: $file (pages $start_page-$end_page)" >&2
        exit 1
      fi

      chunk_prompt="$PROMPT_TEXT\n\n対象ページ: ${start_page}〜${end_page} ページのみをその順番で Markdown 化してください。前後のページの内容は記述しないでください。"
      chunk_output="$temp_dir/${filename}_chunk_${chunk_label}.md"

      if ! process_chunk "$chunk_pdf" "$chunk_output" "$chunk_prompt" "$start_page" "$end_page"; then
        echo "chunk ${chunk_label} (pages ${start_page}-${end_page}) の処理に失敗しました。" >&2
        exit 1
      fi

      if [[ -s "$temp_output" ]]; then
        printf '\n\n' >> "$temp_output"
      fi
      cat "$chunk_output" >> "$temp_output"
      rm -f "$chunk_output"

      echo "  chunk ${chunk_label}: pages ${start_page}-${end_page}" >&2
      start_page=$((end_page + 1))
    done
  fi

  mv "$temp_output" "$output_path"
done
