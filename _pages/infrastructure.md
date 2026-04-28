---
layout: archive
title: "Research Infrastructure"
permalink: /infrastructure/
author_profile: true
---

Infrastructure projects focused on secure data ingest, metadata systems, monitoring, governed provisioning, and reproducible workflows for large-scale biomedical research platforms.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "infrastructure" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
