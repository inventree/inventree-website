---
layout: default
backLink: false
main_page: True
---

{% include hero.html title=site.tagline title_2='and more' image='https://dummyimage.com/860x600' color='with InvenTree' detail='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.' %}

{% include functions.html data=site.data.functions.general %}

{% include features.html data=site.data.for_maker link=true %}
{% include features.html data=site.data.for_business link=true%}
{% include features.html data=site.data.for_edu link=true %}

{% include stats.html data=site.data.general.stats %}

{% include cta.html cta=site.data.ctas.end %}

