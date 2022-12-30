---
title: "Get Price"
slug: "getprice"
excerpt: "Retrieves price data given a specific SKU ID. Within the `fixedPrices` object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.\r\n\r\n ## Response body example\r\n\r\n```json\r\n{\r\n    \"itemId\": \"1\",\r\n    \"listPrice\": 50,\r\n    \"costPrice\": 90,\r\n    \"markup\": 30,\r\n    \"basePrice\": 117,\r\n    \"fixedPrices\": [\r\n        {\r\n            \"tradePolicyId\": \"1\",\r\n            \"value\": 50.5,\r\n            \"listPrice\": 50.5,\r\n            \"minQuantity\": 2,\r\n            \"dateRange\": {\r\n                \"from\": \"2021-12-31T01:00:00Z\",\r\n                \"to\": \"2022-12-31T01:00:00Z\"\r\n            }\r\n        },\r\n        {\r\n            \"tradePolicyId\": \"2\",\r\n            \"value\": 30,\r\n            \"listPrice\": 50,\r\n            \"minQuantity\": 2\r\n        }\r\n    ]\r\n}\r\n```"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2022-06-20T13:26:39.109Z"
---
