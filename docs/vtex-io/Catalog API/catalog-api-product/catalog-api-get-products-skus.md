---
title: "Get Product And SkuIds"
slug: "catalog-api-get-products-skus"
excerpt: "Retrieves the IDs of all products and SKUs from a specific category by this category's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-07-03T15:49:53.658Z"
---
> know more about [Product](https://help.vtex.com/en/search/Product) and [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `categoryId` | integer | Replace this variable with the category ID that you need retrieves Product and SKU |



For example, in case you need get all Product and SKU from category ID `7`.

You will have to replace de variable `categoryId` for `7`:


```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/products/GetProductAndSkuIds?categoryId=7&_from=1&_to=10
```







## Pagination


For paging the results you have to use the request parameters `_from` and `_to`:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `_from` | integer | Insert the number that will start the request result |
| `_to` | integer |  Insert the number that will end the request result |






## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `data` | object | Object compose by Product IDs and SKU IDs, where the parent ID is from Products and the SKU IDs are the Child IDs |


## Authentication

This is a public API and don't need credentials to access.