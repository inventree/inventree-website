---
author: matmair
title: Starting the Plugin List
---

Recently a new feature was launched: A central plugin list.

## TLDR

The Plugin List is managed by the [InvenTree org](https://github.com/inventree) and is [open for submissions](https://github.com/inventree/inventree-website#adding-a-plugin-to-the-list). It is a simple list [on the website]({% link plugins.html %}) for a start. Being on the list is not an endorsement or guarantee of service by the core team.

## Why plugins and a plugin list?

InvenTree is a powerful tool but the use cases very widely. Many things can be done with it, but too many special features also create confusion for the average hobbyist user. 
That is why we created the plugin system. It allows users to extend InvenTree with custom functionality without having to modify or ding into core code. It is a great way to add features that are not needed by everyone but are still useful for a subset of users. It can also be used to customize InvenTree to fit existing patterns (eg. part numbering scheme or order references).

One of my main goals was to enable complex changes without the need of forking the code. This way users can still benefit from upstream changes and bugfixes without having to merge them manually. As a positive side effect, it should also reduce requests for fixes of very old versions and enable users to always use the latest version of InvenTree as we try to keep the plugin (python) APIs stable.

The plugin system has been in core for a while now and from my own usage, conversations with users and requests on GitHub I know that small plugin collections have started to form.  
I think most plugins are very tailored to the businesses/users that deploy them. I have seen some for shipping, integrating ERP systems, connecting machines or generating files for orders. Therefore, they are not fit for public consumption.  
There are, however, a number of public repos on GitHub and GitLab with integrations for printers, adding functionality that we are not willing/able to add to core or do other cool things.

The plugin list is a way to share the cool, public plugins you made with the community. I also hope that it enables new users to onboard faster.

## How it works

As mentioned [before]({% link  _news/2022-04-23-news-are-starting.md %}), we use Jekyll for this website. This means that the list consists of static pages that are generated from YAML/Markdown files. The output is hosted by GitHub pages (for free ;-)) and can be previewed on PRs thanks to the Netlify app integration.

A file contains a number of standardised fields in the header and markup text for the plugin page that uses Markdown (just like GitHub README pages). That information is used to generate:
- the individual plugin pages (eg. [this one]({% link _repo/inventree-brother-plugin.md %}))
- plugin cards on the main page (showing the newest entries)
- a list of [all plugins]({% link plugins.html %})
- overview pages for [tags]({% link tags.html %}) and [categories]({% link categories.html %})

Adding a new entry is as simple as forking, creating a new file in the plugins folder and opening a PR. More on that is below.

There are also entries and pages for authors/publishers. Currently, we only support one author per plugin, but that might change in the future. The author entry is used to generate a page for the author (eg. [this one]({% link _publishers/schrodingersgat.md %})). That page also contains all blog posts written by the author and a few links.

### Disclaimer

While the list is moderated, the core team does not endorse or guarantee any service for the plugins listed. If you have any questions, please contact the plugin author directly.

### Submitting a plugin

If you want to add your plugin to the list, please follow the [instructions in the README](https://github.com/inventree/inventree-website#adding-a-plugin-to-the-list) of the repo for the website. The list is managed by members of the [InvenTree org](https://github.com/inventree), so it might take a few days to process your request. If you are submitting a plugin for the first time, there is a good chance you do not have a publisher/author entry either - please add that as well. The steps are listed in the README.

Please make sure to update your listing if your plugin is no longer maintained or if anything important changes. For now, there is no automated process to update listings from their repos.

## Future ideas

Several ideas have been brought forward regarding possible improvements to the plugin list since I started public work on it (the original idea is from Feb/Mar 2022, like the rest of the website). If you have any ideas, please let us know in the discussions on GitHub or in an issue. And if you want to help, please feel free to open a PR for anything listed below.

Inclusion in InvenTree: Users of InvenTree should be able to browse and install plugins directly from within the web app. This would require a way to install plugins and probably a way to update them too. A good example would be Octoprint's plugin manager. The main work would be to create a nice interface, the API endpoints (for installing and activating/deactivation) are already there.

Regarding browsing the list on the site:
* A more detailed list with screenshots, short descriptions and standardised sections in the page itself
* A way to rate plugins
* A way to show how often a plugin is used/downloaded (would probably need [4150](https://github.com/inventree/InvenTree/issues/4150))
* A better way to search for plugins (by name, description, author, tags, etc.) - we deploy statically so that might be tricky
* A way to filter plugins by InvenTree version
* A way to filter plugins by language (if they are translated)
* A way to filter plugins by license (there are so many licenses that I did not include it in the first version)
Quality of life:
* A more automated process to update the list from the plugin repos
* Improve the PyPI scraper to also work with GitHub and GitLab repos
* A way to automatically test plugins for compatibility with InvenTree and show that on the listing
* RSS feed for new plugins

Moon-shot idea: A privacy-friendly way to register your instance once and then have a button on the website that directly installs the plugin. That would also enable some cool other stuff with browser integrations, fast pairing for the app (very much requested by uni labs) and more.
