---
author: matmair
title: UI Roadmap - going 1.0
---

In August 2023 we announced [in a blog post](/blog/2023/08/28/react) that we are working on a new user interface for InvenTree. This post is a follow-up to that announcement and provides an overview of the progress we have made so far and what we are planning to do next.
The most important information for you: the next release (0.17.0) will be the last with the old interface (CUI) as the default. The new interface (PUI) will be the default starting with the 0.18.0 release.  
The plan is to release 1.0 once PUI has all features ported, that will probably be the release after 0.18.0. 1.0 will not include CUI or the needed front- and backend code to support it.

Most of this article is probably only interesting for (plugin) developers, but we hope it gives you a good overview of what is happening.

## PUI / CUI - A short overview

The new interface is called PUI (Platform User Interface) and the old one CUI (Classic User Interface). PUI is built with React and is a single-page application. CUI is built with Django templates and uses a mixture of jQuery, templated JS and some libraries.
PUI is designed to be more consistent, use the API everywhere and support better testing (end-to-end, typing). The original blog post has more information on the [design goals](/blog/2023/08/28/react#design-goals).

## Why remove CUI?

CUI has proven to be hard to understand for new contributors and hard to maintain in a consistent quality. Some common issues like cache invalidation, inconsistent rendering and hard-to-enforce permissions are easier to solve in PUI.
Therefore 1.0 will be PUI only. The compiled javascript, CSS and html files will be removed from the repository. CUI-only endpoints/tags will also be removed. Some HTML rendering will be kept as the report/label generation uses that.

This will probably remove around 2k files from the repo, around 370k lines. As of writing, we have 4.4k files and 2.4M lines in the repo.

## Effect on plugins

Plugins that render into the UI will need to be updated to work with PUI. This could affect you if your plugins use the mixins `PanelMixin`, `SettingsContentMixin`, `NavigationMixin` or `UrlsMixin`. Rendering into PUI is best done with `UserInterfaceMixin` (available in 0.17.0) - which is actively expanded to support rendering more tightly integrated than `PanelMixin` and CUI. For example [#8137](https://github.com/inventree/InvenTree/pull/8137) supports rendering custom template editors in PUI.

We will issue guidance regarding the transition of plugins into the new mechanisms before 1.0 goes to production.

## How can you help?

- Use the new UI - if you are on the 0.16.x release train your instance should already be serving it
- Report bugs - if you find something that is not working as expected please report it
- Report missing features - if you are missing something from CUI please report it (we have an EPIC[ that tracks them](https://github.com/inventree/InvenTree/issues/5212))
- Start looking into developing PUI and contributing - we use React and Mantine, widely used technologies
- Support the development - we have been developing PUI for over a year with more or less 3 people. Donations could help us spend more time or awarding bounties for features/design improvements.

## The big 1.0

1.0 will be a big milestone for InvenTree. InvenTree has been running in the heart of many companies for years. The switch to PUI enables much safer work on the UI. The release number 1.0 signals that the last part of the system is now modernised and ready for the future. We are looking forward to it and hope you are too.

Switching to 1.0 will also mean that we will follow SemVer fully. Big breaking changes will only be in major releases, feature releases (1.0, 1.1, 1.2) will follow the SemVer rules. This will make it easier for some of our enterprise users who face backlash or difficulty because of the below 1.0 version number.

We are discussing a few more breaking changes in 1.0 - feel free to chime in on the dedicated issue [#6417](https://github.com/inventree/InvenTree/issues/6417).
