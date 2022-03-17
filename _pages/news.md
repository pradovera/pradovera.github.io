---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

{% capture written_year %}'None'{% endcapture %}
{% for post in site.news reversed %}
  {% capture year %}{{ post.year }}{% endcapture %}
  {% if year != written_year %}
    <div class="{{ include.type | default: "list" }}__item">
      <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
    </div>
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  <div class="{{ include.type | default: "list" }}__item">
    <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
      <h4 class="archive__item-title" itemprop="headline">
        {{ post.date }}: {{ post.title }}
      </h4>
    </article>
  </div>
{% endfor %}

&nbsp;

Last updated: **March 2022**


