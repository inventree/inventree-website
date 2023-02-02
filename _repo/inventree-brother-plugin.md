---
name: inventree-brother-plugin
author: SchrodingersGat
license: MIT
open_source: true
stable: False
maintained: true
pypi: true
package_name: inventree-brother-plugin
github: https://github.com/inventree/inventree-brother-plugin
gitlab:
source:
issue_tracker: https://github.com/inventree/inventree-brother-plugin/issues
website: https://inventree.org
categories: Printer
tags: Label Printer Brother
---
Brother label printer plugin for InvenTree

A label printing plugin for [InvenTree](https://inventree.org), which provides support for the [Brother label printers](https://www.brother.com.au/en/products/all-labellers/labellers).

This plugin supports printing to *some* Brother label printers with network (wired or WiFi) support. Refer to the [brother_ql docs](https://github.com/pklaus/brother_ql/blob/master/brother_ql/models.py) for a list of label printers which are directly supported.

## Installation

Install this plugin manually as follows:

```
pip install inventree-brother-plugin
```

Or, add to your `plugins.txt` file to install automatically using the `invoke install` command:

```
inventree-brother-plugin
```
