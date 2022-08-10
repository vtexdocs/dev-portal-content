---
title: "Get SKU seller"
slug: "catalog-api-get-seller-sku"
excerpt: "Retrieves the details of a seller's SKU by its ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-09-10T14:56:55.158Z"
---
Retrieves the Seller SKU details by its ID

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `sellerId` | integer | Seller ID |
| `sellerSkuId` | integer | Seller SKU ID |


For example, in case you need get details from Seller SKU `799` from Seller `myseller`.

You will have to replace the variables `sellerSkuId` for `799` and `sellerId` for `myseller` :

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/seller/myseller
```





## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `IsPersisted` | boolean | If the seller is Persisted |
| `IsRemoved` | boolean |  If the seller is removed |
| `SkuSellerId` | integer | SKU Id in Seller |
| `sellerId` | string | Product Seller ID |
| `StockKeepingUnitId` | integer | SKU ID in VTEX  |
| `SellerStockKeepingUnitId` | string | SKU Seller ID |
| `isActive` | boolean | If the SKU binding is active  |
| `UpdateDate` | string | Last Update Date |
| `RequestedUpdateDate` | string | Last Update Request Date  |




## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)