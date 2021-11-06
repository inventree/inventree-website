---
layout: default
backLink: false
---

{% include hero.html title=site.tagline title_2='and more' image='https://dummyimage.com/860x600' color='with InvenTree' %}


{% assign for_b = site.data.for_b %}
{% include features.html data=for_b %}


{% assign for_h = site.data.for_h %}
{% include features.html data=for_h %}

{% include cta.html %}

---
