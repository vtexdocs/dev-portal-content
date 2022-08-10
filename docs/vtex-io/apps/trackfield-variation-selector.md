---
title: "VARIATION SELECTOR"
slug: "trackfield-variation-selector"
excerpt: "trackfield.variation-selector@0.7.0"
hidden: true
createdAt: "2022-07-13T16:41:51.778Z"
updatedAt: "2022-07-13T16:41:51.778Z"
---
This will render a colors variations for call the costumer to a product page with the selected color variation

![Variation Selector](https://gitlab.com/acct.global/program-04/track-and-field-io/trackandfield.variation-selector/uploads/46c29ad2c0d00db641a5ef897ae673c5/image.png)

## Configuration

1. Adding the app as a theme dependency in the `manifest.json` file;

```diff
"dependencies": {
+  "trackfield.variation-selector": "0.x"
}
```

2. Declaring the app's main block inside a product-summary block from the theme. ( also works inside a `"store.product":{}`)

```json
{
  "product-summary.shelf": {
    "children": ["variation-selector"]
  }
}
```

### `Variation selector` props

| Prop name                | Type      | Description                                                       | Default value |
| ------------------------ | --------- | ----------------------------------------------------------------- | ------------- |
| `SpecificationFieldName` | `string`  | The Filter to the name of specification registered in the catalog | `"COR HEX"`   |
| `label`                  | `string`  | a label to be in the top os the variations,                       | `""`          |
| `maxDisplay`             | `number`  | number of max variations to be rendered                           | `4`           |
| `maxDisplayMobile`       | `number`  | number of max variations to be rendered on mobile                 | `5`           |
| `showMore`               | `boolean` | button to unhide the hidden variations, not showed on mobile      | `true`        |
| `showActive`             | `boolean` | highlight the button of the current product color                    | `true`        |

## Modus Operandi

There are scenarios in which an app can behave differently in a store, according to how it was added to the catalog, for example. It's crucial to register your product based on the following specification:

1. your main product needs to be registered with similars
2. your main product needs to have a specifications called: { `SpecificationFieldName` }
3. the `SpecificationFieldName` must be a valid hexadecimal color, example: { `#fff` }
4. check if the product search query is correctctly responding with the required informations

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

| CSS Handles                        |
| ---------------------------------- |
| `variations__container`            |
| `variations__colors`               |
| `variations__show-more`            |
| `variations__show-more-text`       |
| `variations__label`                |
| `variations__colors--{{modifier}}` |

### The Modifier is the color variation a product description

Check out some documentation models that are already live:

- [Apollo React](https://www.apollographql.com/docs/react/)
- [Vtex Render runtime](https://github.com/vtex-apps/render-runtime)
- [Vtex Css Handles](https://github.com/vtex/css-handles)
- [Vtex Product Context](https://github.com/vtex-apps/product-context)
- [Class Names](https://github.com/JedWatson/classnames)