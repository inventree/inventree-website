---
name: ShopifyIntegrationPlugin                                     # Name of the plugin (should be either NAME, TITLE or SLUG)
author: matmair                                                    # Maintainer must be the same as the publisher reference
license: MIT                                                       # License, we prefer open source
open_source: true                                                  # Is this project licensed with an OSI-approved license - aka 'open source'
stable: true                                                       # Is this project stable? Should users deploy this in their instace?
maintained: true                                                   # Is this project maintained?
pypi: true                                                         # Is availanle via PyPi
package_name: inventree-shopify                                    # Name of the package on the index, required if pypi true
github: https://github.com/matmair/ShopifyIntegrationPlugin        # Ĺink to repo in GitHub, one of github, gitlab or source is required
gitlab: https://gitlab.com/matmair/ShopifyIntegrationPlugin        # Ĺink to repo in Gitlab, one of github, gitlab or source is required
source: https://git.mjmair.com/matmair/ShopifyIntegrationPlugin    # Link to source, one of github, gitlab or source is required
issue_tracker: https://github.com/matmair/ShopifyIntegrationPlugin # Link to Issue tracker, optional
website: https://mjmair.com                                        # Website, full path with protocol, optional
categories:                                                        # Mixins/integrations that are used, optional
    - Integration
    - Webhook
tags:                                                              # Freetext tags - treat them like kewords, optional
    - Shopify
    - Orders
---
A simple Integration into Shopify.

Let your orders from Shopify be created in autopilot, update your Inventory-Levels from InvenTree and vice-versa.

## Installation

1. Navigate to your InvenTree directory and cd into `src/InvenTree/plugins` and execute `git submodule add https://github.com/matmair/ShopifyIntegrationPlugin` there. Enable plugins in the general plugin settings and reload InvenTree.
2. Add a private app to your Shopify store (please register as a dev and use a development store. This is a PoC)
3. Go to the InvenTree settings and fill in the settings for the ShopifyIntegrationPlugin from your new private app.
4. Check out the new navigation tab.

## Caveat

Your instance must be reachable for webhooks from Shopify so use ngrok or something like that to expose your instance with HTTPS.

## State of the code

This code is bad. It is neither optimized nor is it CI/Cd ready or covered in any way.
I use this Plugin as a PoC to show what will be possible with the new system.

## Contribute

The whole plugin system is currently not even in the dev branch.
Feel free to submit issues or just send me a mail to dev AT mjmair.com


## No open source?

Currently I have defined no license so forking is a bad idea copyright-wise. This code should not be used as basis for anything - I will define a license once the plugin system gets released.
