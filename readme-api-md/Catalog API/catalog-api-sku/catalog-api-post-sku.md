---
title: "Create SKU"
slug: "catalog-api-post-sku"
excerpt: "Creates a new SKU. \r\n\r\n### Request body example\r\n\r\n```json\r\n{\r\n   \"ProductId\": 310117069,\r\n   \"IsActive\": true,\r\n   \"ActivateIfPossible\": true,\r\n   \"Name\": \"sku test\",\r\n   \"RefId\": \"125478\",\r\n   \"PackagedHeight\": 10,\r\n   \"PackagedLength\": 10,\r\n   \"PackagedWidth\": 10,\r\n   \"PackagedWeightKg\": 10,\r\n   \"Height\": null,\r\n   \"Length\": null,\r\n   \"Width\": null,\r\n   \"WeightKg\": null,\r\n   \"CubicWeight\": 0.1667,\r\n   \"IsKit\": false,\r\n   \"CreationDate\": null,\r\n   \"RewardValue\": null,\r\n   \"EstimatedDateArrival\": null,\r\n   \"ManufacturerCode\": \"123\",\r\n   \"CommercialConditionId\": 1,\r\n   \"MeasurementUnit\": \"un\",\r\n   \"UnitMultiplier\": 2.0000,\r\n   \"ModalType\": null,\r\n   \"KitItensSellApart\": false,\r\n   \"Videos\": [ \"https://www.youtube.com/\" ]\r\n}\r\n``` \r\n\r\n### Response body example\r\n\r\n```json\r\n{\r\n   \"Id\":3,\r\n   \"ProductId\": 310117069,\r\n   \"IsActive\": true,\r\n   \"ActivateIfPossible\": true,\r\n   \"Name\": \"sku test\",\r\n   \"RefId\": \"125478\",\r\n   \"PackagedHeight\": 10,\r\n   \"PackagedLength\": 10,\r\n   \"PackagedWidth\": 10,\r\n   \"PackagedWeightKg\": 10,\r\n   \"Height\": null,\r\n   \"Length\": null,\r\n   \"Width\": null,\r\n   \"WeightKg\": null,\r\n   \"CubicWeight\": 0.1667,\r\n   \"IsKit\": false,\r\n   \"CreationDate\": null,\r\n   \"RewardValue\": null,\r\n   \"EstimatedDateArrival\": null,\r\n   \"ManufacturerCode\": \"123\",\r\n   \"CommercialConditionId\": 1,\r\n   \"MeasurementUnit\": \"un\",\r\n   \"UnitMultiplier\": 2.0000,\r\n   \"ModalType\": null,\r\n   \"KitItensSellApart\": false,\r\n   \"Videos\": [ \"https://www.youtube.com/\" ]\r\n}\r\n```"
hidden: false
createdAt: "2020-03-12T19:12:33.305Z"
updatedAt: "2022-11-09T17:52:38.818Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Warning!",
  "body": "You can't create a new SKU as active. To set an SKU as active, it must have:\n\n- At least one [SKU File](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-post-sku-file) associated with it.\n- At least one [active component](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-post-sku-kit) associated with it, if the SKU is set as a kit.\n\nIf you create an SKU with `IsActive` as `true`, it will return a `400 - Bad Request`."
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Attention!",
  "body": "The `PackagedWeightKg` and `WeightKg` attributes are not exclusive in Kilos. It can be used in another weight unit. It is important to maintain consistency and use the same weight unit on both attributes."
}
[/block]