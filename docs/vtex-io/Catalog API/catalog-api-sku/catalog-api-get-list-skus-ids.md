---
title: "List all SKU IDs"
slug: "catalog-api-get-list-skus-ids"
excerpt: "Retrieves the IDs of all SKUs in the store. Presents the result with page size and pagination."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:46:25.981Z"
---
Retrieves all SKUs IDs from store in a result with page size and pagination


> know more about [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `page` | integer | Replace this variable with the result page number that you need retrieves SKU ID |
| `pagesize` | integer | Replace this variable with the page size that you need retrieves SKU ID, maximum value `1000` |



For example, in case you need get all SKU ID from page `7` with a page size `50`.

You will have to replace de variable `page` for `7` and the variable `pagesize` to `50`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/sku/stockkeepingunitids?page=7&pagesize=50
```





## Pagination
For paging the results you have to use the request parameter `page`:

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `page` | integer | Replace this variable with the result page number that you need retrieves SKU ID |






## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `skuIds` | object | Object compose by SKU IDs, that where in the search context |






## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)