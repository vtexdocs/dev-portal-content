---
title: "Interfaces"
slug: "vtex-io-documentation-interface"
hidden: false
createdAt: "2021-04-07T19:00:37.442Z"
updatedAt: "2022-12-13T20:17:44.448Z"
---

Interfaces establish a relation between a block and a React component, allowing the Store Builder to build the store's frontend. They can be found within an app's `interfaces.json` file.

For every exported block, the app also defines a React component linked to that block. For example:

```json
// product-summary/store/interfaces.json
{
  "product-summary": {
    "component": "ProductSummary",
    "composition": "children",
    "content": {
      "$ref": "app:vtex.product-summary#/definitions/ProductSummary"
    }
  }
}
```

In general, frontend apps export different [blocks](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition#blocks), which are declared and configured in the Store Theme's code, and React components related to these blocks. These [components](https://developers.vtex.com/docs/guides/vtex-io-documentation-components) are then rendered on the store's frontend.

## Example

Let's delve into the provided interface definition for a component named `ProductSummary`:

- `product-summary`: Name of the interface block being defined.
- `component`: Specifies the React component (`ProductSummary`) associated with the interface. Refer to [Component](https://developers.vtex.com/docs/guides/vtex-io-documentation-components) for more information.
- `composition`: Indicates the structure and composition of the component within its parent component. Refer to [Composition](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition) for more information.
- `content`: Refers to an external schema definition for the `ProductSummary` component. This means that the structure and properties expected within the `ProductSummary` component are defined in a separate schema file associated with the `vtex.product-summary` app. Refer to [Content](https://developers.vtex.com/docs/guides/vtex-io-documentation-content) for more information.
