---
title: "Product Customizer"
slug: "vtex-product-customizer"
excerpt: "vtex.product-customizer@2.11.4"
hidden: false
createdAt: "2020-06-03T15:19:31.995Z"
updatedAt: "2022-12-12T14:10:01.827Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/basic-components/#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Product Customizer component can be used on the Product Details Page (PDP) to display [attachments](https://help.vtex.com/tutorial/o-que-e-um-anexo--aGICk0RVbqKg6GYmQcWUm) and/or a [subscription form](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453).

An attachment is the optional and cost-free customization of a product.

![attachment-product-customization-select](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-customizer-0.png)
*Example of a PDP with the Product Customizer component displaying the product's attachments.*

Product subscriptions facilitate recurring sales by automatically scheduling the purchase of a specific product at the frequency requested by the customer.

![subscription-gif](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-customizer-1.gif)
*Example of a PDP with the Product Customizer component displaying the product subscription.*

## Before you start

- If you'll use the Product Customizer component to display **attachments**, [set up Assembly Options.](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) 
- If you'll use the Product Customizer component to display a **subscription form**, [set up Subscriptions.](https://help.vtex.com/tutorial/setting-up-subscription-v2--1FA9dfE7vJqxBna9Nft5Sj) The Product Customizer's integration with the Subscription module is native and automatically enabled when subscriptions settings are detected.

## Configuration 

1. Add the `product-customizer` app to your theme's dependencies in the `manifest.json`, for example:

```diff
  dependencies: {
+   "vtex.product-customizer": "2.x"
 }
```

2. Add the `product-assembly-options` block as a child of the `store.product` template (PDP template). This is enough to enable the subscription form.

```diff
  "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "flex-layout.row#product-main",
      "flex-layout.row#description",
      "shelf.relatedProducts",
      "product-reviews",
      "product-questions-and-answers",
+     "product-assembly-options"
    ]
  },
 ```

3. Declare the [`product-assembly-options` props](#product-assembly-options-props) according to your scenario.

### Displaying attachments (Optional)

1. Declare the `product-assembly-options` block and add the `assembly-option-input-values` block as its child to display the attachments of a product on the PDP. 

```json
  "product-assembly-options": {
    "children": [
      "assembly-option-input-values"
    ]
  },
```

2. Use the blocks exported by the `product-customizer` app to build the most suitable solution for your scenario.

| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `assembly-option-item-image` | Displays the attachment image. | 
| `assembly-option-item-quantity-selector` | Displays a quantity selector. | 
| `assembly-option-item-name` | Displays the attachment name. | 
| `assembly-option-item-price` | Displays the attachment price. |
| `assembly-option-item-customize` | Displays the `Customize` button. When clicked, it opens a modal that allows shoppers to customize the attachment. | 
| `assembly-option-item-children-description` | Displays a summary with all attachments selected. | 

3. Declare the [props](#props) for the chosen blocks according to your scenario. For example:

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

While building your solution, notice that you can receive inputs from three types of [attachments](https://help.vtex.com/tutorial/adding-an-attachment?locale=en):

- **Predefined options** - Predefined attachment options set in the `Permitted Values` field. Set up the `optionsDisplay` prop from the `assembly-option-input-values` block to define how these options are displayed.
-  **Free text** - Text input. Depending on the **Maximum Number of Characters** field in the attachment settings, shoppers may or may not face a character limit.
 -  **Boolean** - Boolean attachment options set in the `Permitted Values` field. Shoppers can select the attachment by simply clicking on a checkbox.
 
Check the following example where the three attachment types are implemented:

![product-customizer-select](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-customizer-2.png)

Check out below how the product attachment displayed above was registered in the Catalog: 

![attachment-product-customizer](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-customizer-3.png)

It's worth noting that when an attachment is registered as **required**, all attachment options are automatically made available to shoppers. If an attachment is **not required**, the `Add customization` button is rendered as in the example above, giving shoppers the option to add or not an attachment to their product.

Also, keep in mind that the **Checkout** doesn't natively display the customized product option selected by the shopper. To display the product in the Checkout with the selected attachments, it's necessary to customize the Checkout page, allowing it to read and render product data.

## Props

### `product-assembly-options` props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `initiallyOpened` | `enum` | Defines whether the customization box will be opened even if an attachment is not required (`always`) or if the customization box will be opened only if the attachment is required (`required`). | `required` |

### `assembly-option-input-values` props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `optionsDisplay` | `enum` | Defines whether a Checkbox (`box`) or a dropdown list (`select`) will be used to select the attachment's pre-defined options. | `select` |

### `assembly-option-item-customize`props

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `buttonProps` | `object` | Defines the behavior of the `Customize` button. In addition to the `collapse` prop, the `buttonProps` object also receives child blocks to build the content of the modal triggered when the button is clicked on.| `undefined` | 

- **`buttonProps`  object:**

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `collapse` | `enum` | `Customize` button positioning. Possible values are: `left` or `right`. | `left` | 

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

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
    <td align="center"><a href="https://github.com/leoWorkingGood"><img src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-product-customizer-4.png">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->