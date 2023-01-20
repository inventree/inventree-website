---
layout: default
permalink: /functions
---

{%- include block/hero.html title='A wealth of functions' title_2='provided' gallery='webgallery/' color='out of the box' detail='InvenTree ships with a wide range of functions for managing parts, inventory, supplier and manufacturer data, machine and BOM managment <em>and so much more</em>!<br>It also enables reports, can be integrated with external applications and can be extended with plugins.' -%}

{%- include block/functions.html data=site.data.functions.general extend=true no_link=true padding=false -%}
{%- include block/functions.html data=site.data.functions.extras extend=true padding=false -%}
{%- include block/cta.html cta=site.data.ctas.end -%}
