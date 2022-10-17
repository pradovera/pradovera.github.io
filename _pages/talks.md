---
title: "Talks at conferences"
permalink: /talks/
author_profile: true
---

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


