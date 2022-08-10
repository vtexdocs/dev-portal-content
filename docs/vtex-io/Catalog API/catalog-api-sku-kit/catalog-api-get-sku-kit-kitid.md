---
title: "Get SKU Kit"
slug: "catalog-api-get-sku-kit-kitid"
excerpt: "Retrieves general information about a component of a Kit"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-22T14:50:49.029Z"
---
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