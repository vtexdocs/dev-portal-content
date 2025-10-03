---
title: Minimum items on Shelf 
excerpt: "The minimum number of items that can be displayed on a Shelf component can now be set regardless of the display mode (mobile, tablet or desktop)."
createdAt: "2019-09-08T14:47:00.000Z"
type: 'info'
---
The minimum number of items that can be displayed on a Shelf component can now be set regardless of the display mode (mobile, tablet or desktop).

## What has changed

Previously, it was only possible to set the maximum number of items displayed on a shelf by using the prop `itemsPerPage`. This configuration aimed to limit the number of items displayed on large screens. However, the prop did not work with small screens, that always displayed one product per row.

By setting the new prop `minItemsPerPage`, you can also control the number of items displayed even on the smallest screen size.

## Main advantages

Using these two props together, you can control how many items are displayed on any screen size, with the component adjusting itself for intermediate sizes.

For example, if you want to always display 2 items on mobile, you just need to set `minItemsPerPage: 2`. For a maximum of 5 items on a large screen, you could declare the already existing prop `itemsPerPage: 5` in the same block.

## What you need to do

1. Make sure you’re running version __1.23.0__ or newer of the [__Shelf__](https://github.com/vtex-apps/shelf) component and that it’s declared in your blocks files.
2. Configure your shelf block with the `minItemsPerPage` prop. Its value must be the minimum number of slides you want on the screen. > ⚠️ Its default value is 1.

:eyes: The `minItemsPerPageprop` is part of the `productList` set of props. An example on how to set it in a valid block can be seen below:

```json
"shelf": {
  "props": {
    "orderBy": "OrderByTopSaleDESC",
    "productList": {
      "maxItems": 10,
      "itemsPerPage": 4,
      "minItemsPerPage": 2,
      "scroll": "BY_PAGE",
      "arrows": true,
      "titleText": "New collection",
      "hideUnavailableItems": true,
      "summary": {
        "isOneClickBuy": false,
        "showBadge": true,
        "badgeText": "OFF",
        "buyButtonText": "Comprar",
        "displayBuyButton": "displayButtonHover",
        "showCollections": false,
        "showListPrice": true,
        "showLabels": false,
        "showInstallments": true,
        "showSavings": true,
        "name": {
          "showBrandName": false,
          "showSku": false,
          "showProductReference": false
        }
      }
    }
  }
}
```
