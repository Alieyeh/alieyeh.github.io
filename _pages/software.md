---
layout: archive
title: "Software Projects"
permalink: /software/
author_profile: true
---

Software projects spanning research packages, preprocessing pipelines, validation tooling, backend design and practical applications.

The common thread is usability: code should be clear enough to reuse, documented enough to hand over and structured enough to support real research work.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "software" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
