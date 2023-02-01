---
title: "SKUs"
slug: "skus"
hidden: false
createdAt: "2021-12-14T13:56:04.502Z"
updatedAt: "2022-02-04T21:26:33.803Z"
---

Once you have created a product, it is time to submit the respective SKUs. For an SKU to be active, it must have an image file associated with it. If the SKU is a kit, it must have at least one component active. For more information, check our [How to activate an SKU](https://developers.vtex.com/docs/guides/how-to-activate-an-sku) guide.

Learn more in our [SKUs documentation](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA#).

## Data Model

| **Field**    | **Description**    | **Required**    | **Format**    | **Default**    |
|---|---|---|---|---|
| Id    | SKU ID. If not provided, it will be generated automatically (sequence)    | No    | Integer    | AutoIncrement    |
| ProductId    | Product ID associated with this SKU    | Yes    | Integer    | -    |
| ActivateIfPossible    | Automatically activate the SKU if all the mandatory fields are filled out. Example: SKU image    | No    | Boolean    | false    |
| IsActive    | Activate/Inactivate  SKU    | No    | Boolean   | false    |
| Name    | Should contain the SKU name, meaning the variation of the previously added product. Product - Fridge, SKU - 110V.   | Yes   | String(200)   | -   |
| RefId    | Reference code used internally for organizational purposes. Must be unique. It's not required only  if EAN code already exists. If not, this field must be provided.    | No    | String(50)    | null    |
| PackagedHeight    | Height used for shipping calculation.    | No*    | Decimal    | 0.0    |
| PackagedLength    | Length used for shipping calculation.    | No*    | Decimal    | 0.0   |
| PackagedWidth    | Width used for shipping calculation.    | No*    | Decimal    | 0.0    |
| PackagedWeightKg    | Weight used for shipping calculation.    | No*   | Decimal    | 0.0    |
| Height    | Real Height   | No   | Decimal    | null    |
| Length    | Real Length    | No    | Decimal    | null    |
| Width    | Real Width    | No    | Decimal    | null    |
| WeightKg    | Real Weight    | No    | Decimal    | null    |
| CubicWeight    |    | No    | Decimal    | 0.0    |
| IsKit    | Indicates whether the product SKU is made up of one or more SKUs, thereby becoming a bundle. Must be enabled if you are adding a bundle. Once activated, the flag cannot be reverted.    | No    | Boolean    | false    |
| CreationDate    | Date and time SKU created in VTEX    | Automatic generated    | DateTime    | null    |
| RewardValue    | Credit that the customer receives when finalizing an order of one specific SKU unit. By filling this field out with "1", the customer gets $1 credit on the store.    | No    | Decimal    | null    |
| EstimatedDateArrival    | To add the product as pre-sale, enter the product estimated arrival date. You must take into consideration both the launch date and the freight calculation for the arrival date.    | No    | DateTime    | DateTime (dd/mm/yyyy)    |
| ManufacturerCode    | Provided by the manufacturers to identify their product. This field is required if the product has a specific manufacturer’s code.    | No    | String(100)    | null    |
| CommercialConditionId    | Used to define SKU specific promotions/installment rules. Find out more by reading the [Commercial condition article](https://help.vtex.com/en/subcategory/commercial-conditions--6312YEqn0AGYCsOOESSIQM#). In case of no specific condition, use the default value.    | No    | Integer    | null    |
| MeasurementUnit    | Used only in cases when you need to convert the unit of measure for sale. If a product is sold in boxes for example, but customers want to buy per sqm (m²). For common cases, use `un`.    | No    | String    | null    |
| UnitMultiplier    | Unit multiplier number for the SKU. If the multiplier is 5, the product can be added in quantities such as 5, 10, 15, 20, onward.    | No    | Integer    | 1.0    |
| ModalType    | Links an unusual type of product to a carrier specialized in delivering it. To learn more about this feature, read our articles How the modal works and Setting up modal for carriers.    | No    | String    | null    |
| KitItensSellApart    | if the SKU is part of a bundle this option needs to be true.    | No    | Boolean    | false    |

## API Integration

### Create SKU

To create a new SKU use the [Create SKU API endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit).

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

After an SKU has been successfully created, if any changes are needed, use the [Update SKU endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-).

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
