---
title: "Enable cart transfer and capture between devices"
slug: "enable-cart-transfer-between-devices"
hidden: false
createdAt: "2021-08-11T19:17:03.518Z"
updatedAt: "2022-02-24T20:38:12.774Z"
---

The cart transfer and capture feature on VTEX Sales App allows a purchase started on one device to be completed on any other device present in the purchase flow, without the need to reinsert the items in the cart.

This is particularly useful for stores where the customer can be served by more than one sales associate. In that case, at each interaction with a different sales associate, they can add products to the same cart used by the previous sales associate. This same cart is transferred between one sales associate and the other, until the purchase is done.

This feature streamlines the order and facilitates the commissioning of the sales associates involved in the purchase, as it removes the need for labels with sales associate identification codes.

## Edit the `checkout-instore-custom.js` file

To activate the cart transfer and capture feature on VTEX Sales App, you must edit the `checkout-instore-custom.js` file. Check out the [How to customize VTEX Sales App](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-vtex-sales-app) guide for further information on how to access it.

Inside this file, you need to find the `window.INSTORE_CONFIG` object and add the `transferEnabled` property in it, with the value `true`. Do not remove any of the other properties present on that object.

The result should look like:

```json
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  transferEnabled: true,\n}",
      "language": "javascript"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "After making changes in the code, make sure you press the `Save` button."
}
```

## Check out your changes

After making this change, open the VTEX Sales App menu and update the data by clicking on the `Reset app local data` button.

Once this is done, a slider will appear at the bottom of the VTEX Sales App identification page:
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-cart-transfer-between-devices-0.png)
When you drag the screen to the right, you will see the **Cart Capture** option, as shown in the image below.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/enable-cart-transfer-between-devices-1.png)
For more information on how to use this feature, check our [guide](https://help.vtex.com/en/tracks/vtex-sales-app-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2hlBqxHlxgFo2o4R52pbsk).
