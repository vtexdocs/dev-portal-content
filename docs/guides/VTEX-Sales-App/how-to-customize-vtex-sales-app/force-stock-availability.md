---
title: "Force stock availability"
slug: "force-stock-availability"
hidden: false
createdAt: "2021-08-11T19:20:28.614Z"
updatedAt: "2022-02-24T20:39:44.565Z"
---
By default, if an SKU has zero stock in the store catalog, it is not possible to sell that SKU with inStore. However, there are cases where — even if the stock is zero — the SKU exists and is available in the physical store. And you may want to give your sales associates the ability to sell SKUs in this situation.

inStore allows this through a customization in the `checkout-instore-custom.js` file that enables the __Force Stock Availability__ feature. Check out the [How to customize VTEX Sales App](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-vtex-sales-app) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

1. To activate this feature, you need to include the `sellWithoutStockInHands` property in the `window.INSTORE_CONFIG` object, with the value `true`.

The code should look like the example below:

```json
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  sellWithoutStockInHands: true,\n}",
      "language": "javascript"
    }
  ]
}
```

>❗ Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities.

2. After making changes in the code, make sure you press the `Save` button.
