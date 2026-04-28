---
layout: archive
title: "Research Projects"
permalink: /research/
author_profile: true
---

Research projects focused on biomedical data science, statistical genetics, machine learning, and translational use of complex health and omics data.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "research" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
