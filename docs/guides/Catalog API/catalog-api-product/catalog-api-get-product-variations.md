---
title: "Get Product's SKUs by Product ID"
slug: "catalog-api-get-product-variations"
excerpt: "Retrieves data about the product and all SKUs related to it by the product's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2021-05-28T17:37:27.170Z"
---
## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `productId` | integer | ID of the Product |
| `name` | string      |  Name of the Product  |
| `salesChannel` | integer      |  Sales Channel Product Context  |
| `available`      | boolean | If the product are Available |
| `displayMode`     | integer      |  |
| `dimensions`  | string |Category URL |
| `dimensionsInputType` | string | Product Reference ID|
| `dimensionsMap` | boolean | If the product are visible in search and list pages |
| `skus` | object | Array with all releated SKUs |
| `sku` | integer | SKU ID |
| `skuname` | string | SKU Name |
| `dimensions` | string | |
| `available` | boolean | If the SKU is available |
| `availablequantity` | integer | Available SKU stock quantity |
| `cacheVersionUsedToCallCheckout` | string | |
| `listPriceFormated` | string | List price with currency formatting |
| `listPrice` | integer | SKU List Price |
| `taxFormated` | string | Tax cost with currency formatting |
| `taxAsInt` | integer | Tax cost as integer |
| `bestPriceFormated` | string | Price after all discounts and benefits with currency formatting |
| `bestPrice` | integer | Price after all discounts and benefits |
| `installments` | integer | Maximum Installments quantity in the product context |
| `installmentsValue` | integer | Value of the Installments |
| `installmentsInsterestRate` | integer | Installments Interest Rate |
| `image` | string | URL of SKU image |
| `sellerId` | integer | SKU Seller ID |
| `seller` | string | SKU Seller Name|
| `measures` | object | Object of the SKU dimensions |
| `cubicweight` | integer | SKU Cubic Weight |
| `height` | integer | SKU Height |
| `length` | integer | SKU Length |
| `weight` | integer | SKU Weight |
| `width` | integer | SKU Width |
| `unitMultiplier` | integer | SKU Unit Multiplier |
| `rewardValue` | integer | Reward value for Reward Program |