---
title: "Composition"
slug: "vtex-io-documentation-composition"
hidden: false
createdAt: "2020-11-23T13:33:26.394Z"
updatedAt: "2022-12-13T20:17:44.627Z"
---

The composition property in the `interfaces.json` file defines how React components behave and structure themselves when used as blocks in a VTEX Store Theme. Components in VTEX are arranged in a parent-child hierarchy, allowing developers to build flexible and well-organized UI layouts.

>ℹ️ Note: The `composition` property determines how child blocks are organized, not the position of the parent block itself.

## Types of composition

The `composition` property can be set to one of three types: `blocks`, `children`, or `slots`. Each type offers a different approach for organizing and positioning child components within the parent block.

>ℹ️ Recommendation: For greater flexibility, use the [`slots`](#slots) composition whenever possible.

### Blocks

The `blocks` composition is the default method for organizing child blocks. When using this composition, all child blocks must be explicitly listed in a `blocks` array. 

These child blocks have predetermined, fixed positions in the UI that are dictated by the React component’s structure, regardless of their placement in the store theme's `json` file.

#### Example

```json
"shelf#home": {
  "blocks": ["product-summary.shelf"]
},
```

In this example, the `product-summary.shelf` block is listed as a child of the `shelf#home` block using the `blocks` composition. This means the `product-summary.shelf` will be positioned in a predetermined location in the UI.

### Children

The `children` composition allows for more flexibility in determining the order of child blocks. Child blocks are declared in a `children` array, and their order in this array directly controls their positioning on the page. 

The first block in the `children` array will appear first, followed by the others in sequence.

#### Example

```json
"product-summary.shelf": {
  "children": [
    "product-summary-name",
    "product-summary-description",
    "product-summary-image",
    "product-summary-price",
    "product-summary-sku-selector",
    "product-summary-buy-button"
  ]
},
```

In this example, `product-summary.shelf` has several child blocks listed in its `children` array. The order in which these blocks appear in the array determines their position on the page. For example, `product-summary-name` will appear first, followed by `product-summary-description`, and so on.

### Slots

The `slots` composition is the most flexible option. Instead of listing child blocks in an array, you define them using React props, allowing for more dynamic control of how child blocks are passed to the parent component. Each child block can be assigned a custom prop name, which is defined by the parent block.

> For more information on using slots, refer to the [Slots](https://developers.vtex.com/docs/guides/vtex-io-documentation-slots/) guide.

#### Example

```json
{
  "hello-world": {
    "props": {
      "Icon": "icon-caret#point-up"
    }
  },
  "icon-caret#point-up": {
    "props": {
      "orientation": "up"
    }
  }
}
```

In this example, the `icon-caret#point-up` block is declared as a prop of the `hello-world` block using the `slots` composition. The prop name, `Icon`, is custom-defined by the parent block.

