---
title: "Get SKU by EAN"
slug: "catalog-api-get-sku-ean"
excerpt: "Retrieves an SKU by its EAN ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-03-24T18:15:23.057Z"
---
Retrieves a specific SKU by its EAN ID



> know more about [SKU in VTEX Help](https://help.vtex.com/en/search/SKU)



| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `ean` | integer | Replace this variable with the SKU EAN ID that you need retrieves details |






## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `id` | integer | SKU ID |
| `ProductId` | integer | ID from the related Product |
| `ProductRefId` | integer | Ref ID from the related Product |
| `NameComplete` | string | Product Name and SKU Name concatenated |
| `ProductName` | string| Product Name |
| `ProductDescription` | string | Product Description, HTML is allowed |
| `TaxCode` | string | SKU Tax Code |
| `SkuName` | string| SKU Name 
| `IsActive` | boolean | If the SKU is Active |
| `IsTransported` | boolean | Obsolete Field |
| `IsInventoried` | boolean | Obsolete Field |
| `IsGiftCardRecharge` | boolean | If the buy will generate Reward |
| `ImageUrl` | string | SKU image URL |
| `DetailUrl`  | string | Product URL |
| `CSCIdentification` | string      |  SKU Seller Identification  |
| `BrandId`     | integer      | Product Brand ID |
| `BrandName`     | string      | Product Brand Name |
| `Dimension` | object | Object of the SKU dimensions that used on shipping calculation |
| `cubicweight` | integer | SKU Cubic Weight |
| `height` | integer | SKU Height |
| `length` | integer | SKU Length |
| `weight` | integer | SKU Weight |
| `width` | integer | SKU Width |
| `RealDimension` | object | Object of the Real SKU dimensions, that appears in product page |
| `realCubicWeight` | integer | Real SKU Cubic Weight |
| `realHeight` | integer | Real SKU Height |
| `realLength` | integer | Real SKU Length |
| `realWeight` | integer | Real SKU Weight |
| `realWidth` | integer | Real SKU Width |
| `ManufacturerCode` | string | Product Supplier ID |
| `IsKit` | boolean | If the SKU is budle |
| `KitItems` | array of objects | Array with SKU ID from bundle components |
| `Services` | array of objects |  Array with Service ID that are related to the SKU  |
| `Categories` | array of objects | Categories from the related Product |
| `Attachments` | array of objects |  Array with Attachments ID that are related to the SKU  |
| `Collections` | array of objects |  Array with Collections ID that are related to the Product |
| `SkuSellers` | array of objects |  Array with related Sellers data |
| `SellerId` | integer | SKU Seller ID |
| `StockKeepingUnitId` | integer | SKU ID |
| `SellerStockKeepingUnitId` | integer | SKU ID in SKU Seller |
| `IsActive` | boolean | If the SKU is Active |
| `isFilter` | boolean | If the SKU is filter |
| `FreightCommissionPercentage` | integer | Registered value for Seller Freight Commission |
| `ProductCommissionPercentage` | integer | Registered value for Seller Product Commission |
| `SalesChannels` | integer | Array with the ID of all the Sales Channel that are related to the product |
| `Images` | object | Object with SKU image details |
| `ImageUrl` | string | Image URL |
| `ImageName` | string | Image Name |
| `Videos` | string | Videos URL |
| `FileId` | integer | SKU image ID |
| `SkuSpecifications` | object |  Array with related SKU Specifications |
| `ProductSpecifications` | object |  Array with related Product Specifications
| `FieldId` | integer | Specification ID |
| `FieldName` | string | Specification Name |
| `FieldValueIds` | object |  Array with related Specification Values ID |
| `FieldValues` | object |  Array with related Specification Values |
| `ProductClustersIds` | object |  Array with related Products Clusters ID |
| `ProductCategoryIds` | string | Category Hierarchy with Category IDs |
| `ProductGlobalCategoryId` | string | Global Category IDs  |
| `ProductCategories` | string | Category Hierarchy with Category Name |
| `CommercialConditionId`     | integer      | SKU Commercial Condition  ID |
| `RewardValue`     | integer | Reward value related to SKU |
| `AlternateIds` | object |  Array with alternate SKU IDs, like EAN and RefId |
| `AlternateIdValues` | object |  Array with values of alternative SKU IDs |
| `EstimatedDateArrival` | string | Estimated Arrival Date |
| `MeasurementUnit` | integer | SKU Unit Measurement|
| `UnitMultiplier` | integer | SKU Unit Multiplier |
| `InformationSource` | string | Information Source |
| `ModalType` | string | Modal Type |
| `KeyWords` | string | KeyWords related to the product |
| `ReleaseDate` | string | Release date of the product |




## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)