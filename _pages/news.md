---
layout: archive
title: "News and upcoming events"
permalink: /news/
author_profile: true
---

{% capture written_year %}'None'{% endcapture %}
{% for post in site.news reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
  <div class="{{ include.type | default: "list" }}__item">
    <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
  </div>
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  <div class="{{ include.type | default: "list" }}__item">
    <p style="margin-bottom:1mm;"><b>{{ post.date | date: '%B %e' }}</b>: {{ post.title }}</p>
  </div>
{% endfor %}

&nbsp;

*Last updated in April 2022*


