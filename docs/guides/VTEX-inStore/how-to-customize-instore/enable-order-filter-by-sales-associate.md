---
title: "Enable order filter by sales associate"
slug: "enable-order-filter-by-sales-associate"
hidden: false
createdAt: "2021-08-11T19:19:18.457Z"
updatedAt: "2022-02-24T20:39:26.065Z"
---
Sales associates can see the full list of completed orders on inStore. However, it sometimes makes sense for a sales associate to see only the orders they have personally completed. To enable this option, it is necessary to edit the `checkout-instore-custom.js` file. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

Inside this file, you must find the `window.INSTORE_CONFIG` object and add the `OMSFilters` object to it.

The code snippet should look like the example below:
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  OMSFilters: {\n    'f_UtmSource': '{{ vendor.storeId }}',\n    'CallCenterOperatorEmail': '{{ vendor.username }}',\n  },\n}",
      "language": "javascript"
    }
  ]
}
[/block]
With that, the app will filter orders to display only those made by the sales associate currently logged in on inStore.
>❗ Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities.

[block:callout]
{
  "type": "info",
  "body": "After making changes in the code, make sure you press the `Save` button."
}
[/block]

## Check out your changes

To see the reflected changes on inStore, enter the menu and click the `Reset app local data` button. After this, each sales associate will only see orders they were responsible for.