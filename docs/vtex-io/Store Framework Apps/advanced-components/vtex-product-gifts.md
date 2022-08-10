---
title: "Product Gifts"
slug: "vtex-product-gifts"
excerpt: "vtex.product-gifts@0.4.0"
hidden: false
createdAt: "2020-06-03T15:19:16.346Z"
updatedAt: "2022-06-09T17:19:17.708Z"
---
The Product Gifts app provides blocks responsible for displaying, in the Product Description block, all gifts available for a given product.

:information_source: *A product's gift is configured in a [Buy&Win promotion](https://help.vtex.com/tutorial/buy-and-win--tutorials_322)*

![product-gift](https://user-images.githubusercontent.com/52087100/75782082-20a08380-5d3d-11ea-9ae1-60873e03f1ac.png)

## Configuration

1. Add the `product-gifts` app to your theme's dependencies in the `manifest.json`. For example:

```json
"dependencies": {
  "vtex.product-gifts": "0.x"
}
```

Now, you are able to use all blocks exported by the `product-gifts` app. Check out the full list below:

| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `product-gifts`| ![mandatory](https://img.shields.io/badge/-Mandatory-red) Renders a default Product Gifts block implementation. | 
| `gift-text` | ![mandatory](https://img.shields.io/badge/-Mandatory-red) Reads Catalog data regarding the product's gifts and provides it to its children. |
| `product-gift-list` | Renders the available gifts in a list format. It also provides context for its 3 children listed below. |
| `gift-name` | Renders the product's gift name. |
| `gift-image` | Renders the product's gift image.|
| `gift-description` | Renders the gift's description provided by the `product-gift-list` block. |

2. Add the `product-gifts` block to your `store.product` template:

```jsonc
"store.product": {
  "children": [
    // (...)
    "product-gifts",
  ]
}
```

When added to the `store.product` template but not declared with any children or prop, the Product Gifts block is rendered even so.

For the rendering, it uses the following block implementation behind the scenes:

```json
{
  "product-gifts": {
    "props": {
      "maxVisibleItems": {
        "desktop": 2,
        "mobile": 1
      }
    },
    "children": ["flex-layout.row#product-gifts-text", "product-gift-list"]
  },

  "flex-layout.row#product-gifts-text": {
    "props": {
      "verticalAlign": "middle",
      "colSizing": "auto",
      "preserveLayoutOnMobile": true
    },
    "children": [
      "rich-text#product-gifts",
      "flex-layout.col#product-gifts-text"
    ]
  },
  "flex-layout.col#product-gifts-text": {
    "children": ["gift-text"],
    "props": {
      "verticalAlign": "middle"
    }
  },
  "rich-text#product-gifts": {
    "props": {
      "text": "**+ GIFT**"
    }
  },
  "gift-text": {
    "props": {
      "text": "{exceedingItems, plural, =0{ } one {+ # gift} other {+ # gifts}}"
    }
  },
  "product-gift-list": {
    "children": ["flex-layout.row#gift"]
  },
  "flex-layout.row#gift": {
    "props": {
      "fullWidth": true
    },
    "children": ["flex-layout.col#gift-name-description", "gift-image"]
  },
  "flex-layout.col#gift-name-description": {
    "props": {
      "verticalAlign": "middle",
      "rowGap": 3
    },
    "children": ["gift-name", "gift-description"]
  }
}
```

### Advanced configuration

If desired, you can change the Product Gifts default implementation by explicitly declaring the code showed above in your `store.product` template.

As a result, you will be able to configure the Product Gifts behavior by using all available props for each block:

- **`product-gifts`**

![product-gifts](https://user-images.githubusercontent.com/27777263/75771051-ee385b80-5d27-11ea-8600-5ea7f47ff64c.png)

| Prop name         | Type                        | Description                                            | Default value |
| ----------------- | --------------------------- | ------------------------------------------------------ | ------------- |
| `maxVisibleItems` | `number` &#124; `"showAll"` | Maximum number of gifts that will be displayed at once | `"showAll"`   |

- **`gift-text`**

![gift-text](https://user-images.githubusercontent.com/27777263/75767717-01e0c380-5d22-11ea-8054-4440438a5441.png)

| Prop name | Type     | Description                                                                                         | Default value                                                       |
| --------- | -------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `text`    | `String` | A translatable string (according to [ICU pattern](https://formatjs.io/guides/message-syntax/)) that has variables that might be used to render any desired text regarding the gifts. | `"{exceedingItems, plural, =0{ } one {+ # gift} other {+ # gifts}}"` |

You can configure the string received by the `text` prop using the following variables:

| Variable name    | Description                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| `exceedingItems` | Number of items that were not rendered because of the `maxVisibleItems` prop of `product-gifts`. |
| `totalGifts`     | Total number of gifts available.                                                               |
| `visibleItems`   | Number of items that are being rendered.                                                       |

-  **`gift-name`**

![gift-name](https://user-images.githubusercontent.com/27777263/75767722-03aa8700-5d22-11ea-8150-2cbe2a7bb37a.png)

| Prop name           | Type      | Description                                                               | Default value |
| ------------------- | --------- | ------------------------------------------------------------------------- | ------------- |
| `linkToProductPage` | `Boolean` | Whether or not the `gift-name` block should be a link to the gift's product page. | `false`       |
| `nameType` | `enum` | Name type to be displayed alongside the gift. Possible values are:  `productName` (displays the gift's product name) and `skuName` (displays the gift's SKU name). | `skuName` |

- **`gift-image`** 

![gift-image](https://user-images.githubusercontent.com/27777263/75767721-02795a00-5d22-11ea-8f51-fe80664b7f68.png)

| Prop name    | Type                     | Description                                     | Default value |
| ------------ | ------------------------ | ----------------------------------------------- | ------------- |
| `maxWidth`   | `Number` &#124; `String` | Gift image maximum width.                    | `125`         |
| `maxHeight`  | `Number` &#124; `String` | Gift image maximum height.                   | `125`         |
| `minWidth`   | `Number` &#124; `String` | Gift image minimum width.                    | `125`         |
| `minHeight`  | `Number` &#124; `String` | Gift image minimum height.                   | `125`         |
| `imageLabel` | `String`                 | The label of the image that should be rendered. | `undefined`   |

:information_source: *If no image label is defined, the* `gift-image` *block will use the first available image from the product's SKU.*

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for that block:

| CSS Handles              |
| ------------------------ |
| giftDescription          |
| giftListItem             |
| giftNameLink             |
| giftNameText             |
| productGiftListContainer |
| productGiftText          |
| productGiftsContainer    |