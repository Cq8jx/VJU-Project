---
title: index
layout: page
lang: en
---

# University Regulations

{% assign docs = site.pages | where: "category", "University Regulations" %}
{% assign docs = docs | where_exp: "doc", "doc.path contains '/University Regulations/English/'" %}
{% assign docs = docs | sort: "id" %}

{% for doc in docs %}
- [{{ doc.id }} — {{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}
