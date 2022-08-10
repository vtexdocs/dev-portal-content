---
title: "Get Specifications Field Value"
slug: "catalog-api-get-specification-field-value"
excerpt: "Retrieves details from a specification field's value by this value's ID."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2020-02-28T17:47:24.678Z"
---
Retrieve details from a Specification Field Value by its ID

> know more about [Specifications in VTEX Help](https://help.vtex.com/en/search/Specifications)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `fieldValueId` | integer | Specification Field Value ID |


For example, in case you need get details from specification field value Id `70` .

You will have to replace the variables `fieldValueId` for `70`:

```
https://{{accountName}}.{{environment}}.com.br/api/catalog_system/pvt/specification/fieldValue/{{fieldValueId}}
```



## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `FieldValueId` | integer | Specification Field Value ID |
| `FieldId` | integer | Specification Field ID |
| `Name` | string |  Specification Field Value Name |
| `Text` | string |  Specification Field Value Description |
| `IsActive` | boolean | If the Specification Field Value is active |
| `Position` | integer | Specification Field Value Position |


## Authentication

This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)