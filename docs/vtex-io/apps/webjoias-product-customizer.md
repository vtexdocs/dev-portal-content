---
title: "Product Customizer"
slug: "webjoias-product-customizer"
excerpt: "webjoias.product-customizer@0.0.2"
hidden: true
createdAt: "2022-07-11T19:47:48.561Z"
updatedAt: "2022-07-11T19:47:48.561Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Product Customizer allows a product's [attachments](https://help.vtex.com/tutorial/o-que-e-um-anexo--aGICk0RVbqKg6GYmQcWUm) and/or its subscription to be made available and ready to be defined by users on the product details page. 

![attachment-product-customization-select](https://user-images.githubusercontent.com/52087100/65711995-707f6e00-e06c-11e9-8faa-43aecfed3e51.png)
*Example of a product details page with the Product Customizer component displaying the product's attachments.*

![subscription-gif](https://user-images.githubusercontent.com/52087100/104508392-eba0c680-55c6-11eb-9d08-772a173c1df3.gif)
*Example of a product details page with the Product Customizer component displaying the product subscription.*

> ℹ️ ***The Product Customizer's integration with the Subscription module is native and automatically enabled by the component**. In order to allow your users to set the subscription on the product details page, set up the [Subscription v2](https://help.vtex.com/tutorial/setting-up-subscription-v2--1FA9dfE7vJqxBna9Nft5Sj) in your VTEX account and follow the instructions below to implement the Product Customizer app.* 

## Configuration 

1. Add `product-customizer` app to your theme's dependencies in the `manifest.json`, for example:

```diff
  dependencies: {
+   "vtex.product-customizer": "2.x"
 }
```

Now, you are able to use all blocks exported by the `product-customizer` app. Check out the full list below:

| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `product-assembly-options` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red)  Top level block responsible for displaying the product customizer default component, showing product's attachments. Use this block's children list to define which attachment data you want to display for users.   |
| `assembly-option-input-values` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Displays a checkbox or a dropdown list field so users can choose the desired attachment for their products. |
| `assembly-option-item-image` | Renders the attachment image. | 
| `assembly-option-item-quantity-selector` | Renders a quantity selector. | 
| `assembly-option-item-name` | Renders the attachment name. | 
| `assembly-option-item-price` | Renders the attachment price. |
| `assembly-option-item-customize` | Renders a button `Customize` that when clicked on opens a modal to customize the attachment. | 
| `assembly-option-item-children-description` | Renders a summary with all attachments selected. | 

2. In the theme's product template (`store.product`), add the `product-assembly-options` block to the children list. This will be enough to display the subscription options for the products if the [Subscription v2](https://help.vtex.com/tutorial/setting-up-subscription-v2--1FA9dfE7vJqxBna9Nft5Sj) was previously configured in your VTEX account.

```json
  "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "flex-layout.row#product-main",
      "flex-layout.row#description",
      "shelf.relatedProducts",
      "product-reviews",
      "product-questions-and-answers",
      "product-assembly-options"
    ]
  },
 ```

3. Declare the `product-assembly-options` block and add the `assembly-option-input-values` block as its child to display the product's attachments on the product details page. 

```json
  "product-assembly-options": {
    "children": [
      "assembly-option-input-values"
    ]
  },
````

> ℹ️  *Notice that you can use other blocks, such as the `assembly-option-item-image`, as `product-assembly-options`'s child in order to build the Product Customizer component most suitable for your desired scenario.*

4. Declare the blocks' props according to the desired scenario. For example:

```json
 "product-assembly-options": {
 "props":{
   "initiallyOpened": "always"
  },
 "children": [
   "flex-layout.row#product-assembly-options",
   "assembly-option-input-values"
    ]
  },
```

### `product-assembly-options` props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `initiallyOpened` | `enum` | By default, the customization box is opened if the attachment is required and closed if it's not. You can override this behavior by setting this prop to `always`, making it be opened even if the attachment is not required. Leave it as `required` for the default behavior. | `required` |

### `assembly-option-input-values` props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `optionsDisplay` | `enum` | Define whether the attachment's pre-defined options will be displayed to be selected in a Checkbox (`box`) or in a dropdown list (`select`) . | `select` |

### `assembly-option-item-customize`props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `buttonProps` | `object` | Defines how the `Customize` button will behave. In addition to the `collapse` prop, the `buttonProps` object also receives child blocks to build the content of the modal triggered when the button is clicked on.| `undefined` | 

- **`buttonProps`  object:**

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `collapse` | `enum` | `Customize` button positioning. Possible values are: `left` or `right`. | `left` | 

## Modus Operandi

According to the [data entry](https://help.vtex.com/tutorial/adding-an-attachment?locale=en) in the catalog, the Product Customizer takes 3 types of attachments into account when being rendered:

-  **Free text** - Any text can be entered in this field. Users may or may not have a character limit, depending on what was filled in the `Maximum Number of Characters` field in the attachment register.
  - **Predefined options**  - Users can only choose between an attachment's predefined options, according to what's set in the `Permitted Values` field in the attachment register. The way these options will be displayed can be defined with the `optionsDisplay` prop from `assembly-option-input-values` block.
 -  **Boolean** -  If the options that are predefined in the `Permitted Values` field are either `true` ou `false`, users can choose the attachment by simply clicking on a checkbox.
 
Notice the example below and check out the three attachment types simultaneously displayed for the same product:

![product-customizer-select](https://user-images.githubusercontent.com/52087100/65720836-32d81080-e07f-11e9-9782-0f5a2e6934f0.png)

Then, check out below how the product attachment displayed above was registered in the admin's Catalog: 

![attachment-product-customizer](https://user-images.githubusercontent.com/52087100/65720878-471c0d80-e07f-11e9-8267-27c35fb4c6b4.png)

> ℹ️ *Notice that **when a product's attachment was registered as required, all attachment options will be automatically made available to users**. If the product's attachment is not added as required, the `Add customization` button is rendered, as shown in the example above, giving users the options to add or not to add an attachment to their product.*

> ℹ️ *The Product Customizer uses the new Assembly Options API (the traditional Attachments API will be discontinued). As a result, **Checkout still doesn't natively render the customized product option previously selected by the user in the product page**. For the product to be correctly displayed with the chosen attachment, it's necessary for now to customize the Checkout page interface for it to read the product data in its context and render it.*

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles | 
| ---------- | 
| `booleanInputValue`| 
| `inputValueOptionBox` |
| `itemContainer` | 
| `modalViewDoneButton` | 
| `modalViewProductContainer` | 
| `modalViewProductImage` | 
| `modalViewProductInfos` |
| `modalViewProductName` | 
| `multipleItemQuantitySelector` |
| `optionsInputValue` |
| `optionsInputValueDropdown` |
| `optionsInputValueLabel` |
| `optionsInputValueLabelContainer` |
| `optionsInputValueOptionBoxContainer` |
| `productAssemblyGroupName` |
| `productAssemblyGroupNameRow` |
| `productAssemblyGroupRequiredTag` |
| `productAssemblyOptionItemCustomize` |
| `productAssemblyOptionItemCustomize__label` |
| `productAssemblyOptionItemImage` |
| `productAssemblyOptionItemName` |
| `textInputValue` |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/leoWorkingGood"><img src="https://avatars2.githubusercontent.com/u/51805410?v=4" width="100px;" alt=""/><br /><sub><b>leoWorkingGood</b></sub></a><br /><a href="https://github.com/vtex-apps/product-customizer/commits?author=leoWorkingGood" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->