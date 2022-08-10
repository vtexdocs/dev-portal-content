---
title: "Get Specifications Field"
slug: "catalog-api-get-specification-field"
excerpt: "Retrieves details from a specification field by this field's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-28T17:37:24.841Z"
---
Retrieve details from Specification Field by its ID

> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `fieldId` | integer | Specification Field ID |


For example, in case you need get details from specification field Id `70` .

You will have to replace the variables `fieldId` for `70`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/specification/fieldGet/{{fieldId}}
```




> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)



## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `Name` | string | Specification Field ID |
| `CategoryId` | integer |  Category ID |
| `FieldId` | integer | Specification Field ID |
| `IsActive` | boolean | If the Specification Field is active |
| `IsRequired` | boolean | If the Specification Field is required |
| `FieldTypeId` | integer | Specification Field Type ID |
| `FieldValueId` | integer | Specification Field Value ID |
| `FieldTypeName` | string | Field Type Name |
| `Description` | string | Specification Field Description |
| `IsStockKeepingUnit` | boolean | If is a SKU Specification Field |
| `IsFilter` | boolean | If is a Filter Specification |
| `IsOnProductDetails` | boolean | If is visible in Product Page |
| `Position` | integer | Specification Field Position |
| `IsWizard` | boolean | Obsolete Field |
| `IsTopMenuLinkActive` | boolean | If is visible in Top Menu |
| `IsSideMenuLinkActive` | boolean | If is visible in Menu Link |
| `DefaultValue` | string | Specification Field default Value |
| `FieldGroupId` | integer | Specification Field Group ID |
| `FieldGroupName` | string | Specification Field Group Name |





## Authentication

This is a public API and don't need credentials to access.