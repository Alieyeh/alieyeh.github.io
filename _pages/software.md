---
layout: archive
title: "Software Projects"
permalink: /software/
author_profile: true
---

Software projects focused on reusable research tools, preprocessing pipelines, backend systems, and practical application development.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "software" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
