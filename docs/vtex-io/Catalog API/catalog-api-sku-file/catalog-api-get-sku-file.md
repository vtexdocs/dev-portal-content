---
title: "Get SKU File"
slug: "catalog-api-get-sku-file"
excerpt: "Gets general information about all Files inside the SKU"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-07-02T22:18:29.364Z"
---
## Response body has the following properties:

| Attribute | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| Id        | integer | Unique identifier of the Image                  |
| SkuId     | integer | Unique identifier of an SKU                     |
| Name      | string  | Image Name                                      |
| IsMain    | boolean | Tells if the Image is the Main Image of the SKU |
| Label     | string  | Image Label                                      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 503,\n        \"SkuId\": 1,\n        \"Name\": \"Royal-Canin-Feline-Urinary-SO\",\n        \"IsMain\": true,\n        \"Label\": \"\"\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]