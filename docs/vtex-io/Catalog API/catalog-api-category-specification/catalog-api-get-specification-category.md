---
title: "Get Specifications By Category Id"
slug: "catalog-api-get-specification-category"
excerpt: "Gets all specifications from a category by its ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2021-02-24T15:56:53.352Z"
---
## Response body has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `Name` | string | Specification Name |
| `CategoryId` | integer |  Category ID |
| `FieldId` | integer | Specification ID |
| `IsActive` | boolean | If the specification is active |
| `IsStockKeepingUnit` | boolean | If is an SKU specification |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Name\": \"Specification A\",\n        \"CategoryId\": 1,\n        \"FieldId\": 33,\n        \"IsActive\": true,\n        \"IsStockKeepingUnit\": false\n    },\n    {\n        \"Name\": \"Specification B\",\n        \"CategoryId\": 1,\n        \"FieldId\": 34,\n        \"IsActive\": true,\n        \"IsStockKeepingUnit\": false\n    },\n    {\n        \"Name\": \"Specification C\",\n        \"CategoryId\": 1,\n        \"FieldId\": 35,\n        \"IsActive\": false,\n        \"IsStockKeepingUnit\": false\n    },\n    {\n        \"Name\": \"Specification D\",\n        \"CategoryId\": 1,\n        \"FieldId\": 36,\n        \"IsActive\": false,\n        \"IsStockKeepingUnit\": false\n    },\n    {\n        \"Name\": \"Specification E\",\n        \"CategoryId\": 1,\n        \"FieldId\": 37,\n        \"IsActive\": false,\n        \"IsStockKeepingUnit\": false\n    },\n    {\n        \"Name\": \"Specification F\",\n        \"CategoryId\": 1,\n        \"FieldId\": 39,\n        \"IsActive\": false,\n        \"IsStockKeepingUnit\": false\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]