---
name: inventree-kicad-plugin
author: afkiwers
license: MIT
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-kicad-plugin
github: https://github.com/afkiwers/inventree_kicad
issue_tracked: https://github.com/afkiwers/inventree_kicad/issues
website: https://github.com/afkiwers/inventree_kicad
categories: Integration
tags: schematic bom kicad
---

KiCad Integration for InvenTree

A plugin which allows InvenTree to serve component data to [KiCad](https://kicad.org) via the HTTP library interface.

This plugin provides an API wrapper which provides an API interface that conforms to the KiCad HTTP library interface specification. This allows KiCad to pull component data directly from your InvenTree database.

## Installation

The plugin can be installed via the InvenTree web interface, using the tag `inventree-kicad-plugin`.

Alternatively, install the plugin manually as follows:

```
pip install inventree-kicad-plugin
```

Or, add to your `plugins.txt` file and run `invoke install`.

## Documentation

Refer to the [plugin documentation](https://github.com/afkiwers/inventree_kicad) for further instructions and information.