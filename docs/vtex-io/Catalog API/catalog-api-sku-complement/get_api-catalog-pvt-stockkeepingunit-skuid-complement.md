---
title: "Get SKU Complement by SKU ID"
slug: "get_api-catalog-pvt-stockkeepingunit-skuid-complement"
excerpt: "Retrieves a existing Complement of an SKU by its SKU ID"
hidden: false
createdAt: "2021-02-03T14:44:01.888Z"
updatedAt: "2021-02-03T18:10:22.540Z"
---
## Response body has the following properties:

| Attribute        | Type    | Description                                                                                                                       |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Id      | integer | SKU Complement ID                                                                      |
| ParentSkuId      | integer | SKU in which you are inserting the Complement                                                                                     |
| SkuId            | integer | SKU in which you are inserting as a Complement in the Parent SKU                                                                  |
| ComplementTypeId | integer | Type of the Compliment you are inserting the SKU as. `1` = assessor; `2` = suggestion; `3` = similar; `5` = show together |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"Id\": 21,\n        \"SkuId\": 15,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 2\n    },\n    {\n        \"Id\": 22,\n        \"SkuId\": 14,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 3\n    },\n    {\n        \"Id\": 23,\n        \"SkuId\": 13,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 3\n    },\n    {\n        \"Id\": 24,\n        \"SkuId\": 5,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 5\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]