---
title: "Get SKU by RefId"
slug: "catalog-api-get-sku-refid"
excerpt: "Retrieves information about a specific SKU by its RefId"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-17T20:24:32.626Z"
---
## Response body has the following properties:

| Attribute                  | Type    | Description                                                                                         |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- |
| Id                         | integer | SKU ID                                                                                              |
| ProductId                  | integer | Product ID                                                                                          |
| IsActive                   | boolean | Shows if the SKU is active                                                                          |
| Name                       | string  | SKU Name                                                                                            |
| RefId                      | string  | SKU RefId                                                                                           |
| PackagedHeight             | decimal | Packaged Height                                                                                     |
| PackagedLength             | decimal | Packaged Length                                                                                     |
| PackagedWidth              | decimal | Packaged Width                                                                                      |
| PackagedWeightKg           | decimal | Packaged Weight in Kilos                                                                            |
| Height                     | decimal | SKU Height                                                                                          |
| Length                     | decimal | SKU Length                                                                                          |
| Width                      | decimal | SKU Width                                                                                           |
| WeightKg                   | decimal | SKU Weight in Kilos                                                                                 |
| CubicWeight                | decimal | [Cubic Weight](https://help.vtex.com/tutorial/understanding-the-cubic-weight-factor--tutorials_128) |
| IsKit                      | boolean | Shows if the SKU is a Kit                                                                           |
| CreationDate | string  | SKU Creation Date                                                                                   |
| RewardValue                | decimal | How much the client will get rewarded by buying the SKU                                             |
| EstimatedDateArrival | string  | SKU Estimated Date Arrival                                                                          |
| ManufacturerCode           | string  | Manufacturer Code                                                                                   |
| CommercialConditionId      | integer | Commercial Condition ID                                                                             |
| MeasurementUnit            | string  | Measurement Unit                                                                                    |
| UnitMultiplier             | decimal | Multiplies the amount of SKUs inserted on the cart                                                  |
| ModalType                  | string  | Defines deliver model                                                                               |
| KitItensSellApart          | boolean | Defines if Kit components can be sold apart                                                         |
| Videos                     | string  | Videos URLs                                                                                         |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"ProductId\": 1,\n    \"IsActive\": true,\n    \"Name\": \"Royal Canin Feline Urinary 500g\",\n    \"RefId\": \"0001\",\n    \"PackagedHeight\": 6.0000,\n    \"PackagedLength\": 24.0000,\n    \"PackagedWidth\": 14.0000,\n    \"PackagedWeightKg\": 550.0000,\n    \"Height\": null,\n    \"Length\": null,\n    \"Width\": null,\n    \"WeightKg\": null,\n    \"CubicWeight\": 1.0000,\n    \"IsKit\": false,\n    \"CreationDate\": \"2020-03-12T15:42:00\",\n    \"RewardValue\": null,\n    \"EstimatedDateArrival\": null,\n    \"ManufacturerCode\": \"\",\n    \"CommercialConditionId\": 1,\n    \"MeasurementUnit\": \"un\",\n    \"UnitMultiplier\": 1.0000,\n    \"ModalType\": null,\n    \"KitItensSellApart\": false,\n    \"Videos\": null\n}",
      "language": "json"
    }
  ]
}
[/block]