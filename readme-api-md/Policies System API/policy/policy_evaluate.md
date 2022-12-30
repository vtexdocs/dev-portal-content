---
title: "Evaluate Policies"
slug: "policy_evaluate"
excerpt: "This endpoint consults all policies and checks the ones that satisfy the request body’s conditions."
hidden: false
createdAt: "2021-05-04T19:56:47.527Z"
updatedAt: "2021-05-05T15:03:49.477Z"
---
## Request body has the following properties:

| Attribute | Type   | Description                                 |
| --------- | ------ | ------------------------------------------- |
| resource  | string | Location of the data used on the policy     |
| context   | object | Conditions that the Policy needs to satisfy |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"resource\": \"vrn:vtex.promotions-alert:aws-us-east-1:kamila:master:/_v/promotions_alert\",\n    \"context\" : {\n        \"brandId\": \"2000001\",\n        \"discountPercentage\": \"91.00\" \n    }\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute | Type   | Description                             |
| --------- | ------ | --------------------------------------- |
| id        | string | Action ID                               |
| metadata  | object | Metadata object from the current action |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"id\": \"SendSlackMessage\",\n        \"metadata\": {\n            \"channel\": \"C01NJFF35R6\",\n            \"relatedUsers\": [\n                \"URUNDC2NB\"\n            ],\n            \"alertDescription\": \"Avoid selling products from Berenice with a discount greater than 70%.\"\n        }\n    }\n]",
      "language": "json"
    }
  ]
}
[/block]