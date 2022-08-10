---
title: "Update Specifications Field Value"
slug: "catalog-api-put-specification-field-value"
excerpt: "Updates a specification field value by the specification field's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-05-12T22:32:47.168Z"
---
[block:callout]
{
  "type": "info",
  "body": "This is a legacy endpoint. We recommend using [Update Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead."
}
[/block]
## Request body has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `FieldId` | integer | Specification Field ID |
| `Name` | string |  Specification Field Value Name |
| `Text` | string |  Specification Field Value Description |
| `IsActive` | boolean | If the Specification Field Value is active |
| `Position` | integer | Specification Field Value Position |

## ## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldValueId\": 276,\n    \"Name\": \"TesteInsertUpdate\",\n    \"Text\": \"Value Description2\",\n    \"IsActive\": true,\n    \"Position\": 100\n}",
      "language": "json"
    }
  ]
}
[/block]