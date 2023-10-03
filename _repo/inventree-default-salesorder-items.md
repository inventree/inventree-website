---
name: Default sales order items                                                    # Name of the plugin (should be either NAME, TITLE or SLUG)
author: lippoliv                                                           # Maintainer must be the same as the publisher reference
license: MIT                                                                      # License, we prefer open source
open_source: true                                                                 # Is this project licensed with an OSI-approved license - aka 'open source'
stable: true                                                                      # Is this project stable? Should users deploy this in their instace?
maintained: true                                                                  # Is this project maintained?
pypi: false                                                                        # Is availanle via PyPi
package_name: inventree_default_salesorder_items                                            # Name of the package on the index, required if pypi true
github: https://github.com/lippoliv/inventree-default-salesorder-items                     # Ĺink to repo in GitHub, one of github, gitlab or source is required
gitlab: 
source: 
issue_tracker: https://github.com/lippoliv/inventree-default-salesorder-items/issues       # Link to Issue tracker, optional
website: https://github.com/lippoliv/inventree-default-salesorder-items                                                    # Website, full path with protocol, optional
categories:                                                                       # Mixins/integrations that are used, optional
    - Event
    - Settings
tags:                                                                             # Freetext tags - treat them like kewords, optional
    - Sales orders
    - Parts
    - Automation
---
Add default parts (configurable) to every newly created sales order automatically.