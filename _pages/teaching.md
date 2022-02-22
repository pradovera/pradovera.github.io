---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

I have contributed to the following courses as teaching assistant. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

&nbsp;

Student supervision
=====

I have also acted as supervisor in the following projects carried out by individual students.

{% for post in site.teaching reversed %}
  {% if post.label == "project" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

