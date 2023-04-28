---
title: "Teaching"
permalink: /teaching/
author_profile: true
---

Vienna, Austria
-----

During my time at the University of Vienna, I have been in charge of the following courses.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_univie" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}


Lausanne, Switzerland
-----

During my time at EPFL, I have contributed to the following courses as teaching assistant. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_epfl" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

<h4>&nbsp;</h4>

I have also acted as supervisor in the following projects carried out by individual students.

{% for post in site.teaching reversed %}
  {% if post.label == "project_epfl" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

<h4>&nbsp;</h4>

Later, I have also contributed to the following doctoral course as invited lecturer.

{% for post in site.teaching reversed %}
  {% if post.label == "lecturer_epfl" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

Piacenza, Italy
-----

During my undergrad and grad studies, I have given special preparatory courses for high-school-level students participating in scientific competitions. This was at the scientific high school L. Respighi in my hometown of Piacenza, I. My involvement includes, among other things, preparation of course and exercise material.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_piacenza_1" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

<h4>&nbsp;</h4>

Also, during my grad studies, I have done scientific tutoring for high-school students in need. This was at the scientific high school L. Respighi in my hometown of Piacenza, I. My involvement includes, among other things, preparation of course and exercise material, as well as preparation and grading of weekly assignments and exams.

{% for post in site.teaching reversed %}
  {% if post.label == "assistant_piacenza_2" %}
    {% include archive-single-teaching.html %}
  {% endif %}
{% endfor %}

Teaching education
-----

In pursuit of a better understanding of teaching and learning, I have attended the following events.

{% for post in site.teaching reversed %}
  {% if post.label == "education" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

