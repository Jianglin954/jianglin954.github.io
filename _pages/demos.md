---
layout: page
title: demos
permalink: /demos/
description: Selected research demos and project pages.
nav: true
nav_order: 1
horizontal: false
---

<!-- pages/demos.md -->
<div class="projects">
  {% assign sorted_demos = site.demos | sort: "importance" %}
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
      {% for demo in sorted_demos %}
        {% assign project = demo %}
        {% include projects_horizontal.liquid %}
      {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for demo in sorted_demos %}
      {% assign project = demo %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
</div>
