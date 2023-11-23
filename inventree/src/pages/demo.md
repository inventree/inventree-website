---
title: InvenTree Demo
---

## InvenTree Demo

Want to take InvenTree for a spin? A working demo of InvenTree is available online at <a href="https://demo.inventree.org" data-umami-event="demo">https://demo.inventree.org</a>

### Login Details

Multiple default accounts are provided, as detailed below. Each account is afforded a different set of permissions, so users can see the InvenTree roles/permission system in action

| Username | Password | Description | Login |
| --- | --- | --- | --- |
| allaccess | nolimits | *View / create / edit all pages and items* | <a href="https://demo.inventree.org/accounts/login/?login=allaccess&password=nolimits" data-umami-event="demo-allaccess">log in</a> |
| reader | readonly | *Can view all pages but cannot create, edit or delete database records* | <a href="https://demo.inventree.org/accounts/login/?login=reader&password=readonly" data-umami-event="demo-reader">log in</a> |
| engineer | partsonly | *Can manage parts, view stock, but no access to purchase orders or sales orders* | <a href="https://demo.inventree.org/accounts/login/?login=engineer&password=partsonly" data-umami-event="demo-engineer">log in</a> |
| admin | inventree | *Superuser account, access all areas plus administrator actions* | <a href="https://demo.inventree.org/accounts/login/?login=admin&password=inventree" data-umami-event="demo-admin">log in</a> |

### Data Persistence

The InvenTree demo database resets to a known state once per day.

- Database records are reset to the latest state of the [demo dataset](https://github.com/inventree/demo-dataset)
- InvenTree software is kept up to date with the latest master branch, using the [inventree docker image](https://hub.docker.com/r/inventree/inventree)

:::warning Update Period
During the update period, the demo server may be inaccessible for a few minutes.
:::