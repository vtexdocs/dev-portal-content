---
title: "Product List"
slug: "vtex-product-list"
hidden: false
createdAt: "2020-06-03T15:19:16.041Z"
updatedAt: "2022-07-27T14:36:38.486Z"
---

The Product List component displays all items in the user's cart and informs the user when some of them are unavailable.

> ⚠️ Currently, the Product List only works with the [Minicart v2](https://developers.vtex.com/docs/guides/vtex-minicart/).

![product-list image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-list-0.png)

## Configuration

1. Add the Product List app to your theme's dependencies in `manifest.json`. For example:

```json
  "dependencies": {
    "vtex.product-list": "0.x"
  }
```

2. Add the `product-list` block to the `minicart-product-list` block (exported by the Minicart app). For example:

```json
  "minicart-product-list#example": {
    "blocks": ["product-list"]
  }
```

Once you added the `product-list` to the `minicart-product-list`, no further actions are required, as the block works with a default implementation behind the scenes. In other words, the Product List component is ready to be rendered.

### Advanced Configuration

Currently, the `product-list` default implementation is as follows:

```json
{
  "product-list": {
    "blocks": ["product-list-content-desktop", "product-list-content-mobile"]
  },
  "product-list-content-desktop": {
    "children": ["flex-layout.row#list-row.desktop"]
  },
  "flex-layout.row#list-row.desktop": {
    "children": [
      "flex-layout.col#image.desktop",
      "flex-layout.col#main-container.desktop"
    ],
    "props": {
      "fullWidth": true,
      "paddingBottom": "7",
      "paddingTop": "6",
      "colSizing": "auto",
      "preserveLayoutOnMobile": "true"
    }
  },
  "flex-layout.col#image.desktop": {
    "children": ["product-list-image"],
    "props": {
      "marginRight": "6"
    }
  },
  "flex-layout.col#main-container.desktop": {
    "children": [
      "flex-layout.row#sub-container.desktop",
      "flex-layout.row#message.desktop"
    ],
    "props": {
      "width": "grow"
    }
  },
  "flex-layout.row#sub-container.desktop": {
    "children": [
      "flex-layout.col#product-description",
      "flex-layout.col#quantity.desktop",
      "flex-layout.row#price-remove"
    ],
    "props": {
      "preserveLayoutOnMobile": "true",
      "colSizing": "auto"
    }
  },
  "flex-layout.col#quantity.desktop": {
    "children": [
      "flex-layout.row#quantity-selector.desktop",
      "flex-layout.row#unit-price.desktop"
    ],
    "props": {
      "marginLeft": "8"
    }
  },
  "flex-layout.row#price-remove": {
    "children": [
      "flex-layout.col#price.desktop",
      "flex-layout.col#remove-button.desktop"
    ],
    "props": {
      "colSizing": "auto"
    }
  },
  "flex-layout.row#quantity-selector.desktop": {
    "children": ["quantity-selector"],
    "props": {
      "preventHorizontalStretch": "true"
    }
  },
  "flex-layout.row#unit-price.desktop": {
    "children": ["unit-price#desktop"],
    "props": {
      "marginTop": "3",
      "preventHorizontalStretch": "true"
    }
  },
  "unit-price#desktop": {
    "props": {
      "textAlign": "center"
    }
  },
  "flex-layout.col#price.desktop": {
    "children": ["price#desktop"],
    "props": {
      "blockClass": "priceWrapper",
      "marginLeft": "6",
      "preventHorizontalStretch": "true",
      "verticalAlign": "middle"
    }
  },
  "price#desktop": {
    "props": {
      "textAlign": "right"
    }
  },
  "flex-layout.col#remove-button.desktop": {
    "children": ["remove-button"],
    "props": {
      "marginLeft": "6",
      "verticalAlign": "middle"
    }
  },
  "flex-layout.row#message.desktop": {
    "children": ["message#desktop"],
    "props": {
      "marginTop": "4"
    }
  },
  "message#desktop": {
    "props": {
      "layout": "cols"
    }
  },
  "product-list-content-mobile": {
    "children": ["flex-layout.row#list-row.mobile"]
  },
  "flex-layout.row#list-row.mobile": {
    "children": [
      "flex-layout.col#image.mobile",
      "flex-layout.col#main-container.mobile"
    ],
    "props": {
      "fullWidth": true,
      "paddingBottom": "6",
      "paddingTop": "5",
      "colSizing": "auto",
      "preserveLayoutOnMobile": "true"
    }
  },
  "flex-layout.col#image.mobile": {
    "children": ["product-list-image"],
    "props": {
      "marginRight": "5"
    }
  },
  "flex-layout.col#main-container.mobile": {
    "children": [
      "flex-layout.row#top.mobile",
      "flex-layout.row#quantity-selector.mobile",
      "flex-layout.row#unit-price.mobile",
      "flex-layout.row#price.mobile",
      "flex-layout.row#message.mobile"
    ],
    "props": {
      "width": "grow"
    }
  },
  "flex-layout.row#top.mobile": {
    "children": [
      "flex-layout.col#product-description",
      "flex-layout.col#remove-button.mobile"
    ],
    "props": {
      "colSizing": "auto",
      "preserveLayoutOnMobile": "true"
    }
  },
  "flex-layout.row#quantity-selector.mobile": {
    "children": ["quantity-selector"],
    "props": {
      "marginTop": "5",
      "preventHorizontalStretch": "true"
    }
  },
  "flex-layout.row#unit-price.mobile": {
    "children": ["unit-price"],
    "props": {
      "marginTop": "3"
    }
  },
  "flex-layout.row#price.mobile": {
    "children": ["price#mobile"],
    "props": {
      "marginTop": "5",
      "preventHorizontalStretch": "true"
    }
  },
  "price#mobile": {
    "props": {
      "textAlign": "left"
    }
  },
  "flex-layout.col#remove-button.mobile": {
    "children": ["remove-button"],
    "props": {
      "marginLeft": "3"
    }
  },
  "flex-layout.row#message.mobile": {
    "children": ["message#mobile"],
    "props": {
      "marginTop": "3"
    }
  },
  "message#mobile": {
    "props": {
      "layout": "rows"
    }
  }
}
```

By default implementation we mean that whenever you declare the `product-list` block in your store you're actually telling your theme to render the `json` above behind the scenes.

Therefore, in order to customize the `product-list` configuration, you can simply copy the code above, paste it and then change it as you wish.

| Block name                     | Description                                                                                                                                                                                                                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `product-list`                 | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-list-1.png) Top level block that must be declared in the `minicart-product-list` block to render a default detailed list with all products added to the shopping cart. |
| `product-list-content-desktop` | Creates the product list layout for desktop devices.                                                                                                                                                                                                                                                   |
| `product-list-content-mobile`  | Creates the product list layout for mobile devices.                                                                                                                                                                                                                                                    |
| `message`                      | Renders a message text about the product availability.                                                                                                                                                                                                                                                 |
| `product-name`                 | Renders the product names.                                                                                                                                                                                                                                                                             |
| `product-reference`            | Renders the product reference information.                                                                                                                                                                                                                                                             |
| `price`                        | Renders the product prices.                                                                                                                                                                                                                                                                            |
| `unit-price`                   | Renders the price for each product unit added to the cart.                                                                                                                                                                                                                                             |
| `product-list-image`           | Renders the product images.                                                                                                                                                                                                                                                                            |
| `product-brand`                | Renders the product brands.                                                                                                                                                                                                                                                                            |
| `product-variations`           | Renders the product variations.                                                                                                                                                                                                                                                                        |
| `product-quantity-label`       | Renders a product label that displays a sua quantidade de unidades added to the cart.                                                                                                                                                                                                                  |
| `quantity-selector`            | Renders a selector that allows users to add a chosen number of a product in their cart.                                                                                                                                                                                                                |
| `remove-button`                | Renders a button that allows users to remove a product from the list.                                                                                                                                                                                                                                  |

### `product-list` props

| Prop name          | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Default value |
| ------------------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `itemCountMode`    | `enum`   | Quantity badge behavior when displaying the number of total items added in Minicart. Possible values are: `total` (quantity badge displays the number of items added to the cart), `distinct` (quantity badge only displays the number of different products added to the cart), `totalAvailable` (quantity badge displays the number of available items added to the cart), and `distinctAvailable` (quantity badge only displays the number of different and available products added to the cart). | `distinct`    |
| `lazyRenderHeight` | `number` | The height (px) of each item's loading element.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `100`         |
| `lazyRenderOffset` | `number` | The distance (px) to the bottom of the viewport that each item should be at the moment of it's render.                                                                                                                                                                                                                                                                                                                                                                                                | `300`         |

### `message` props

| Prop name | Type   | Description                                                                                                                                                      | Default value |
| --------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `layout`  | `enum` | Availability message position on the list. Possible values are: `rows` (displaying the message in the product row) or `cols` (displaying in the product column). | `cols`        |

### `price` props

| Prop name       | Type      | Description                                                                           | Default value |
| --------------- | --------- | ------------------------------------------------------------------------------------- | ------------- |
| `textAlign`     | `string`  | Product price position on the list.                                                   | `left`        |
| `showListPrice` | `boolean` | Whether the product prices should be displayed on the list (`true`) or not (`false`). | `true`        |

### `unit-price` props

| Prop name              | Type     | Description                                                                                                                                                                                                                    | Default value |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `textAlign`            | `string` | Product unit prices position on the list.                                                                                                                                                                                      | `left`        |
| `unitPriceType`        | `enum`   | Defines whether the price type should be displayed. Possible values are: `sellingPrice` or `price`                                                                                                                             | `price`       |
| `unitPriceDisplay`     | `enum`   | Defines when the unit price should be displayed. Possible values are: `always` (unit price is always displayed) or `default` (unit price is only displayed when the number of products is greater than one).                   | `default`     |
| `displayUnitListPrice` | `enum`   | Defines whether the product list price should be displayed or not. Possible values are: `showWhenDifferent` (list price is displayed when it is different from the regular price) or`notShow` (list price is never displayed). | `notShow`     |

### `product-list-image` props

| Prop name | Type     | Description                      | Default value |
| --------- | -------- | -------------------------------- | ------------- |
| `width`   | `number` | Product image width (in pixels). | `96`          |

### `product-reference` props

|     Prop name      |   Type   |                                                                                    Description                                                                                    |    Default value     |
| :----------------: | :------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------: |
| `identifierLabel`  | `string` |                                                      Text label to be displayed to the left of the product reference value.                                                       |     `undefined`      |
| `identifierOption` |  `enum`  | Desired product reference data i.e. product identifier to be displayed. Possible options are: `ProductId`, `ProductSkuItemId`, `ProductReferenceId`, and `ProductSkuReferenceId`. | `ProductReferenceId` |

### `remove-button` props

| Prop name     | Type   | Description                                                                                                                                                                                                                                                                                                                     | Default value |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `variation`   | `enum` | Variation for the button visual proeminence based on the [VTEX Styleguide](https://styleguide.vtex.com/#/Components/Forms/Button). Possible values are: `primary`, `secondary`, `tertiary`, `inverted-tertiary`, `danger` and `danger-tertiary`.                                                                                | `danger`      |
| `displayMode` | `enum` | Defines how the remove button should be displayed. Possible values are: `icon-button` (to render an icon button) and `text-button` (to render a text message button). If you desire to [create a modal in the remove button](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-modals-using-icons), use the `icon-button` value. | `icon-button` |

### `quantity-selector` props

| Prop name              | Type   | Description                                                                                                                                                                                                                                                                                                   | Default value    |
| ---------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `mode`                 | `enum` | Mode of the quantity selector input. Possible values are `default` and `stepper`. On the default mode, the quantity stepper will initially render a dropdown component, and after the quantity exceeds 10, it will switch to an input. In the stepper mode it will always render a numeric stepper component. | `default`        |
| `quantitySelectorStep` | `enum` | Defines how the number of products that have unitMultiplier will works. Possible values are: `singleUnit` (the quantity will be not affected with the unitMultiplier) and `unitMultiplier` (the quantity will be affected with the unitMultiplier).                                                           | `unitMultiplier` |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles                          |
| ------------------------------------ |
| `availabilityMessageContainer`       |
| `availabilityMessageTextContainer`   |
| `availabilityMessageText`            |
| `productBrandName`                   |
| `productImageAnchor`                 |
| `productImageContainer`              |
| `productImage`                       |
| `productListAvailableItemsMessage`   |
| `productListItem`                    |
| `productListUnavailableItemsMessage` |
| `productName`                        |
| `productPriceContainer`              |
| `productPriceCurrency`               |
| `productPrice`                       |
| `productQuantityLabel`               |
| `productIdentifier`                  |
| `productIdentifierValue`             |
| `productIdentifierLabelValue`        |
| `productVariationsContainer`         |
| `productVariationsItem`              |
| `quantityDropdownContainer`          |
| `quantityDropdownMobileContainer`    |
| `quantityInputContainer`             |
| `quantityInputMobileContainer`       |
| `quantitySelectorContainer`          |
| `quantitySelectorWrapper`            |
| `quantitySelectorButton`             |
| `quantitySelectorDecrease`           |
| `quantitySelectorIncrease`           |
| `removeButtonContainer`              |
| `item`                               |
| `removeButton`                       |
| `unitPriceContainer`                 |
| `unitListPrice`                      |
| `unitPriceMeasurementUnit`           |
| `unitPricePerUnitCurrency`           |
