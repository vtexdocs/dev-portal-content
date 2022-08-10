---
title: "Get SKU Kit by SKU ID or Parent SKU ID"
slug: "catalog-api-get-sku-kit"
excerpt: "Retrieves general information about the components of an SKU Kit by SKU ID or Parent SKU ID"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2021-01-12T19:22:28.428Z"
---
[block:callout]
{
  "type": "warning",
  "body": "You can choose only one query param per time. If you insert both query params at the same time, the request will be invalid.",
  "title": "Attention"
}
[/block]
## Query Params has the following properties:
| Attribute              | Type    | Description                                    |
| ---------------------- | ------- | ---------------------------------------------- |
| skuId | integer | SKU’s unique numerical identifier |
| parentSkuId | integer | Parent SKU’s unique numerical identifier                         |

## Response body has the following properties:

| Attribute              | Type    | Description                                    |
| ---------------------- | ------- | ---------------------------------------------- |
| Id                     | integer | Kit SKU ID, same as the StockKeepingUnitParent |
| StockKeepingUnitParent | integer | SKU ID of the Kit SKU                          |
| StockKeepingUnitId     | integer | Kit component SKU ID                           |
| Quantity               | integer | Component Quantity                             |
| UnitPrice              | integer | Component Price                                |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 7,\n    \"StockKeepingUnitParent\": 7,\n    \"StockKeepingUnitId\": 1,\n    \"Quantity\": 1,\n    \"UnitPrice\": 50.0000\n}",
      "language": "json"
    }
  ]
}
[/block]