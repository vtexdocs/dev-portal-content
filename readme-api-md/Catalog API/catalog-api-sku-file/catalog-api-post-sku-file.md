---
title: "Create SKU File"
slug: "catalog-api-post-sku-file"
excerpt: "Creates a new Image for an SKU based on its URL or on a form-data request body. \r\n## Request body example\r\n\r\n```json\r\n{\r\n      \"IsMain\": true,\r\n      \"Label\": \"\",\r\n      \"Name\": \"Royal-Canin-Feline-Urinary-SO\",\r\n      \"Text\": null,\r\n      \"Url\": \"https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\"\r\n      \r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n      \"Id\": 503,\r\n      \"ArchiveId\": 155491,\r\n      \"SkuId\": 1,\r\n      \"Name\": \"Royal-Canin-Feline-Urinary-SO\",\r\n      \"IsMain\": true,\r\n      \"Label\": \"\"\r\n}\r\n```"
hidden: false
createdAt: "2020-04-01T19:50:27.986Z"
updatedAt: "2022-07-11T17:57:40.184Z"
---
> ℹ️️ You can add up to 50 files for each SKU. If you have any questions, please feel free to contact [our Support](https://help.vtex.com/support).

[block:callout]
{
  "type": "warning",
  "body": "If you prefer, you can create the SKU File via file upload by a form-data request instead of using a JSON request body object. Using either option, you must upload an image file within the size limit of **3200 x 3200 pixels**.\n\nIf you opt to use a form-data request, you cannot add `IsMain`, `Label` or `Text` to it. To add these fields to your SKU file, you need to use the [Update SKU File](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-put-sku-file) endpoint."
}
[/block]