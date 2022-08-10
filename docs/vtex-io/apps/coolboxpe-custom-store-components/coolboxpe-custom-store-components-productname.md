---
title: "Product Name"
slug: "coolboxpe-custom-store-components-productname"
excerpt: "coolboxpe.custom-store-components@0.2.360"
hidden: true
createdAt: "2022-07-05T09:42:34.359Z"
updatedAt: "2022-08-09T20:06:07.663Z"
---
The `ProductName` is a block responsible for **displaying the product name** along other informations such as **SKU** or **brand**.

![image](https://user-images.githubusercontent.com/284515/70231165-8f6b4200-1738-11ea-9f06-3583c08fc693.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```json
  "dependencies: {
    "vtex.store-components": "3.x"
  }
```

2. Add the `product-name` block to any block below `store.product` (Product template). For example:

```json
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
      "product-name"
    ]
  },
  "product-name": {
    "props": {
      "showSKU": true,
      "showBrandName": true
    }
  },
```

| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `showSku` | `Boolean` | Show product SKU | `false` |
| `showProductReference` | `Boolean` | Show product reference | `false`| 
| `showBrandName` | `Boolean` | Show brand name | `false`| 

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| --- |
| `productNameContainer` |
| `productBrand` |
| `productSku` |
| `productReference` |
| `productNameLoader` |
| `productNameBrandLoader` |
| `productNameSkuLoader` |