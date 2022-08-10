---
title: "TaTa BuyBox"
slug: "tatauyshop-tata-buy-box"
excerpt: "tatauyshop.tata-buy-box@0.6.8"
hidden: true
createdAt: "2022-08-09T10:57:47.911Z"
updatedAt: "2022-08-09T10:57:47.911Z"
---
## Description

This app displays the main information of sellers of a product.

It has some component blocks, such as:
* [buy-box](#buy-box)
* [buy-box-context](#buy-box-context)
* [buy-box-compare-seller-info](#buy-box-compare-seller-info)
* [seller-page-back-button](#seller-page-back-button)
* [seller-page-buy-box](#seller-page-buy-box)

You can see the customization section [here](#customization).
## Integrating with your store

On your store-theme repository, add this in the manifest.json file: tatauyshop.tata-buy-box": "0.x".
# Store Blocks
## Buy Box

Insert the block "buy-box" on the product details page containing offers from other sellers.

Within this block, the use of the product insertion button in the shopping cart is also allowed.
```
"buy-box": {
    "component": "BuyBox",
    "allowed": ["add-to-cart-button"]
 }
```
![Media Placeholder](https://i.ibb.co/Zc7WMb4/buybox3.png)
## Buy Box Context
This block is the context of the BuyBox. It is a block that has the necessary functions to build a BuyBox.
```
"buy-box-context": {
    "component": "BuyBoxContext"
 }
```
## Buy Box Compare Seller Info
Insert the block "buy-box-compare-seller-info" on the product details page containing the amount of product offers and a link to check out these offers.
```
"buy-box-compare-seller-info": {
    "component": "BuyBoxCompareSellerInfo"
 }
```

![Media Placeholder](https://i.ibb.co/9Z0vHtQ/buybox1.png)
## Seller Page Back Button
Insert the block "seller-page-back-button" that is a link back to the product details page.
```
"seller-page-back-button": {
    "component": "SellerPageBackButton"
 }
```

![Media Placeholder](https://i.ibb.co/D5YXz5P/buybox2.png)
## Seller Page Buy Box
Insert the block "seller-page-buy-box" that is responsible for rendering the BuyBox on the sellers page, where it shows all sellers.
```
"seller-page-buy-box": {
    "component": "SellerPageBuyBox",
    "allowed": ["add-to-cart-button"]
  }
```

![Media Placeholder](https://i.ibb.co/CK3jf0n/buybox4.png)
## Customization

| CSS Handles            |
| ------------------     |
| `BuyBoxContainer`      |
| `BuyBoxTitle`          |
| `BuyBoxTitleContainer` |
| `BuyBoxProductPrice`   |
| `BuyBoxProductName`    |
| `BuyBoxSellerShipping` |