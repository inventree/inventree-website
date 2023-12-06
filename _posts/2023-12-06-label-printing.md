---
author: SchrodingersGat
title: Label Printing Updates
---

Available in the upcoming 0.13.0 stable release are some significant enhancements for label printing functionality. The label printing code has received a major overhaul to allow greater flexibility for label printing plugins, and enabling new features which were not previously possible.

### Label Printing Plugins

Previously, we had separate concepts for "native label printing" and "printing via plugins", with different software pipelines for each. This meant that:

- We had a lot of duplicated or inefficient code
- External printing plugins did not have the same available features

In [#5251](https://github.com/inventree/InvenTree/pull/5251) we refactored the label printing codebase entirely, and now all label printing is handled via plugins. A builtin plugin is provided which simply renders a single label as a `.pdf` file (maintaining previous behavior).

The refactor also provided a number of significant improvements and new functionality:

#### Background Printing

Printing plugins can run in the *foreground* - and return a `.pdf` object - or in the *background*. Background printing plugins return a response immediately (to prevent blocking of the web application) and the printing is offloaded to the background worker process. This allows flexibility to (for example) communicate with an external physical printing device.

#### Multiple Labels

Before this refactor, plugins received each label individually, with a single "print job" being sent to the printing plugin for each selected label. This was inefficient, and also meant that the printing plugin did not have the flexibility to handle simultaneous printing of multiple labels.

Now, printing plugins have access to the `print_labels` method, which receives *all* labels to be printed. If desired, multiple labels could be printed together onto a single paper sheet (*an example of this is below*).

The default implementation of `print_labels` simply calls the existing `print_label` method in sequence for each separate label - maintaining backwards compatibility for existing plugins.

### Printing Options

In [PR #5786](https://github.com/inventree/InvenTree/pull/5786) we introduced the concept of "printing options". Each printing plugin can provide a set of printing options which are presented to the user before initiating label printing. This allows for greater flexibility for label printing plugins.

For example, these run-time options could be used to:

- Select paper size
- Switch between multiple connected printers
- Specify the number of copies of each label to print
- etc

### Label Sheets

In [PR #5883](https://github.com/inventree/InvenTree/pull/5883), a builtin plugin was developed to print multiple labels to a single "sheet". This could be used to print a set of labels onto a specialized label sheet with peelable labels, or just a sheet of paper where the individual labels can be cut from the sheet.

This plugin also provides an example of how the [printing options](#printing-options) can be used to customize printing behavior at runtime.

#### Example

The images below demonstrate how the new label sheet plugin works.

**Select Items to Print**

Select a number of individual stock items, for which labels will be printed:

![Select Items](/assets/blog/select-labels.png)

**Label Printing Dialog**

Select the *InvenTree Sheet Label Printer* plugin:

![Select printer](/assets/blog/printer-dialog.png)

**Print Labels**

Labels are printed in a regular grid on the resulting sheet. Note that the first three cells have been skipped, as per the selected option in the printing dialog:

![Print labels](/assets/blog/print-labels.png)

### Available Soon

The new label printing features will be available in the upcoming 0.13.0 stable release. Or, available now in the master code branch!