---
title: Ecosystem
---

# Ecosystem

InvenTree is designed to be part of a larger system of tools, supporting both hobbyists and SMEs with their management needs. It can be extended with plugins, connected to other software through its API, and used alongside a range of community-built tools.

## REST API

InvenTree ships with an extensive, self-documenting REST API. Every feature of InvenTree is available through the API, which is used by the InvenTree web interface and mobile app, and can be used to connect InvenTree to your own systems.

A native [Python library](https://docs.inventree.org/en/stable/api/python/) makes it easy to write scripts and integrations against the API.

Read more about the API in the [documentation](https://docs.inventree.org/en/stable/api/).

## Mobile App

The [InvenTree Mobile App](app.md) for Android and iOS brings stock control to your pocket, with native barcode scanning and instant access to parts, stock and orders.

## Plugins

Plugins run inside the InvenTree server and can extend almost every part of it - adding user interface panels, integrations, barcode formats, label printers and much more.

Find out more about [InvenTree's plugin system](../plugins/index.md), or browse the [community plugin list](../plugins/community.md).

## AI Assistants

The [InvenTree MCP plugin](../plugins/inventree-mcp.md) exposes your InvenTree data to AI assistants and other applications via the [Model Context Protocol](https://modelcontextprotocol.io) (MCP). Ask questions about stock levels, orders and BOMs, and get answers from your live InvenTree data - with the same permission checks as the API. Read more in the [announcement](../blog/posts/2026-09-17-inventree-mcp.md).

## Third-party Tools

In addition to plugins, InvenTree is supported by a range of third-party tools built by members of the InvenTree community. Below is a non-exhaustive list of external tools that may be used in conjunction with InvenTree, or to extend its functionality:

| Tool | Publisher | Description |
| --- | --- | --- |
| [Ki-n-Tree](https://github.com/sparkmicro/Ki-nTree) | [@sparkmicro](https://github.com/sparkmicro) | Tool for automating creation of InvenTree data from external systems such as DigiKey |
| [InvenTree Part Import](https://github.com/30350n/inventree-part-import) | [@30350n](https://github.com/30350n) | CLI to import parts from suppliers like DigiKey, LCSC, Mouser, etc. to InvenTree |
| [PK2InvenTree](https://github.com/rgilham/PK2InvenTree) | [@rgilham](https://github.com/rgilham) | An open-source tool for migrating an existing [PartKeepr](https://github.com/partkeepr/PartKeepr) database to InvenTree |
| [Digikey-Inventree-Integration](https://github.com/EUdds/Digikey-Inventree-Integration) | [@EUdds](https://github.com/EUdds) | A project that takes a DigiKey part number and creates a part in InvenTree |

If you have (or know of) a third-party tool which should be featured here, please reach out and let us know!
