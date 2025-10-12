---
title: 大学規程
layout: page
lang: ja
---

# 大学規程

{% assign docs = site.pages | where: "category", "University Regulations" %}
{% assign docs = docs | where_exp: "doc", "doc.path contains '/University Regulations/Japanese/'" %}
{% assign docs = docs | sort: "id" %}

{% for doc in docs %}
- [{{ doc.id }} — {{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}
