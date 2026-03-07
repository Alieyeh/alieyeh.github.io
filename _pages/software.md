---
layout: archive
title: "Software Projects"
permalink: /software/
author_profile: true
---

This section contains software engineering projects exploring system architecture, backend services and application development.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "software" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
