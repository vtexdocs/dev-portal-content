---
title: "Get SKU and context"
slug: "catalog-api-get-sku-context"
excerpt: "Retrieves context of an SKU"
hidden: false
createdAt: "2020-07-08T15:21:24.529Z"
updatedAt: "2020-07-08T15:42:57.653Z"
---
## Response body has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `id` | integer | SKU ID |
| `ProductId` | integer | ID from the related Product |
| `NameComplete` | string | Product Name and SKU Name concatenated |
| `ProductName` | string| Product Name |
| `ProductDescription` | string | Product Description, HTML is allowed |
| `ProductRefId` | integer | Ref ID from the related Product |
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
| `FreightCommissionPercentage` | integer | Registered value for Seller Freight Commission |
| `ProductCommissionPercentage` | integer | Registered value for Seller Product Commission |
| `SalesChannels` | array | Array with the ID of all the Sales Channel that are related to the product |
| `Images` | object | Object with SKU image details |
| `ImageUrl` | string | Image URL |
| `ImageName` | string | Image Name |
| `Videos` | array of strings | Videos URL |
| `FileId` | integer | SKU image ID |
| `SkuSpecifications` | object |  Array with related SKU Specifications |
| `ProductSpecifications` | object |  Array with related Product Specifications
| `FieldId` | integer | Specification ID |
| `FieldName` | string | Specification Name |
| `FieldValueIds` | array of objects |  Array with related Specification Values ID |
| `FieldValues` | array of objects |  Array with related Specification Values |
| `isFilter` | boolean | If the SKU is filter |
| `ProductClustersIds` | string |  Products Clusters ID |
| `ProductCategoryIds` | string | Category Hierarchy with Category IDs |
| `ProductGlobalCategoryId` | integer | Global Category IDs  |
| `ProductCategories` | object | Category Hierarchy with Category's ID and Name |
| `CommercialConditionId` | integer      | SKU Commercial Condition  ID |
| `RewardValue`     | float | Reward value related to SKU |
| `AlternateIds` | object |  Array with alternate SKU IDs, like EAN and RefId |
| `AlternateIdValues` | array |  Array with values of alternative SKU IDs |
| `EstimatedDateArrival` | string | Estimated Arrival Date |
| `MeasurementUnit` | integer | SKU Unit Measurement|
| `UnitMultiplier` | integer | SKU Unit Multiplier |
| `InformationSource` | string | Information Source |
| `ModalType` | string | Modal Type |
| `KeyWords` | string | KeyWords related to the product |
| `ReleaseDate` | string | Release date of the product |
| `ProductIsVisible` | boolean | If the Product is visible or not |
| `ShowIfNotAvailable` | boolean | If the Product will be shown if it is not available |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 7,\n    \"ProductId\": 1,\n    \"NameComplete\": \"Ração Royal Canin Feline Urinary sku test\",\n    \"ProductName\": \"Ração Royal Canin Feline Urinary\",\n    \"ProductDescription\": \"\",\n    \"ProductRefId\": \"\",\n    \"TaxCode\": \"\",\n    \"SkuName\": \"sku test\",\n    \"IsActive\": false,\n    \"IsTransported\": true,\n    \"IsInventoried\": true,\n    \"IsGiftCardRecharge\": false,\n    \"ImageUrl\": \"\",\n    \"DetailUrl\": \"/racao-royal-canin-feline-urinary/p\",\n    \"CSCIdentification\": null,\n    \"BrandId\": \"2000000\",\n    \"BrandName\": \"Orma Carbono\",\n    \"Dimension\": {\n        \"cubicweight\": 1.0000,\n        \"height\": 10.0000,\n        \"length\": 10.0000,\n        \"weight\": 10.0000,\n        \"width\": 10.0000\n    },\n    \"RealDimension\": {\n        \"realCubicWeight\": 0.0,\n        \"realHeight\": 0.0,\n        \"realLength\": 0.0,\n        \"realWeight\": 0.0,\n        \"realWidth\": 0.0\n    },\n    \"ManufacturerCode\": \"123\",\n    \"IsKit\": true,\n    \"KitItems\": [\n        {\n            \"Id\": 1,\n            \"Name\": \"Ração Royal Canin Feline Urinary 500g\",\n            \"UnitPrice\": 50.0000,\n            \"Amount\": 1,\n            \"EstimatedDateArrival\": null,\n            \"Dimension\": {\n                \"cubicweight\": 1.0000,\n                \"height\": 6.0000,\n                \"length\": 24.0000,\n                \"weight\": 550.0000,\n                \"width\": 14.0000\n            },\n            \"RefId\": \"0001\",\n            \"EAN\": \"1234567890123\",\n            \"IsKitOptimized\": false\n        },\n        {\n            \"Id\": 2,\n            \"Name\": \"Ração Royal Canin Feline Urinary 1,5kg\",\n            \"UnitPrice\": 100.0000,\n            \"Amount\": 1,\n            \"EstimatedDateArrival\": null,\n            \"Dimension\": {\n                \"cubicweight\": 1.0000,\n                \"height\": 25.0000,\n                \"length\": 19.0000,\n                \"weight\": 1550.0000,\n                \"width\": 9.0000\n            },\n            \"RefId\": \"0002\",\n            \"EAN\": \"\",\n            \"IsKitOptimized\": false\n        }\n    ],\n    \"Services\": [],\n    \"Categories\": [],\n    \"Attachments\": [\n        {\n            \"Id\": 1,\n            \"Name\": \"Nome\",\n            \"Keys\": [],\n            \"Fields\": [],\n            \"IsActive\": true,\n            \"IsRequired\": false\n        }\n    ],\n    \"Collections\": [],\n    \"SkuSellers\": [\n        {\n            \"SellerId\": \"1\",\n            \"StockKeepingUnitId\": 7,\n            \"SellerStockKeepingUnitId\": \"7\",\n            \"IsActive\": true,\n            \"FreightCommissionPercentage\": 0.0,\n            \"ProductCommissionPercentage\": 0.0\n        }\n    ],\n    \"SalesChannels\": [\n        1,\n        2,\n        3\n    ],\n    \"Images\": [\n        {\n            \"ImageUrl\": \"https://lojadobreno.vteximg.com.br/arquivos/ids/155455/Water-Bottle.jpg?v=637213074965370000\",\n            \"ImageName\": \"\",\n            \"FileId\": 155455\n        }\n    ],\n    \"Videos\": [\n        \"google.com\"\n    ],\n    \"SkuSpecifications\": [\n        {\n            \"FieldId\": 40,\n            \"FieldName\": \"SKUFieldA\",\n            \"FieldValueIds\": [\n                133\n            ],\n            \"FieldValues\": [\n                \"A\"\n            ],\n            \"IsFilter\": false,\n            \"FieldGroupId\": 17,\n            \"FieldGroupName\": \"NewGroupName 2\"\n        },\n        {\n            \"FieldId\": 32,\n            \"FieldName\": \"Peso\",\n            \"FieldValueIds\": [\n                131\n            ],\n            \"FieldValues\": [\n                \"500g\"\n            ],\n            \"IsFilter\": false,\n            \"FieldGroupId\": 11,\n            \"FieldGroupName\": \"Especificações\"\n        }\n    ],\n    \"ProductSpecifications\": [\n        {\n            \"FieldId\": 34,\n            \"FieldName\": \"Field B\",\n            \"FieldValueIds\": [],\n            \"FieldValues\": [\n                \"Giant\"\n            ],\n            \"IsFilter\": false,\n            \"FieldGroupId\": 17,\n            \"FieldGroupName\": \"NewGroupName 2\"\n        }\n    ],\n    \"ProductClustersIds\": \"152\",\n    \"ProductCategoryIds\": \"/1/10/\",\n    \"ProductGlobalCategoryId\": 3367,\n    \"ProductCategories\": {\n        \"10\": \"Ração Seca\",\n        \"1\": \"Alimentação\"\n    },\n    \"CommercialConditionId\": 1,\n    \"RewardValue\": 0.0,\n    \"AlternateIds\": {\n        \"Ean\": \"12341234\",\n        \"RefId\": \"125478\"\n    },\n    \"AlternateIdValues\": [\n        \"1234123\",\n        \"12341234\",\n        \"125478\"\n    ],\n    \"EstimatedDateArrival\": null,\n    \"MeasurementUnit\": \"un\",\n    \"UnitMultiplier\": 1.0000,\n    \"InformationSource\": \"Database\",\n    \"ModalType\": null,\n    \"KeyWords\": \"aaaaaaa\",\n    \"ReleaseDate\": \"2020-01-06T00:00:00\",\n    \"ProductIsVisible\": true,\n    \"ShowIfNotAvailable\": true\n}",
      "language": "json"
    }
  ]
}
[/block]