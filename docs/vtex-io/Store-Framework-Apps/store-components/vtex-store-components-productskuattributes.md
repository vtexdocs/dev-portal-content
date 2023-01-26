---
title: "Product SKU Attributes"
slug: "vtex-store-components-productskuattributes"
excerpt: "vtex.store-components@3.163.4"
hidden: false
createdAt: "2020-09-21T20:47:31.412Z"
updatedAt: "2022-11-22T18:39:23.237Z"
---
The `product-sku-attributes` block displays a list of the current SKU variations of a product.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-productskuattributes-0.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```diff
  "dependencies: {
+   "vtex.store-components": "3.x"
  }
```  

2. Add the `product-sku-attributes` block to any child of the `store.product` template (Product Details Page template). For example:

```diff
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
+     "product-sku-attributes"
    ]
  },
```

3. Then, declare the `product-sku-attributes` block using the props stated in the [Props](#props) table. For example:

### Props

| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `classes` | `CustomCSSClasses` | Overrides default CSS handles. To better understand how this prop works, check [this document](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only helpful if you're using this block as a React component.| `undefined` |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `attributeLine` |
| `attributeName` |
| `attributeValue` |
| `ProductSKUAttributesContainer` |