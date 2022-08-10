---
title: "Get Specifications Group"
slug: "catalog-api-get-specification-group"
excerpt: "Retrieves details from a specification group by the ID of this group."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-27T20:38:48.901Z"
---
Retrieve details from Specification Group by its ID

> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `groupId` | integer | Specification Field ID |


For example, in case you need get details from specification group Id `7` .

You will have to replace the variables `groupId` for `7`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/specification/groupGet/7
```



## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `CategoryId` | integer |  Category ID |
| `Id` | integer | Specification Group ID |
| `Name` | string | Specification Group Name |
| `Position` | integer | Specification Group Position |


## Authentication

This is a public API and don't need credentials to access.