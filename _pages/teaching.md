---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

As part of my Ph.D. training, I have contributed to the following courses as teaching assistant. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "main" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

&nbsp;

Student supervision
=====

I have also acted as supervisor in the following elective projects carried out by individual students.

{% for post in site.teaching reversed %}
  {% if post.label == "project" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

