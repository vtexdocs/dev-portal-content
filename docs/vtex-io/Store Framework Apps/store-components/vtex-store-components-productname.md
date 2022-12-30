---
title: "Product Name"
slug: "vtex-store-components-productname"
excerpt: "vtex.store-components@3.163.4"
hidden: false
createdAt: "2020-06-03T16:04:30.380Z"
updatedAt: "2022-11-22T18:39:23.151Z"
---
The `product-name` block is responsible for displaying a product name along with other information about the product, such as the **SKU** or **brand**.

![image](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-productname-0.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file, as in the following example:

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Add the `product-name` block to any child of the `store.product` template (Product Details Page template). For example:

```diff
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
+     "product-name"
    ]
  },
```

3. Then, declare the `product-name` block using the props stated in the [Props](#props) table. For example:

```json
  "product-name": {
    "props": {
      "showSku": true,
      "showBrandName": true
    }
  },
```

### Props

| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `classes` | `CustomCSSClasses` | Overrides default CSS handles. For further information, please refer to [this document](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only helpful if you're using this block as a React component. | `undefined` |
| `displayMode` | `enum` | Displays the product name (`plainText`) or the link to the product page (`linkToProductPage`). | `plainText`| 
| `showBrandName` | `boolean` | Displays the brand name. | `false`| 
| `showProductReference` | `boolean` | Displays the product reference code. | `false`| 
| `showSku` | `boolean` | Displays the SKU value. | `false` |
| `tag` | `string` | Defines the HTML tag of the product container. Possible values are: `div`, `h1`, `h2`, `h3`.  | `div` |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles |
| --- |
| `productBrand` |
| `productNameBrandLoader` |
| `productNameContainer` |
| `productNameLoader` |
| `productNameSkuLoader` |
| `productReference` |
| `productSku` |