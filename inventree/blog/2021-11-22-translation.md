---
author: oliver
title: Translating InvenTree
---

How we provide translation support for InvenTree in multiple languages

### Community Contributed Translations

At the time of writing, InvenTree provides language translations for 25 languages (in addition to English), with over 11,000 translated words! This is thanks to the sustained efforts of 130+ InvenTree users, who have contributed their time to make our software better for everyone.

Translation progress can be viewed on our [Crowdin project page](https://crowdin.com/project/inventree). Here you can view the current status of the translation efforts:

![Translation](/img/blog/2022-11-22-translation.png)

### Translation Pipeline

As translations are entirely community contributed, we need a software framework that allows non-technical users to submit and proofread translations, and a way to bring those translations back into the InvenTree software.

#### Backend - Django

At its core, InvenTree is built on the [Django](https://www.djangoproject.com/) framework, which provides a [translation framework](https://docs.djangoproject.com/en/4.1/topics/i18n/translation/) "out of the box". 

The Django translation framework provides a toolkit for marking certain text strings as "translatable". Translation strings are able to be replaced by a translated string from a language specified by the user - *if a translation for the text is available in that language*.

There are many files within the InvenTree project which can provide these translation strings:

- Python source files
- Javascript source files
- HTML template files

Additionally, translation support is provided for the InvenTree mobile app.

#### Exporting Translations - GitHub

On every commit to the InvenTree main branch, the source code is analyzed to discover and extract translation strings. This information is then pushed to a separate code branch, which is monitored by the [translation service](#community-translation---crowdin)

#### Community Translation - Crowdin

The crucial piece of the puzzle is the integration with [Crowdin](https://crowdin.com/) - an online translation service which provides community contributed translation, and supports open source projects.

Crowdin monitors the [InvenTree GitHub repository](https://github.com/inventree/inventree) for any changes to translation files, and provides a user interface for translators to suggest appropriate translated strings.

Suggested translations are then approved (again, by the InvenTree user community), and periodically pushed back to the InvenTree GitHub repo.

#### Merging Translations - GitHub

Updated translated strings are periodically merged back into the main code branch, keeping the InvenTree code base up to date.

### Contributing

The translation framework is provided by the InvenTree team to make our software more useful and appealing to a greater number of people. The entire translation effort is driven by the InvenTree community. Any contributions, no matter how large or small, are greatly encouraged!

If you would like to see improved translations in a particular language, read the [contribution guide](/contribute)! The InvenTree project benefits greatly from your efforts, and you get a great piece of open source software in your native language.

#### Adding New Languages

If you would like to see support for a new language, [raise an issue on our GitHub page](https://github.com/inventree/InvenTree/issues/new?assignees=&labels=enhancement%2Ctriage%3Anot-checked&template=feature_request.yaml&title=%5BFR%5D+title).
