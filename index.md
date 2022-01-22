---
layout: default
backLink: false
main_page: True
---

{% include hero.html title=site.tagline title_2='and more' image='https://dummyimage.com/860x600' color='with InvenTree' %}

{% include functions.html data=site.data.general.function %}

{% include features.html data=site.data.for_maker link=true %}
{% include features.html data=site.data.for_business link=true%}
{% include features.html data=site.data.for_edu link=true %}

{% include stats.html data=site.data.general.stats %}

{% include cta.html cta=site.data.general.end_cta %}

