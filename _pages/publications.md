---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% for post in site.publications reversed %}
  {% if post.label == "main" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

&nbsp;

Pending publications
=====

{% for post in site.publications reversed %}
  {% if post.label == "pending" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
