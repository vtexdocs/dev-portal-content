---
title: "Update SKU"
slug: "catalog-api-put-sku"
excerpt: "Updates an existing SKU. \r\n\r\n### Request body example\r\n\r\n```json\r\n{\r\n   \"Id\": 310118448,\r\n   \"ProductId\": 310117069,\r\n   \"IsActive\": true,\r\n   \"ActivateIfPossible\": true,\r\n   \"Name\": \"sku test\",\r\n   \"RefId\": \"125478\",\r\n   \"PackagedHeight\": 10,\r\n   \"PackagedLength\": 10,\r\n   \"PackagedWidth\": 10,\r\n   \"PackagedWeightKg\": 10,\r\n   \"Height\": null,\r\n   \"Length\": null,\r\n   \"Width\": null,\r\n   \"WeightKg\": null,\r\n   \"CubicWeight\": 0.1667,\r\n   \"IsKit\": false,\r\n   \"CreationDate\": null,\r\n   \"RewardValue\": null,\r\n   \"EstimatedDateArrival\": null,\r\n   \"ManufacturerCode\": \"123\",\r\n   \"CommercialConditionId\": 1,\r\n   \"MeasurementUnit\": \"un\",\r\n   \"UnitMultiplier\": 2.0000,\r\n   \"ModalType\": null,\r\n   \"KitItensSellApart\": false,\r\n   \"Videos\": [ \"https://www.youtube.com/\" ]\r\n}\r\n```\r\n\r\n### Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 310118449,\r\n    \"ProductId\": 1,\r\n    \"IsActive\": true,\r\n    \"ActivateIfPossible\": true,\r\n    \"Name\": \"sku test\",\r\n    \"RefId\": \"1254789\",\r\n    \"PackagedHeight\": 10.0,\r\n    \"PackagedLength\": 10.0,\r\n    \"PackagedWidth\": 10.0,\r\n    \"PackagedWeightKg\": 10.0,\r\n    \"Height\": null,\r\n    \"Length\": null,\r\n    \"Width\": null,\r\n    \"WeightKg\": null,\r\n    \"CubicWeight\": 0.1667,\r\n    \"IsKit\": false,\r\n    \"CreationDate\": \"2020-04-22T12:12:47.5219561\",\r\n    \"RewardValue\": null,\r\n    \"EstimatedDateArrival\": null,\r\n    \"ManufacturerCode\": \"123\",\r\n    \"CommercialConditionId\": 1,\r\n    \"MeasurementUnit\": \"un\",\r\n    \"UnitMultiplier\": 2.0000,\r\n    \"ModalType\": null,\r\n    \"KitItensSellApart\": false,\r\n    \"Videos\": [ \"https://www.youtube.com/\" ]\r\n}\r\n```"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-11-09T17:52:39.189Z"
---
[block:callout]
{
  "type": "warning",
  "body": "You can't update an SKU as active if it doesn't have:\n\n- At least one [SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-file) associated with it.\n- At least one [active component](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-post-sku-kit) associated with it, if the SKU is set as a kit.\n\nIf you update an SKU with `IsActive` as `true` without this conditions, it will return a `400 - Bad Request`.",
  "title": "Warning!"
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "The `PackagedWeightKg` and `WeightKg` attributes are not exclusive in Kilos. It can be used in another weight unit. It is important to maintain consistency and use the same weight unit on both attributes.",
  "title": "Attention!"
}
[/block]