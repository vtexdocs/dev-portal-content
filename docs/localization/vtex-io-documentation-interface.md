---
title: "Interfaces"
slug: "vtex-io-documentation-interface"
hidden: false
createdAt: "2021-04-07T19:00:37.442Z"
updatedAt: "2024-09-17T14:35:35.726Z"
---

Interfaces establish a relation between a block and a React component, allowing the [store builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) to build the store frontend. These interfaces are defined in the app's `interfaces.json` file.

Interfaces provide a set of rules that dictate the behavior of theme blocks when rendering their React components and the available properties and methods.

For each theme block exported by your app, you should define a corresponding interface that defines the props available to the React component.

The following table shows some possible keys that could be added to the block interface, as well as their respective descriptions:

| Key           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `component`   | Name of the React component that the theme block will render.|
| `allowed` | List of other theme blocks that help build the desired React component. When declared, these blocks can be included as children to the block you developed in the Store Theme app.|
| `composition` | Defines the rendering position of the children of the block that you are developing. Remember that when defining the `composition` key, you don't control the position of the block it defines but the position of the children of that block. Possible values for this key are `blocks` (the child blocks have a specific position in the interface based on the React component on which they are based) or `children` (the position of the child blocks depends exclusively on how they are declared in the theme). If no value is defined for the `composition` key, the platform default is `blocks.` |
| `device`      | Defines whether your theme block is designed for mobile or desktop devices. Possible values are `mobile` and `desktop`.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `required`    | List of theme blocks that must be rendered in the interface to support the block rendering you are developing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `around`      | List of theme blocks that must be rendered in the interface around your new block for it to work correctly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `before`      | List of theme blocks that must be rendered in the interface before your block (above it) for it to work correctly. For example: header.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `after`       | List of theme blocks that must be rendered in the interface after your block (below it) for it to work correctly. For example: footer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `preview`     | Defines the behavior of the page while the block is loading.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `render`      | Defines the block rendering type. Possible values are `lazy` (the block is only rendered when a user interacts with it), `server` (the block is rendered from the server side), or `client` (the block is rendered from the client side.                                                                                                                                                                                                                                                                                                                                                                                    |

The only required key that needs to be declared in a block interface is `component`. You may declare the other ones based on the desired scenario for your new theme block.

## Example

For each exported block, the app specifies a corresponding React component. For example:

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

Let's delve into this example of a component named `ProductSummary`:

- `product-summary`: Sets the name of the interface block being defined.
- `component`: Specifies the name of the React component (`ProductSummary`) associated with the interface. Check [Component](https://developers.vtex.com/docs/guides/vtex-io-documentation-components) for more information.
- `composition`: Indicates the structure and composition of the component within its parent component. Check [Composition](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition) for more information.
- `content`: Points to an external schema definition for the `ProductSummary` component. The structure and properties expected within the `ProductSummary` component are defined in a separate schema file associated with the `vtex.product-summary` app.
