---
title: "Update SKU File"
slug: "catalog-api-put-sku-file"
excerpt: "Updates a new Image on an SKU based on its URL or on a form-data request body. \r\n## Request body example\r\n\r\n```json\r\n{\r\n    \"IsMain\": true,\r\n    \"Label\": null,\r\n    \"Name\": \"toilet-paper\",\r\n    \"Text\": null,\r\n    \"Url\": \"https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\"\r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 508,\r\n    \"ArchiveId\": 155491,\r\n    \"SkuId\": 7,\r\n    \"IsMain\": true,\r\n    \"Label\": null\r\n}\r\n```"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-07-11T17:58:22.088Z"
---
[block:callout]
{
  "type": "warning",
  "title": "",
  "body": "The `skuFileId` used in this request is the ID of the association of the image to the SKU that the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint responds (`Id` field)."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The SKU file has a size limit of `3200 x 3200` pixels."
}
[/block]

> ℹ️️ You can add up to 50 files for each SKU. If you have any questions, please feel free to contact [our Support](https://support.vtex.com/hc/en-us/requests).
