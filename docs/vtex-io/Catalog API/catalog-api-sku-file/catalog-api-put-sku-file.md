---
title: "Update SKU File"
slug: "catalog-api-put-sku-file"
excerpt: "Updates a new Image on an SKU based on its URL or on a form-data request body"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2021-02-22T14:43:32.012Z"
---
## Request body has the following properties:

| Attribute | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| IsMain    | boolean | Tells if the Image is the Main Image of the SKU |
| Label     | string  | Image Label                                     |
| Name      | string  | Image Name                                      |
| Text      | string  | General text of the Image. If you don't include the text on your request body, the current text will be erased.                       |
| Url       | string  | Image URL                                       |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"IsMain\": true,\n\t\"Label\": null,\n\t\"Name\": \"toilet-paper\",\n\t\"Text\": null,\n\t\"Url\": \"https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| Id        | integer | Unique identifier of the Image                  |
| SkuId     | integer | Unique identifier of an SKU                     |
| IsMain    | boolean | Tells if the Image is the Main Image of the SKU |
| Label     | string  | Image Labe                                      |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 508,\n    \"SkuId\": 7,\n    \"IsMain\": true,\n    \"Label\": null\n}",
      "language": "json"
    }
  ]
}
[/block]