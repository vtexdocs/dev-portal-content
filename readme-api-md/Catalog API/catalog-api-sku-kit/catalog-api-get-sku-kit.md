---
title: "Get SKU Kit by SKU ID or Parent SKU ID"
slug: "catalog-api-get-sku-kit"
excerpt: "Retrieves general information about the components of an SKU Kit by SKU ID or Parent SKU ID. \r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 7,\r\n    \"StockKeepingUnitParent\": 7,\r\n    \"StockKeepingUnitId\": 1,\r\n    \"Quantity\": 1,\r\n    \"UnitPrice\": 50.0000\r\n}\r\n```"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-07-11T20:51:19.614Z"
---
[block:callout]
{
  "type": "warning",
  "body": "You can choose only one query param per time. If you insert both query params at the same time, the request will be invalid.",
  "title": "Attention"
}
[/block]