---
title: "Create / Edit Fixed Prices on a price table (or trade policy)"
slug: "createeditfixedpricesonapricetableortradepolicy"
excerpt: "This method will create or update the Fixed Prices of an SKU just for an specific Price Table (according to its Trade Policy)"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-04-10T20:43:21.678Z"
---
This method doesn't change the fixed prices of a different Price Table for the same SKU.

This method will delete all previous prices from the requested Price Table before inserting the new Fixed Prices.


> know more about [Prices in VTEX Help](https://help.vtex.com/en/tutorial/prices-v2)


| Attribute    | Type        | Description |
| --------------- |:-------:| -------------------------------------------------------------------------------------------:|
| `itemId` | string | SKU Id |
| `tradePolicyId` | string | Trade Policy Id or Price Table Name |
| `minQuantity` | integer | Minimum Quantity to active Fixed Price |
| `listPrice` | integer | SKU List Price |
| `value` | integer | SKU Fixed Price Value |




## Response codes


200 - Success

403 - The credentials is not enabled to access the service

404 - Not found value

429 - Too many requests




## Authentication


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)