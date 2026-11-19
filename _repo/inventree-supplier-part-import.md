---
name: inventree-supplier-part-import
author: Kamaar
license: GPL-3.0-or-later
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-supplier-part-import
github: https://github.com/Kamaar/inventree-supplier-part-import
issue_tracker: https://github.com/Kamaar/inventree-supplier-part-import/issues
categories:
    - Supplier
    - Part
tags:
    - mouser
    - digikey
    - farnell
    - import
    - ki-ntree
---
Search Mouser, DigiKey and Farnell and import parts with the Ki-nTree rules

# Supplier Part Import

Searches parts on **Mouser**, **DigiKey** and **Farnell** and creates them in InvenTree with the import rules of
[Ki-nTree](https://github.com/sparkmicro/Ki-nTree): part, manufacturer part, supplier parts with prices, category,
parameters, datasheet, image and RoHS / REACH.

- Search on one or all suppliers, with the requests left today
- Category proposed from editable mappings (DigiKey, Mouser and Farnell defaults included); missing categories are
  created only when they are used
- Parameters mapped to the InvenTree templates and converted to their units
- Alternate suppliers, datasheet and image, manufacturer RoHS / REACH declarations
- Duplicate detection (MPN, SKU of any supplier, old names of renamed products): update the existing part instead
- Optional IPN proposal

Requires [inventree-part-pricing-update](https://github.com/Kamaar/inventree-part-pricing-update) (API credentials,
daily quota and prices).

![Import form](https://raw.githubusercontent.com/Kamaar/inventree-supplier-part-import/main/docs/images/import-preview.png)

## Installation

From PyPI (the pricing plugin is installed as a dependency; activate both): *Package Name*
`inventree-supplier-part-import` in the InvenTree *Install plugin* dialog, or

```
pip install inventree-supplier-part-import
```

See the [README](https://github.com/Kamaar/inventree-supplier-part-import) for the details.
