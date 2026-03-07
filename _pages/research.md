---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

This page is dedicated to research projects and data science work.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "research" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
