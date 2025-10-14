---
title: Related Documents
lang: en
layout: page
permalink: /
nav_exclude: false
nav_title: English
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

<div class="language-switcher" role="navigation" aria-label="Language switcher">
  <span>Language</span>
  <strong>EN</strong>
  <a href="{{ '/vi/' | relative_url }}">VI</a>
  <a href="{{ '/ja/' | relative_url }}">JA</a>
</div>

# Related Documents

This site centralizes related documents for VNU – Vietnam-Japan University. English is the default language; use the links above to switch to Vietnamese or Japanese indexes.

## Quality Assurance

{% assign qa_docs = site.data.quality_assurance_en %}
{% for doc in qa_docs %}
- [{%- include doc-label.html doc=doc -%}]({{ doc.url | relative_url }})
{% endfor %}

## University Regulations

{% assign regulations = site.data.university_regulations_en %}
<details class="collection-toggle" open>
  <summary>University Regulations ({{ regulations | size }})</summary>
  <div class="collection-toggle__body">
    <ul class="document-list">
    {% for doc in regulations %}
      <li><a href="{{ doc.url | relative_url }}">{%- include doc-label.html doc=doc -%}</a></li>
    {% endfor %}
    </ul>
  </div>
</details>

## Public Report 2025

{% assign report_docs = site.data.public_report_2025_en %}
{% for doc in report_docs %}
- [{%- include doc-label.html doc=doc -%}]({{ doc.url | relative_url }})
{% endfor %}

## Guides

- [GWS and Gemini Usage Guide]({{ '/Guide/GWS and Gemini Usage Guide - English.html' | relative_url }})
- [Professional Manner and Workstyle Guide]({{ '/Guide/Professional Manner and Workstyle - English.html' | relative_url }})
- [Google Meet Guide]({{ '/Guide/Google Meet/Google Meet Guide - English.html' | relative_url }})
