---
name: inventree-niimbot-plugin
author: piramja
license: MIT
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-niimbot-plugin
github: https://github.com/piramja/inventree-niimbot-plugin
issue_tracker: https://github.com/piramja/inventree-niimbot-plugin/issues
categories:
    - Label
tags:
    - Niimbot
    - Printer
    - Label
---

## Introduction
A label printing plugin for [InvenTree](https://inventree.org), which provides support for the [Niimbot Label Printers](https://www.niimbot.com/enweb/product_label.html?category_id=6). This plugin is based on the amazing work from [labbots/NiimPrintX](https://github.com/labbots/NiimPrintX/tree/main) and modifications from [LorisPolenz/NiimPrintX](https://github.com/LorisPolenz/NiimPrintX/tree/main).

## Installation

Install this plugin manually as follows:

```
pip install inventree-niimbot-plugin
```

Or, add to your `plugins.txt` file to install automatically using the `invoke install` command:

```
inventree-niimbot-plugin
```

## Configuration Options
The following list gives an overview of the available settings. You find them under the InvenTree plugin specific settings.

* **Printer Model**
Currently supported models are: 
b1, b18, b21, d11, d110 (but i was only able to test b1 because i don't have other printer models. Please report back if you can test other models!!).

* **Density**
The print density. Different models seem to accept only certain values (b1 accepts 1-3).

* **Rotation**
Rotation angle, either 0, 90, 180 or 270 degrees.

* **Scaling**
Scaling factor, from 10% to 200%.

* **Vertical Offset**
Vertical offset, from 0 to 200px.

* **Horizontal Offset**
Horizontal offset, from 0 to 200px.
