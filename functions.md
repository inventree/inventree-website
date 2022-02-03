---
layout: default
---

{% include hero.html title='A wealth of functions' title_2='is provided' image='https://dummyimage.com/860x600' color='by default with InvenTree' detail='By default InvenTree ships with a lot of functions in the area of part, inventory, supplier, manufacturer, machine and BOM managment.
It also enables reports, is extendible and can be extended with plugins.' %}

{% include functions.html data=site.data.functions.general extend=true no_link=true padding=false %}
{% include functions.html data=site.data.functions.extras extend=true padding=false %}
{% include cta.html cta=site.data.ctas.end %}
