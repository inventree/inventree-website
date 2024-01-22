---
name: inventree-bulk-plugin
author: wolflu05
license: MIT
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-bulk-plugin
github: https://github.com/wolflu05/inventree-bulk-plugin
gitlab:
source:
issue_tracker: https://github.com/wolflu05/inventree-bulk-plugin/issues
website:
categories: AppMixin
tags: Bulk Stock Part Locations
---
Bulk creation plugin for InvenTree

# inventree-bulk-plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![CI](https://github.com/wolflu05/inventree-bulk-plugin/actions/workflows/ci.yml/badge.svg)

This plugin helps you bulk create storage locations and part categories in [InvenTree](https://inventree.org/) by using customized naming strategies. That means you not only have the option to generate multidimensional\* names for stock locations or part categories, but also have the option to save the templates for later usage if your storage room uses e.g. drawer towers, saved templates help to ensure naming consistency for all later added towers.

> ℹ️ \* multidimensional means that you are not limited to namings like `D1`,`D2`, .. but also something like `D1.A`, `D1.B`, `D2.A`, `D2.B`, ...

This will generate the previous mentioned example:

<img src="https://github.com/wolflu05/inventree-bulk-plugin/assets/76838159/c1ad6ccd-bc27-445b-a3fc-ae5ce74390b5" alt="image" />

If you want to try out the templates on you're own, you can just copy the below json to your clipboard and use the "New untitled schema from clipboard" button to import them (see [import/export](https://github.com/wolflu05/inventree-bulk-plugin#import-export)). For more examples refer to the [plugin documentation](https://github.com/wolflu05/inventree-bulk-plugin).

```json
{"name":"Example","template_type":"STOCK_LOCATION","template":{"version":"1.0.0","input":{},"templates":[],"output":{"parent_name_match":"true","dimensions":["*NUMERIC","*ALPHA"],"count":["3","2"],"generate":{"name":"D{{dim.1}}.{{dim.2}}"},"childs":[]}}}
```

## ⚙️ Installation

Install this plugin as follows:

1. Make sure you allow the use of the url integration and app integration (see [Why does this plugin needs the app mixin?](https://github.com/wolflu05/inventree-bulk-plugin#why-does-this-plugin-needs-the-app-mixin))
2. Goto Settings > Plugins > Install Plugin, enter `inventree-bulk-plugin` as package name. Enable the confirm switch and click submit.
3. Restart your server and activate the plugin.
4. Stop your server and run `invoke update` (for docker installs it is `docker-compose inventree-server invoke update`). This ensures that all migrations run and the static files get collected. You can now start your server again and start using the plugin.

> ❗At least InvenTree v0.12.7 is required to use this plugin.

## 📖 Documentation

Refer to the [plugin documentation](https://github.com/wolflu05/inventree-bulk-plugin) for further examples, instructions and information.
