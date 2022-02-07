---
layout: default
backLink: false
main_page: True
---

{% include block/hero.html title=site.tagline title_2='and more' image='https://dummyimage.com/860x600' color='with InvenTree' detail='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.' %}

{% include block/functions.html data=site.data.functions.general %}

{% include block/features.html data=site.data.for_maker link=true %}
{% include block/features.html data=site.data.for_business link=true%}
{% include block/features.html data=site.data.for_edu link=true %}

{% include block/stats.html data=site.data.general.stats %}

{% include block/cta.html cta=site.data.ctas.end %}

