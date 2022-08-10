---
title: "Get List of SKUs"
slug: "listsku"
excerpt: "The endpoint retrieves general information about all store's variations."
hidden: true
createdAt: "2021-09-28T20:47:44.088Z"
updatedAt: "2021-09-29T15:22:22.663Z"
---
## Query params

| Param      | Type   | Description                                              |
| ---------- | ------ | -------------------------------------------------------- |
| from                 | integer           | The first page of the interval of the variation list.                                                                                                                     |
| to                 | integer           | The last page of the interval of the variation list.                                                                                                                     |


## Response object has the following properties:

| Attribute          | Type             | Description                                                                                                                                            |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| data                 | array           | List with information about the variation.                                                                                                                     |
| ↳ id                 | string           | Variation unique identifier number.                                                                                                                     
| _metadata                 | object           | Information about the organization and exhibition of the variation list.                                                                                                                     |
| ↳ total                 | integer           | Total of variations on the list.                                                                                                                     |
| ↳ from                 | integer           | The first page of the interval of the variation list.                                                                                                                     |
| ↳ to                 | integer           | The last page of the interval of the variation list.                                                                                                                     |


## Response body example: