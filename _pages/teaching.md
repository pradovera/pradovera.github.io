---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

At EPFL
-----

During my time at EPFL, I have contributed to the following courses as teaching assistant. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_epfl" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

&nbsp;

I have also acted as supervisor in the following projects carried out by individual students.

{% for post in site.teaching reversed %}
  {% if post.label == "project_epfl" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

&nbsp;

At the L. Respighi scientific high school
-----

During my undergrad and grad studies, I have given special preparatory courses for high-school-level students participating in scientific competitions. This was at the scientific high school L. Respighi in my hometown of Piacenza, I. My involvement includes, among other things, preparation of course and exercise material.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_piacenza_1" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

&nbsp;

Also, during my grad studies, I have done scientific tutoring for high-school students in need. This was at the scientific high school L. Respighi in my hometown of Piacenza, I. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_piacenza_2" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

