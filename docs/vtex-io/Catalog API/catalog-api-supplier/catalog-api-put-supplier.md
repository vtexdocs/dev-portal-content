---
title: "Update Supplier"
slug: "catalog-api-put-supplier"
excerpt: "Updates general information of an existing Supplier"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-24T17:35:59.463Z"
---
## Request body has the following properties:

| Attribute        | Type    | Description                  |
| ---------------- | ------- | ---------------------------- |
| Name             | string  | Supplier Name                |
| CorporateName    | string  | Supplier Corporate Name      |
| StateInscription | string  | State Inscription            |
| Cnpj             | string  | Business ID                  |
| Phone            | string  | Supplier Phone               |
| CellPhone        | string  | Supplier Cellphone           |
| CorportePhone    | string  | Supplier Corporate Phone     |
| Email            | string  | Supplier email               |
| IsActive         | boolean | If Supplier is active or not |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Supplier\",\n    \"CorporateName\": \"asdfg\",\n    \"StateInscription\": \"\",\n    \"Cnpj\": \"33304981001272\",\n    \"Phone\": \"3333333333\",\n    \"CellPhone\": \"4444444444\",\n    \"CorportePhone\": \"5555555555\",\n    \"Email\": \"email@email.com\",\n    \"IsActive\": true\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute        | Type    | Description                  |
| ---------------- | ------- | ---------------------------- |
| Id               | integer | Supplier ID                  |
| Name             | string  | Supplier Name                |
| CorporateName    | string  | Supplier Corporate Name      |
| StateInscription | string  | State Inscription            |
| Cnpj             | string  | Business ID                  |
| Phone            | string  | Supplier Phone               |
| CellPhone        | string  | Supplier Cellphone           |
| CorportePhone    | string  | Supplier Corporate Phone     |
| Email            | string  | Supplier email               |
| IsActive         | boolean | If Supplier is active or not |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\":1\n    \"Name\": \"Supplier\",\n    \"CorporateName\": \"asdfg\",\n    \"StateInscription\": \"\",\n    \"Cnpj\": \"33304981001272\",\n    \"Phone\": \"3333333333\",\n    \"CellPhone\": \"4444444444\",\n    \"CorportePhone\": \"5555555555\",\n    \"Email\": \"email@email.com\",\n    \"IsActive\": true\n}",
      "language": "json"
    }
  ]
}
[/block]