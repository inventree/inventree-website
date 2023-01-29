---
name: inventree-zapier
author: matmair
license: MIT
open_source: true
stable: False
maintained: true
pypi: true
package_name: inventree-zapier
github: https://github.com/matmair/inventree-zapier
gitlab:
source:
issue_tracker:
website:
categories:
tags: inventree inventree-plugin zapier inventory
---
Zapier plugin for InvenTree

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PEP](https://github.com/matmair/inventree-zapier/actions/workflows/pep.yaml/badge.svg)


# inventree-zapier

Integrate Zapier into InvenTree

## Setup

1. Install
Install this plugin as follows **in the enviroment of your InvenTree instance**:

```bash
pip install inventree-zapier
```

Or, add to your `plugins.txt` file:

```txt
inventree-zapier
```

2. Enable
Enable the plugin in the plugin settings. You need to be signed in as a superuser for this.
**The server will erstart if you enable the plugin**

3. Migrate
Access your instances python enviroment and run

```bash
inv migrate
```

4. Configure
Create an API-token in the admin interface and add set up the zapier integration in Zapier.com itself.

## License
This project is licensed as MIT. Copy and do what you want - maybe tag your new plugin so others can find it. The more the merrier.

## State of the Code
This is currently a PoC / 'beta' - at least till the Zapier App is published. Please feel free to file FRs, issues or just ideas.

