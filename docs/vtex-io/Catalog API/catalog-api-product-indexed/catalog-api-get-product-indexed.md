---
title: "Get Indexed Info"
slug: "catalog-api-get-product-indexed"
excerpt: "Retrieve details of Product Indexed Info"
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:56:55.441Z"
---
Retrieve details of Product Indexed Info




| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `productId` | integer | Replace this variable with the Product ID that you need retrieve details |



For example, in case you need retrieve indexed info from Product ID `7`.

You will have to replace de variable `productId` for `7`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/products/GetIndexedInfo/7
```


## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `body` | object | XML object with product indexed info |





## Authentication



This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)