---
title: "Get SKU Complement by SKU Complement ID"
slug: "get_api-catalog-pvt-skucomplement-skucomplementid"
excerpt: "Retrieves a existing Complement of an SKU by its SKU Complement ID"
hidden: false
createdAt: "2020-08-20T17:10:13.286Z"
updatedAt: "2021-02-03T18:44:27.280Z"
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
      "code": "{\n    \"Id\": 22,\n    \"SkuId\": 14,\n    \"ParentSkuId\": 14,\n    \"ComplementTypeId\": 3\n}",
      "language": "json"
    }
  ]
}
[/block]