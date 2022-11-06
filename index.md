---
layout: default
backLink: false
main_page: True
---

{% capture image_link %}{{ "/assets/front.png" | absolute_url }}{% endcapture %}
{% include block/hero.html
    title=site.tagline
    title_2='and more'
    image=image_link
    color='with InvenTree'
    detail='InvenTree is an open-source inventory management system which provides intuitive parts management and stock control. A wide range of features makes InvenTree the perfect choice for businesses and hobbyists alike. InvenTree is designed to be extensible, and provides multiple options for integration with external applications or addition of custom plugins.'
%}

{% include block/functions.html data=site.data.functions.general padding=false %}

{% include block/cta.html cta=site.data.ctas.newsletter %}

{% include block/stats.html data=site.data.general.stats %}
{% include block/team.html data=site.data.team %}

{% include block/cta.html cta=site.data.ctas.end %}

