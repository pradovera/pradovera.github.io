---
title: "Talks"
permalink: /talks/
author_profile: true
---

Talks at conferences
-----

{% for post in site.talks reversed %}
  {% if post.label == "main" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

Seminars
-----

{% for post in site.talks reversed %}
  {% if post.label == "seminar" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

Organized events
-----

{% for post in site.talks reversed %}
  {% if post.label == "chair" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

Posters
-----

{% for post in site.talks reversed %}
  {% if post.label == "poster" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

Others
-----

{% for post in site.talks reversed %}
  {% if post.label == "other" %}
    {% include archive-single-talk.html %}
  {% endif %}
{% endfor %}

Attendance at events
-----

{% for post in site.talks reversed %}
  {% if post.label == "attendance" %}
    {% include archive-single-attendance.html %}
  {% endif %}
{% endfor %}


