---
title: "Associate Product Specification"
slug: "catalog-api-post-create-product-specification"
excerpt: "Associates a previously defined Specification to a Product"
hidden: false
createdAt: "2020-03-10T13:42:06.197Z"
updatedAt: "2021-03-11T15:21:13.515Z"
---
## Request has the following properties:

| Attribute    | Type    | Description               |
| ------------ | ------- | ------------------------- |
| FieldId      | integer | Field ID                  |
| FieldValueId | integer | Fied Value ID             |
| Text         | string  | Value inside the Field ID |

## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldId\": 19,\n    \"FieldValueId\": 1,\n    \"Text\": \"test\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response has the following properties:

| Attribute    | Type    | Description                                                |
| ------------ | ------- | ---------------------------------------------------------- |
| Id           | integer | Unique ID of the Specifications association with a Product |
| FieldId      | integer | Field ID                                                   |
| FieldValueId | integer | Fied Value ID                                              |
| Text         | string  | Value inside the Field ID                                  |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 41,\n    \"FieldId\": 19,\n    \"FieldValueId\": 1,\n    \"Text\": \"test\"\n}",
      "language": "json"
    }
  ]
}
[/block]