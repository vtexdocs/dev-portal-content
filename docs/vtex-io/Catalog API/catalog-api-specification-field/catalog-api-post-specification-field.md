---
title: "Create Specifications Field"
slug: "catalog-api-post-specification-field"
excerpt: "Creates a specification field in a category."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-03-13T19:47:44.318Z"
---
> know more about [Specifications in VTEX Help](https://help.vtex.com/search?q=Specifications)


## Request object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `Name` | string | Specification Field ID |
| `CategoryId` | integer |  Category ID |
| `FieldId` | integer | Specification Field ID |
| `IsActive` | boolean | If the Specification Field is active, default value is true  |
| `IsRequired` | boolean | If the Specification Field is required |
| `FieldTypeId` | integer | Specification Field Type ID |
| `FieldValueId` | integer | Specification Field Value ID |
| `Description` | string | Specification Field Description |
| `IsStockKeepingUnit` | boolean | If is a SKU Specification Field |
| `IsFilter` | boolean | If is a Filter Specification |
| `IsOnProductDetails` | boolean | If is visible in Product Page, default value is false |
| `Position` | integer | Specification Field Position |
| `IsWizard` | boolean | Obsolete Field |
| `IsTopMenuLinkActive` | boolean | If is visible in Top Menu, default value is false |
| `IsSideMenuLinkActive` | boolean | If is visible in Menu Link, default value is false |
| `DefaultValue` | string | Specification Field default Value |
| `FieldGroupId` | integer | Specification Field Group ID |
| `FieldGroupName` | string | Specification Field Group Name |



```
FieldTypeIds:  
1 - Text  
2 - Multi-Line Text  
4 - Number  
5 - Combo  
6 - Radio  
7 - CheckBox  
8 - Indexed Text  
9 - Indexed Multi-Line Text
```

> Read more about FieldTypeIds in our [Help Center](https://help.vtex.com/tutorial/setting-up-the-category-field-type--tutorials_286) article.


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
| `Description` | integer | Specification Field Description |
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


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)