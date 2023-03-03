---
title: "SKUs"
slug: "skus"
hidden: false
createdAt: "2021-12-14T13:56:04.502Z"
updatedAt: "2022-02-04T21:26:33.803Z"
---

A [Stock Keeping Unit (SKU)](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA#) corresponds to the actual item in the inventory that customers can purchase, which means it is equivalent to a product variation at VTEX, such as a _long sleeve gray size S shirt_.

Once you have created a product, it is time to submit its respective SKUs.

## Creating an SKU

To create a new SKU, use the [Create SKU endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit).

Follow these instructions when creating the request body:

* During SKU creation, don't set `IsActive` as `true`. If you send the request to activate the SKU when creating it, you will receive a `400 Bad Request` error. The value to `IsActive` must always be `false` when sending that request for activation to occur afterwards, as explained in [Activating an SKU](#activating-an-sku).
* We suggest you set `ActivateIfPossible` as `true,` unless you plan to have an internal workflow to [manually activate SKUs](#manual-activation).
* If there is a need to create a new SKU with a specific custom ID, specify the `Id` (integer) in the request. Otherwise, VTEX will generate the ID automatically.
* Besides the main ID, you must provide at least one of the following alternate IDs in the request body: `RefId` or `EAN`. It is possible to provide both as well.

#### **Request body example (custom ID)**

```json
{
   "Id": 1, 
   "ProductId": 310117069,
   "IsActive": false,
   "ActivateIfPossible": true,
   "Name": "sku test",
   "RefId": "125478",
   "Ean": "8949461894984",
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
   "ManufacturerCode": "123",
   "CommercialConditionId": 1,
   "MeasurementUnit": "un",
   "UnitMultiplier": 2.0000,
   "ModalType": null,
   "KitItensSellApart": false,
   "Videos": [ "https://www.youtube.com/" ]
}
```

#### **Request body example (automatically generated ID)**

```json
{
   "ProductId": 310117069,
   "IsActive": false,
   "ActivateIfPossible": true,
   "Name": "sku test",
   "RefId": "125478",
   "Ean": "8949461894984",
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
   "ManufacturerCode": "123",
   "CommercialConditionId": 1,
   "MeasurementUnit": "un",
   "UnitMultiplier": 2.0000,
   "ModalType": null,
   "KitItensSellApart": false,
   "Videos": [ "https://www.youtube.com/" ]
}
```

#### **Response body example**

```json
{
   "Id":1,
   "ProductId": 310117069,
   "IsActive": false,
   "ActivateIfPossible": true,
   "Name": "sku test",
   "RefId": "125478",
   "Ean": "8949461894984",
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
   "ManufacturerCode": "123",
   "CommercialConditionId": 1,
   "MeasurementUnit": "un",
   "UnitMultiplier": 2.0000,
   "ModalType": null,
   "KitItensSellApart": false,
   "Videos": [ "https://www.youtube.com/" ]
}
```

## Updating an SKU

After an SKU has been successfully created, if any changes are needed or if it's necessary to [activate it manually](#manual-activation), use the [Update SKU endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-).

#### **Request body example**

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

#### **Response body example**

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

## Activating an SKU

Before you can activate an SKU, it must meet the following requirements:

* The SKU must have at least one of the following alternate IDs configured: `RefId` or `EAN`.
* The SKU must have at least one image associated. To associate an image to an SKU, use the [Create SKU file endpoint](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file).
* If the SKU has [specifications](https://developers.vtex.com/docs/guides/specifications), they must be filled in.
* If the field `ActivateIfPossible` is `false`, the SKU must be activated manually. For more information, check the [Manual activation](#manual-activation) section.
* If the SKU is a [kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit), it must have at least one component active.
* The SKU must be associated with an active product, which, in turn, must be associated with an active Brand and an active Category.

Once the SKU complies with all the aspects listed above, there are two ways that you can activate your SKU - [manually](https://developers.vtex.com/docs/guides/how-to-activate-an-sku#manual-activation) or [automatically](https://developers.vtex.com/docs/guides/how-to-activate-an-sku#automatic-activation). Read the following sections for more details.

>⚠️ Note that additional configurations are necessary for a product and its SKUs to become visible in a store:
> - Having registered a price for the SKU in the associated trade policy (also known as sales channel). Read the Pricing onboarding guide for more information on this process.
> - Having at least one unit in stock. Read the Fulfillment onboarding guide for more information on managing inventory.
> - Configuring your storefront's CMS to display products correctly, as described in this Frequently Asked Question.

### Manual activation

To manually activate your SKU, follow these steps:

1. [Create the SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit), setting `IsActive` as `false `and `ActivateIfPossible` as `false`.
2. If the SKU is a kit, [create and associate SKU components](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-kit).
3. [Create and associate SKU files](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file).
4. [Update the SKU](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-) as active, setting `IsActive` as `true`.

Now the SKU should be active in your store.

### Automatic activation

This configuration will automatically update the SKU as active once it is associated with an image or an active component. You do not need to update the SKU as in the previous steps.

To automatically activate your SKU, follow these steps:

1. [Create the SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit), setting `IsActive` as `false` and `ActivateIfPossible` as `true`.
2. If the SKU is a kit, [create and associate SKU components](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunitkit).
3. [Create and associate SKU files](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file).

Now the SKU should be active in your store.
