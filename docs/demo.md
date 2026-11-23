---
title: InvenTree Demo
description: "Try InvenTree in your browser - log in to the online demo with one of the example accounts."
---

Want to take InvenTree for a spin? A working demo of InvenTree is available online at <a href="https://demo.inventree.org" data-umami-event="demo">https://demo.inventree.org</a>

### Login Details

Multiple default accounts are provided, as detailed below. Each account is afforded a different set of permissions, so users can see the InvenTree roles/permission system in action.

| Username | Password | Description | Login |
| --- | --- | --- | --- |
| noaccess | youshallnotpass | Can log in, but has no permissions | <a href="https://demo.inventree.org/web/login?login=noaccess&password=youshallnotpass" target="_blank" rel="noopener noreferrer" data-umami-event="demo-noaccess">log in</a> |
| allaccess | nolimits | View / create / edit all pages and items | <a href="https://demo.inventree.org/web/login?login=allaccess&password=nolimits" target="_blank" rel="noopener noreferrer" data-umami-event="demo-allaccess">log in</a> |
| reader | readonly | Can view all pages but cannot create, edit or delete database records | <a href="https://demo.inventree.org/web/login?login=reader&password=readonly" target="_blank" rel="noopener noreferrer" data-umami-event="demo-reader">log in</a> |
| engineer | partsonly | Can manage parts, view stock, but no access to purchase orders or sales orders | <a href="https://demo.inventree.org/web/login?login=engineer&password=partsonly" target="_blank" rel="noopener noreferrer" data-umami-event="demo-engineer">log in</a> |
| steven | wizardstaff | Staff account, can access some admin sections | <a href="https://demo.inventree.org/web/login?login=steven&password=wizardstaff" target="_blank" rel="noopener noreferrer" data-umami-event="demo-steven">log in</a> |
| admin | inventree | Superuser account, access all areas plus administrator actions | <a href="https://demo.inventree.org/web/login?login=admin&password=inventree" target="_blank" rel="noopener noreferrer" data-umami-event="demo-admin">log in</a> |

### Data Persistence

The InvenTree demo database resets to a known state once per day.

- Database records are reset to the latest state of the [demo dataset](https://github.com/inventree/demo-dataset)
- InvenTree software is kept up to date with the latest `inventree:master` available via docker

!!! info
    During the update period, the demo server may be inaccessible for a few minutes.    
