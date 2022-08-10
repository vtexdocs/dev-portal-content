---
title: "Delete an SKU seller association"
slug: "catalog-api-delete-seller-sku"
excerpt: "Remove the Seller SKU binding"
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:55:59.537Z"
---
Remove the Seller SKU binding

> know more about [Seller SKU in VTEX Help](https://help.vtex.com/en/search/seller%20sku)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `sellerId` | integer | Seller ID |
| `sellerSkuId` | integer | Seller SKU ID |


For example, in case you need remove the association/biding from Seller SKU `799` from Seller `myseller`.

You will have to replace the variables `sellerSkuId` for `799` and `sellerId` for `` :

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/kuseller/remove/myseller/799
```




## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)