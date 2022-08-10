---
title: "Update Specification Group"
slug: "catalog-api-put-specification-group"
excerpt: "Update a specification group"
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-04-22T19:00:27.006Z"
---
## Request body has the following properties:
| Attribute | Type    | Description              |
| --------- | ------- | ------------------------ |
| `Id`      | integer | Specification Group ID   |
| `Name`    | string  | Specification Group Name |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 24,\n    \"Name\": \"NewGroupName\"\n}",
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
      "code": "{\n    \"CategoryId\": 1,\n    \"Id\": 24,\n    \"Name\": \"NewGroupName\",\n    \"Position\": 4\n}",
      "language": "json"
    }
  ]
}
[/block]