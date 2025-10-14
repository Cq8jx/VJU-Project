---
title: Tài liệu liên quan
lang: vi
layout: page
permalink: /vi/
nav_exclude: false
nav_title: Vietnamese
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

<div class="language-switcher" role="navigation" aria-label="Chuyển đổi ngôn ngữ">
  <span>Language</span>
  <a href="{{ '/' | relative_url }}">EN</a>
  <strong>VI</strong>
  <a href="{{ '/ja/' | relative_url }}">JA</a>
</div>

# Tài liệu liên quan

Trang này tổng hợp các tài liệu liên quan bằng tiếng Việt của Trường Đại học Việt Nhật – Đại học Quốc gia Hà Nội. Để xem bản tiếng Anh hoặc tiếng Nhật, vui lòng sử dụng liên kết chuyển ngữ phía trên.

## Đảm bảo chất lượng

{% assign qa_docs_vi = site.data.quality_assurance_vi %}
{% for doc in qa_docs_vi %}
- [{% include doc-label.html doc=doc %}]({{ doc.url | relative_url }})
{% endfor %}

## Quy định của trường

{% assign regulations_vi = site.data.university_regulations_vi %}
<details class="collection-toggle" open>
  <summary>Danh mục quy định ({{ regulations_vi | size }})</summary>
  <div class="collection-toggle__body">
    <ul class="document-list">
    {% for doc in regulations_vi %}
      <li><a href="{{ doc.url | relative_url }}">{% include doc-label.html doc=doc %}</a></li>
    {% endfor %}
    </ul>
  </div>
</details>

## Báo cáo công khai 2025

{% assign reports_vi = site.data.public_report_2025_vi %}
{% for doc in reports_vi %}
- [{% include doc-label.html doc=doc %}]({{ doc.url | relative_url }})
{% endfor %}

## Hướng dẫn

- [Hướng dẫn sử dụng GWS và Gemini]({{ '/Guide/GWS and Gemini Usage Guide - Vietnamese.html' | relative_url }})
- [Hướng dẫn phong cách nghề nghiệp và tác phong làm việc]({{ '/Guide/Professional Manner and Workstyle - Vietnamese.html' | relative_url }})
- [Hướng dẫn Google Meet]({{ '/Guide/Google Meet/Google Meet Guide - Vietnamese.html' | relative_url }})
