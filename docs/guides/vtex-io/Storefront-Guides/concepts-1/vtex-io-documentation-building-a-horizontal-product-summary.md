---
title: "Building a horizontal Product Summary"
slug: "vtex-io-documentation-building-a-horizontal-product-summary"
hidden: false
createdAt: "2020-12-15T16:28:08.220Z"
updatedAt: "2022-12-13T20:17:44.651Z"
---

The [Product Summary](https://developers.vtex.com/docs/guides/vtex-product-summary) is a VTEX native app responsible for displaying important product data in your store's components, such as the Shelf and the Minicart.

![product-summary-vertical](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-horizontal-product-summary-0.png)

Thanks to the [Flex Layout app](https://developers.vtex.com/docs/guides/vtex-flex-layout), it is possible to customize the default presentation showed above and thereby display the Product Summary blocks in a **horizontal alignment** to your users:

![horizontal-product-summary](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-horizontal-product-summary-1.png)

Learn in the instructions below how to use the powerful combination between the Flex Layout and the Product Summary apps in order to display your product data horizontally.

## Instructions

> ℹ️ This recipe requires previous understanding of the [Flex Layout app](https://developers.vtex.com/docs/guides/vtex-flex-layout). It is strongly advised that you read the app documentation before performing the steps below!

1. Make sure the Flex Layout app has been declared as a theme's dependency in the `manifest.json` file:

```json
"dependencies": {
  "vtex.flex-layout": "0.x"
}
```

2. Add the `flex-layout.row` block as a child of the `product-summary.shelf` and/or the `product-summary` blocks, according to the desired scenario:

```json
"product-summary.shelf": {
  "children": ["flex-layout.row#product-summary-mobile"]
},
```

> ℹ️ The `flex-layout.row` block allows its children to be displayed side by side on the UI.

> ⚠️ Notice that the block naming always depends on your store scenario. In the example above, `#product-summary-mobile` is only being used for identification purposes.

3. Add the `flex-layout.col` blocks as children of the `flex-layout.row` block to define the desired disposition of elements on the screen - the first `flex-layout.col`'s children will be displayed on the left side of the horizontal Product Summary, whereas the second will be on the right side:

```json
"flex-layout.row#product-summary-mobile": {
  "children": [
    "flex-layout.col#product-image",
    "flex-layout.col#product-summary-details"
  ],
},
```

4. Add the [`product-summary-image` block](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryimage) to the `flex-layout.col#product-image`'s children list and then declare it as desired:

```json
"flex-layout.col#product-image": {
  "children": ["product-summary-image#shelf"]
},
"product-summary-image#shelf": {
  "props": {
    "showBadge": false,
    "aspectRatio": "1:1",
    "maxHeight": 300
  }
},
```

5. Add the desired blocks responsible for displaying product data to the `flex-layout.col#product-summary-details`'s children list and then declare them as desired. For example:

```json
"flex-layout.col#product-summary-details": {
  "children": [
    "product-summary-name",
    "product-summary-space",
    "product-list-price",
    "flex-layout.row#selling-price-savings",
    "product-installments",
    "product-summary-sku-selector#buy-together"
  ],
  "props": {
    "marginLeft": 4
  },
},
"flex-layout.row#selling-price-savings": {
  "children": [
    "product-selling-price",
    "product-price-savings#summary"
  ],
  "props": {
    "colGap": 2,
    "preserveLayoutOnMobile": true,
    "preventHorizontalStretch": true,
    "marginBottom": 4
  },
},
"product-price-savings#summary": {
  "props": {
    "markers": ["discount"]
  }
},
"product-summary-sku-selector#buy-together": {
  "props": {
    "thumbnailImage": "skuvariation",
    "imageHeight": 28,
    "blockClass": "buyTogether",
    "visibility": "more-than-one"
  }
}
```

6. [Deploy your changes](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).
