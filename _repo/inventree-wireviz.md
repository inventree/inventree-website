---
name: inventree-wireviz-plugin
author: SchrodingersGat
license: MIT
open_source: true
stable: false
maintained: true
pypi: true
package_name: inventree-wireviz-plugin
github: https://github.com/inventree/inventree-wireviz
issue_tracked: https://github.com/inventree/inventree-wireviz/issues
website: https://inventree.org
categories: Extension
tags: BOM Build Part
---

Wireviz Extension for InvenTree

A plugin which provides support for [wireviz](https://github.com/wireviz/WireViz), a software tool for generating harness / wiring diagrams programmatically.

This plugin generates wireviz diagrams and integrates them natively into the InvenTree interface. Additionally, BOM data can be extracted directly from the wireviz file:

![](/assets/plugins/inventree_wireviz.png)

## Installation

Install the plugin manually as follows:

```
pip install inventree-wireviz-plugin
```

Or, add to your `plugins.txt` file to install automatically using the `invoke install` command:

```
inventree-wireviz-plugin
```

## Documentation

Refer to the [plugin documentation](https://github.com/inventree/inventree-wireviz) for further instructions and information.