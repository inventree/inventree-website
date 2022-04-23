---
publisher: matmair
title: We have news now!
---
Hi there,
here is something new: News!

These news items will automatically show up for all admins in the **homepage** as the *lowest* category (starting with the next minor release **0.7.0**).
If you do not want to see them there you can **disable** the function in your user-settings. There is also the option to disable news globally in the general server settings.

### But why?
The good news first: We will **not** spam you with this function daily.  
It is more of a tool to *communicate* with the *power users* and *admins*. There is wide array of reasons for the dev-team to want to communicate with you.  
For example when we
- are looking for inputs on new big, roadmap worthy FRs
- want to show you a cool show-and-tell as an inspiration
- have security advisories (please also follow releases - we always try to push new releases as fast as possible)
- are planning to depreciate a function and want to gauge if there are still users

### How does it work?
Like the update-checks we are using the infrastructure GitHub provides.  
While the checks use the GitHub APIs, news are gathered from an **RSS-feed** that is served via **GitHub Pages**. The Jekyll-based website generates through a **GitHub Action** and then passes the **static output** to Pages, where it gets hosted for free (thank you GitHub) and delivered through CDNs worldwide.
On your InvenTree instance the **background worker** loads the RSS-feed on a regular basis and creates **entries** for the news items and **notifications** for all applicable users.

### And my data?
As listed above we are using GitHub pages for this feature. We are not introducing additional trackers to that so the [general InvenTree privacy statement](https://inventree.readthedocs.io/en/latest/privacy/) applies.  
The short version: we **do not sell your data** or share it with third parties. We cannot guarantee what readthedocs and GitHub do with the metrics. We might use them as a metric for the stats section of the site. However, we get very little *actionable* information from that, a screenshot of the total info available is shown below.

![Sample screenshot of the collected analytics]({{ '/assets/news/2022-04-23-news-are-starting/media1.png' | relative_url }})
*Sample screenshot of the collected analytics*
