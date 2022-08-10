---
title: "Get Product by RefId"
slug: "catalog-api-get-product-refid"
excerpt: "Retrieves a specific product by its Reference ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:27:14.787Z"
---
Retrieves a specific Product by its Reference ID


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
| `IsVisible` | boolean | If the product are visible in search and list pages |
| `Description` | string | Product Description, HTML is allowed |
| `DescriptionShort` | string | Product Short Description |
| `ReleaseDate` | string | Product Release Date, for list ordering and product cluster highlight |
| `KeyWords` | string | Alternatives Keywords to improve the product findability |
| `Title` | string | Meta Title for the Product page |
| `IsActive` | boolean | If the product is Active |
| `TaxCode` | string | SKU Tax Code |
| `MetaTagDescription` | string | Meta Description for the Product page |
| `SupplierId` | string | Product Supplier ID |
| `ShowWithoutStock` | boolean | If the product can be visible without stock |
| `ListStoreId` | integer | Array with the ID of all the Sales Channel that are related to the product |
| `AdWordsRemarketingCode` | integer | Obsolete Field |
| `LomadeeCampaignCode` | integer | Obsolete Field |



## Authentication

This is a private API and need credentials with viewer access



> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)