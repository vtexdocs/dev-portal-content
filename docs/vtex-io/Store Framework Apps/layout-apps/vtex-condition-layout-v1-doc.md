---
title: "Condition Layout"
slug: "vtex-condition-layout-v1-doc"
excerpt: "vtex.condition-layout@2.6.0"
hidden: true
createdAt: "2020-10-26T15:24:19.885Z"
updatedAt: "2022-07-19T14:16:44.931Z"
---

> ⚠️ ***Condition Layout app v1 has been deprecated in favor of Condition Layout app v2**. Although support for the former version is still granted, we strongly recommend you to access the [Migration Guide](https://github.com/vtex-apps/condition-layout/tree/master/docs/MIGRATION-GUIDE.md) and update your store theme with the app's newest version in order to keep up with the components' evolution.*

As the name implies, the Condition Layout app allows a block to be rendered if certain conditions are met.

![Screen-Recording-certo](https://user-images.githubusercontent.com/12139385/79379694-a8c99980-7f35-11ea-9f01-7021c6529332.gif)
  
## Configuration

### Step 1 - Adding the Condition Layout app to your theme's dependencies

In your theme's `manifest.json`, add the Condition Layout app as a dependency:

```diff
  "dependencies": {
+   "vtex.condition-layout": "1.x"
  }
```

You are now able to use all blocks that are exported by the `condition-layout` app. Check out the full list below:

| Block name | Description |
| -------------- | ----------------------------------------------- |
| `condition-layout.{context}` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Top level block in which you will specify (replacing the `{context}` value in the block name) which context will be used for providing data to its child block namely `condition`. **Currently, the Condition Layout only works with the product context** therefore the top block must be `condition-layout.product`. |
| `condition.{context}` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Defines the condition logic and the children blocks that are going to be rendered in case the predefined condition is met. Remember to replace the `{context}` value for the context name specified in the Condition Layout block (`product`). |
| `condition.else` | This block is optional and can be used as a child of the `condition-layout.{context}` block. When declared, its children are rendered if no condition was met. In scenarios where no condition was met and the `condition.else` block was not declared, no content will be displayed. |

### Step 2 - Adding the `condition-layout.{context}` block to your theme's templates

In the product theme template, add the `condition-layout.{context}` block, replacing the `{context}` value with `product`. For example:

```
{
  "store.product": {
    "children": ["condition-layout.product"]
  },
```

> ⚠️ *You should never use `condition-layout` directly. Make sure to always use it with the context variant, such as `condition-layout.product`.*
  
### Step 3 - Configuring the `condition-layout.{context}` block

Once the `condition-layout.product` block was added to the product template, you must declare its children using the `condition.{context}` block replacing the `{context}` value with `product`.

If desired, add the `condition.else` block as well. For example:

```diff
{
  "store.product": {
    "children": ["condition-layout.product"]
  },
+ "condition-layout.product": {
+   "children": [
+     "condition.product#custom-pdp-12",
+     "condition.product#custom-pdp-20",
+     "condition.else"
+   ]
+ },
```

### Step 4 - Defining the desired conditions

Now it is time to configure the `condition.product` block: **use the block's props to define your layout condition** and declare as its child a block of your choosing that will be rendered if this condition is met. For example:

```diff
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
+ "condition.product#custom-pdp-12": {
+   "props": {
+     "conditions": [
+       {
+         "subject": "productId",
+         "verb": "is",
+         "object": "12"
+       },
+     ]
+   },
+   "children": ["flex-layout.row#custom-pdp-layout-12"]
+ },
+ "condition.product#custom-pdp-20": {
+   "props": {
+     "conditions": [
+       {
+         "subject": "productId",
+         "verb": "is",
+         "object": "20"
+       },
+     ]
+   },
+   "children": ["flex-layout.row#custom-pdp-layout-20"]
+ },
+  
+ "condition.else": {
+   "children": ["flex-layout.row#default"]
+ }
```

According to the example above, whenever users interact with a product whose ID is equal to 12, the block `flex-layout.row#custom-pdp-layout-12` is rendered.

If users interact with a product whose ID is not equal to 12, the block that is rendered is the `rich-text#default`.

#### `condition.{context}` props

| Prop name | Type | Description | Default value |
| ------------ | ---------------- | -------------------- | -------- |
| `conditions` | `object` | List of desired conditions. | `undefined` |
| `match` | `enum` | Layout rendering criteria. Possible values are: `all` (all conditions must be matched in order to be rendered), `any` (at least one of the conditions must be matched in order to be rendered) or `none` (no conditions must be matched in order to be rendered). | `all` |

- `conditions` prop's object:

| Prop name | Type | Description | Default value |
| --------- | --------------- | ----- | ---------------------|
| `subject` | `string` | A subject is a similar data fetched from a given context. When passed as a value to this prop, the subject will be used to identify which data is needed from the UI to validate the value chosen in the  `object` prop. Check below the possible value for the subject prop provided by the product context. | `undefined` |
| `verb` | `enum` | The condition validator. It directly depends on the subject chosen for the `subject` prop. For `value` type subjects, possible `verb`values are `is` or `is-not` (checking, respectively, for equality or inequality between the subject's value and the object prop's value). For  `array` type subjects, possible values are `contains` and `does-not-contain` (checking, respectively, if the subject's array contains or does not contain the object prop's value). | `is` (for `value` type subjects) and `contains` (for `array` type subjects). |
| `object` | `string` | Value that you want to be matched when comparing to the data fetched in the `subject` prop in order to render the predefined layout. | `undefined` |

- Possible `subject` prop's values provided by the product context:

| Subject | Type | Description |
| ----------------- | ------- | ------------------------------------- |
| `productId` | `value` | Product's IDs displayed on the UI. |
| `categoryId` | `value` | Category's IDs displayed on the UI. |
| `brandId` | `value` | Brand's IDs displayed on the UI. |
| `selectedItemId` | `value` | ID of the item being selected by the user on the UI. |
| `productClusters` | `array` | List of product clusters on the UI. |
| `categoryTree` | `array` | List of categories on the UI. |
| `specificationProperties` | `array` | List of product specifications. |
| `areAllVariationsSelected` | `value` | Whether all product variations available on the page were selected by the user (`true`) or not (`false`). |

> ℹ️ *Since the Condition Layout can only be used with product contexts, only the subjects listed above are needed for the proper functioning of the `condition` block. Remember to choose the subject's value according to the value passed to the `object` prop*.

## Modus Operandi

In practice, the Condition Layout does not render a block on its own. **The app provides 3 logic blocks**, meaning blocks that lay out the reasoning behind rendering other Store Framework blocks.

The `condition.{context}` block is the one that does your store's actual Layout logic and, using the `conditions` and `match` props to set the conditions that blocks must meet to be rendered or not.

The `conditions` prop object has 3 other props, namely `subject`, `verb` and `object`, that together define the condition that must be met and how it is going to be validated: the `object` prop from `conditions` compares its value with the values fetched by the subject passed to the `subject` prop. The criteria used for this comparison stems from the value passed in the `verb`. The result being to define whether the condition put forth by the `condition` block and its props is acuatlly valid or not.

Lastly, the `match` prop decides the necessary number of valid conditions (defined in `condition.{context}` blocks) for the layout rendering to actually occur.

## Customization

The Condition Layout merely establishes a logic to render other blocks. Therefore, the app doesn't have CSS Handles for its specific customization.

Instead, you should use the Handles of the child blocks chosen for rendering.
