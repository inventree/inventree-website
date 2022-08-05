---
title: InvenTree Demo
---

Want to take InvenTree for a spin? A working demo of InvenTree is available online at **[https://demo.inventree.org](https://demo.inventree.org)**

### Login Details

Multiple default accounts are provided, as detailed below. Each account is afforded a different set of permissions, so users can see the InvenTree roles/permission system in action

| Username | Password | Description | Login |
| --- | --- | --- | --- |
| allaccess | nolimits | View / create / edit all pages and items | [log in](https://demo.inventree.org/accounts/login/?login=allaccess&password=nolimits) |
| reader | readonly | Can view all pages but cannot create, edit or delete database records | [log in](https://demo.inventree.org/accounts/login/?login=reader&password=readonly) |
| engineer | partsonly | Can manage parts, view stock, but no access to purchase orders or sales orders | [log in](https://demo.inventree.org/accounts/login/?login=engineer&password=partsonly) |
| admin | inventree | Superuser account, access all areas plus administrator actions | [log in](https://demo.inventree.org/accounts/login/?login=admin&password=inventree) |

### Data Persistence

The InvenTree demo database resets to a known state once per day.

- Database records are reset to the latest state of the [demo dataset](https://github.com/inventree/demo-dataset)
- InvenTree software is kept up to date with the latest `inventree:master` available via docker

<div markdown="span" class="alert alert-info" role="alert">
During the update period, the demo server may be inaccessible for a few minutes.
</div>    