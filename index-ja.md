---
title: VJU プロジェクト文書
lang: ja
layout: page
permalink: /ja/
nav_exclude: false
nav_title: Japanese
---

<style>
  .language-switcher {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.45rem 0.75rem;
    border-radius: 999px;
    background: linear-gradient(135deg, #eef4ff 0%, #ffffff 100%);
    box-shadow: inset 0 0 0 1px rgba(11, 77, 145, 0.12);
    margin: 0 0 1.5rem;
    font-size: 0.95rem;
  }

  .language-switcher span {
    font-weight: 600;
    color: #2d3e52;
  }

  .language-switcher a,
  .language-switcher strong {
    padding: 0.3rem 0.85rem;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 600;
  }

  .language-switcher a {
    color: #0b4d91;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(11, 77, 145, 0.15);
    transition: background 0.15s ease, color 0.15s ease, box-shadow 0.15s ease;
  }

  .language-switcher a:hover,
  .language-switcher a:focus-visible {
    background: #0b4d91;
    color: #ffffff;
    box-shadow: 0 4px 10px rgba(11, 77, 145, 0.2);
  }

  .language-switcher strong {
    color: #ffffff;
    background: #0b4d91;
  }

  details.collection-toggle {
    margin-top: 1.1rem;
    border-radius: 12px;
    border: 1px solid rgba(11, 77, 145, 0.12);
    background: #f7fbff;
    padding: 0.75rem 1rem;
  }

  details.collection-toggle summary {
    cursor: pointer;
    font-weight: 600;
    color: #0b4d91;
    list-style: none;
  }

  details.collection-toggle summary::-webkit-details-marker {
    display: none;
  }

  details.collection-toggle[open] {
    box-shadow: 0 8px 20px rgba(11, 77, 145, 0.12);
  }

  .collection-toggle__body {
    margin-top: 0.7rem;
  }

  .collection-toggle__body .document-list {
    margin: 0;
    padding-left: 1.1rem;
  }

  .collection-toggle__body .document-list li {
    margin-bottom: 0.4rem;
  }
</style>

<div class="language-switcher" role="navigation" aria-label="言語切替">
  <span>Language</span>
  <a href="{{ '/' | relative_url }}">EN</a>
  <a href="{{ '/vi/' | relative_url }}">VI</a>
  <strong>JA</strong>
</div>

# VJU プロジェクト文書

VNU – Vietnam-Japan University 関連の日本語資料にアクセスできます。英語版やベトナム語版を閲覧する場合は、上部の切替リンクを利用してください。

## 品質保証

{% assign qa_docs_ja = site.data.quality_assurance_ja %}
{% for doc in qa_docs_ja %}
- [{{ doc.id }} — {{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}

## 大学規程

{% assign regulations_ja = site.data.university_regulations_ja %}
<details class="collection-toggle" open>
  <summary>大学規程 ({{ regulations_ja | size }})</summary>
  <div class="collection-toggle__body">
    <ul class="document-list">
    {% for doc in regulations_ja %}
      <li><a href="{{ doc.url | relative_url }}">{{ doc.id }} — {{ doc.title }}</a></li>
    {% endfor %}
    </ul>
  </div>
</details>

## 公開レポート 2025

{% assign reports_ja = site.data.public_report_2025_ja %}
{% for doc in reports_ja %}
- [{{ doc.id }} — {{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}

## ガイドライン

- [GWS と Gemini 利用ガイド]({{ '/Guide/GWS and Gemini Usage Guide - Japanese.html' | relative_url }})
- [Professional Manner and Workstyle ガイド]({{ '/Guide/Professional Manner and Workstyle - Japanese.html' | relative_url }})
- [Google Meet ガイド]({{ '/Guide/Google Meet/Google Meet Guide - Japanese.html' | relative_url }})
