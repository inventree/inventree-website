---
author: matmair
title: Action required - Package Repository Change
---

Due to changes to the package publishing platform, packager.io, all users of the package-based installer (most often installed through the 1-line install script) must manually update their package repository configuration to continue receiving updates.

The following Bash commands will ensure that you continue receiving updates from the new package repository configuration. The update procedure, package structure and general commands are unchanged.

## Upgrade Instructions

### Command for Ubuntu 26.04

```bash
sudo curl -fsSL "https://go.packager.io/srv/deb/inventree/InvenTree/gpg-key.gpg" -o /usr/share/keyrings/InvenTree.gpg
sudo curl -fsSL "https://go.packager.io/srv/inventree/InvenTree/stable/installer/ubuntu/26.04.list" -o /etc/apt/sources.list.d/InvenTree.list
sudo apt update
sudo apt install -y inventree
```

### Command for Ubuntu 24.04

```bash
sudo curl -fsSL "https://go.packager.io/srv/deb/inventree/InvenTree/gpg-key.gpg" -o /usr/share/keyrings/InvenTree.gpg
sudo curl -fsSL "https://go.packager.io/srv/inventree/InvenTree/stable/installer/ubuntu/24.04.list" -o /etc/apt/sources.list.d/InvenTree.list
sudo apt update
sudo apt install -y inventree
```

### Command for Debian 13
```bash
sudo curl -fsSL "https://go.packager.io/srv/deb/inventree/InvenTree/gpg-key.gpg" -o /usr/share/keyrings/InvenTree.gpg
sudo curl -fsSL "https://go.packager.io/srv/inventree/InvenTree/beta/installer/debian/13.list" -o /etc/apt/sources.list.d/InvenTree.list
sudo apt update
sudo apt install -y inventree
```

## Supported OS versions - you might need to upgrade

We are phasing out versions of Ubuntu and Debian that are at, or approaching, end of support, particularly as Python 3.11 has only one year until EOL.

If you are using Ubuntu 20.04 (LTS), which many of the old Docker droplet deployments used, we strongly recommend updating to 26.04 (LTS) to continue receiving updates. This will likely also require you to update your PostgreSQL version to at least 14; version 17 or 18 is recommended. Note that PostgreSQL should be updated one major version at a time (13 -> 14 -> 15 -> 16 -> 17 -> 18), or by using [pg_upgrade](https://www.postgresql.org/docs/18/pgupgrade.html).
The volunteer InvenTree core team does not have the resources to assist with individual upgrades.

## Additional Notes on OS version selections

As of InvenTree version 1.5.3, the supported versions are Debian 13 and Ubuntu 24.04 / 26.04 LTS. This is mainly because Bookworm is the only supported Debian release [shipping Python 3.11](https://wiki.debian.org/Python#Supported_Python_Versions) (as does [Ubuntu 22.04](https://ubuntu.com/developers/docs/reference/availability/python/)).

As Python 3.11 has received only security updates since 2024 and will reach EOL in October 2027, the libraries on which we depend have increasingly announced that they will soon end support for it. Although most still support it, this is likely to change. Therefore, we are raising the minimum versions in advance so that we are not caught off guard by dependency issues that require urgent releases.

Python 3.12 also has [some nice QoL features](https://docs.python.org/3.12/whatsnew/3.12.html) that developers using Python 3.14 (myself included) can forget are relatively new. It also drops distutils and a few importlib functions. Raising the minimum versions allows us to drop shims and use these newer features.

## Acknowledgements

We are very thankful to Cyril Rohr for packager.io and the support provided on various issues and questions throughout the years. We are not switching away from his solutions, but using the newer version, go.packager.io, as the old one is being sunset in the near future.
