---
title: "Product Specifications"
slug: "coolboxpe-custom-store-components-productspecifications"
excerpt: "coolboxpe.custom-store-components@0.2.360"
hidden: true
createdAt: "2022-07-05T09:42:34.312Z"
updatedAt: "2022-08-09T20:06:07.796Z"
---
`ProductSpecifications` is a block that shows the technical [specifications](https://help.vtex.com/tutorial/what-are-fields-or-specifications--2lB4AgibEseceMggKE2k2m) of a product.

![Screen Shot 2019-12-27 at 14 07 30](https://user-images.githubusercontent.com/27777263/71525823-4bd8a380-28b2-11ea-8d5c-7678426ec1ab.png)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json`;

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Add the `product-specifications` block to any block bellow `store.product` (Product template). For example:

```json
  "store.product": {
    "children": [
      "flex-layout.row#product",
    ]
  },
  "flex-layout.row#product": {
    "children": [
      "product-specifications#product"
    ]
  },
   "product-specifications#product": {
    "props": {
      "shoudCollapseOnTabChange": true,
      "collapsible": "desktopOnly"
    }
  },
```

⚠️ The block consumes data from the product-context therefore it should only be used in the store.product block i.e. in the product template.

| Prop name                | Type                                                       | Description                                                                                                            | Default value |
| ------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------- |
| hiddenSpecifications     | `String[]`                                                 | Type names of specifications you want to hide                                                                          | `[]`          |
| visibleSpecifications    | `String[]`                                                 | Type names of specifications you want to appear. Only provide one of `hiddenSpecifications` or `visibleSpecifications` | `[]`          |
| showSpecificationsTab    | `Boolean`                                                  | Choose if you want to show the component with tabs mode                                                                | `false`       |
| shoudCollapseOnTabChange | `Boolean`                                                  | If it should collapse if you change the tab                                                                            | `false`       |
| collapsible              | `mobileOnly`&#124;`desktopOnly`&#124;`always`&#124;`never` | Control when should the content of the specifications be collapsible                                                   | `always`      |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                                |
| ----------------------------------------- |
| `specificationsTitle`                     |
| `specificationsTableContainer`            |
| `specificationsTable`                     |
| `specificationsTabsContainer`             |
| `specificationsTab`                       |
| `specificationsTablePropertyHeading`      |
| `specificationsTableSpecificationHeading` |
| `specificationItemProperty`               |
| `specificationItemSpecifications`         |