---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

See also my [ORCID]({{ site.author.orcid }}) and [Google Scholar]({{ site.author.googlescholar }}) profiles.

&nbsp;

Journal articles
=====

{% for post in site.publications reversed %}
  {% if post.label == "main" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

&nbsp;

Conference proceedings
=====

{% for post in site.publications reversed %}
  {% if post.label == "proceedings" %}
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

&nbsp;

Theses and project reports
=====

{% for post in site.publications reversed %}
  {% if post.label == "thesis" %}
    {% include archive-single-thesis.html %}
  {% endif %}
{% endfor %}`
