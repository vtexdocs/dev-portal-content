---
title: "Create SKU Kit"
slug: "catalog-api-post-sku-kit"
excerpt: "Creates new component to a specific Kit"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-10-13T15:53:44.357Z"
---
## Request body has the following properties:

| Attribute              | Type    | Description           |
| ---------------------- | ------- | --------------------- |
| StockKeepingUnitParent | integer |   SKU ID of the Kit SKU  |
| StockKeepingUnitId     | integer |  Component SKU ID  |
| Quantity               | integer | Component Quantity                             |
| UnitPrice              | integer | Component Price                                |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"StockKeepingUnitParent\": 7,\n    \"StockKeepingUnitId\": 1,\n    \"Quantity\": 1,\n    \"UnitPrice\": 50.0000\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute              | Type    | Description                                    |
| ---------------------- | ------- | ---------------------------------------------- |
| Id                     | integer | Kit SKU ID, same as the StockKeepingUnitParent |
| StockKeepingUnitParent | integer |   SKU ID of the Kit SKU  |
| StockKeepingUnitId     | integer |  Component SKU ID  |
| Quantity               | integer | Component Quantity                             |
| UnitPrice              | integer | Component Price                                |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 9,\n    \"StockKeepingUnitParent\": 7,\n    \"StockKeepingUnitId\": 1,\n    \"Quantity\": 1,\n    \"UnitPrice\": 50.0000\n}",
      "language": "json"
    }
  ]
}
[/block]