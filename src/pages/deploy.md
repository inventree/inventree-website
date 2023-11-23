---
title: Deploying InvenTree
---

## Deploying InvenTree

There are multiple methods to deploy InvenTree. The most popular methods (supported by the development team) are listed below:

### Installer
We provide a [single-line installer](https://docs.inventree.org/en/latest/start/installer/) that enables a quick installation and updates using the packager manager.

### Docker

InvenTree supports a simple containerized installation via docker. An official [docker image](https://hub.docker.com/r/inventree/inventree/) is provided with regular updates. 

:::tip Docker Guide
Refer to the [docker installation guide](https://docs.inventree.org/en/latest/start/docker/) for more information
:::

### AppJail

InvenTree can be installed on FreeBSD using AppJail. An [AppJail Makejail](https://github.com/AppJail-makejails/inventree) is provided with regular updates.

### Cloud Install

A member of the team provides a [1-click app for InvenTree](https://marketplace.digitalocean.com/apps/inventree) on the DigitalOcean marketplace.

### Bare Metal Install

A [bare metal installation guide](https://docs.inventree.org/en/latest/start/intro/) is provided for users who are looking for a low-level or custom installation. 

:::warning Advanced Users Only
The bare metal installation is recommended only for advanced users, if any of the above deployment options are not sufficient
:::

### Other Options

The core InvenTree server is built using the widely used python-based framework [Django](https://djangoproject.com/). Therefore there are  deployment methods for nearly all plattforms and architectures. 
