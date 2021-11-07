---
layout: default
backLink: false
---

{% include hero.html title=site.tagline title_2='for Education' image='https://dummyimage.com/860x600' color='with InvenTree' %}

{% assign for_e = site.data.for_edu %}
{% include features.html data=for_e %}

{% include cta.html text='InvenTree provides functions for all kinds of users and parts' link = '/' link_text = 'Learn More' %}

{% assign function = site.data.function %}
{% include functions.html data=function %}

{% assign end = site.data.end_cta %}
{% include cta.html cta=end %}

---
