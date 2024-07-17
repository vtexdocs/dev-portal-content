---
title: "Master Data v1: Calculated Field and Change field value trigger deprecation"
slug: "2024-04-17-master-data-v1-calculated-field-and-change-field-value-trigger-deprecation"
type: "deprecated"
excerpt: "The Calculated field and the Change field value trigger action will be discontinued in Master Data v1."
createdAt: "2024-04-17T16:47:00.000Z"
updatedAt: "2024-04-17T09:30:00.000Z"
---

On June 17, we will deprecate the following settings in [Master Data v1](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw): **Calculated Field** and the **Change field value** trigger action.

Instead of using these settings, we recommend one of the following alternatives to update field values, depending on which Master Data version you want to use:

- [Creating a VTEX IO service to interact with Master Data v1](https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services)
- [Creating an app to communicate with Master Data v2](https://developers.vtex.com/docs/guides/create-master-data-crud-app)

## What has changed?

These two dynamic settings will be deprecated in Master Data v1.

Existing **Calculated Fields** and triggers that use the **Change field value** action will stop working on the same date. Check the [What needs to be done?](#what-needs-to-be-done) section for more information on how to adapt to these changes.

### Calculated Field

**Calculated Field** was a setting within [data entity](https://help.vtex.com/en/tutorial/data-entity--tutorials_1265) fields that allowed merchants to run C# code to recalculate the field value whenever a new document was added or updated.

This type of field, illustrated below, will no longer be available after June 17. Existing calculated fields will stop working on the same date.

![calculated-field](https://github.com/vtexdocs/dev-portal-content/assets/77292838/b5907281-d7c8-42ca-8e31-d6dfe1329f69)

### Change field value

When [setting up trigger actions](https://help.vtex.com/en/tutorial/creating-trigger-in-master-data--tutorials_1270), the **Change field value** option allowed merchants to add C# code to modify the value of selected fields upon trigger execution.

The **Change field value** option, illustrated below, will no longer be available when setting up trigger actions after June 17. Triggers created previously with this action will only work until the same date.

![change-field-value](https://github.com/vtexdocs/dev-portal-content/assets/77292838/e0278a99-33ff-4c72-be19-de39cd58e0b7)

## What needs to be done?

If you need to update Master Data field values based on a trigger, we recommend setting up a trigger that [sends an HTTP request](https://help.vtex.com/en/tutorial/creating-trigger-in-master-data--tutorials_1270#sending-an-http-request) to a VTEX IO app that communicates with Master Data. This must be done before June 17.

For instructions on how to create this type of app, check the following guides:

- [Creating a VTEX IO service to interact with Master Data v1](https://developers.vtex.com/docs/guides/interacting-with-master-data-v1-through-vtex-io-services)
- [Creating an app to communicate with Master Data v2](https://developers.vtex.com/docs/guides/create-master-data-crud-app)
