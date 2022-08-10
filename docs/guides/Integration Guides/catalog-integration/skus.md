---
title: "SKUs"
slug: "skus"
hidden: false
createdAt: "2021-12-14T13:56:04.502Z"
updatedAt: "2022-02-04T21:26:33.803Z"
---
Once you have created a product, it is time to submit the respective SKUs. For an SKU to be active, it must have an image file associated with it. If the SKU is a kit, it must have at least one component active. For more information, check our [How to activate an SKU](https://developers.vtex.com/vtex-rest-api/docs/how-to-activate-an-sku) guide.

Learn more in our [SKUs documentation](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA#).


## Data Model

<table>
  <tr>
   <td><strong>Field</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Required</strong>
   </td>
   <td><strong>Format</strong>
   </td>
   <td><strong>Default</strong>
   </td>
  </tr>
  <tr>
   <td>Id
   </td>
   <td>SKU ID. If not provided, it will be generated automatically (sequence)
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>AutoIncrement
   </td>
  </tr>
  <tr>
   <td>ProductId
   </td>
   <td>Product ID associated with this SKU
   </td>
   <td>Yes
   </td>
   <td>Integer
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>ActivateIfPossible
   </td>
   <td>Automatically activate the SKU if all the mandatory fields are filled out. Example: SKU image
   </td>
   <td>No
   </td>
   <td>Boolean
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>IsActive
   </td>
   <td>Activate/Inactivate  SKU
   </td>
   <td>No
   </td>
   <td>Boolean
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>Name
   </td>
   <td>Should contain the SKU name, meaning the variation of the previously added product. Product - Fridge, SKU - 110V.
   </td>
   <td>Yes
   </td>
   <td>String(200)
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td>RefId
   </td>
   <td>Reference code used internally for organizational purposes. Must be unique. It's not required only  if EAN code already exists. If not, this field must be provided.
   </td>
   <td>No
   </td>
   <td>String(50)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>PackagedHeight
   </td>
   <td>Height used for shipping calculation.
   </td>
   <td>No*
   </td>
   <td>Decimal
   </td>
   <td>0.0
   </td>
  </tr>
  <tr>
   <td>PackagedLength
   </td>
   <td>Length used for shipping calculation.
   </td>
   <td>No*
   </td>
   <td>Decimal
   </td>
   <td>0.0
   </td>
  </tr>
  <tr>
   <td>PackagedWidth
   </td>
   <td>Width used for shipping calculation.
   </td>
   <td>No*
   </td>
   <td>Decimal
   </td>
   <td>0.0
   </td>
  </tr>
  <tr>
   <td>PackagedWeightKg
   </td>
   <td>Weight used for shipping calculation.
   </td>
   <td>No*
   </td>
   <td>Decimal
   </td>
   <td>0.0
   </td>
  </tr>
  <tr>
   <td>Height
   </td>
   <td>Real Height
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Length
   </td>
   <td>Real Length
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>Width
   </td>
   <td>Real Width
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>WeightKg
   </td>
   <td>Real Weight
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>CubicWeight
   </td>
   <td>
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>0.0
   </td>
  </tr>
  <tr>
   <td>IsKit
   </td>
   <td>Indicates whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted.
   </td>
   <td>No
   </td>
   <td>Boolean
   </td>
   <td>false
   </td>
  </tr>
  <tr>
   <td>CreationDate
   </td>
   <td>Date and time SKU created in VTEX
   </td>
   <td>Automatic generated
   </td>
   <td>DateTime
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>RewardValue
   </td>
   <td>Credit that the customer receives when finalizing an order of one specific SKU unit. By filling this field out with "1", the customer gets $1 credit on the store.
   </td>
   <td>No
   </td>
   <td>Decimal
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>EstimatedDateArrival
   </td>
   <td>To add the product as pre-sale, enter the product estimated arrival date. You must take into consideration both the launch date and the freight calculation for the arrival date.
   </td>
   <td>No
   </td>
   <td>DateTime
   </td>
   <td>DateTime (dd/mm/yyyy)
   </td>
  </tr>
  <tr>
   <td>ManufacturerCode
   </td>
   <td>Provided by the manufacturers to identify their product. This field is required if the product has a specific manufacturer’s code.
   </td>
   <td>No
   </td>
   <td>String(100)
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>CommercialConditionId
   </td>
   <td>Used to define SKU specific promotions/installment rules. Find out more by reading the [Commercial condition article](https://help.vtex.com/en/subcategory/commercial-conditions--6312YEqn0AGYCsOOESSIQM#). In case of no specific condition, use the default value.
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>MeasurementUnit
   </td>
   <td>Used only in cases when you need to convert the unit of measure for sale. If a product is sold in boxes for example, but customers want to buy per sqm (m²). For common cases, use `un`.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>UnitMultiplier
   </td>
   <td>Unit multiplier number for the SKU. If the multiplier is 5, the product can be added in quantities such as 5, 10, 15, 20, onward.
   </td>
   <td>No
   </td>
   <td>Integer
   </td>
   <td>1.0
   </td>
  </tr>
  <tr>
   <td>ModalType
   </td>
   <td>Links an unusual type of product to a carrier specialized in delivering it. To learn more about this feature, read our articles <a href="https://help.vtex.com/en/tutorial/como-funciona-o-modal--tutorials_125">How the modal works</a> and <a href="https://help.vtex.com/en/tutorial/configurar-modal-para-transportadoras--3jhLqxuPhuiq24UoykCcqy#">Setting up modal for carriers</a>.
   </td>
   <td>No
   </td>
   <td>String
   </td>
   <td>null
   </td>
  </tr>
  <tr>
   <td>KitItensSellApart
   </td>
   <td>if the SKU is part of a bundle this option needs to be true.
   </td>
   <td>No
   </td>
   <td>Boolean
   </td>
   <td>false
   </td>
  </tr>
</table>


## API Integration


### Create SKU
To create a new SKU use the [Create SKU API endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku).


#### Example request
Body:
```json
{
    "Id": null,
    "ProductId": 42,
    "IsActive": false,
    "ActivateIfPossible": true,
    "Name": "Size 10",
    "RefId": "B096QW8Y8Z",
    "PackagedHeight": 10,
    "PackagedLength": 10,
    "PackagedWidth": 10,
    "PackagedWeightKg": 10,
    "Height": null,
    "Length": null,
    "Width": null,
    "WeightKg": null,
    "CubicWeight": 0.1667,
    "IsKit": false,
    "CreationDate": null,
    "RewardValue": null,
    "EstimatedDateArrival": null,
    "ManufacturerCode": null,
    "CommercialConditionId": 1,
    "MeasurementUnit": "un",
    "UnitMultiplier": 1,
    "ModalType": null,
    "KitItensSellApart": false
}
```
Response:
```json
{
    "Id": 70,
    "ProductId": 42,
    "IsActive": false,
    "Name": "Size 10",
    "RefId": "B096QW8Y8Z",
    "PackagedHeight": 10.0,
    "PackagedLength": 10.0,
    "PackagedWidth": 10.0,
    "PackagedWeightKg": 10.0,
    "Height": null,
    "Length": null,
    "Width": null,
    "WeightKg": null,
    "CubicWeight": 0.1667,
    "IsKit": false,
    "CreationDate": "2020-01-25T15:51:29.2614605",
    "RewardValue": null,
    "EstimatedDateArrival": null,
    "ManufacturerCode": null,
    "CommercialConditionId": 1,
    "MeasurementUnit": "un",
    "UnitMultiplier": 1.0,
    "ModalType": null,
    "KitItensSellApart": false,
    "Videos": []
}
```


### Update SKU

After an SKU has been successfully created, if any changes are needed, use the [Update SKU endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-sku).


#### Example request

Body:
```json
{
    "Id": 70,
    "ProductId": 42,
    "IsActive": true,
    "Name": "Size 10",
    "RefId": "B096QW8Y8Z",
    "PackagedHeight": 15.0,
    "PackagedLength": 15.0,
    "PackagedWidth": 15.0,
    "PackagedWeightKg": 15.0,
    "Height": null,
    "Length": null,
    "Width": null,
    "WeightKg": null,
    "CubicWeight": 0.0,
    "IsKit": false,
    "CreationDate": "2020-01-25T15:51:00",
    "RewardValue": null,
    "EstimatedDateArrival": null,
    "ManufacturerCode": null,
    "CommercialConditionId": 1,
    "MeasurementUnit": "un",
    "UnitMultiplier": 1.0,
    "ModalType": null,
    "KitItensSellApart": false,
    "Videos": []
}
```

Response:
```json
{
    "Id": 70,
    "ProductId": 42,
    "IsActive": true,
    "Name": "Size 10",
    "RefId": "B096QW8Y8Z",
    "PackagedHeight": 15.0,
    "PackagedLength": 15.0,
    "PackagedWidth": 15.0,
    "PackagedWeightKg": 15.0,
    "Height": null,
    "Length": null,
    "Width": null,
    "WeightKg": null,
    "CubicWeight": 0.0,
    "IsKit": false,
    "CreationDate": "2020-01-25T15:51:00",
    "RewardValue": null,
    "EstimatedDateArrival": null,
    "ManufacturerCode": null,
    "CommercialConditionId": 1,
    "MeasurementUnit": "un",
    "UnitMultiplier": 1.0,
    "ModalType": null,
    "KitItensSellApart": false,
    "Videos": []
}
```
[block:callout]
{
  "type": "warning",
  "body": "During the SKU creation we suggest you set `ActivateIfPossible` as `true` unless the company has an internal workflow to activate SKUs.",
  "title": "Best Practices"
}
[/block]

[block:callout]
{
  "type": "danger",
  "title": "Watch out for these pitfalls",
  "body": "- Requirements to activate a SKU. \n    - Must have ReferenceCode or EAN\n    - At least one image\n    - If SKU has specifications, they must be filled out\n- If the field `ActivateIfPossible` is `false`, the SKU must be activated manually."
}
[/block]