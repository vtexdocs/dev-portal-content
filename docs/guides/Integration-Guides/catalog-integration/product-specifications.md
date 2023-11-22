---
title: "Product specifications"
slug: "product-specifications"
hidden: false
createdAt: "2021-12-14T13:58:54.540Z"
updatedAt: "2022-02-04T21:23:05.347Z"
---
Learn more with this [article about specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?&utm_source=autocomplete#).

>ℹ️ If you wish to implement color variation in your products, we recommend you do not use specifications. Instead, see this tutorial about [How to implement product color variation](https://developers.vtex.com/docs/guides/how-to-implement-product-color-variation).

## Data Model

| Field | Description | Required | Format | Default |
|---|---|---|---|---|
| Id | ID of Specification. This Id is used to delete/update the specification | No | Integer | AutoIncrement |
| ProductId | ID of Product | Yes | Integer | - |
| FieldId | Field ID | Yes | Integer | - |
| FieldValueId | ID of FieldValue. ONLY for `FieldTypeId`(5,6,7). | Mandatory for 5,6,7. MUST NOT be used for any other field types | Integer | null |
| Text | Value of specification. Only for `FieldTypeId` different from (5,6,7) | Mandatory for all fields EXCEPT 5,6,7 where it MUSTN’T be used | String | null |

## Implementation

To create a product specification, use the API below. Remembering that you must have saved the ID of the field for which you want to create a specification.

>ℹ️ If the specification field is of the Combo, Radio or Checkbox type (`FieldTypeId` of 5, 6 and 7 respectively), the `FieldValueId` field is required and the `Text` field is not.\n- For text type fields, it is not necessary to create values for the field, that is, the `FieldValueId` attribute must be `null` and the `Text` attribute must be provided with the specification value.

### Create Specification - Example #1 (text field)

POST

```
https://{{accountName}}.vtexcommercestable.com.br/api/catalog/pvt/product/{{productId}}/specification
```

Body:

```json
{
    "FieldId": 21,
    "Text": "This is a test for specification field type text",
}
```

Header:

```
Accept: application/json 
Content-Type: application/json 
X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}} 
X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}
```

Response:

```
Status: 200 OK 
```

```json
{
    "Id": 39,
    "ProductId": 42,
    "FieldId": 21,
    "FieldValueId": null,
    "Text": "This is a test for specification field type text"
}
```

### Create Specification - Example #2 (Non-text field)

POST

```
https://{{accountName}}.vtexcommercestable.com.br/api/catalog/pvt/product/{{productId}}/specification
```

Body:

```json
{
    "FieldId": 22,
    "FieldValueId": 65,
}
```

Headers:

```
Accept: application/json 
Content-Type: application/json 
X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}} 
X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}
```

Response:

```
Status: 200 OK 
```

```json
{
    "Id": 38,
    "ProductId": 42,
    "FieldId": 22,
    "FieldValueId": 65,
    "Text": "Metal"
}
```

### Get all specifications from a product

To get all specification fields and values from a product, use the [Get product specification and its information by product ID endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/specification). See an example response below.

```json
[
    {
        "Id": 38,
        "ProductId": 42,
        "FieldId": 22,
        "FieldValueId": 65,
        "Text": "Metal"
    },
    {
        "Id": 39,
        "ProductId": 42,
        "FieldId": 21,
        "FieldValueId": null,
        "Text": "This is a test for specification field type text"
    }
]
```

### Update product specification

To update a product specification use the [Update a product specification by product ID API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/products/-productId-/specification). It's also possible to update specification values in bulk.

>⚠️ Updating product specification by `fieldName` does not work.

#### Example request

Body:

```json
[
    {
        "value": [
            "Metal"
        ],
        "Id": 22
    },
    {
        "value": [
            "This is the second test for specification field type text"
        ],
        "Id": 21
    }
]
```

Response:

```
Status: 200 OK 
```

### Remove product specifications

To remove a specification from a product, use the [Delete product specification API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification/-specificationId-).

### Remove all specifications from a product

To delete all specifications registered in a product, use the [Delete all product specification API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification).
