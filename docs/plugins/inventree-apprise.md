---
name: InvenTree Apprise
author: matmair
license: MIT
open_source: true
stable: true
maintained: true
pypi: true
package_name: inventree-apprise
github: https://github.com/matmair/inventree-apprise
issue_tracker: https://github.com/matmair/inventree-apprise/issues
website: https://mjmair.com
categories:
    - Notifications
tags:
    - Apprise
    - 3rd party integration
    - Discord
    - IFTTT
    - Matrix
    - Microsoft Teams
    - Slack
    - Twilio
    - 
---
Send notifications from InvenTree via Apprise

## Setup

1. Install this plugin in the webinterface with the packagename `inventree-apprise`

1. Enable the plugin in the plugin settings. You need to be signed in as a superuser for this.
**The server will restart if you enable the plugin**

1. Add all endpoints you want to use in the plugin settings. You can use the [Apprise URL Syntax](https://github.com/caronc/apprise#supported-notifications).

## License
This project is licensed as MIT. Copy and do what you want - maybe tag your new plugin so others can find it. The more the merrier.
