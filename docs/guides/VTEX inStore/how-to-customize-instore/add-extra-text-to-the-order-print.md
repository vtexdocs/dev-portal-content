---
title: "Add extra text to the order summary print"
slug: "add-extra-text-to-the-order-print"
hidden: false
createdAt: "2021-08-11T19:20:47.780Z"
updatedAt: "2022-02-24T20:40:37.713Z"
---

By default, the order summary print does not contain any custom text. If you want to add extra text to the order print, it is necessary to edit the file `checkout-instore-custom.js`. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

In this file, inside the `window.INSTORE_CONFIG` object, add the `printedOrderExtraText` property. The value of this property will be the new printed text. The code should look like the example below:

```js
window.INSTORE_CONFIG = {
  printedOrderExtraText: 'Write your extra text here',
}
```

> ❗ Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object, to avoid breaking other functionalities.

After making changes in the code, make sure you press the `Save` button.

Once you reload inStore, whenever a sales associate prints an order, the text you configured will appear on the order summary printout.

## Example

Before adding extra text, the printout of the order summary has the following format:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/how-to-customize-instore/add-extra-text-to-the-order-print-0_34.png)
In the example below, we changed the `checkout-instore-custom.js` file by inserting the following extra text:

```js
window.INSTORE_CONFIG = {
  printedOrderExtraText: 'Essa nota não tem validade fiscal',
}
```

Now, whenever an order summary is printed, we will get the following result:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20inStore/how-to-customize-instore/add-extra-text-to-the-order-print-1_48.png)
