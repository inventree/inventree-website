---
name: inventree-part-pricing-update
author: Kamaar
license: MIT
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-part-pricing-update
github: https://github.com/Kamaar/inventree-part-pricing-update
issue_tracker: https://github.com/Kamaar/inventree-part-pricing-update/issues
categories:
    - Supplier
    - Pricing
tags:
    - mouser
    - digikey
    - farnell
    - pricing
    - price history
---
Keeps the supplier part prices up to date from Mouser, DigiKey and Farnell, with price history

# Part Pricing Update

Keeps the **supplier part prices** up to date from **Mouser**, **DigiKey** and **Farnell** and records their **history**.

- Scheduled background updates within the daily API limits of each supplier (requests counted and spread over the day)
- Price breaks and availability of the supplier parts; InvenTree recalculates the part pricing
- **Supplier Prices** panel on the part page: price history chart at the selected quantity, current prices, changes, status
- **Discontinued parts** page: supplier parts reported as discontinued or not available, other sources and the
  alternatives suggested by the supplier
- Renumbered supplier codes found through the MPN, temporary API errors retried
- Permissions of the InvenTree *Purchase Order* role
- Public API for other plugins (used by [inventree-supplier-part-import](https://github.com/Kamaar/inventree-supplier-part-import))

![Supplier Prices panel](https://raw.githubusercontent.com/Kamaar/inventree-part-pricing-update/main/docs/images/supplier-prices-panel.png)

## Installation

From PyPI: *Package Name* `inventree-part-pricing-update` in the InvenTree *Install plugin* dialog, or

```
pip install inventree-part-pricing-update
```

See the [README](https://github.com/Kamaar/inventree-part-pricing-update) for configuration (API keys of the suppliers).
