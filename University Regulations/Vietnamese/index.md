---
title: Quy định của trường
layout: page
---

# Quy định của trường

{% assign docs = site.pages | where: "category", "University Regulations" %}
{% assign docs = docs | where_exp: "doc", "doc.path contains '/University Regulations/Vietnamese/'" %}
{% assign docs = docs | sort: "id" %}

{% for doc in docs %}
- [{{ doc.id }} — {{ doc.title }}]({{ doc.url | relative_url }})
{% endfor %}
