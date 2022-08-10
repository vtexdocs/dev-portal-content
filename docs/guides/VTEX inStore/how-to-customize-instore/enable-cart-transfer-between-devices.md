---
title: "Enable cart transfer and capture between devices"
slug: "enable-cart-transfer-between-devices"
hidden: false
createdAt: "2021-08-11T19:17:03.518Z"
updatedAt: "2022-02-24T20:38:12.774Z"
---
The cart transfer and capture feature on inStore allows a purchase started on one device to be completed on any other device present in the purchase flow, without the need to reinsert the items in the cart.

This is particularly useful for stores where the customer can be served by more than one sales associate. In that case, at each interaction with a different sales associate, they can add products to the same cart used by the previous sales associate. This same cart is transferred between one sales associate and the other, until the purchase is done. 

This feature streamlines the order and facilitates the commissioning of the sales associates involved in the purchase, as it removes the need for labels with sales associate identification codes.

[block:html]
{
  "html": "<br>"
}
[/block]
## Edit the `checkout-instore-custom.js` file

To activate the cart transfer and capture feature on inStore, you must edit the `checkout-instore-custom.js` file. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access it.

Inside this file, you need to find the `window.INSTORE_CONFIG` object and add the `transferEnabled` property in it, with the value `true`. Do not remove any of the other properties present on that object. 

The result should look like:
[block:code]
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
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
## Check out your changes

After making this change, open the inStore menu and update the data by clicking on the `Reset app local data` button.

Once this is done, a slider will appear at the bottom of the inStore identification page:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/41c68e3-24._Enable_cart_transfer_between_devices_-_1_-_EN.png",
        "24._Enable_cart_transfer_between_devices_-_1_-_EN.png",
        852,
        1722,
        "#efeff1"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]
When you drag the screen to the right, you will see the __Cart Capture__ option, as shown in the image below.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/742d448-24._Enable_cart_transfer_between_devices_-_2_-_EN.png",
        "24._Enable_cart_transfer_between_devices_-_2_-_EN.png",
        844,
        1707,
        "#e4e8f1"
      ],
      "sizing": "smart"
    }
  ]
}
[/block]
For more information on how to use this feature, check our [guide](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/2hlBqxHlxgFo2o4R52pbsk).