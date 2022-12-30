---
title: "Associate SKU Service"
slug: "catalog-api-post-sku-service"
excerpt: "Associates an SKU Service to an SKU."
hidden: false
createdAt: "2020-06-08T19:47:12.373Z"
updatedAt: "2022-07-22T17:32:33.280Z"
---
## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"SkuServiceTypeId\": 2,\n    \"SkuServiceValueId\": 1,\n    \"SkuId\": 1,\n    \"Name\": \"Test name\",\n    \"Text\": \"Test text\",\n    \"IsActive\": true\n}\n",
      "language": "json"
    }
  ]
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 2,\n    \"SkuServiceTypeId\": 1,\n    \"SkuServiceValueId\": 1,\n    \"SkuId\": 7,\n    \"Name\": \"Test name\",\n    \"Text\": \"Test text\",\n    \"IsActive\": true\n}\n",
      "language": "json"
    }
  ]
}
[/block]