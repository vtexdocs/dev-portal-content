---
title: "Create or Update Base Price or Fixed Prices"
slug: "createupdatepriceorfixedprice"
excerpt: "Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.\r\n\r\n ## Request body example\r\n\r\n```json\r\n{\r\n    \"markup\": 30,\r\n    \"basePrice\": 100,\r\n    \"listPrice\": 35,\r\n    \"fixedPrices\": [\r\n        {\r\n            \"tradePolicyId\": \"1\",\r\n            \"value\": 31,\r\n            \"listPrice\": 32,\r\n            \"minQuantity\": 1,\r\n            \"dateRange\": {\r\n                \"from\": \"2022-05-21T22:00:00Z\",\r\n                \"to\": \"2023-05-28T22:00:00Z\"\r\n            }\r\n        },\r\n        {\r\n            \"tradePolicyId\": \"1\",\r\n            \"value\": 31.5,\r\n            \"listPrice\": 33,\r\n            \"minQuantity\": 2\r\n        }\r\n    ]\r\n}\r\n```"
hidden: false
createdAt: "2021-07-20T20:09:04.121Z"
updatedAt: "2022-06-20T13:27:25.077Z"
---
[block:callout]
{
  "type": "info",
  "body": "You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula `costPrice * (1 + markup) = basePrice`."
}
[/block]