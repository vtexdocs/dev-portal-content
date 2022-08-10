---
title: "Create SKU"
slug: "catalog-api-post-sku"
excerpt: "Creates a new SKU from scratch"
hidden: false
createdAt: "2020-03-12T19:12:33.305Z"
updatedAt: "2020-11-17T17:59:24.506Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Warning!",
  "body": "You can't create a new SKU as active. To set an SKU as active, it must have:\n\n- At least one [SKU File](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-sku-file#catalog-api-post-sku-file) associated with it.\n- At least one [active component](https://developers.vtex.com/vtex-developer-docs/reference/catalog-api-sku-kit#catalog-api-post-sku-kit) associated with it, if the SKU is set as a kit.\n\nIf you create an SKU with `IsActive` as `true`, it will return a `400 - Bad Request`."
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "Attention!",
  "body": "The `PackagedWeightKg` and `WeightKg` attributes are not exclusive in Kilos. It can be used in another weight unit. It is important to maintain consistency and use the same weight unit on both attributes."
}
[/block]
## Request body  has the following properties:

| Attribute                  | Type    | Description                                                                                         |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| ProductId                  | integer | Product ID                                                                                          |
| IsActive                   | boolean | Shows if the SKU is active. To avoid receiving a `400 - Bad Request` this attribute must be `false`     |
| Name                       | string  | SKU Name                                                                                            |
| RefId                      | string  | SKU RefId                                                                                           |
| PackagedHeight             | decimal | Packaged Height                                                                          |
| PackagedLength             | decimal | Packaged Length                                                                           |
| PackagedWidth              | decimal | Packaged Width                                                                       |
| PackagedWeightKg           | decimal | Packaged Weight  |
| Height        | decimal | SKU Height                                                                                          |
| Length         | decimal | SKU Length                                                                                          |
| Width                      | decimal | SKU Width                                                                                           |
| WeightKg | decimal | SKU Weight                                                                               |
| CubicWeight                | decimal | [Cubic Weight](https://help.vtex.com/tutorial/understanding-the-cubic-weight-factor--tutorials_128) |
| IsKit                      | boolean | Shows if the SKU is a Kit                                                                           |
| CreationDate   | string  | SKU Creation Date                                                                                   |
| RewardValue           | decimal | How much the client will get rewarded by buying the SKU                |
| EstimatedDateArrival | string  | SKU Estimated Date Arrival                                                                          |
| ManufacturerCode      | string  | Manufacturer Code                                                                                   |
| CommercialConditionId      | integer | Commercial Condition ID                                                                             |
| MeasurementUnit            | string  | Measurement Unit                                                                                    |
| UnitMultiplier             | decimal | Multiplies the amount of SKUs inserted on the cart                                                  |
| ModalType                  | string  | Defines deliver model                                                                               |
| KitItensSellApart         | boolean | Defines if Kit components can be sold apart                              |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"ProductId\": 310117069,\n   \"IsActive\": true,\n   \"Name\": \"sku test\",\n   \"RefId\": \"125478\",\n   \"PackagedHeight\": 10,\n   \"PackagedLength\": 10,\n   \"PackagedWidth\": 10,\n   \"PackagedWeightKg\": 10,\n   \"Height\": null,\n   \"Length\": null,\n   \"Width\": null,\n   \"WeightKg\": null,\n   \"CubicWeight\": 0.1667,\n   \"IsKit\": false,\n   \"CreationDate\": null,\n   \"RewardValue\": null,\n   \"EstimatedDateArrival\": null,\n   \"ManufacturerCode\": \"123\",\n   \"CommercialConditionId\": 1,\n   \"MeasurementUnit\": \"un\",\n   \"UnitMultiplier\": 1,\n   \"ModalType\": null,\n   \"KitItensSellApart\": false\n}\n",
      "language": "json"
    }
  ]
}
[/block]
## Response  has the following properties:
| Attribute                  | Type    | Description                                                                                         |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| Id                         | integer | SKU ID                                                                                              |
| ProductId                  | integer | Product ID                                                                                          |
| IsActive                   | boolean | Shows if the SKU is active                                                                          |
| Name                       | string  | SKU Name                                                                                            |
| RefId                      | string  | SKU RefId                                                                                           |
| PackagedHeight             | decimal | Packaged Height        |
| PackagedLength             | decimal | Packaged Length                         |
| PackagedWidth              | decimal | Packaged Width                             |
| PackagedWeightKg           | decimal | Packaged Weight in Kilos                |
| Height              | decimal | SKU Height                                                                                          |
| Length              | decimal | SKU Length                                                                                          |
| Width                      | decimal | SKU Width                                                                                           |
| WeightKg         | decimal | SKU Weight in Kilos                                                                                 |
| CubicWeight                | decimal | [Cubic Weight](https://help.vtex.com/tutorial/understanding-the-cubic-weight-factor--tutorials_128) |
| IsKit                      | boolean | Shows if the SKU is a Kit                                                                           |
| CreationDate        | string  | SKU Creation Date                                                                                   |
| RewardValue                | decimal | How much the client will get rewarded by buying the SKU     |
| EstimatedDateArrival | string  | SKU Estimated Date Arrival           |
| ManufacturerCode           | string  | Manufacturer Code                   |
| CommercialConditionId      | integer | Commercial Condition ID                |
| MeasurementUnit            | string  | Measurement Unit                                 |
| UnitMultiplier             | decimal | Multiplies the amount of SKUs inserted on the cart                       |
| ModalType                  | string  | Defines deliver model                                                                               |
| KitItensSellApart          | boolean | Defines if Kit components can be sold apart                           |
| Videos                     | string  | List of Videos URLs                                                                                 |
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Id\":3,\n   \"ProductId\": 310117069,\n   \"IsActive\": true,\n   \"Name\": \"sku test\",\n   \"RefId\": \"125478\",\n   \"PackagedHeight\": 10,\n   \"PackagedLength\": 10,\n   \"PackagedWidth\": 10,\n   \"PackagedWeightKg\": 10,\n   \"Height\": null,\n   \"Length\": null,\n   \"Width\": null,\n   \"WeightKg\": null,\n   \"CubicWeight\": 0.1667,\n   \"IsKit\": false,\n   \"CreationDate\": null,\n   \"RewardValue\": null,\n   \"EstimatedDateArrival\": null,\n   \"ManufacturerCode\": \"123\",\n   \"CommercialConditionId\": 1,\n   \"MeasurementUnit\": \"un\",\n   \"UnitMultiplier\": 1,\n   \"ModalType\": null,\n   \"KitItensSellApart\": false\n}\n",
      "language": "json"
    }
  ]
}
[/block]