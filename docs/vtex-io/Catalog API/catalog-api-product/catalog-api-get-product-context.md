---
title: "Get Product and context"
slug: "catalog-api-get-product-context"
excerpt: "Retrieves context of a Product"
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-07-03T16:02:56.028Z"
---
Retrieves a specific Product by its ID



> know more about [Product in VTEX Help](https://help.vtex.com/en/search/Product)




## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `id` | integer | ID of the Product|
| `name` | string      |  Name of the Product  |
| `DepartmentId` | integer      |  Name of the Product  |
| `CategoryId`      | integer | ID of product Category|
| `BrandId`     | integer      | ID of the product Brand |
| `LinkId`  | string |Category URL |
| `RefId` | string     | Product Reference ID|
| `IsVisible` | boolean | If the product is visible in search and list pages |
| `Description` | string | Product Description, HTML is allowed |
| `DescriptionShort` | string | Product Short Description |
| `ReleaseDate` | string | Product Release Date, for list ordering and product cluster highlight |
| `KeyWords` | string | Alternatives Keywords to improve the product findability |
| `Title` | string | Meta Title for the Product page |
| `IsActive` | boolean | If the product is Active |
| `TaxCode` | string | SKUTax Code |
| `MetaTagDescription` | string | Meta Description for the Product page |
| `SupplierId` | string | Product Supplier ID |
| `ShowWithoutStock` | boolean | If the product can be visible without stock |
| `ListStoreId` | integer | Array with the ID of all the Sales Channel that are related to the product |
| `AdWordsRemarketingCode` | integer | Code specific for AdWords Remarketing |
| `LomadeeCampaignCode` | integer | Code specific for Lomadee Campaign |

## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"Name\": \"Ração Royal Canin Feline Urinary\",\n    \"DepartmentId\": 1,\n    \"CategoryId\": 10,\n    \"BrandId\": 2000000,\n    \"LinkId\": \"racao-royal-canin-feline-urinary\",\n    \"RefId\": \"\",\n    \"IsVisible\": true,\n    \"Description\": \"\",\n    \"DescriptionShort\": \"\",\n    \"ReleaseDate\": \"2020-01-06T00:00:00\",\n    \"KeyWords\": \"cat\",\n    \"Title\": \"Ração Royal Canin Feline Urinary\",\n    \"IsActive\": true,\n    \"TaxCode\": \"\",\n    \"MetaTagDescription\": \"\",\n    \"SupplierId\": null,\n    \"ShowWithoutStock\": true,\n    \"AdWordsRemarketingCode\": null,\n    \"LomadeeCampaignCode\": null,\n}",
      "language": "json"
    }
  ]
}
[/block]
## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)