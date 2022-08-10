---
title: "Get SkuId by RefId"
slug: "catalog-api-get-skuid-refid"
excerpt: "Retrieves an SKU ID by the SKU's Reference ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:42:55.168Z"
---
Identify the SKU ID by SKU Reference ID

> know more about [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `refId` | integer | Replace this variable with SKU reference ID that you need identify the SKU ID |



For example, in case you need get the SKU ID for the SKU reference ID `799`

You will have to replace de variable `refId` for `799`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/799
```






## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `skuId` | object | Object compose by SKU ID related to Reference ID searched |



## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)