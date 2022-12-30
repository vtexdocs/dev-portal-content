---
title: "Get custom prices schema"
slug: "get_-v-custom-prices-session-schema"
excerpt: "Retrieves all custom price for all shopping scenarios"
hidden: false
createdAt: "2020-09-04T15:44:57.986Z"
updatedAt: "2022-02-03T13:15:28.163Z"
---
## Response body has the following properties:
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`fields`",
    "1-0": "`name`",
    "2-0": "`type`",
    "3-0": "`useEmail`",
    "0-1": "array of objects",
    "0-2": "Order Configuration criteria",
    "1-2": "Criteria name",
    "2-2": "Criteria type",
    "3-2": "Defines if the custom price should use the user's email to validate it",
    "3-1": "boolean",
    "2-1": "string",
    "1-1": "string"
  },
  "cols": 3,
  "rows": 4
}
[/block]
## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"fields\": [\n    {\n      \"name\": \"orderType\",\n      \"type\": \"string\"\n    },\n    {\n      \"name\": \"state\",\n      \"type\": \"string\"\n    }\n  ],\n    \"useEmail\": true\n}",
      "language": "json"
    }
  ]
}
[/block]