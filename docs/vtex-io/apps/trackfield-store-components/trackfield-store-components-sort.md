---
title: "Sort"
slug: "trackfield-store-components-sort"
excerpt: "trackfield.store-components@0.18.0"
hidden: true
createdAt: "2022-07-05T22:31:25.115Z"
updatedAt: "2022-08-04T10:48:21.283Z"
---
Sort is a solution that allows you to sort components by Site Editor, as well as enabling and disabling components.

## Configuration

1. Add the `store-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "trackfield.store-components": "0.x"
}
```

2. You are now able to use the `sort` and `sort-wrapper` blocks. This allows you to create ordered components. For example:

```json
{
  "sort-wrapper": {
    "children": ["sort#1", "sort#2", "sort#3"]
  },
  "sort#1": {
    "children": ["flex-layout.row#3"],
    "props": {
      "order": 1
    }
  },
  "sort#2": {
    "children": ["flex-layout.row#1"],
    "props": {
      "order": 2
    }
  },
  "sort#3": {
    "children": ["flex-layout.row#2"],
    "props": {
      "order": 3
    }
  }
}
```

### `sort` props

| Prop name      | Type      | Description                                                                      | Default value |
| -------------- | --------- | -------------------------------------------------------------------------------- | ------------- |
| `active`       | `boolean` | Allows you to enable or disable the component.                                   | `true`        |
| `blockClass`   | `string`  | A modifier class for the component.                                              | `undefined`   |
| `order`        | `number`  | The numerical order of the component.                                            | `undefined`   |
| `marginBottom` | `string`  | A number from 0 to 10 that applies the Tachyons `mb` class to the bottom margin. | `"3"`         |
| `marginTop`    | `string`  | A number from 0 to 10 that applies the Tachyons `mt` class to the top margin.    | `"3"`         |

:information_source: Use the **admin's Site Editor** to manage all `sort` components in the page.