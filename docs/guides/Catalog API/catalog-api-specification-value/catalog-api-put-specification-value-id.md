---
title: "Update Specification Value"
slug: "catalog-api-put-specification-value-id"
excerpt: "Updates a new Specification Value for a Category."
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-05-20T22:23:45.421Z"
---
## Request body has the following properties:

| Attribute | Type    | Description                                                            |
| --------- | ------- | ---------------------------------------------------------------------- |
| FieldId   | integer | Field ID                                                               |
| Name      | string  | Specification Value Name                                               |
| Text      |         | Specification Value Text                                               |
| IsActive  | boolean | Shows if the Category is active or not                                 |
| Position  | integer | The current Specification Value’s position in comparison to the others |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 101,\n    \"Name\": \"Test\",\n    \"Text\": null,\n    \"IsActive\": true,\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute  | Type    | Description                                                            |
| ---------- | ------- | ---------------------------------------------------------------------- |
| FieldValue | integer | Unique numerical identifier of the Specification Value                 |
| FieldId    | integer | Field ID                                                               |
| Name       | string  | Specification Value Name                                               |
| Text       | string  | Specification Value Text                                               |
| IsActive   | boolean | Shows if the Category is active or not                                 |
| Position   | integer | The current Specification Value’s position in comparison to the others |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldValue\": 23\n    \"FieldId\": 101,\n    \"Name\": \"Test\",\n    \"Text\": null,\n    \"IsActive\": true,\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]