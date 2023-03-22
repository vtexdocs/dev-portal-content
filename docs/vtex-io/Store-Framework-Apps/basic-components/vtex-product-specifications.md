---
title: "Product Specifications"
slug: "vtex-product-specifications"
hidden: false
createdAt: "2020-08-28T17:56:14.433Z"
updatedAt: "2021-08-27T00:05:10.919Z"
---

The Product Specifications app provides blocks to render product specification data.

![Product Specifications Example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-specifications-0.png)

## Configuration

### Step 1 - Adding the Product Specifications app to your theme's dependencies

In your theme's `manifest.json`, add the Product Specification app as a dependency:

```json
"dependencies": {
  "vtex.product-specifications": "1.x"
}
```

Now, you can use all the blocks exported by the `product-specifications` app. Check out the full list below:

| Block name                    | Description                                                                                                                                                                                                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `product-specification-group` | Renders the product specification group.                                                                                                                                                                                                                                           |
| `product-specification`       | Renders the product specification. It should be declared as a children of `product-specification-group`.                                                                                                                                                                           |
| `product-specification-value` | Renders the product specification value. It should be declared as a children of `product-specification`. It is possible to render with `HTML`.                                                                                                                                     |
| `product-specification-text`  | Mandatory children of `product-specification-group`, `product-specification` and `product-specification-value`. Depending on which block it is declared, the `product-specification-text` renders data regarding a specification group, a specification, or a specification value. |

### Step 2 - Adding the Product Specifications' blocks to your theme's templates

Copy the example stated below and paste it into your theme's desired template, making the necessary changes according to your desire. Remember to add the `product-specification-group` block to the template's block list if needed.

```json
{
  "product-specification-group": {
    "children": ["product-specification-text#group", "product-specification"]
  },
  "product-specification": {
    "children": [
      "product-specification-text#specification",
      "product-specification-values"
    ]
  },
  "product-specification-values": {
    "children": ["product-specification-text#value"]
  },
  "product-specification-text#group": {
    "props": {
      "message": "{groupName}"
    }
  },
  "product-specification-text#specification": {
    "props": {
      "message": "{specificationName}"
    }
  },
  "product-specification-text#value": {
    "props": {
      "message": "{specificationValue}"
    }
  }
}
```

> ⚠️ _Notice that the Product Specifications' blocks necessarily need a Product context in order to work properly since they handle product data. Therefore, when declaring them, be sure that they are in a theme template in which this context is available, such as the `store.product`._

You also can use other blocks to wrap the blocks provided by the Product Specifications app, such as the ones exported by the [Flex Layout app](https://developers.vtex.com/docs/guides/vtex-flex-layout/). For example:

```json
{
  "product-specification-group#table": {
    "children": ["flex-layout.row#spec-group"]
  },
  "flex-layout.row#spec-group": {
    "props": {
      "blockClass": "productSpecificationGroup"
    },
    "children": ["flex-layout.col#spec-group"]
  },
  "flex-layout.col#spec-group": {
    "children": ["flex-layout.row#spec-group-name", "product-specification"]
  },
  "flex-layout.row#spec-group-name": {
    "props": {
      "blockClass": "productSpecificationGroupName"
    },
    "children": ["product-specification-text#group"]
  },
  "product-specification": {
    "children": ["flex-layout.row#spec-item"]
  },
  "flex-layout.row#spec-item": {
    "props": {
      "blockClass": "productSpecification"
    },
    "children": ["flex-layout.col#spec-name", "flex-layout.col#spec-value"]
  },
  "flex-layout.col#spec-name": {
    "props": {
      "blockClass": "productSpecificationName",
      "width": {
        "mobile": "50%",
        "desktop": "25%"
      }
    },
    "children": ["product-specification-text#specification"]
  },
  "flex-layout.col#spec-value": {
    "props": {
      "blockClass": "productSpecificationValue"
    },
    "children": ["product-specification-values"]
  },
  "product-specification-values": {
    "children": ["product-specification-text#value"]
  },
  "product-specification-text#group": {
    "props": {
      "message": "{groupName}"
    }
  },
  "product-specification-text#specification": {
    "props": {
      "message": "{specificationName}"
    }
  },
  "product-specification-text#value": {
    "props": {
      "message": "{specificationValue}"
    }
  }
}
```

### `product-specification-group` props

| Prop name | Type     | Description                                                       | Default value |
| --------- | -------- | ----------------------------------------------------------------- | ------------- |
| `filter`  | `object` | Filters the specifications that should be displayed by the block. | `undefined`   |

- **`filter` object:**

| Prop name             | Type       | Description                                                                                                                                                                                                                                                                                                             | Default value |
| --------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `specificationGroups` | `[string]` | Array of specification group names to be hidden or shown (according to what is defined in the `type` property) by the `product-specification-group` block.                                                                                                                                                              | `undefined`   |
| `type`                | `enum`     | Whether the specification group names passed to the `specificationGroups` prop should be displayed or hidden on the UI. Possible values are: `hide` (hides specification groups declared in the `specificationGroups` prop) or `show` (only shows the specification groups declared in the `specificationGroups` prop). | `undefined`   |

#### `product-specification-text` props

| Prop name    | Type       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       | Default value |
| ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass` | `string`   | Block ID of your choosing to be used in [CSS customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization#using-the-blockclass-property).                                                                                                                                                                                                                                               | `undefined`   |
| `message`    | `string`   | Defines the block's default text message to be rendered on the UI. You can also define which text message a block will render on the UI using the admin's Site Editor and the `markers` prop.                                                                                                                                                                                                                                                     | `undefined`   |
| `markers`    | `[string]` | IDs of your choosing to identify the block's rendered text message and customize it using the admin's Site Editor. Learn how to use them accessing the documentation on [Using the Markers prop to customize a block's message](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message). Notice the following: a block's message can also be customized in the Store Theme source code using the `message` prop. | `[]`          |

### Step 3 - Editing the `product-specification-text`'s messages

As stated in the previous step, the `product-specification-text` uses the [ICU Message Format](https://format-message.github.io/icu-message-format-for-translators/), making it possible to fully edit the block's rendered text messages.

When using the `message` prop, you won't need to perform any advanced configurations: declare the prop directly in your Store Theme app, passing to it the desired text value to be rendered with the block.

The `markers` prop, in turn, requires you to perform an extra configuration in the admin's Site Editor to properly work. When using this prop, do not forget to check out the block's message variables (shown in the table below) and the [Using the Markers prop to customize a block's message](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-markers-prop-to-customize-a-blocks-message) documentation.

| Message variable            | Type      | Description                                                            |
| --------------------------- | --------- | ---------------------------------------------------------------------- |
| `groupName`                 | `string`  | Specification group name.                                              |
| `specificationName`         | `string`  | Speficiation name.                                                     |
| `specificationValue`        | `string`  | Specification value.                                                   |
| `isFirstSpecificationValue` | `boolean` | Whether it is the first specification value (`true`) or not (`false`). |
| `isLastSpecificationValue`  | `boolean` | Whether it is the last specification value (`true`) or not (`false`).  |

## Customization

To apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles                 |
| --------------------------- |
| `groupName`                 |
| `specificationName`         |
| `specificationValue`        |
| `specificationValue--first` |
| `specificationValue--last`  |
