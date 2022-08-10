---
title: "Create SKU Complement"
slug: "catalog-api-post-sku-complement"
excerpt: "Creates a new SKU Complement on a Parent SKU"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2021-02-01T18:43:22.621Z"
---
## Request body has the following properties:

| Attribute        | Type    | Description                                                                                                                       |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| ParentSkuId      | integer | SKU in which you are inserting the Complement                                                                                     |
| SkuId            | integer | SKU in which you are inserting as a Complement in the Parent SKU                                                                  |
| ComplementTypeId | integer | Type of the Compliment you are inserting the SKU as. `1` = assessor; `2` = suggestion; `3` = similar; `5` = show together |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"ParentSkuId\": 1,\n    \"SkuId\": 7,\n    \"ComplementTypeId\": 1\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute        | Type    | Description                                                                                                                       |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Id               | integer | SKU Complement ID: Identifier of SKU Complement association                                                                       |
| ParentSkuId      | integer | SKU in which you are inserting the Complement                                                                                     |
| SkuId            | integer | SKU in which you are inserting as a Complement in the Parent SKU                                                                  |
| ComplementTypeId | integer | Type of the Compliment you are inserting the SKU as. `1` = assessor; `2` = suggestion; `3` = similar; `5` = show together |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 23,\n    \"SkuId\": 7,\n    \"ParentSkuId\": 1,\n    \"ComplementTypeId\": 1\n}",
      "language": "text"
    }
  ]
}
[/block]