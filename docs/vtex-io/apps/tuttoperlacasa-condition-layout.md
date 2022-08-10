---
title: "Condition Layout"
slug: "tuttoperlacasa-condition-layout"
excerpt: "tuttoperlacasa.condition-layout@2.5.2"
hidden: true
createdAt: "2022-07-28T13:02:53.963Z"
updatedAt: "2022-07-28T13:02:53.963Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Condition Layout app allows a component to be rendered in your store if predefined conditions are met.

![Screen-Recording-certo](https://user-images.githubusercontent.com/12139385/79379694-a8c99980-7f35-11ea-9f01-7021c6529332.gif)

## Configuration

### Step 1 - Adding the Condition Layout app to your theme's dependencies

In your theme's `manifest.json`, add the Condition Layout app as a dependency:

```diff
  "dependencies": {
+   "vtex.condition-layout": "2.x"
  }
```

You are now able to use all blocks that are exported by the `condition-layout` app. Check out the full list below:

| Block name                 | Description                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `condition-layout.product` | Defines the condition logic on the product context and the children blocks that are going to be rendered in case the predefined conditions are met. |
| `condition-layout.binding` | Defines the condition logic on the current binding and the children blocks that are going to be rendered in case the predefined conditions are met.  |
| `condition-layout.category` | Defines the condition logic on the current category page or department page and the children blocks that are going to be rendered in case the predefined conditions are met.  |

### Step 2 - Adding the `condition-layout.product` block to your theme's templates

In the product theme template, add the `condition-layout.product` block as a children. For example:

```
{
  "store.product": {
    "children": ["condition-layout.product"]
  },
```

Or the `condition-layout.binding` block, for example:

```json
{
  "store.product": {
    "children": ["condition-layout.binding"]
  }
}
```

Or the `condition-layout.category` block, for example:

```json
{
  "store.search#my-category-page": {
    "children": ["condition-layout.category"]
  }
}
```

:warning: _Never use `condition-layout` directly. Make sure to always use it with the context variant, such as `condition-layout.product`._

### Step 3 - Defining the desired conditions

Now it is time to configure the `condition-layout.product` block!

**Use the block's props to define your layout condition**. You can also declare as the children the `condition-layout.product`'s children some blocks of your choosing to be rendered if the condition is met. 

For example:

```diff
{
  "store.product": {
    "children": ["condition-layout.product#cond1"]
  },
  "condition-layout.product#cond1": {
+   "props": {
+     "conditions": [
+       {
+         "subject": "productId",
+         "arguments": {
+           "id": "12"
+         }
+       }
+     ]
+     "Then": "flex-layout.row#custom-pdp-layout-12",
+     "Else": "flex-layout.row#default"
+   }
+ }
```

Or for `condition-layout.binding`:

```diff
{
  "store.product": {
    "children": ["condition-layout.binding#cond42"]
  },
  "condition-layout.binding#cond42": {
+   "props": {
+     "conditions": [
+       {
+         "subject": "bindingId",
+         "arguments": {
+           "id": "13fb71d0-binding-code-here-87h9c28h9013"
+         }
+       }
+     ]
+     "Then": "flex-layout.row#just-for-this-binding",
+     "Else": "flex-layout.row#for-other-bindings"
+   }
+ }
```

Or for `condition-layout.category`:

 ```diff
 {
   "store.product": {
     "children": ["condition-layout.category#cond42"]
   },
   "condition-layout.category#cond42": {
 +   "props": {
 +     "conditions": [
 +       {
 +         "subject": "department",
 +         "arguments": {
 +           "ids": ["1", "42"]
 +         }
 +       }
 +       {
 +         "subject": "category",
 +         "arguments": {
 +           "ids": ["301", "304"]
 +         }
 +       }
 +     ]
 +     "matchType": "any",
 +     "Then": "flex-layout.row#just-for-this-category-or-department",
 +     "Else": "flex-layout.row#for-other-category-or-department"
 +   }
 + }
 ```

:information_source: *According to the example above, whenever users interact with a product whose ID is equal to 12, the block `flex-layout.row#custom-pdp-layout-12` is rendered. If users interact with a product whose ID is not equal to 12, the rendered block is the `flex-layout.row#default`.*

| Prop name    | Type     | Description  | Default value |
| ------------ | -------- | ------------ | ------------- |
| `conditions` | `object` | List of desired conditions. | `undefined`   |
| `matchType`      | `enum`   | Layout rendering criteria. Possible values are: `all` (all conditions must be matched in order to render the layout), `any` (at least one of the conditions must be matched in order to render the layout) or `none` (no conditions must be matched in order to render the layout). | `all`         |
| `Then`       | `block`  | Name of the block to be rendered if the conditions are met. If no value is defined, the blocks declared as children of `condition-layout.product` will be rendered instead.  | `undefined`   |
| `Else`       | `block`  | Name of the block to be rendered if the conditions are not met. | `undefined`   |

- **`conditions` object:**

| Prop name   | Type      | Description | Default value |
| ----------- | --------- | ----------- | ------------- |
| `subject`   | `string`  | Defines, according to the product context where the block in declared in, which data is needed from the UI to validate the value chosen in the `object` prop. Check below the possible values for this prop. | `undefined`   |
| `arguments` | `object`  | Defines the condition parameters. Notice: this prop value varies according to the value set to the `subject` prop. Check below the table for the `subject`'s possible values and their expected arguments. | `undefined`   |
| `toBe`      | `boolean` | Whether the data fetched in the `subject` prop must met the predefined conditions to render the new layout (`true`) or not (`false`). | `true` |

Possible values for the `condition-layout.product`'s `subject` prop:

| Subject                    | Description            | Arguments      |
| -------------------------- | ---------------------- | -------------- |
| `productId`                | Product's IDs currently displayed on the UI.  | `{ id: string }` |
| `categoryId`               | Category's IDs currently displayed on the UI. | `{ id: string }` |
| `brandId`                  | Brand's IDs currently displayed on the UI.    | `{ id: string }` |
| `selectedItemId`           | ID of the item currently selected by the user.   | `{ id: string }` |
| `productClusters`          | List of product clusters currently displayed on the UI.   | `{ id: string }` |
| `categoryTree`             | List of categories currently displayed on the UI. **Note:** only available in the Product Detail Page.   | `{ id: string }`  |
| `specificationProperties`  | List of product specifications currently displayed on the UI. | `{ name: string, value: string }`. Notice: `value` is an optional prop. If omitted, only the specification name (`name`) will be checked. |
| `areAllVariationsSelected` | Whether all product variations currently available on the UI were selected by the user (`true`) or not (`false`). | No arguments are expected. |
| `isProductAvailable`                  | Whether the product is available (`true`) or not (`false`).  | No arguments are expected. |
| `isBestPrice` | Whether the current product has the best price | No arguments are expected. |
| `hasMoreSellersThan`                  | Whether the quantity of sellers for the product is more than argument passed.  | `{ quantity: number }`|

Possible values for the` condition-layout.binding`'s `subject` prop:

| Subject | Description | Arguments |
| -------- | ------------ | ---------- |
| `bindingId` | ID of the desired store binding.  | `{ id: string }` |

Possible values for the `condition-layout.category`'s `subject` prop:

| Subject                    | Description            | Arguments      |
| -------------------------- | ---------------------- | -------------- |
| `category`               | Category's IDs currently displayed on the UI.    | `{ ids: string[] }` |
| `department`             | Department's IDs currently displayed on the UI.  | `{ ids: string[] }` |

## Modus Operandi

The `condition-layout.product` mainly uses the `matchType` and `conditions` props to set, respectively, the criteria and the conditions that blocks must meet to be rendered or not.

The `conditions` prop, in turn, does not rely on any automatic grammar to define the desired conditions. Instead, it relies on its two props, namely `subject` and `arguments`, that together define which condition must be met by using an underlying data validation method (with specific arguments) according to the UI behavior.

Lastly, the `matchType` prop has the responsibility for deciding the necessary number of valid conditions for the layout rendering to actually occur.

## Customization

The Condition Layout merely establishes a logic to render other blocks. Therefore, the app doesn't have CSS Handles for its specific customization.

Instead, you should use its child block's Handles.

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes out to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/LucasCastroAcctGlobal"><img src="https://avatars0.githubusercontent.com/u/55210107?v=4?s=100" width="100px;" alt=""/><br /><sub><b>LucasCastroAcctGlobal</b></sub></a><br /><a href="https://github.com/vtex-apps/condition-layout/commits?author=LucasCastroAcctGlobal" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/vini-lima-acct"><img src="https://avatars.githubusercontent.com/u/78028684?v=4?s=100" width="100px;" alt=""/><br /><sub><b>vini-lima-acct</b></sub></a><br /><a href="https://github.com/vtex-apps/condition-layout/commits?author=vini-lima-acct" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->