---
title: "Create Specification Group"
slug: "catalog-api-post-specification-group"
excerpt: "Create a specification group."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2021-02-22T16:49:13.633Z"
---
> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


## Request object has the following properties:

| Attribute  | Type    | Description                                                            |
| ---------- | ------- | ---------------------------------------------------------------------- |
| CategoryId | integer | Category ID                                                            |
| Name       | string  | Group Name                                                             |

## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": 11,\n    \"Name\": \"Test\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute  | Type    | Description                                                            |
| ---------- | ------- | ---------------------------------------------------------------------- |
| Id | integer | Group ID                                                            |
| CategoryId | integer | Category ID                                                            |
| Name       | string  | Group Name                                                             |
| Position   | integer | The current Specification Group’s position in comparison to the others |

## Response boy example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": 11,\n    \"Id\": 7,\n    \"Name\": \"Test\",\n    \"Position\": 3\n}\n",
      "language": "json"
    }
  ]
}
[/block]