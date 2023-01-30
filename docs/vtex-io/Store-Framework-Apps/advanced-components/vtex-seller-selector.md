---
title: "Seller Selector"
slug: "vtex-seller-selector"
hidden: false
createdAt: "2020-06-03T15:19:50.046Z"
updatedAt: "2022-02-09T19:12:58.545Z"
---
Seller Selector displays the number of [**sellers**](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w) your marketplace has for each product. It enables users to compare prices from each seller and add the desired product to their cart.

![exampleLayout](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-seller-selector-0.png)

## Configuration

1. Install the Seller Selector app to your store with the following command:
```sh
vtex install vtex.seller-selector@0.x
```

2. Add the Seller Selector app to your theme's dependencies in the `manifest.json` as shown below:

```json
"dependencies": {
  "vtex.seller-selector": "0.x"
}
```

3. Add the `link-seller` block, exported by the `vtex.seller-selector` app, inside your product page (`store.product` template). When rendered, the block will create a link to the Seller Selector main page. For example:

```diff
 "flex-layout.col#right-col": {
    "props": {
      "preventVerticalStretch": true,
      "rowGap": 0
    },
    "children": [
      "product-name",
+     "link-seller"
      "product-price#product-details",
      "product-separator",
      "flex-layout.row#buy-button",
      "availability-subscriber",
      "shipping-simulator",
      "share#default"
    ]
  },
```

By declaring the `link-seller` block, a page containing all available sellers will be displayed automatically. However, you can configure the Seller Selector page layout, using props for each one of the blocks used to build it behind the scenes. 


### Advanced Configuration
Behind the scenes, the Seller Selector page uses the following default implementation:

```json
{
  "store.sellers": {
    "blocks": [
      "seller-table"
    ]
  },
  "seller-table": {
    "children": [
      "vtex.store-components:product-name",
      "seller-simulate-shipping",
      "seller-head",
      "seller-body"
    ]
  },
  "seller-head": {
    "children": [
      "seller-head-cell#Seller",
      "seller-head-cell#Price",
      "seller-head-cell#Shipping",
      "seller-head-cell#PriceWithShipping",
      "seller-head-cell#BuyButton"
    ]
  },
  "seller-head-cell#Seller": {
    "props": {
      "title": "Seller"
    }
  },
  "seller-head-cell#Price": {
    "props": {
      "title": "Price"
    }
  },
  "seller-head-cell#Shipping": {
    "props": {
      "title": "Shipping"
    }
  },
  "seller-head-cell#PriceWithShipping": {
    "props": {
      "title": "Price With Shipping"
    }
  },
  "seller-head-cell#BuyButton": {
    "props": {
      "title": "Add To Cart"
    }
  },
  "seller-body": {
    "children": [
      "seller-row"
    ]
  },
  "seller-row": {
    "children": [
      "seller-name",
      "seller-price",
      "seller-shipping",
      "seller-price-with-shipping",
      "seller-add-to-cart"
    ]
  },
  "seller-add-to-cart":{
    "blocks":[
      "add-to-cart-button"
    ]
  }
}
```



| Block name   | Description  |
| -------- | ------------------------ |
| `seller-table`     |  Layout block that provides a table to build the Seller Selector page with other blocks. It is possible to build the page using three main blocks: `seller-simulate-shipping`, `seller-head` and `seller-body` (declared as children of `seller-head`). 
| `seller-simulate-shipping`  | Builds a form so users can add a postal code and then simulate the shipping costs to the desired address. |
| `seller-head`  | Builds a header to be used on the Seller Selector table. You can pass to it the `seller-head-cell` block as children. |
| `seller-head-cell` | Defines a title for each column in the table header. |
| `seller-body`  | Defines the page main content. It is responsible for displaying all sellers' data in the table body.|
| `seller-row`  | Used inside the Seller Selector table to separate seller's data into columns. You can use the blocks listed below (`seller-name`, `seller-price`, `seller-shipping`, `seller-price-with-shipping`, `seller-add-to-cart`) as `seller-row`'s children in order to provide all needed seller's data. |
| `seller-name` | Displays the seller name. |
| `seller-price` | Displays the seller price for a given product. |
| `seller-shipping` | Displays shipping cost considering the sellers' data. |
| `seller-price-with-shipping` | Displays the purchase final cost (shipping cost + product price). |
| `seller-add-to-cart` | Displays a Buy button that adds a given seller's product to the shopping cart. It is possible to use two different blocks inside of it `buy-button` or `add-to-cart-button` |
|`buy-button`  | Default buy button, will be used if nothing is provided in the blocks section of `seller-add-to-cart`|
|`add-to-cart-button`  | Buy button to use with Minicart.V2 and GoCommerce Stores |

#### `link-seller` props

| Prop name              | Type      | Description                                                                                                                                                                                                                                     | Default value |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `message`     | `string`  | Text displayed on link counter | `store/seller-link.linkText`|

| Message variables | Type | Description | Example |
| --- | --- | --- | --- |
| `sellerQuantity` | `number` | Number of sellers sell this product | <code>View {**sellerQuantity**, plural, one {1 more seller} other {# more sellers}}</code> |

This block uses the [ICU Message Format](https://format-message.github.io/icu-message-format-for-translators/), making it possible to fully edit the text message and variables displayed on block.

#### `seller-table` props

| Prop name              | Type      | Description                                                                                                                                                                                                                                     | Default value |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `limitShownShippingInformation`       | `number`  | Max number of shipping options to be displayed.                                                                                                                                                                             | `3`         |


#### `seller-add-to-cart` props

| Prop name              | Type      | Description                                                                                                                                                                                                                                     | Default value |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `isOneClickBuy`          | `boolean` | Defines if users will keep navigating in the same page once the Buy button was clicked on (`true`) or if they will be redirected (`false`)   | `false`         |



#### `seller-head-cell` props

| Prop name              | Type      | Description                                                                                                                                                                                                                                     | Default value |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `title`     | `string`  | Text displayed on the table header for each column. | `undefined`|                                                                                                                 



## Modus operandi
The Seller Selector app fetch seller's data automatically from the [admin's Catalog ](https://help.vtex.com/tutorial/configuring-the-seller--tutorials_392). 
Behind the scenes, the blocks exported from the app use the product context in which they are inserted to identify the seller's data in the SKU registry. 
Based on this, they are able to display seller data without having to declare each desired seller in your theme.



## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                     |
| ------------------------------- |
| `linkSellerContainer`           |
| `linkSeller`                    |
| `linkSellerText`                |
| `linkSellerNumber`              |
| `sellerMasterContainer`         |
| `sellerBuyContainer`            |
| `sellerList`                    |
| `sellerBodyCell`                |
| `sellerHead`                    |
| `sellerHeadCell`                |
| `sellerHeadText`                |
| `sellerName`                    |
| `sellerPrice`                   |
| `sellerPriceShipping`           |
| `sellerPriceShippingText`       |
| `sellerRow`                     |
| `sellerShipping`                |
| `sellerShippingText`            |
| `sellerRow`                     |
| `simulateShipping`              |
| `simulateShippingSearch`        |
| `simulateShippingSpinner`       |