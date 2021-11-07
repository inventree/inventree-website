---
layout: default
backLink: false
---

{% include hero.html title=site.tagline title_2='for Business' image='https://dummyimage.com/860x600' color='with InvenTree' %}

{% assign for_b = site.data.for_business %}
{% include features.html data=for_b %}

{% include cta.html text='read more on the site!' %}

{% assign function = site.data.function %}
{% include functions.html data=function %}

{% assign end = site.data.end_cta %}
{% include cta.html cta=end %}

---
