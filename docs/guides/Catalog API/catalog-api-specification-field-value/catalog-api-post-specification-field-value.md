---
title: "Create Specifications Field Value"
slug: "catalog-api-post-specification-field-value"
excerpt: "Creates a specification field value by the specification field's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-05-12T22:31:50.924Z"
---
[block:callout]
{
  "type": "info",
  "body": "This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead."
}
[/block]
> Learn more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


## Request object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `FieldId` | integer | Specification Field ID |
| `Name` | string |  Specification Field Value Name |
| `Text` | string |  Specification Field Value Description |
| `IsActive` | boolean | If the Specification Field Value is active |
| `Position` | integer | Specification Field Value Position |



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

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)