---
title: Deploying InvenTree
---

There are multiple methods to deploy InvenTree. The most popular methods (supported by the development team) are listed below.

!!! success "Docker Recommended"
    The recommended method of installing InvenTree is with Docker, which provides a simple, reliable and repeatable setup on any operating system.

Before deploying InvenTree in production, read the [security considerations](https://docs.inventree.org/en/stable/concepts/threat_model/) in the documentation.

### Docker

InvenTree supports a simple containerized installation via docker. An official [docker image](https://hub.docker.com/r/inventree/inventree/) is provided with regular updates.

Refer to the [docker installation guide](https://docs.inventree.org/en/stable/start/docker/) for more information.

### Installer

We provide a [single-line installer](https://docs.inventree.org/en/stable/start/installer/) for Debian and Ubuntu, which installs InvenTree as a system package, and allows updates via the package manager.

!!! warning "Package repository change"
    The package repository changed in September 2026. Existing installations must update their package repository configuration to continue receiving updates - see [the announcement](blog/posts/2026-09-09-package-repo.md) for instructions.

### AppJail

InvenTree can be installed on FreeBSD using AppJail. An [AppJail Makejail](https://github.com/AppJail-makejails/inventree) is provided with regular updates.

### Manual Bare Metal Install

A [bare metal installation guide](https://docs.inventree.org/en/stable/start/install/) is provided for users who are looking for a low-level or custom installation.

### DigitalOcean

<a href="https://marketplace.digitalocean.com/apps/inventree?refcode=d6172576d014"><img src="https://www.deploytodo.com/do-btn-blue-ghost.svg" alt="Deploy to DO" width="auto" height="40" /></a>

InvenTree is available as a one-click install on the DigitalOcean marketplace. The image makes use of the installer and is maintained by team member [matmair](plugins/publishers.md#matmair). The source is available [here](https://github.com/invenhost/inventree_droplet).

<p>
  <a href="https://www.digitalocean.com/">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/PoweredByDO/DO_Powered_by_Badge_blue.svg" alt="Powered by DigitalOcean badge" width="201px">
  </a>
</p>

DigitalOcean is kind enough to provide open source projects with free credits to use their services. InvenTree is a proud recipient of these credits. If you are interested in applying for credits, you can do so [here](https://www.digitalocean.com/open-source/credits-for-projects).

### Other Options

The core InvenTree server is built using the widely used python-based framework [Django](https://djangoproject.com/). Therefore there are deployment methods for nearly all platforms and architectures.
