---
title: "Set up the order summary printing"
slug: "set-up-the-order-summary-printing"
hidden: false
createdAt: "2021-08-12T13:20:35.444Z"
updatedAt: "2022-02-24T20:40:08.499Z"
---
When a sales associate completes an order with inStore, they can print a summary of that order, as described in the [Print order summary](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/5UeqJA3sHp5goJacvHwPoS) article on Help Center.

 To enable this feature, you must follow the steps below to customize inStore's JavaScript file and make additional settings on the inStore app main menu.
[block:html]
{
  "html": "<br>"
}
[/block]
## Edit the `checkout-instore-custom.js` file

1. Open the `checkout-instore-custom.js` file, available in the Admin of your VTEX account (if you do not know how to access this file, check out the guide on [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore).

2. In that file, add the `configureDeviceEnabled` property with the value `true`. In addition, add the `printingConfig` object, and inside it add the `printByBroker` property, also with the value `true`.

The code should look like the example below:
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = { \n  configureDeviceEnabled: true, \n  printingConfig: { \n    printByBroker: true \n  },\n}",
      "language": "javascript"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "danger",
  "body": "Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities."
}
[/block]
3. After making changes in the code, make sure you press the `Save` button.

This change will make the `Configure device` option appear in the inStore main menu. It is through this option that you will configure the printer.

[block:html]
{
  "html": "<br>"
}
[/block]
### [OPTIONAL] Print automatically

There is an option to automatically print the order summary as soon as the order is completed. To enable it, add the <code>printPageAutomatically</code> property with the value <code>true</code> inside the <code>printingConfig</code> object. See below how the code would look like in this case.
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = { \n  configureDeviceEnabled: true, \n  printingConfig: { \n    printByBroker: true,\n    printPageAutomatically: true\n  },\n}",
      "language": "javascript"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
## Configure the printer device on inStore

The next step is to configure the printer on inStore. Make sure you follow the instructions on the [Print order summary](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/5UeqJA3sHp5goJacvHwPoS) article on Help Center to do so.
[block:callout]
{
  "type": "info",
  "body": "To connect a printer to the inStore system, it is necessary to have a pair of VTEX credentials (AppKey and AppToken) with the appropriate access permissions. Read this [Authentication](https://developers.vtex.com/vtex-rest-api/docs/getting-started-authentication) guide to learn more about these credentials.\n\nWe recommend that the role linked to these credentials is `inStore Sales Person`. However, a profile with access to more Admin modules, such as `Admin Super`, can also be used."
}
[/block]