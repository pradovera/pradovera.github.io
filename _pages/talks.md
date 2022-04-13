---
layout: archive
title: "Talks at conferences"
permalink: /talks/
author_profile: true
---

{% for post in site.talks reversed %}
  {% if post.label == "main" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

&nbsp;

Seminars
=====

{% for post in site.talks reversed %}
  {% if post.label == "seminar" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

&nbsp;

Posters
=====

{% for post in site.talks reversed %}
  {% if post.label == "poster" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

&nbsp;

Others
=====

{% for post in site.talks reversed %}
  {% if post.label == "other" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

&nbsp;

Attendance at events
=====

{% for post in site.talks reversed %}
  {% if post.label == "attendance" %}
    {% include archive-single-attendance.html %}
  {% endif %}
{% endfor %}


