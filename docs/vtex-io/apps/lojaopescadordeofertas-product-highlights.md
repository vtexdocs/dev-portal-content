---
title: "Product Highlights"
slug: "lojaopescadordeofertas-product-highlights"
excerpt: "lojaopescadordeofertas.product-highlights@0.0.0"
hidden: true
createdAt: "2022-08-09T16:38:15.679Z"
updatedAt: "2022-08-09T16:38:15.679Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Product Highlights app provides blocks to display highlight badges on products according to the collection or promotion they are linked to.

![Product Highlights Example](https://user-images.githubusercontent.com/284515/92048986-7216e300-ed5f-11ea-86d4-abf535227ef1.png)
_In the image above, the product has a `Top Seller` highlight._

## Configuration

### Step 1 - Adding the Product Highlights app to your theme's dependencies

In your theme's `manifest.json` file, add the Product Highlights app as a dependency:

```diff
 "dependencies": {
+  "vtex.product-highlights": "2.x"
}
```

Now, you can use all the blocks exported by the `product-highlights` app. Check out the full list below:

| Block name                  | Description                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `product-highlights`        | Parent block responsible for defining, according to its children blocks (`product-highlight-text` and `product-highlight-wrapper`) and props, how the Product Highlights component will be displayed.                                   |
| `product-highlight-text`    | Renders a `span` HTML tag with the hightlight name. It also provides data attributes and CSS handles for style customizations. |
| `product-highlight-wrapper` | If you need to render other blocks along side with the highlight name, you may use this block. It renders a `div` HTML tag and its children blocks (if any). |

### Step 2 - Adding the Product Highlights' blocks to your theme's templates

According to your desire, copy one of the examples stated below and paste it in your theme's desired template, making the necessary changes. Remember to add the `product-highlights` block to the template's block list if needed.

- Simple example:

```json
{
  "vtex.product-highlights@2.x:product-highlights": {
    "children": ["product-highlight-text"]
  },
  "product-highlight-text": {
    "props": {
      "message": "{highlightName}"
    }
  }
}
```

- Example using the `link` prop:

```json
{
  "vtex.product-highlights@2.x:product-highlights": {
    "children": ["product-highlight-text"]
  },
  "product-highlight-text": {
    "props": {
      "message": "{highlightName}",
      "link": "/collection/{highlightId}"
    }
  }
}
```

- Example using `product-highlight-wrapper`:

```jsonc
{
  "vtex.product-highlights@2.x:product-highlights": {
    "children": ["product-highlight-wrapper"]
  },
  "product-highlight-wrapper": {
    "children": [
      "icon-star", // You can add anything inside a product-highlight-wrapper
      "product-highlight-text"
    ]
  },
  "product-highlight-text": {
    "props": {
      "message": "{highlightName}"
    }
  }
}
```

- Example using the prop `filter` and the prop `type`:

```jsonc
{
  "vtex.product-highlights@2.x:product-highlights": {
    "props": {
      "type": "teaser",
      "filter": {
        "type": "show",
        "highlightNames": ["10% Boleto"]
      }
    },
    "children": ["product-highlight-text"]
  },
  "product-highlight-text": {
    "props": {
      "message": "{highlightName}",
      "blockClass": "boleto"
    }
  }
}
```

> ⚠️ warning
>
>  Notice that **the Product Highlights' blocks need a Product context in order to work properly since they handle product data**. Therefore, when declaring them, be sure that they are in a theme template or block in which this context is available, such as the `store.product` and `product-summary.shelf`.

### `product-highlights` props

| Prop name | Type     | Description                                                                 | Default value |
| --------- | -------- | --------------------------------------------------------------------------- | ------------- |
| `type`    | `enum`   | Desired type of product highlight to be displayed. Possible values are: `collection`, `promotion`, and `teaser`. `collection` highlights the product's collection therefore it must be be used in conjuction with the [Collection Highlight](https://help.vtex.com/en/tutorial/collection-highlight-control--1tGdb2ndjqy6yWsk2YwKMu?locale=en) feature. `promotion` and `teaser` should be used when the product is configured with a [promotion with highlights](https://help.vtex.com/en/tutorial/configuring-promotions-with-a-highlightflag--tutorials_2295?locale=en), but notice the following: `teaser` must only be used when the promotion presents restrictions. `promotion`, in turn, when it does not. ⚠️*Be aware that nominal promotions will only be displayed in the cart, not on the shelf or product page.*| `collection`  |
| `filter`  | `object` | Defines the highlights that should and should not be displayed by the block. | `undefined`   |

> ⚠️ warning
> 
> Technically, `collection` maps to the property [`clusterHighlights`](https://github.com/vtex-apps/search-graphql/blob/ea1d7e244e6b00b58e5aa4272fbb16987c483468/graphql/types/Product.graphql#L29); `promotion` to [`discountHighlights`](https://github.com/vtex-apps/search-graphql/blob/ea1d7e244e6b00b58e5aa4272fbb16987c483468/graphql/types/Product.graphql#L283); and `teaser` to [`teasers`](https://github.com/vtex-apps/search-graphql/blob/ea1d7e244e6b00b58e5aa4272fbb16987c483468/graphql/types/Product.graphql#L284).

- **`filter` object:**

| Prop name        | Type       | Description                                                                                                                                                                                                                                                                 | Default value |
| ---------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `highlightNames` | `[string]` | Array of highlight names to be hidden or shown (according to what is defined in the `type` property) by the `product-highlights` block.                                                                                                                                     | `undefined`   |
| `type`           | `enum`     | Whether the highlights names passed to the `highlightNames` prop should be displayed or hidden on the UI. Possible values are: `hide` (hides highlights declared in the `highlightNames` prop) or `show` (only shows the highlights declared in the `highlightNames` prop). | `undefined`   |

#### `product-highlight-text` props

| Prop name    | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       | Default value |
| ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass` | `string`   | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property).                                                                                                                                                                                                                                                                          | `undefined`   |
| `message`    | `string`   | Defines the block's default text message to be rendered on the UI. You can also define which text message a block will render on the UI using the admin's Site Editor and the `markers` prop.                                                                                                                                                                                                                                                     | `undefined`   |
| `markers`    | `[string]` | IDs of your choosing to identify the block's rendered text message and customize it using the admin's Site Editor. Learn how to use them accessing the documentation on [Using the Markers prop to customize a block's message](https://vtex.io/docs/recipes/style/using-the-markers-prop-to-customize-a-blocks-message). Notice the following: a block's message can also be customized in the Store Theme source code using the `message` prop. | `[]`          |
| `link`       | `string`   | If set, creates a link to the string passed. You can interpolate the variables: `highlightText` and `highlightId`. Example: `/collection/{highlightId}`.  | `undefined`   |

#### `product-highlight-wrapper` props

| Prop name    | Type     | Description                                                                                                                                                              | Default value |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property). | `undefined`   |

### Step 3 - Editing the `product-highlight-text`'s messages

The `product-highlight-text` uses the [ICU Message Format](https://format-message.github.io/icu-message-format-for-translators/), making it possible to fully edit the block's rendered text messages.

When using the `message` prop, you won't need to perform any advanced configurations: declare the prop directly in your Store Theme app, passing to it the desired text value to be rendered with the block.

The `markers` prop, in turn, requires you to perform an extra configuration in the admin's Site Editor to properly work. When using this prop, do not forget to check out the block's message variables (shown in the table below) and the [Using the Markers prop to customize a block's message](https://vtex.io/docs/recipes/style/using-the-markers-prop-to-customize-a-blocks-message) documentation.

| Message variable | Type     | Description     |
| ---------------- | -------- | --------------- |
| `highlightName`  | `string` | Highlight name. |

## Customization

To apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles               |
| ------------------------- |
| `productHighlightText`    |
| `productHighlightWrapper` |

| Data Attributes       |
| --------------------- |
| `data-highlight-name` |
| `data-highlight-id`   |
| `data-highlight-type` |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/igor-becker-73b7901a3/"><img src="https://avatars.githubusercontent.com/u/57180581?v=4?s=100" width="100px;" alt=""/><br /><sub><b>proudynyu</b></sub></a><br /><a href="https://github.com/vtex-apps/product-highlights/commits?author=proudynyu" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->