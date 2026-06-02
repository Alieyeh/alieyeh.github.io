---
layout: archive
title: "Research Infrastructure"
permalink: /infrastructure/
author_profile: true
---

Infrastructure projects focused on the systems that make biomedical data usable: secure ingest, metadata, validation, monitoring, governed provisioning and reproducible workflows.

Much of this work sits behind the scenes, but it is what allows researchers to trust that complex genomics data is findable, well described, access controlled and ready for analysis.

{% include base_path %}

{% for post in site.portfolio %}
  {% if post.category == "infrastructure" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
