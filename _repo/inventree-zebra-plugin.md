---
name: inventree-zebra-plugin
author: SergeoLacruz
license: MIT
open_source: true
stable: true
maintained: true
pypi: false
package_name:
github: https://github.com/SergeoLacruz/inventree-zebra-plugin
gitlab:
source:
issue_tracker: https://github.com/SergeoLacruz/inventree-zebra-plugin/issues
website:
categories: Printer
tags: Label Printer Zebra ZPL
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
