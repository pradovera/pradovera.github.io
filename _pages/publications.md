---
title: "Publications"
permalink: /publications/
author_profile: true
---

See also my [ORCID]({{ site.author.orcid }}) and [Google Scholar]({{ site.author.googlescholar }}) profiles.

Journal articles
-----

{% for post in site.publications reversed %}
  {% if post.label == "main" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

Conference proceedings
-----

{% for post in site.publications reversed %}
  {% if post.label == "proceedings" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

Pending publications
-----

{% assign found = false %}
{% for post in site.publications reversed %}
  {% if post.label == "pending" %}
    {% include archive-single.html %}
    {% assign found = true %}
  {% endif %}
{% endfor %}
{% unless found %}
  Nothing here as of now!
{% endunless %}

Theses and project reports
-----

{% for post in site.publications reversed %}
  {% if post.label == "thesis" %}
    {% include archive-single-thesis.html %}
  {% endif %}
{% endfor %}
