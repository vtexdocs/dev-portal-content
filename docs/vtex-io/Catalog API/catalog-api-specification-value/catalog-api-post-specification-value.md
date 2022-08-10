---
title: "Create Specification Value"
slug: "catalog-api-post-specification-value"
excerpt: "Creates a new Specification Value for a Category"
hidden: false
createdAt: "2020-03-04T00:59:55.765Z"
updatedAt: "2020-04-22T20:33:47.135Z"
---
## Request body has the following properties:
| Attribute | Type    | Description                                                            |
| --------- | ------- | ---------------------------------------------------------------------- |
| FieldId   | integer | Field ID                                                               |
| Name      | string  | Specification Value Name                                               |
| Text      | string  | Specification Value Text                                               |
| IsActive  | boolean | Shows if the Category is active or not                                 |
| Position  | integer | The current Specification Value’s position in comparison to the others |

## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 101,\n    \"Name\": \"Teste\",\n    \"Text\": null,\n    \"IsActive\": true,\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute | Type    | Description                                                            |
| --------- | ------- | ---------------------------------------------------------------------- |
| FieldId   | integer | Field ID                                                               |
| Name      | string  | Specification Value Name                                               |
| Text      | string  | Specification Value Text                                               |
| IsActive  | boolean | Shows if the Category is active or not                                 |
| Position  | integer | The current Specification Value’s position in comparison to the others |