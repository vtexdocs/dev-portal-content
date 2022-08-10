---
title: "Migration guide"
slug: "tuttoperlacasa-condition-layout-migration-guide"
excerpt: "tuttoperlacasa.condition-layout@2.5.2"
hidden: true
createdAt: "2022-07-28T13:05:31.482Z"
updatedAt: "2022-07-28T13:05:31.482Z"
---
If you're currently using the Condition Layout in its **`1.x.x`** version, the following guide aims to help you to perform a **version upgrade**, migrating your store theme to the latest version of the app (**`2.x.x`**).

If you’re using the former version, you can still find its documentation [here](https://github.com/vtex-apps/condition-layout/tree/master/docs/v1-DOC.md). Do not forget to also access the [**Condition Layout current documentation**](https://github.com/vtex-apps/condition-layout/tree/master/docs/README.md) for its `2.x.x` version. 

:information_source: *Although support for the former version is still granted, we strongly recommend you to update your store theme with the app's newest version in order to keep up with the components' evolution.*

## Overview

The rewriting of this app aimed to provide a clearer logic when setting the conditions to build the new desired layout. 

The changes included in the app upgrade are, namely:

<!-- code_chunk_output -->

- [Block structure](#block-structure)
- [Prop's syntax](#props-syntax)
- [Negative conditions](#negative-conditions)

<!-- /code_chunk_output -->
  
### Block structure

In the `1.x.x` version, the `condition-layout` app exports three different types of blocks for your store theme:

- `condition-layout.product` - Wraps the desired `condition.product` blocks.
- `condition.product` - Defines the desired conditions to be met.
- `condition.else` - Defines in its child blocks a component to be rendered in case no condition is met.

```json
{
  "store.product": {
    "children": ["condition-layout.product"]
  },
  "condition-layout.product": {
    "children": [
      "condition.product#custom-pdp-12",
      "condition.product#custom-pdp-20",
      "condition.else"
    ]
  },
  "condition.product#custom-pdp-12": {
    "props": {
      "conditions": [
        {
          "subject": "productId",
          "verb": "is",
          "object": "12"
        }
      ]
    },
    "children": ["flex-layout.row#custom-pdp-layout-12"]
  },
  "condition.product#custom-pdp-20": {
    "props": {
      "conditions": [
        {
          "subject": "productId",
          "verb": "is",
          "object": "20"
        }
      ]
    },
    "children": ["flex-layout.row#custom-pdp-layout-20"]
  },

  "condition.else": {
    "children": ["flex-layout.row#default"]
  }
}
```

The block configuration is simplified in the `2.x.x` version: now, all three blocks were merged into a single one called `condition-layout.product`.

The same structure above can now be rewritten using the new block's props:

```json
{
  "store.product": {
    "children": ["condition-layout.product#custom-pdp-12"]
  },
  "condition-layout.product#custom-pdp-12": {
    "props": {
      "conditions": [
        {
          "subject": "productId",
          "arguments": { "id": "12" }
        }
      ],
      "Then": "flex-layout.row#custom-pdp-layout-12",
      "Else": "condition-layout.product#custom-pdp-20"
    }
  },
  "condition-layout.product#custom-pdp-20": {
    "props": {
      "conditions": [
        {
          "subject": "productId",
          "arguments": { "id": "20" }
        }
      ]
    },
    "Then": "flex-layout.row#custom-pdp-layout-20",
    "Else": "flex-layout.row#default"
  }
}
```

### Prop's syntax

In **`1.x.x`**, a simple logic for creating conditions was provided, where you could mix the `subject`, `verb`, and `object` props to set conditions in an idiomatic way. 

Since it provided a very effortless and easy syntax to set conditions, these last ones were, in turn, very limited as well. For example, it was not possible to check for a specification property name *and* value at the sime time.

```jsonc
{
  "condition.product": {
    "props": {
      "conditions": [
        // checks if the product has the
        // specification named `Material`
        {
          "subject": "specificationProperties",
          "verb": "contains",
          "object": "Material"
        }
      ]
    },
    "children": ["..."]
  }
}
```

In **`2.x.x`**, the aforementioned syntax was replaced with a pair of `subject` and `arguments` props. 

In practice, a `subject` is linked to an internal method that receives the `arguments`. Make sure to check [which arguments each `subject` can receive in the Condition Layout documentation](/docs/readme.md).

The above condition can be rewritten in the app's newest version as:

```jsonc
{
  "condition.product": {
    "props": {
      "conditions": [
        // checks if the product has the
        // specification named `Material`
        {
          "subject": "specificationProperties",
          "arguments": {
            "name": "Material"
            // Optional: could also check for its value
            // "value": "Leather"
          }
        }
      ],
      "Then": "..."
    }
  }
}
```

### Negative conditions

Previously (`1.x.x`), negative conditions were built using the `is-not` and `does-not-contain` values from the `verb` prop, as shown below:

```jsonc
{
  "condition.product": {
    "props": {
      "conditions": [
        {
          "subject": "specificationProperties",
          "verb": "does-not-contain",
          "object": "Material"
        }
      ]
    },
    "children": ["..."]
  }
}
```

In the latest version (`2.x.x`), the `verb` prop has given way to the `toBe` prop, which assigns in its value (`true` or `false`) the expected value of the condition.

The above condition can be rewritten as:

```json
{
  "condition.product": {
    "props": {
      "conditions": [
        {
          "subject": "specificationProperties",
          "arguments": {
            "name": "Material"
          },
          "toBe": false
        }
      ],
      "Then": "..."
    }
  }
}
```