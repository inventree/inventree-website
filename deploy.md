---
title: Deploying InvenTree
---

There are multiple methods to deploy InvenTree. The most popular methods (supported by the development team) are:

### Docker

InvenTree supports a simple containerized installation via docker. An official [docker image](https://hub.docker.com/r/inventree/inventree/) is provided with regular updates. 

Refer to the [docker installation guide](https://docs.inventree.org/en/stable/start/docker/) for more information

### Installer
We provide a [single-line installer](https://docs.inventree.org/en/stable/start/installer/) that enables a quick installation and updates using the packager manager.

### AppJail

InvenTree can be installed on FreeBSD using AppJail. An [AppJail Makejail](https://github.com/AppJail-makejails/inventree) is provided with regular updates.

### Manual Bare Metal Install

A [bare metal installation guide](https://docs.inventree.org/en/stable/start/) is provided for users who are looking for a low-level or custom installation. 

### Other Options

The core InvenTree server is built using the widely used python-based framework [Django](https://djangoproject.com/). Therefore there are  deployment methods for nearly all platforms and architectures. 
