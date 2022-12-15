---
title: "Product specifications"
slug: "product-specifications"
hidden: false
createdAt: "2021-12-14T13:58:54.540Z"
updatedAt: "2022-02-04T21:23:05.347Z"
---
Learn more with this [article about specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?&utm_source=autocomplete#).

[block:callout]
{
  "type": "info",
  "body": "If you wish to implement color variation in your products, we recommend you do not use specifications. Instead, see this tutorial about [How to implement product color variation](https://developers.vtex.com/vtex-rest-api/docs/how-to-implement-product-color-variation)."
}
[/block]

## Data Model

<table>
    <tr>
        <td><strong>Field</strong></td>
        <td><strong>Description</strong></td>
        <td><strong>Required</strong></td>
        <td><strong>Format</strong></td>
        <td><strong>Default</strong></td>
    </tr>
    <tr>
        <td>Id</td>
        <td>ID of Specification. This Id is used to delete/update the specification</td>
        <td>No</td>
        <td>Integer</td>
        <td>AutoIncrement</td>
    </tr>
    <tr>
        <td>ProductId</td>
        <td>ID of Product</td>
        <td>Yes</td>
        <td>Integer</td>
        <td>-</td>
    </tr>
    <tr>
        <td>FieldId</td>
        <td>Field ID</td>
        <td>Yes</td>
        <td>Integer</td>
        <td>-</td>
    </tr>
    <tr>
        <td>FieldValueId</td>
        <td>ID of FieldValue. <span style="text-decoration:underline;">ONLY</span> for `FieldTypeId`(5,6,7).</td>
        <td>Mandatory for 5,6,7. MUST NOT be used for any other field types</td>
        <td>Integer</td>
        <td>null</td>
    </tr>
    <tr>
        <td>Text</td>
        <td>Value of specification. Only for `FieldTypeId` different from (5,6,7)</td>
        <td>Mandatory for all fields EXCEPT 5,6,7 where it MUSTN’T be used</td>
        <td>String</td>
        <td>null</td>
    </tr>
</table>

## Implementation

To create a product specification, use the API below. Remembering that you must have saved the ID of the field for which you want to create a specification.
[block:callout]
{
  "type": "info",
  "body": "- If the specification field is of the Combo, Radio or Checkbox type (`FieldTypeId` of 5, 6 and 7 respectively), the `FieldValueId` field is required and the `Text` field is not.\n- For text type fields, it is not necessary to create values for the field, that is, the `FieldValueId` attribute must be `null` and the `Text` attribute must be provided with the specification value.",
  "title": "Keep in mind"
}
[/block]

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

To get all specification fields and values from a product, use the [Get product specification and its information by product ID endpoint](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-product-productid-specification). See an example response below.

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

To update a product specification use the [Update a product specification by product ID API endpoint](https://developers.vtex.com/vtex-rest-api/reference/updateproductspecificacatalog-api-post-update-product-specificationtion). It's also possible to update specification values in bulk.
[block:callout]
{
  "type": "warning",
  "body": "Updating product specification by `fieldName` does not work."
}
[/block]

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

To remove a specification from a product, use the [Delete product specification API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-delete-product-specification-id).

### Remove all specifications from a product

To delete all specifications registered in a product, use the [Delete all product specification API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-delete-product-specification).
