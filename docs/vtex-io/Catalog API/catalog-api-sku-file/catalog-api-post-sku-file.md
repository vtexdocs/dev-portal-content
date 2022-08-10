---
title: "Create SKU File"
slug: "catalog-api-post-sku-file"
excerpt: "Creates a new Image on an SKU based on its URL or on a form-data request body"
hidden: false
createdAt: "2020-04-01T19:50:27.986Z"
updatedAt: "2021-03-16T20:42:29.472Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Attention",
  "body": "If you create the SKU File via form-data, you cannot add `IsMain`, `Label` or `Text` to it. To add these fields to your SKU file, you need to use the [Update SKU File](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-sku-file#catalog-api-put-sku-file) endpoint."
}
[/block]
## Request body has the following properties:
| Attribute | Type    | Description                                     |
| --------- | ------- | ----------------------------------------------- |
| IsMain    | boolean | Tells if the Image is the Main Image of the SKU |
| Label     | string  | Image Label                                     |
| Name      | string  | Image Name                                      |
| Text      | string  | General text of the Image                       |
| Url       | string  | Image URL                                       |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": " {\n      \"IsMain\": true,\n      \"Label\": \"\",\n      \"Name\": \"Royal-Canin-Feline-Urinary-SO\",\n      \"Text\": null,\n      \"Url\": \"https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\"\n      \n}",
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
| Label     | string  | Image Label                                      |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n      \"Id\": 503,\n      \"SkuId\": 1,\n      \"Name\": \"Royal-Canin-Feline-Urinary-SO\",\n      \"IsMain\": true,\n      \"Label\": \"\"\n}",
      "language": "json"
    }
  ]
}
[/block]