---
title: Deploying InvenTree
---

### Deployment Methods for InvenTree

There are multiple methods to deploy InvenTree. The most popular methods (supported by the development team) are:

### Installer
We provide a [single-line installer](https://inventree.readthedocs.io/en/latest/start/installer/) that enables a quick installation and updates using the packager manager.

#### Docker

InvenTree supports a simple containerized installation via docker. An official [docker image](https://hub.docker.com/r/inventree/inventree/) is provided with regular updates. 

Refer to the [docker installation guide](https://inventree.readthedocs.io/en/latest/start/docker/) for more information

#### Manual Bare Metal Install

A [bare metal installation guide](https://inventree.readthedocs.io/en/latest/start/intro/) is provided for users who are looking for a low-level or custom installation. 

#### Cloud

A member of the team provides a [1-click app for InvenTree](https://marketplace.digitalocean.com/apps/inventree?refcode=d6172576d014&action=deploy) on the DigitalOcean marketplace.

### Other Options

The core InvenTree server is built using the widely used python-based framework [Django](https://djangoproject.com/). Therefore there are  deployment methods for nearly all plattforms and architectures. If you want to read more about InvenTree's structure and a typical installation read the [architecture overview](../contribute/code/architecture).
