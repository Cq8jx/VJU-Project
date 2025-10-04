# Naming analysis for DHVN-Report-826 (2024-2025)

## Observed file set

| Artifact | Current file name |
| --- | --- |
| Original PDF | `DHVN-Report-826 Public Report for the 2024-2025 School Year.pdf` |
| English transcription | `DHVN-Report-826 Public Report for the 2024-2025 School Year.md` |
| Japanese transcription | `DHVN-Report-826 2024-2025年度の公開レポート.md` |
| Vietnamese transcription | `ĐHVN-Report-826 Public Report 2024-2025 Vietnamese.md` |

## Document titles quoted in the transcriptions

All three text transcriptions reproduce the first heading from the source document as a translation of **"Public report"**:

- English version: `### PUBLIC REPORT FOR THE 2024-2025 SCHOOL YEAR`
- Japanese version: `### 2024-2025年度の公開レポート`
- Vietnamese version: `### BÁO CÁO BA CÔNG KHAI NĂM HỌC 2024-2025`

The Vietnamese heading corresponds directly to the phrase *"Báo cáo ba công khai"* in the PDF download that is published under the "Điều kiện đảm bảo chất lượng" ("Quality assurance conditions") section on https://vju.vnu.edu.vn/dam-bao-chat-luong/thuc-hien-cong-khai-doi-voi-csgd-dai-hoc/dieu-kien-dam-bao-chat-luong/.

## Root cause of the naming mismatch

The PDF file was stored with a descriptive name derived from the website section (`Quality Assurance Conditions 2024-2025`), while the Markdown transcriptions were named after the actual document title that appears inside the PDF (`Public Report for the 2024-2025 School Year`). Because the website category and the document title differ, copying the section label into the PDF filename caused the inconsistency with the English Markdown filename, which is based on the document's internal heading. Aligning the suffix of the filenames with the source document title resolves the inconsistency; consequently the PDF has been renamed to `DHVN-Report-826 Public Report for the 2024-2025 School Year.pdf`.
