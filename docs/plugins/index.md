---
title: Plugins
template: main.html
---

# Plugins

InvenTree is a modular application with a powerful plugin system. Plugins run inside the InvenTree server and can extend almost every part of it, without any changes to the core code. Plugins can:

- **Extend the user interface**: add custom panels, dashboard widgets, navigation items and settings pages
- **React to events**: run custom code when parts, stock items or orders are created or changed
- **Integrate with external systems**: connect to suppliers, ERP, accounting or notification services
- **Print and report**: add label printer drivers, custom report templates and data exports
- **Scan barcodes**: support custom barcode formats and supplier barcodes
- **Add API endpoints and URLs**: expose new functionality to other applications
- **Run scheduled tasks** and **validate data** against your own business rules

Plugins are standard Python packages, and can be installed from PyPI via the InvenTree admin interface, or placed in the plugins directory of your installation.
Read more about the [plugin architecture](https://docs.inventree.org/en/stable/plugins/) and [installing plugins](https://docs.inventree.org/en/stable/plugins/install/) in the documentation.

## Create Your Own Plugin

The [InvenTree Plugin Creator](https://github.com/inventree/plugin-creator) is a command line tool which scaffolds a new plugin in a few seconds - select the features you need, and it generates a ready-to-develop project. Refer to the [plugin creator guide](https://docs.inventree.org/en/stable/plugins/creator/) and the [plugin walkthrough](https://docs.inventree.org/en/stable/plugins/walkthrough/) to get started.

Once your plugin is published, add it to the [community plugin list](community.md) by following the [instructions on GitHub](https://github.com/inventree/inventree-website#adding-a-plugin-to-the-list).

## Community Plugins

Browse the [community plugin list](community.md) to find plugins developed by the InvenTree community, or browse them [by category](categories.md), [by tag](tags.md) or [by publisher](publishers.md).
