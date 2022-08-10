---
title: "Product Price"
slug: "ametllerorigen-ametller-custom-components"
excerpt: "ametllerorigen.ametller-custom-components@1.0.6"
hidden: true
createdAt: "2022-07-04T20:30:06.556Z"
updatedAt: "2022-08-09T07:30:54.088Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Product Price app is responsible for exporting blocks related to the product's price, such as list price, selling price and savings.

![image](https://user-images.githubusercontent.com/8443580/77692675-d5694180-6f85-11ea-8690-49db5be24b3d.png)

:information_source: Currently, **the Product Price is the only app responsible for providing product price blocks for your theme**. Both [Product Summary Price](https://vtex.io/docs/components/all/vtex.product-summary/product-summary-price/) and [Product Price](https://vtex.io/docs/components/all/vtex.store-components/product-price/) blocks, respectively from [Product Summary](https://vtex.io/docs/components/all/vtex.product-summary/) and [Store Components](https://vtex.io/docs/components/all/vtex.store-components/) apps, were deprecated and therefore will no longer be evolved.

## Configuration

### Step 1 - Adding the Product Price app to your theme's dependencies

In your theme's `manifest.json`, add the Product Price app as a dependency:

```json
"dependencies": {
  "vtex.product-price": "1.x"
}
```
  
Now, you can use all the blocks exported by the `product-price` app. Check out the full list below:

| Block name          |  Description |
| --------------------| -------- |
| `product-list-price`         | Renders the product list price. If it is equal or lower than the product selling price, this block will not be rendered. |
| `product-selling-price`      | Renders the product selling price.|
| `product-spot-price`         | Renders the product spot price. If it is equal to the product selling price, this block will not be rendered. This component finds the spot price by looking for the cheapest price of all installments options of count 1. For more information about how to set this up in your store, check this [document](https://docs.google.com/document/d/1zguIGidi_qFtoX101J7zPsjU7-MyV0qiQvTo_dOR_w0/edit?usp=sharing).|
| `product-installments`      | Renders the product installments. If more than one option is available, the one with the biggest number of installments will be displayed. |
| `product-installments-list` | Renders all the installments of the payment system with the biggest amount of installments options. |
| `product-installments-list-item` | Renders an installments option of the `product-installments-list-item` |
| `product-price-savings`           | Renders the product price savings, if there is any. It can show the percentage of the discount or the value of the absolute saving. | 
| `product-spot-price-savings`           | Renders the product spot price savings, if there is any. It can show the percentage of the discount or the value of the absolute saving. | 
| `product-list-price-range`    | Renders the product list price range. It follows the same logic applied to the `ListPrice`: if its value is equal to the product selling price, this block is not rendered. | 
| `product-selling-price-range` | The product selling price range. | 
| `product-seller-name` | Renders the name of the product's seller. |
| `product-price-suspense` | Renders a fallback component when the price is loading and its children blocks when the price is not loading. This block is extremely useful when the store works with asynchronous prices. |

All blocks listed above use product price data fetched from the store catalog. In order to understand further, please access the [Pricing Module overview](https://help.vtex.com/tracks/precos-101--6f8pwCns3PJHqMvQSugNfP).

### Step 2 - Adding the Product Price's blocks to your theme's templates

To add the Product Price's blocks in your theme, you just need to declare them as children of the `product-summary.shelf`, exported by the [Product Summary](https://vtex.io/docs/components/content-blocks/vtex.product-summary@2.52.3) app, or declare them in the theme's Product template (`store.product`).

Notice the following: these blocks necessarily need a Product context in order to work properly. Therefore, when declaring them as children of the `product-summary.shelf`, be sure that they are in a store template in which this context is available.

For example:

```json
"shelf#home": {
  "blocks": ["product-summary.shelf"]
},

"product-summary.shelf": {
  "children": [
    "product-list-price",
    "product-selling-price#summary",
    "product-price-savings",
    "product-installments"
  ]
},
```

Except for the `product-price-suspense`, every block in this app only has three props in common:

| Prop name          | Type      |  Description | Default value |
| --------------------| ----------|--------------|---------------|
| `markers`           |`[string]` | IDs of your choosing to identify the block's rendered message and customize it using the admin's Site Editor. Learn how to use them accessing the documentation on [Using the Markers prop to customize a block's message](https://vtex.io/docs/recipes/style/using-the-markers-prop-to-customize-a-blocks-message). Notice the following: a block's message can also be customized in the Store Theme source code using the `message` prop. |`[]`|
|  `blockClass`  |  `string`  |  Block  ID  of your choosing to  be  used  in [CSS  customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property).  |  `undefined`  |
|  `message`  |  `string`  |  Defines the block's default text i.e. the block message. You can also define which text message a block will render on the UI using the admin's Site Editor.  |  `undefined`  |

For example:

```json
"product-selling-price#summary": {
  "props": {
    "markers": [
      "highlight"
    ],
    "blockClass": "summary",
    "message": "Selling price: {sellingPriceValue}"
  }
},
```

If you are using the asynchronous price feature, you can take advantage of the `product-price-suspense` and its props:

| Prop name    | Type       | Description                                              | Default value       |
| :----------: | :--------: | :------------------------------------------------------: | :-----------------: |
| `Fallback`   | `block`    | Name of the block that will be rendered when the price is loading. | `rich-text#loading`  |

For example:

```json
{
  "rich-text#loading": {
    "props": {
      "text": "Loading..."
    }
  },
  "product-price-suspense": {
    "props": {
      "Fallback": "rich-text#loading"
    },
    "children": [
      "product-list-price#summary",
      "flex-layout.row#selling-price-savings",
      "product-installments#summary",
      "add-to-cart-button"
    ]
  },
  "product-summary.shelf": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-price-suspense"
    ]
  }
}
```

![9SOSUdfAVa](https://user-images.githubusercontent.com/40380674/97020006-69ed4f80-1527-11eb-8165-ff12389c7c81.gif)

### Step 3 - Editing the block's messages

Every Product Price's block uses the [ICU Message Format](https://format-message.github.io/icu-message-format-for-translators/), making it possible to fully edit the text message and variables displayed by each block.

The variable values are rendered according to the context wrapping the block, meaning that this last one uses product data to render the price accordingly. 

It is possible, however, to define which message texts a block will render on the UI using the `message` prop, as explained previously. 

The `markers` prop, in turn, needs an extra configuration in the admin's Site Editor to properly work. When using it, do not forget to access the [Using the Markers prop to customize a block's message](https://vtex.io/docs/recipes/style/using-the-markers-prop-to-customize-a-blocks-message/) documentation. 

![Product-Price-Site-Editor-gif](https://user-images.githubusercontent.com/52087100/78073694-bdbffd80-7377-11ea-9262-40854dccdd53.gif)

In addition to that, keep in mind the message variables for each block since you will need them to edit the desired messages using the admin's Site Editor:

- **`product-list-price`**

| Message variable | Type | Description |
| --- | --- | --- |
| `listPriceValue` | `string` | List price value. |
| `listPriceWithTax` | `string` | List price value with tax. |
| `taxPercentage` | `string` | Tax percentage. |

- **`product-selling-price`**

| Message variable | Type | Description |
| --- | --- | --- |
| `sellingPriceValue` | `string` | Selling price value. |
| `sellingPriceWithTax` | `string` | Selling price with tax. |
| `taxPercentage` | `string` | Tax percentage. |
| `hasListPrice` | `boolean` | Whether the product has a list price (`true`) or not (`false`). |

- **`product-spot-price`**

| Message variable | Type | Description |
| --- | --- | --- |
| `spotPriceValue` | `string` | Spot price value. |

- **`product-installments` and `product-installments-list-item`**

| Message variables | Type | Description |
| --- | --- | --- |
| `spotPriceValue` | `string` | Spot price value. |
| `installmentsNumber` | `string` | Number of installments. |
| `installmentValue` | `string` | Value of each installment. |
| `installmentsTotalValue` | `string` | Total value of installments. |
| `interestRate` | `string` | Interest rate. |
| `paymentSystemName` | `string` | Payment System of the installments. |
| `hasInterest` | `boolean` | Whether the installments have interest (`true`) or not (`false`). |

- **`product-price-savings`**

| Message variables | Type | Description |
| --- | --- | --- |
| `previousPriceValue` | `string` | Previous price value (list price). |
| `newPriceValue` | `string` | New price value (selling price). |
| `savingsValue` | `string` | Difference between previous product price and the new one. |
| `savingsWithTax` | `string` | Difference between previous product price and the new one with taxes. |
| `savingsPercentage` | `string` | Percentage of savings. |

- **`product-spot-price-savings`**

| Message variables | Type | Description |
| --- | --- | --- |
| `previousPriceValue` | `string` | Previous price value (list price). |
| `newSpotPriceValue` | `string` | New price value (spot price). |
| `spotPriceSavingsValue` | `string` | Difference between previous product price and the spot price. |
| `spotPriceSavingsWithTax` | `string` | Difference between previous product price and the spot price with taxes. |
| `spotPriceSavingsPercentage` | `string` | Percentage of savings. |
 
- **`product-list-price-range`**

| Message variables | Type | Description |
| --- | --- | --- |
| `minPriceValue` | `string` | Value of the cheapest list price SKU. |
| `maxPriceValue` | `string` | Value of the most expensive list price SKU. |
| `minPriceWithTax` | `string` | Value of the cheapest list price SKU with tax. |
| `maxPriceWithTax` | `string` | Value of the most expensive list price SKU with tax. |
| `listPriceValue` | `string` | Value of the list price of the only SKU available. |
| `listPriceWithTax` | `string` | Value of the list price of the only SKU available with tax. |

- **`product-selling-price-range`**

| Message variables | Type | Description |
| --- | --- | --- |
| `minPriceValue` | `string` | Value of the cheapest selling price SKU. |
| `maxPriceValue` | `string` | Value of the most expensive selling price SKU. |
| `minPriceWithTax` | `string` | Value of the cheapest selling price SKU with tax. |
| `maxPriceWithTax` | `string` | Value of the most expensive selling price SKU with tax. |
| `sellingPriceValue` | `string` | Value of the selling price of the only SKU available. |
| `sellingPriceWithTax` | `string` | Value of the selling price of the only SKU available with tax. |

- **`product-seller-name`**

| Message variable | Type | Description |
| --- | --- | --- |
| `sellerName` | `string` | The name of the product's seller. |

In the gif example above, the block was firstly displaying a `Save $224.40` message. By editing the message exported, it now renders a `You are saving: $224.40 (37%)` message thanks to the changes performed through the admin's Site Editor:

![product-price-edited-img](https://user-images.githubusercontent.com/52087100/78073688-bc8ed080-7377-11ea-9a7a-53c36d9a9fe2.png)

## Customization

To apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using  CSS  Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `installmentValue` |
| `installmentsListContainer` |
| `installmentsNumber` |
| `installmentsTotalValue` |
| `installments` |
| `interestRate` |
| `listPrice'` |
| `listPriceRangeMaxValue` |
| `listPriceRangeMaxWithTax` |
| `listPriceRangeMinValue` |
| `listPriceRangeMinWithTax` |
| `listPriceRangeUniqueValue` |
| `listPriceRangeUniqueWithTax` |
| `listPriceRange` |
| `listPriceValue` |
| `listPriceWithTax` | 
| `newPriceValue` |
| `newSpotPriceValue` | 
| `paymentSystemName` |
| `previousPriceValue` |
| `savingsPercentage` |
| `savingsValue` |
| `savingsWithTax` |
| `savings` |
| `sellerName` |
| `sellerNameContainer` |
| `sellerNameContainer--isDefaultSeller` |
| `sellingPrice--hasListPrice` |
| `sellingPriceRangeMaxValue` |
| `sellingPriceRangeMaxWithTax` |
| `sellingPriceRangeMinValue` |
| `sellingPriceRangeMinWithTax` |
| `sellingPriceRangeUniqueValue` |
| `sellingPriceRangeUniqueWithTax` |
| `sellingPriceRange` |
| `sellingPriceValue` |
| `sellingPriceWithTax` | 
| `sellingPrice` |
| `spotPriceSavingsPercentage` | 
| `spotPriceSavingsValue` | 
| `spotPriceSavingsWithTax` | 
| `spotPriceSavings` | 
| `spotPriceValue` |
| `spotPrice` |
| `taxPercentage` |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->