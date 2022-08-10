---
title: "Delete fixed prices on a price table (or trade policy)"
slug: "deletefixedpricesonapricetableortradepolicy"
excerpt: "Deletes all Fixed Prices of an SKU in a specific Price Table (or Trade Policy)"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-02-27T16:56:10.833Z"
---
> know more about [Prices in VTEX Help](https://help.vtex.com/en/tutorial/prices-v2)


| Attribute    | Type        | Description |
| --------------- |:-------:| -------------------------------------------------------------------------------------------:|
| `itemId` | string | SKU Id |
| `priceTableId` | string | Price Table or Sales Channel Id |




## Response codes


200 - Success

403 - The credentials is not enabled to access the service

404 - Not found value

429 - Too many requests




## Authentication


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)