---
title: "Get SKU list by ProductId"
slug: "skulistbyproductid"
excerpt: "Retrieves a list with the SKUs related to a product by the product's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:43:59.564Z"
---
Retrieves the list of related SKUs from Product ID

> know more about [Product](https://help.vtex.com/en/search/Product) and [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `productId` | integer | Replace this variable with the Product ID that you need retrieves SKU List |






## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `IsPersisted` | boolean ||
| `IsRemoved` | boolean ||
| `id` | integer | SKU ID |
| `ProductId` | integer | ID from the related Product |
| `IsActive` | boolean | If the SKU is Active |
| `Name` | string| SKU Name
| `height` | integer | SKU Height |
| `RealHeight` | integer | Real SKU Height |
| `width` | integer | SKU Width |
| `RealWidth` | integer | Real SKU Width |
| `length` | integer | SKU Length |
| `RealLength` | integer | Real SKU Length |
| `WeightKg` | integer | SKU Weight |
| `RealWeightKg` | integer | Real SKU Weight |
| `ModalId` | string | Modal Type ID |
| `RefId` | string     | Product Reference ID|
| `CubicWeight` | integer | SKU Cubic Weight |
| `IsKit` | boolean | If the SKU is bundle item |
| `IsDynamicKit` | boolean | If the SKU is Dynamic bundle Item |
| `InternalNote` | string ||
| `DateUpdated` | string | Product Update Date|
| `RewardValue` | integer | Reward value related to SKU |
| `CommercialConditionId` | integer | SKU Commercial Condition ID |
| `EstimatedDateArrival` | string | Estimated Arrival Date |
| `FlagKitItensSellApart` | boolean | If the SKU bundle Items can sell separately |
| `ManufacturerCode` | string | Product Supplier ID |
| `ReferenceStockKeepingUnitId` | integer | SKU Reference ID |
| `Position` | integer | SKU Position |
| `EditionSkuId` | integer | SKU Edition ID |
| `ApprovedAdminId` | integer | Admin ID who has approved the SKU |
| `EditionAdminId` | integer | Admin ID who has edit the SKU |
| `ActivateIfPossible` | boolean    | If the SKU can be activate  |
| `SupplierCode` | string | Product Supplier ID |
| `MeasurementUnit` | integer | SKU Unit Measurement|
| `UnitMultiplier` | integer | SKU Unit Multiplier |
| `IsInventoried` | boolean | Obsolete Field |
| `IsTransported` | boolean | Obsolete Field |
| `IsGiftCardRecharge` | boolean | If the buy will generate Reward |
| `ModalType` | string | Modal Type |
| `isKitOptimized` | boolean | If the SKU is a Optimized bundle |





## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)