---
title: "Contacts"
permalink: /contacts/
author_profile: false
---

{% include base_path %}

{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}


<div itemscope itemtype="http://schema.org/Person">

  <div class="author__avatar">
    {% if author.avatar contains "://" %}
    	<img src="{{ author.avatar }}" alt="{{ author.name }}">
    {% else %}
    	<img src="{{ author.avatar | prepend: "/images/" | prepend: base_path }}" class="author__avatar" alt="{{ author.name }}">
    {% endif %}
  </div>

  <div class="author__content">
    <h2 class="author__name">{{ author.name }}</h2>
      {% if author.location %}
        <p>
        <h3>Address:</h3>
          {% if author.location2 %}
          <a href="https://www.google.com/maps/search/{{ author.location }},{{ author.location2 }}"><i class="fa fa-fw fa-map-marker" aria-hidden="true"></i> {{ author.location }}, {{ author.location2 }}</a>
          {% else %}
          <a href="https://www.google.com/maps/search/{{ author.location }}"><i class="fa fa-fw fa-map-marker" aria-hidden="true"></i> {{ author.location }}</a>
          {% endif %}
        </p>
      {% endif %}
      {% if author.employer %}
        <p>
        <h3>Employer:</h3>
        <i class="fa fa-fw fa-briefcase" aria-hidden="true"></i> {{ author.employer }}
        </p>
      {% endif %}
      {% if author.uri %}
        <p>
        <h3>Work webpage:</h3>
        <a href="{{ author.uri }}"><i class="fas fa-fw fa-link" aria-hidden="true"></i> {{ author.uri }}</a>
        </p>
      {% endif %}
      {% if author.email_work %}
        <p>
        <h3>Work email:</h3>
        <a href="mailto:{{ author.email_work }}"><i class="fas fa-fw fa-envelope" aria-hidden="true"></i> {{ author.email_work }}</a>
        </p>
      {% endif %}
      {% if author.email_private %}
        <p>
        <h3>Personal email:</h3>
        <a href="mailto:{{ author.email_private }}"><i class="fas fa-fw fa-envelope" aria-hidden="true"></i> {{ author.email_private }}</a>
        </p>
      {% endif %}
      {% if author.researchgate %}
        <p>
        <h3>ResearchGate page:</h3>
        <a href="{{ author.researchgate }}"><i class="fab fa-fw fa-researchgate" aria-hidden="true"></i> {{ author.researchgate }}</a>
        </p>
      {% endif %}
      {% if author.linkedin %}
        <p>
        <h3>LinkedIn page:</h3>
        <a href="https://www.linkedin.com/in/{{ author.linkedin }}"><i class="fab fa-fw fa-linkedin" aria-hidden="true"></i> https://www.linkedin.com/in/{{ author.linkedin }}</a>
        </p>
      {% endif %}
      {% if author.googlescholar %}
        <p>
        <h3>Google Scholar page:</h3>
        <a href="{{ author.googlescholar }}"><i class="fas fa-fw fa-graduation-cap"></i> {{ author.googlescholar }}</a>
        </p>
      {% endif %}
      {% if author.orcid %}
        <p>
        <h3>Orcid page:</h3>
        <a href="{{ author.orcid }}"><i class="ai ai-orcid-square ai-fw"></i> {{ author.orcid }}</a>
        </p>
      {% endif %}
      {% if author.wikipedia %}
        <p>
        <h3>Wikipedia user page:</h3>
        <a href="https://en.wikipedia.org/wiki/User:{{ author.wikipedia }}"><i class="fab fa-fw fa-wikipedia-w" aria-hidden="true"></i> https://en.wikipedia.org/wiki/User:{{ author.wikipedia }}</a>
        </p>
      {% endif %}
      {% if author.bitbucket %}
        <p>
        <h3>Bitbucket page:</h3>
        <a href="https://bitbucket.org/{{ author.bitbucket }}"><i class="fab fa-fw fa-bitbucket" aria-hidden="true"></i> https://bitbucket.org/{{ author.bitbucket }}</a>
        </p>
      {% endif %}
      {% if author.github %}
        <p>
        <h3>Github page:</h3>
        <a href="https://github.com/{{ author.github }}"><i class="fab fa-fw fa-github" aria-hidden="true"></i> https://github.com/{{ author.github }}</a>
        </p>
      {% endif %}
      {% if author.stackoverflow %}
        <p>
        <h3>Stackoverflow user page:</h3>
        <a href="https://www.stackoverflow.com/users/{{ author.stackoverflow }}"><i class="fab fa-fw fa-stack-overflow" aria-hidden="true"></i> https://www.stackoverflow.com/users/{{ author.stackoverflow }}</a>
        </p>
      {% endif %}
  </div>
</div>
