---
title: "Get SKU Bindings information"
slug: "getpagedadmin"
excerpt: "Retrieves SKU Bindings administrative information using optional query params `sellerId`, `skuId`, `sellerSkuId` and `IsActive` to filter results and `size` to restrict the amount of results. \r\n\r\n > ℹ This path is an updated version of `/api/catalog_system/pvt/skuseller/admin`.\r\n\r\n## Response body example\r\n\r\n```json\r\n[\r\n    {\r\n        \"IsPersisted\": true,\r\n        \"IsRemoved\": false,\r\n        \"SkuSellerId\": 1,\r\n        \"UpdateDate\": \"2019-12-04T01:56:00.673Z\",\r\n        \"RequestedUpdateDate\": null,\r\n        \"SellerStockKeepingUnitId\": \"12\",\r\n        \"SellerId\": \"cosmetics1\",\r\n        \"StockKeepingUnitId\": 25,\r\n        \"IsActive\": true\r\n    }\r\n]\r\n```"
hidden: false
createdAt: "2022-07-27T15:19:35.876Z"
updatedAt: "2022-07-28T19:14:16.976Z"
---
