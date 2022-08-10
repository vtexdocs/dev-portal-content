---
title: "Get products from a collection"
slug: "get-productsfromacollection"
excerpt: "Retrieves information about the products from a collection"
hidden: false
createdAt: "2020-12-21T16:28:05.321Z"
updatedAt: "2020-12-22T17:27:37.812Z"
---
## Response body has the following properties:

| Attribute     | Type    | Description                                    |
| ------------- | ------- | ---------------------------------------------- |
| `page` | integer | Page number of the Collection|
| `Size` | integer | Page size of the Collection |
| `TotalRows` | integer | Total rows of the Collection page|
| `TotalPage` | integer | Total pages of the Collection|
| `Data` | array of objects| Information about the products in the Collection|
| `ProductId` | integer | Product's ID|
| `SkuId` | integer | SKUs' ID |
| `SubCollectionId` | integer | SubCollection's ID  |
| `Position` | integer | Position of the Product inside the Collection|
| `ProductName` | string | Product name |
| `SkuImageUrl` | string | Image URL of the SKU|

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Page\": 1,\n    \"Size\": 1,\n    \"TotalRows\": 1,\n    \"TotalPage\": 1,\n    \"Data\": [\n        {\n            \"ProductId\": 1,\n            \"SkuId\": 1,\n            \"SubCollectionId\": 10587,\n            \"Position\": 1,\n            \"ProductName\": \"Creme de cabelo Softh 37:2000002 -- 1577991055.\",\n            \"SkuImageUrl\": \"https://cosmetics1.vteximg.com.br/arquivos/ids/155491\"\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]