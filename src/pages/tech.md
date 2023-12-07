---
title: Tech Stack
---

## InvenTree Tech Stack

### Database

InvenTree supports multiple database backends:

- [PostgreSQL](https://www.postgresql.org)
- [MySQL](https://www.mysql.com)
- [SQLite](https://www.sqlite.org)

### Web Server

The back-end web server is written in [Python](https://www.python.org), using the [Django framework](https://www.djangoproject.com/). We also rely heavily on the following libraries (among others):

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Q](https://django-q2.readthedocs.io/en/master/)
- [Django Allauth](https://docs.allauth.org/en/latest/)

For a detailed look at the required packages for the InvenTree server, check out out [requirements.txt](https://github.com/inventree/InvenTree/blob/master/requirements.txt) file.

### Web App

The web app is written in [React](https://react.dev/), and makes use of the following core libraries:

- [Mantine](https://mantine.dev/)
- [Mantine Datatable](https://icflorescu.github.io/mantine-datatable/)

### Mobile App

The [InvenTree mobile app](/app) is written in [Dart](https://dart.dev/), using the [Flutter](https://flutter.dev/) framework.

### Website

The InvenTree website (this site) is powered by [Docusaurus](https://docusaurus.io/)

### Dev Ops

For developing and distributing InvenTree, we use:

- [Docker Hub](https://hub.docker.com/r/inventree/inventree) for distributing InvenTree images
- [Crowdin](https://crowdin.com/project/inventree) for managing community contributed [translations](/contribute#translate)
- [Netlify](https://www.netlify.com/) for providing preview builds via GitHub
- [Coveralls](https://coveralls.io/github/inventree/InvenTree) for tracking source code coverage statistics
- [DeepSource](https://app.deepsource.com/gh/inventree/InvenTree) for deeper source code analysis
- [Packager.io](https://packager.io/gh/inventree/InvenTree) for providing an installer packaging service
- [Digital Ocean](https://www.digitalocean.com/) for hosting the [demo server](/demo)