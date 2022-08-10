---
title: "List Specifications Group by Category"
slug: "catalog-api-get-specification-group-categoryid"
excerpt: "Retrieves a list of specification groups by the category ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:40:40.601Z"
---
Retrieve a list of Specification Group by Category ID

> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `categoryId` | integer | Specification Field ID |


For example, in case you need get a list of specification group from Category Id `7` .

You will have to replace the variables `categoryId` for `7`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/specification/groupbycategory/7
```




## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `CategoryId` | integer |  Category ID |
| `Id` | integer | Specification Group ID |
| `Name` | string | Specification Group Name |
| `Position` | integer | Specification Group Position |


## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)