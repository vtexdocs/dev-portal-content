---
title: "Update Specification Group"
slug: "catalog-api-put-specification-group-groupid"
excerpt: "Update a specification group"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-07-07T20:30:01.720Z"
---
## Request body has the following properties:
| Attribute | Type    | Description              |
| --------- | ------- | ------------------------ |
| `CategoryId`      | integer | Specification Group Category   |
| `Id`      | integer | Specification Group ID   |
| `Name`    | string  | Specification Group Name |
| `Position`      | integer | Specification Group Position  |

## Request body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": 1,\n    \"Id\": 17,\n    \"Name\": \"NewGroupName\",\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:
| Attribute | Type    | Description              |
| --------- | ------- | ------------------------ |
| `CategoryId`      | integer | Specification Group Category   |
| `Id`      | integer | Specification Group ID   |
| `Name`    | string  | Specification Group Name |
| `Position`      | integer | Specification Group Position  |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"CategoryId\": 1,\n    \"Id\": 17,\n    \"Name\": \"NewGroupName 2\",\n    \"Position\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]