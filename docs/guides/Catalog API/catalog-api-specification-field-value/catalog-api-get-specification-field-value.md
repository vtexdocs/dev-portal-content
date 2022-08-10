---
title: "Get Specifications Field Value"
slug: "catalog-api-get-specification-field-value"
excerpt: "Retrieves details from a specification field's value by this value's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-05-12T22:31:15.656Z"
---
[block:callout]
{
  "type": "info",
  "body": "This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead."
}
[/block]
## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `FieldValueId` | integer | Specification Field Value ID |
| `FieldId` | integer | Specification Field ID |
| `Name` | string |  Specification Field Value Name |
| `Text` | string |  Specification Field Value Description |
| `IsActive` | boolean | If the Specification Field Value is active |
| `Position` | integer | Specification Field Value Position |


## Authentication

This is a private API which requires credentials with viewer access.


> Learn more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)