---
title: "Update SKU"
slug: "catalog-api-put-sku"
excerpt: "Updates an existing SKU"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-11-17T18:12:35.341Z"
---
[block:callout]
{
  "type": "warning",
  "body": "You can't update an SKU as active if it doesn't have:\n\n- At least one [SKU File](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-sku-file#catalog-api-post-sku-file) associated with it.\n- At least one [active component](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-sku-kit#catalog-api-post-sku-kit) associated with it, if the SKU is set as a kit.\n\nIf you update an SKU with `IsActive` as `true` without this conditions, it will return a `400 - Bad Request`.",
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
## Request body has the following properties:

| Attribute                  | Type    | Description                                                                                         |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| Id                         | integer | SKU ID                                                                                              |
| ProductId                  | integer | Product ID                                                                                          |
| IsActive                   | boolean | Shows if the SKU is active                                                                          |
| Name                       | string  | SKU Name                                                                                            |
| RefId                      | string  | SKU RefId                                                                                           |
| PackagedHeight             | decimal | Packaged Height                                                                                 |
| PackagedLength             | decimal | Packaged Length                                                                                |
| PackagedWidth              | decimal | Packaged Width                                                                                    |
| PackagedWeightKg           | decimal | Packaged Weight                                                             |
| Height               | decimal | SKU Height                                                                                          |
| Length               | decimal | SKU Length                                                                                          |
| Width                      | decimal | SKU Width                                                                                           |
| WeightKg             | decimal | SKU Weight                                                                                 |
| CubicWeight                | decimal | [Cubic Weight](https://help.vtex.com/tutorial/understanding-the-cubic-weight-factor--tutorials_128) |
| IsKit                      | boolean | Shows if the SKU is a Kit                                                                           |
| CreationDate         | string  | SKU Creation Date                                                                                   |
| RewardValue                | decimal | How much the client will get rewarded by buying the SKU   |
| EstimatedDateArrival | string  | SKU Estimated Date Arrival                                                                   |
| ManufacturerCode           | string  | Manufacturer Code                                                                             |
| CommercialConditionId      | integer | Commercial Condition ID                                                                |
| MeasurementUnit            | string  | Measurement Unit                                                                                 |
| UnitMultiplier             | decimal | Multiplies the number of SKUs inserted on the cart                                |
| ModalType                  | string  | Defines deliver model                                                                               |
| KitItensSellApart          | boolean | Defines if Kit components can be sold apart                                        |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 310118448,\n   \"ProductId\": 310117069,\n   \"IsActive\": true,\n   \"Name\": \"sku test\",\n   \"RefId\": \"125478\",\n   \"PackagedHeight\": 10,\n   \"PackagedLength\": 10,\n   \"PackagedWidth\": 10,\n   \"PackagedWeightKg\": 10,\n   \"Height\": null,\n   \"Length\": null,\n   \"Width\": null,\n   \"WeightKg\": null,\n   \"CubicWeight\": 0.1667,\n   \"IsKit\": false,\n   \"CreationDate\": null,\n   \"RewardValue\": null,\n   \"EstimatedDateArrival\": null,\n   \"ManufacturerCode\": \"123\",\n   \"CommercialConditionId\": 1,\n   \"MeasurementUnit\": \"un\",\n   \"UnitMultiplier\": 1,\n   \"ModalType\": null,\n   \"KitItensSellApart\": false\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute                  | Type    | Description                                                                                         |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| Id                         | integer | SKU ID                                                                                              |
| ProductId                  | integer | Product ID                                                                                          |
| IsActive                   | boolean | Shows if the SKU is active                                                                          |
| Name                       | string  | SKU Name                                                                                            |
| RefId                      | string  | SKU RefId                                                                                           |
| PackagedHeight             | decimal | Packaged Height                                                                                  |
| PackagedLength             | decimal | Packaged Length                                                                                 |
| PackagedWidth              | decimal | Packaged Width                                                                                    |
| PackagedWeightKg           | decimal | Packaged Weight in Kilos                                                                 |
| Height               | decimal | SKU Height                                                                                          |
| Length               | decimal | SKU Length                                                                                          |
| Width                      | decimal | SKU Width                                                                                           |
| WeightKg             | decimal | SKU Weight in Kilos                                                                                 |
| CubicWeight                | decimal | [Cubic Weight](https://help.vtex.com/tutorial/understanding-the-cubic-weight-factor--tutorials_128) |
| IsKit                      | boolean | Shows if the SKU is a Kit                                                                           |
| CreationDate         | string  | SKU Creation Date                                                                                   |
| RewardValue                | decimal | How much the client will get rewarded by buying the SKU                |
| EstimatedDateArrival | string  | SKU Estimated Date Arrival                                                                      |
| ManufacturerCode           | string  | Manufacturer Code                                                                               |
| CommercialConditionId      | integer | Commercial Condition ID                                                                 |
| MeasurementUnit            | string  | Measurement Unit                                                                                  |
| UnitMultiplier             | decimal | Multiplies the number of SKUs inserted on the cart                               |
| ModalType                  | string  | Defines deliver model                                                                               |
| KitItensSellApart          | boolean | Defines if Kit components can be sold apart                                       |
| Videos                     | string  | Videos URLs                                                                                         |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 310118449,\n    \"ProductId\": 1,\n    \"IsActive\": true,\n    \"Name\": \"sku test\",\n    \"RefId\": \"1254789\",\n    \"PackagedHeight\": 10.0,\n    \"PackagedLength\": 10.0,\n    \"PackagedWidth\": 10.0,\n    \"PackagedWeightKg\": 10.0,\n    \"Height\": null,\n    \"Length\": null,\n    \"Width\": null,\n    \"WeightKg\": null,\n    \"CubicWeight\": 0.1667,\n    \"IsKit\": false,\n    \"CreationDate\": \"2020-04-22T12:12:47.5219561\",\n    \"RewardValue\": null,\n    \"EstimatedDateArrival\": null,\n    \"ManufacturerCode\": \"123\",\n    \"CommercialConditionId\": 1,\n    \"MeasurementUnit\": \"un\",\n    \"UnitMultiplier\": 1.0,\n    \"ModalType\": null,\n    \"KitItensSellApart\": false,\n    \"Videos\": []\n}",
      "language": "json"
    }
  ]
}
[/block]