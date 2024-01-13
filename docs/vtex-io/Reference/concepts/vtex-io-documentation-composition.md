---
title: "Composition"
slug: "vtex-io-documentation-composition"
hidden: false
createdAt: "2020-11-23T13:33:26.394Z"
updatedAt: "2022-12-13T20:17:44.627Z"
---

In frontend apps, the `store/interfaces.json` file plays a vital role in establishing connections between blocks and React components. Each entry within the `interfaces.json` file can have an optional property named `composition`, which defines how components interact and structure the layout.

The composition property does define the behavior of the block's children. The are three distinct composition types:

- **Blocks**: The UI positioning of the child blocks is predefined and is not affected by code positioning in the Store Theme app.
- **Children**: The order in which these child blocks are declared in a Store Theme app affects their positioning on the store page.
- **Slots**: Unlike the other compositions, the `slots` composition offers more flexibility. Child blocks are declared using regular React props within the parent block, enabling customization and dynamic adjustments. They are like placeholders where any suitable block can be placed, providing a high degree of adaptability.

Understanding these compositions is pivotal in defining the behavior and layout of React components within your Store Theme.

## Composition comparison

|                 | UI positioning                            | Flexibility                             |
|-----------------------|-------------------------------------------|-----------------------------------------|
| **Blocks**    | Predefined positioning unaffected by the Store Theme code order. | Fixed layout structure.               |
| **Children** | Order-dependent layout based on the Store Theme app declaration. | Dynamic, order-dependent positioning. |
| **Slots**    | Prop-based declaration. | Highly flexible and customizable.     |

## Blocks

When using a block with `blocks` composition, consider the following:

- **Declaration:** Child blocks must be declared within the parent block's `blocks` array.
- **Fixed positioning:** Child blocks have a predefined position on the UI, which is unaffected by their code positioning in the Store Theme app.

Consider the following example of the `video` block, which has a `blocks` composition:

<table>
<tr>
<th>`interfaces.json`</th>
<th>`blocks.json`</th>
</tr>
<tr>
<td>

```json
{
  "video": {
    "component": "Video",
    "content": {
      "$ref": "app:vtex.store-video#/definitions/Video"
    }
  }
}
```

</td>
<td>

```json
"store.custom#about-us": {
  "blocks": [
    "video"
  ]
},
```

</td>
</tr>
</table>

The `video` is specified as block within the `store.custom#about-us` block using the `blocks` composition.

## Children

Blocks with the `children` composition allow for:

- **Order dependency:** Child blocks' order in the Store Theme app dictates their layout positioning on the store page.
- **Dynamic positioning:** The order of declaration impacts the placement of child blocks on the UI. The first declared block appears at the top, followed by subsequent blocks.

Consider the `product-summary.shelf` block as an example, specified with a `children` composition.

<table>
<tr>
<th>`interfaces.json`</th>
<th>`blocks.json`</th>
</tr>
<tr>
<td>

```json
"product-summary.shelf": {
  "component": "ProductSummaryCustom",
  "composition": "children"
},
```

</td>
<td>

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

</td>
</tr>
</table>

In this scenario, the `product-summary-name` will be rendered first, followed by the `product-summary-description` and so on.

## Slots

The `slots` composition, in turn, allows you to declare child blocks using regular React props instead of declaring an array for it.

Blocks with the `slots` composition offer:

- **Prop-based declaration:** Child blocks are declared using regular React props, enabling flexibility and customization.
- **Prop-based child blocks:** Child blocks are specified as props in the parent block, utilizing a prop's name defined by the parent block


<table>
<tr>
<th>`interfaces.json`</th>
<th>`blocks.json`</th>
</tr>
<tr>
<td>

```json
// interfaces.json
{
  "hello-world": {
    "component": "HelloWorld",
  }
}
```

</td>
<td>

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

</td>
</tr>
</table>

The `icon-caret#point-up` has `slots` composition, thereby it is declared as a prop in the `hello-world` block. Notice that the prop name can be any of your choosing and is usually defined by the block in which it is declared.

For more information, please refer to the [Slots](https://developers.vtex.com/docs/guides/vtex-io-documentation-slots/) article.

> ℹ️ We strongly recommend you to use `slots` composition whenever possible due to its greater flexibility.

## Example

Here's an example of how this relationship is defined within the `interfaces.json` file:

```json iterfaces.json
{
  "drawer": {
    "component": "Drawer",
    "composition": "children",
    "allowed": ["drawer-trigger", "drawer-header"]
  },
  "drawer-header": {
    "component": "DrawerHeader",
    "composition": "children"
  },
  "drawer-close-button": {
    "component": "DrawerCloseButton"
  }
}
```

Let's break this down:

- `drawer`: This block is associated with a React component called `Drawer`. Its composition `property` is set to `children`, indicating its layout structure relies on child blocks. Additionally, it specifies the `allowed` child blocks that can be included within it.
- `drawer-header`: Similar to the `drawer` block, the `drawer-header` component also uses a composition of `children`, indicating its reliance on child blocks for layout structuring.
- `drawer-close-button`: This block is linked to a React component named `DrawerCloseButton` but doesn't explicitly specify a composition. This implies that it might not rely on child blocks for its layout and it imples the default `blocks` behavior.
