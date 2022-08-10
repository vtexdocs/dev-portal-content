---
title: "Search for SKU"
slug: "searchsku"
excerpt: "The endpoint retrieves general information about an SKU by the search criterias."
hidden: true
createdAt: "2021-09-28T20:47:44.087Z"
updatedAt: "2021-09-29T15:17:18.895Z"
---
## Query params

| Param      | Type   | Description                                              |
| ---------- | ------ | -------------------------------------------------------- |
| from                 | integer           | The first page of the interval of the variation list.                                                                                                                     |
| to                 | integer           | The last page of the interval of the variation list.                                                                                                                     |
| id                 | string           | Variation unique identifier number.                                                                                                                     |
| externalId                 | string           | Unique identifier number of the association of the variation with a Franchise Account.                                                                                                                 |

## Response object has the following properties:

| Attribute          | Type             | Description                                                                                                                                            |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| data                 | object           | List with information about the variation.                                                                                                                     |
| ↳ id                 | string           | Variation unique identifier number.                                                                                                                     |
| ↳ productId                 | string           | Product unique identifier number.                                                                                                                 |
| ↳ externalId                 | string           | Unique identifier number of the association of the variation with a Franchise Account.                                                                                                                 |
| _metadata                 | object           | Information about the organization and exhibition of the variation list.                                                                                                                     |
| ↳ total                 | integer           | Total of variations on the list.                                                                                                                     |
| ↳ from                 | integer           | The first page of the interval of the variation list.                                                                                                                     |
| ↳ to                 | integer           | The last page of the interval of the variation list.                                                                                                                     |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n\n\t\"data\":[\n\t\t{\n\t\t\t\"id\":\"2\",\n\t\t\t\"productId\":\"2\",\n\t\t\t\"externalId\":\"1909621862\"\n\t\t}\n\t],\n\t\"_metadata\":{\n\t\t\"total\":1,\n\t\t\"from\":1,\n\t\t\"to\":15\n\t}\n}",
      "language": "json"
    }
  ]
}
[/block]