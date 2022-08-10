---
title: "Update Specifications Field"
slug: "catalog-api-put-specification-field"
excerpt: "Updates a specification field in a category."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-05-12T22:30:29.185Z"
---
[block:callout]
{
  "type": "info",
  "body": "This is a legacy endpoint. We recommend using [Update Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification) instead."
}
[/block]
## Request object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `Name` | string | Field Name |
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