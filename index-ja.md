---
title: VJU プロジェクト文書（日本語）
lang: ja
layout: page
permalink: /ja/
---

<style>
  .language-switcher {
    display: inline-flex;
    gap: 0.75rem;
    align-items: center;
    padding: 0.4rem 0.75rem;
    margin: 0 0 1.5rem;
    border-radius: 999px;
    background: #f2f5fb;
    font-size: 0.95rem;
  }

  .language-switcher strong {
    color: #0b4d91;
  }

  .hero {
    padding: 1.5rem 1.8rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #eff5ff 0%, #ffffff 55%, #f8fbff 100%);
    box-shadow: inset 0 0 0 1px rgba(11, 77, 145, 0.06);
    margin-bottom: 2rem;
  }

  .hero h1 {
    margin-top: 0;
    font-size: 1.9rem;
  }

  .collection-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.25rem;
    margin-bottom: 2rem;
  }

  .collection-card {
    border-radius: 12px;
    padding: 1.2rem 1.35rem;
    background: #ffffff;
    box-shadow: 0 8px 18px rgba(15, 43, 80, 0.08);
    border: 1px solid rgba(11, 77, 145, 0.08);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }

  .collection-card:hover,
  .collection-card:focus-within {
    transform: translateY(-2px);
    box-shadow: 0 12px 22px rgba(15, 43, 80, 0.12);
  }

  .collection-card h2 {
    margin-top: 0;
    margin-bottom: 0.4rem;
    font-size: 1.25rem;
  }

  .collection-card p {
    margin: 0 0 0.75rem;
    color: #44546a;
    font-size: 0.95rem;
  }

  .collection-card ul {
    margin: 0;
    padding-left: 1.1rem;
    font-size: 0.95rem;
  }

  .supporting-info {
    padding: 1.2rem 1.4rem;
    border-left: 4px solid #0b4d91;
    background: #f7fbff;
    color: #2d3e52;
    margin-top: 2.5rem;
  }

  @media (max-width: 600px) {
    .hero {
      padding: 1.1rem 1.2rem;
    }

    .hero h1 {
      font-size: 1.6rem;
    }

    .collection-card {
      padding: 1rem 1.1rem;
    }
  }
</style>

<div class="language-switcher" role="navigation" aria-label="言語切替">
  <span>言語:</span>
  <a href="/">EN</a>
  <strong>JA</strong>
  <a href="/vi/">VI</a>
</div>

<section class="hero">
  <h1>VJU プロジェクト文書（日本語）</h1>
  <p>
    <strong>日越大学（VNU – Vietnam-Japan University）</strong> に関する規程・通達・運用ガイドを日本語で確認できます。上部の言語切替から英語版・ベトナム語版にも移動できます。
  </p>
  <p>
    以下のコレクションリンクは日本語訳のページへ直接遷移します。原文確認が必要な場合は、各文書の冒頭に掲載したメタデータを参照してください。
  </p>
</section>

<div class="collection-grid">
  <article class="collection-card">
    <h2>品質保証</h2>
    <p>教育質保証や認証制度に関する通達・決定・運用指針。</p>
    <ul>
      <li><a href="./Quality%20Assurance/Japanese/index.md">文書一覧（日本語）</a></li>
    </ul>
  </article>

  <article class="collection-card">
    <h2>大学規程</h2>
    <p>学内規程、通知、業務指針など日越大学の運営に関わる文書。</p>
    <ul>
      <li><a href="./University%20Regulations/Japanese/index.md">文書一覧（日本語）</a></li>
    </ul>
  </article>

  <article class="collection-card">
    <h2>公開レポート 2025</h2>
    <p>2024–2025年度の予算関連資料や公開報告書。</p>
    <ul>
      <li><a href="./Public%20Report%202025/Japanese/index.md">文書一覧（日本語）</a></li>
    </ul>
  </article>

  <article class="collection-card">
    <h2>ガイド類</h2>
    <p>運用マニュアル、講義資料、IT サービス利用ガイドなど。</p>
    <ul>
      <li><a href="./Guide/">共通ガイド（日本語）</a></li>
    </ul>
  </article>
</div>

<aside class="supporting-info">
  <h3>ご利用のヒント</h3>
  <ul>
    <li>英語版を基準として翻訳しているため、重要語句の原語表記を併記しています。</li>
    <li>文書の同一性は front matter の <code>id</code> で管理しています。英語・ベトナム語版との対照に活用してください。</li>
    <li>誤訳の指摘や更新依頼は、本リポジトリの Issue もしくは Pull Request で受け付けています。</li>
  </ul>
</aside>
