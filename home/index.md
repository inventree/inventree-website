---
layout: default
backLink: false
---

{% include hero.html title=site.tagline title_2='and more' image='https://dummyimage.com/860x600' color='with InvenTree' %}

{% assign function = site.data.function %}
{% include functions.html data=function %}


{% assign for_h = site.data.for_hobby %}
{% include features.html data=for_h %}

{% assign for_b = site.data.for_business %}
{% include features.html data=for_b %}

{% assign for_e = site.data.for_edu %}
{% include features.html data=for_e %}

{% assign stats = site.data.stats %}
{% include stats.html data=stats %}

{% assign end = site.data.end_cta %}
{% include cta.html cta=end %}

---
