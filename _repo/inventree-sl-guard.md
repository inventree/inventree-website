---
name: SL Guard
author: SntPartizan
license: MIT
open_source: true
stable: false
maintained: true
pypi: true
package_name: inventree-sl-guard
github: https://github.com/SntPartizan/inventree-sl-guard
issue_tracker: https://github.com/SntPartizan/inventree-sl-guard/issues
categories:
    - Stock
tags:
    - Stock Locations
    - Permissions
    - Warehouse
    - Bulk Editing
    - Regex
---

## SL Guard — protect stock-location hierarchy

SL Guard is an independent, open-source InvenTree plugin for protecting selected warehouse locations against unauthorized changes to their position in the stock-location tree.

An administrator selects protected **StockLocationType** records. Users with standard location-edit permissions can assign a protected type to a location, but cannot then relocate that protected location or remove/change its protected type without additional authorization. Moving an unprotected parent is also blocked when doing so would indirectly move protected descendants. Superusers and specifically authorized groups can make deliberate changes, subject to normal InvenTree permissions.

The plugin also provides a management panel for **bulk assigning location types**: searchable full location paths, optional regular-expression search, selectable search fields, preview, and transactional application.

**Installation:** In the InvenTree plugin installer, use package name `inventree-sl-guard` with an empty source URL, or run `pip install inventree-sl-guard` in the InvenTree Python environment.

**Compatibility:** Version 0.3.1 beta has been tested on InvenTree 1.6.1. This beta uses an internal serializer hook, so compatibility with other InvenTree versions must be tested before deployment. Protection is intended for normal application-level updates; it does not block direct SQL or all bulk database operations.

[Documentation and source code](https://github.com/SntPartizan/inventree-sl-guard) · [PyPI package](https://pypi.org/project/inventree-sl-guard/)
