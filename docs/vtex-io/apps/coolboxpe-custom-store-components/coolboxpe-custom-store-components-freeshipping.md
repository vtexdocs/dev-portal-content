---
title: "Free Shipping"
slug: "coolboxpe-custom-store-components-freeshipping"
excerpt: "coolboxpe.custom-store-components@0.2.360"
hidden: true
createdAt: "2022-07-05T09:42:34.348Z"
updatedAt: "2022-08-09T20:06:07.853Z"
---
The `free-shipping` is a block responsible for **displaying the missing amount, to access the free shipping promotion**.

![image](https://user-images.githubusercontent.com/74076308/101827422-4fcef700-3afe-11eb-8911-a5d344f90fc8.PNG)

## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
  "dependencies": {
    "vtex.store-components": "3.x"
  }
}
```

2. Add the `free-shipping` block to any block below `store.custom#free-shipping` (page custom template). For example:

```json
"free-shipping": {
  "props": {
    "valueOfFreeShipping": 100,
    "infoLabel": {
      "labelInitial": "Test init:",
      "labelBetween": "¡Test Middle ",
      "labelFinal": "Test end!",
      "labelFreeShippingComplete": "Test complete"
      },
    "show": {
      "informativeFreeShippingText": true,
      "percentageFreeShipping":true,
      "rangeFreeShipping": true,
      "labelInitial": true,
      "subTotal": true,
      "labelBetween": true,
      "missingForFreeShipping": true,
      "labelFinal": true,
      "labelFreeShippingComplete": true
    }
  }
},
{
  "store.custom#free-shipping": {
    "blocks": [
      "flex-layout.row#free-shipping"
    ],
    "flex-layout.row#free-shipping": {
      "children": [
        "free-shipping"
      ]
    }
  }
}
```

| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `valueOfFreeShipping` | `Number` | Value of free shipping | `1` |
| `infoLabel` | `String` | information of free shipping | `Valor actual: {subTotal} ¡Faltan {missingForFreeShipping} para que su envío sea totalmente gratis!` |
| `show` | `Boolean` | Show parts of component of free shipping | `true` |


infoLabel **object**
| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `labelInitial` | `String` | Text initial | `Valor actual:` |
| `labelBetween` | `String` | Text between | `¡Faltan` |
| `labelFinal` | `String` | Text final  | `para que su envío sea totalmente gratis!` |
| `labelFreeShippingComplete` | `String` | Text complete free shipping  | `¡Su envio es totalmente gratis!` |


show **object**
| Prop name | Type | Description | Default value |
| --- | --- | --- | ---| 
| `informativeFreeShippingText` | `Boolean` | Show information of infoLabel in general | `true` |
| `percentageFreeShipping` | `Boolean` | Show progress bar or percentage | `true` |
| `rangeFreeShipping` | `Boolean` | Show information of progress bar or percentage limits | `true` |
| `labelInitial` | `Boolean` | Show text initial of infoLabel | `true` |
| `subTotal` | `Boolean` | Show subtotal for free shipping of infoLabel | `true` |
| `labelBetween` | `Boolean` | Show text between of infoLabel | `true` |
| `missingForFreeShipping` | `Boolean` | Show missing for free shipping of infoLabel | `true` |
| `labelFinal` | `Boolean` | Show text final of infoLabel | `true` |
| `labelFreeShippingComplete` | `Boolean` | Show text when complete amount of free shipping | `true` |



## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| --- |
| `fs_globalFreeShippingContainer` |
| `fs_informativeFreeShippingText` |
| `fs_freeShippingProgressBar` |
| `fs_rangeFreeShippingContainer` |
| `fs_initialRangeFreeShippingText` |
| `fs_endRangeFreeShippingText` |