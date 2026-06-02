---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

Research projects at the intersection of statistical genetics, multi-omics, clinical prediction and responsible use of sensitive biomedical data.

These projects show how I approach scientific questions: define the data problem clearly, build reproducible workflows, validate outputs carefully and keep the limitations visible.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "research" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
