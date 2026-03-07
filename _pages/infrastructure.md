---
layout: archive
title: "Research Infrastructure"
permalink: /infrastructure/
author_profile: true
---

This section showcases projects related to **data infrastructure, pipelines and research platforms**.

These systems support large-scale biomedical datasets and enable reproducible and secure research workflows.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "infrastructure" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
