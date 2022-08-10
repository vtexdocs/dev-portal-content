---
title: "SKU specifications"
slug: "sku-specifications"
hidden: false
createdAt: "2021-12-14T14:04:33.846Z"
updatedAt: "2022-02-04T21:24:41.963Z"
---
SKU specifications are necessary to be able  to choose the SKU, that is, the variation of the product. Example: Color, Size, Voltage. The SKU Selector can be found in the search result or on the product page.
[block:callout]
{
  "type": "info",
  "body": "If you wish to implement color variation in your products, we recommend you do not use SKU specifications. Instead, see this tutorial about [How to implement product color variation](https://developers.vtex.com/vtex-rest-api/docs/how-to-implement-product-color-variation)."
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "VTEX Admin says that if a new SKU Specification field is created, all the SKUs associated will be deactivated. However, if created, products will keep activated."
}
[/block]
## Data Model

<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Required</strong>
   </td>
   <td><strong>Type</strong>
   </td>
   <td><strong>Default</strong>
   </td>
  </tr>
  <tr>
   <td>Id
   </td>
   <td>ID of Specification. This ID is used to delete/update the specification
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>AutoIncrement
   </td>
  </tr>
  <tr>
   <td>SkuId
   </td>
   <td>ID of SKU
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>FieldId
   </td>
   <td>Field ID
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>FieldValueId
   </td>
   <td>ID of FieldValue. Required only for FieldTypeId 5,6,7
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Text
   </td>
   <td>Value of specification. Only for FieldTypeId different from 5,6,7
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
</table>


## Implementation

### Create SKU Specification
To create a SKU specification, simply use the API below. Remember that you must have saved the ID of the field for which you want to create, and the `FieldId` of the value created for the field.

POST
```
https://{{accountName}}.vtexcommercestable.com.br/api/catalog/pvt/stockkeepingunit/{{skuId}}/specification/
```
Body:
```json
{
    "FieldId": 13,
    "FieldValueId": 101
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
    "Id": 1505,
    "SkuId": 1234568387,
    "FieldId": 193,
    "FieldValueId": 360,
    "Text": "Size 10"
}
```


### Remove an SKU Specification
To remove a specification from an SKU, use the [Delete SKU specification API endpoint](https://developers.vtex.com/vtex-rest-api/reference/delete_api-catalog-pvt-stockkeepingunit-skuid-specification-specificationid).


### Remove all specifications of specific SKU
To remove all specifications of one SKU, use the [Delete all SKU specifications endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-delete-sku-specification)