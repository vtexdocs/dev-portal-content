---
title: "Get SKU"
slug: "catalog-api-get-sku"
excerpt: "Retrieves a specific SKU by its ID. This information is exactly what is needed to create a new SKU."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-09-15T23:57:47.422Z"
---
Retrieves a specific SKU by its ID



> know more about [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `skuId` | integer | Replace this variable with the SKU ID that you need retrieves details |







## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `id` | integer | SKU ID |
| `ProductId` | integer | ID from the related Product |
| `IsActive` | boolean | If the SKU is Active |
| `Name` | string |  SKU Name |
| `RefId` | integer | Ref ID from the related Product |
| `PackagedHeight` | integer | SKU Height |
| `PackagedLength` | integer | SKU Length |
| `PackagedWidth` | integer | SKU Width |
| `PackagedWeightKg` | integer | SKU Weight |
| `Height` | integer | Real SKU Height |
| `Length` | integer | Real SKU Length |
| `WeightKg` | integer | Real SKU Weight |
| `Width` | integer | Real SKU Width |
| `CubicWeight` | integer | SKU Cubic Weight |
| `IsKit` | boolean | If the SKU is budle |
| `CreationDate` | string | SKU Creation Date |
| `RewardValue` | string | Reward value related to SKU |
| `EstimatedDateArrival` | string | Estimated Arrival Date |
| `ManufacturerCode` | string | Product Supplier ID |
| `CommercialConditionId`     | integer      | SKU Commercial Condition  ID |
| `MeasurementUnit` | integer | SKU Unit Measurement|
| `UnitMultiplier` | integer | SKU Unit Multiplier |
| `ModalType` | string | Modal Type |
| `KitItensSellApart ` | string | Defines if Kit components can be sold apart |
| `Videos` | string | Videos URL |

## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)