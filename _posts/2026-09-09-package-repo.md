---
author: matmair
title: Action required - Package Repository Change
---

Due to changes in the package publishing plattform packager.io it is necessary for all users of the package based installer (most often done through the 1-line install script) to manually update their package repository configuration to continue receiving updates.

The following few bash lines will ensure you can continue receiving updates from the new package repository configuration. The update procedure, package structure or general commands are unchanged.

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

## Supported OS - you might need to upgrade

We are phasing out end of support / near end of support versions of Ubuntu and Debian - specififally with only a year left on python 3.11.

If you are on Ubuntu 20.04 (LTS) - which many of the old Docker droplet deployments were on - it is strongly recommended to update to 26.04 (LTS) to continue receiving updates. This will likely also require you to update your postgres version to at least 14, recommended is 17 or 18. Note that postgres updated should be done in single version steps (13 -> 14 -> 15 -> 16 -> 17 -> 18) or with [pgupgrade](https://www.postgresql.org/docs/18/pgupgrade.html).  
The volunteer InvenTree core team does not have the resources to assist with individual upgrades.

## Additional Notes on OS version selections

As of InvenTree version 1.5.3 the support versions are Debian 13 and Ubuntu 24.04 / 26.04 LTS. This is mainly a function of Bookworm only [shipping python 3.11](https://wiki.debian.org/Python#Supported_Python_Versions) (as does [Ubuntu 22.04](https://ubuntu.com/developers/docs/reference/availability/python/)).

As Python 3.11 has only received security updates since 2024 and is going to EOL 2027-10 there has been a noticeable uptake in end of support statements for it in the libaries we depend on. While most still support it currently it is foreseeable that they will stop. Threfore we are raising minium versions in anticipation as to not be caught off guard by dependencies causing issues and requiring urgent releases.

Python 3.12 also has [some nice QoL features](https://docs.python.org/3.12/whatsnew/3.12.html) that developers on Python 3.14 (at least me) forget about being relativley new. It also drops distutils and a few importlib functions. Raising the minimum versions allows dropping shims / allows using "new" features.

## Acknowledgements

We are very thankful to Cyril Rohr for packager.io and the support provided on various issues/questions throught the years. We are not switching away from his solutions but using the newer version go.packager.io as the old one is being sunset in the near future.
