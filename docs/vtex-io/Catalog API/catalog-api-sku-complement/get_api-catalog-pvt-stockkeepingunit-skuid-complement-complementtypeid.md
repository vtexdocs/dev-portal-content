---
title: "Get SKU Complements by Complement Type ID"
slug: "get_api-catalog-pvt-stockkeepingunit-skuid-complement-complementtypeid"
excerpt: "Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU"
hidden: false
createdAt: "2021-02-03T14:44:01.890Z"
updatedAt: "2021-02-03T18:11:27.680Z"
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
      "code": "[\n    {\n        \"Id\": 22,\n        \"SkuId\": 14,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 3\n    },\n    {\n        \"Id\": 23,\n        \"SkuId\": 13,\n        \"ParentSkuId\": 14,\n        \"ComplementTypeId\": 3\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]