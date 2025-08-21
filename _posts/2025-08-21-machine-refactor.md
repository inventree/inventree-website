---
author: SchrodingersGat
title: Machine Plugin Refactor
---

## Machine Plugin Refactor

In preparation for the upcoming 1.0.0 release, we have made some *breaking* changes to the machine registry plugin system.

These changes require that any existing plugins which implement custom machine drivers must be updated to use the new plugin system. A new *mixin* class, `MachineDriverMixin`, has been introduced to facilitate this transition.

Plugin developers should refer to the notes below to determine how to update their plugins.

### References

- [Machine Plugin Refactor PR](https://github.com/inventree/InvenTree/pull/10150)
- [MachineDriverMixin Documentation](https://docs.inventree.org/en/latest/plugins/mixins/machine/)

### Changes

The [linked pull request](https://github.com/inventree/InvenTree/pull/10150) makes a number of changes to both the [plugin system](https://docs.inventree.org/en/latest/plugins/) and [machine registry](https://docs.inventree.org/en/latest/plugins/machines/overview/).

The most significant of these changes is the introduction of the [MachineDriverMixin class](https://docs.inventree.org/en/latest/plugins/mixins/machine/), which now provides a standard interface for plugins which register custom machine drivers, or custom machine types.

Plugin developers can refer to linked pull request, in addition to the updated plugin mixin documentation, for more information on how to implement this new interface.

The required changes to existing plugins are minimal, and should be straightforward to implement.

### Example

As an example, the [inventree-brother-plugin](https://github.com/inventree/inventree-brother-plugin/) has been updated to use the new `MachineDriverMixin` class.

Refer to [this pull request](https://github.com/inventree/inventree-brother-plugin/pull/60) to see the changes made to the plugin.

