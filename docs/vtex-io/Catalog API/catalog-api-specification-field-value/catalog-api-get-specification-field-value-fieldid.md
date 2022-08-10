---
title: "Get Specifications Values By Field Id"
slug: "catalog-api-get-specification-field-value-fieldid"
excerpt: "Gets a list of all specification values from a Specification Field by this field's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-28T17:24:44.519Z"
---
Specifications Values By Field Id
Get a list of all specifications Values from a Specification Field by its ID

> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `fieldId` | integer | Specification Field ID |


For example, in case you need get all values from specification field Id `70` .

You will have to replace the variables `fieldId` for `70`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pub/specification/fieldvalue/{{fieldId}}
```




## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `FieldValueId` | integer | Specification Field Value ID |
| `Value` | string |  Specification Field Value |
| `IsActive` | boolean | If the Specification Field Value is active |
| `Position` | integer | Specification Field Value Position |




## Authentication

This is a public API and don't need credentials to access.