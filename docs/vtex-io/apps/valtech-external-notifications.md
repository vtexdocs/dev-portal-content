---
title: "Digital Content Library"
slug: "valtech-external-notifications"
excerpt: "valtech.external-notifications@0.0.1"
hidden: true
createdAt: "2022-08-03T19:40:16.875Z"
updatedAt: "2022-08-03T20:21:18.835Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

## Notification API Requirements

| Prop name    | Type            | Description    | Example                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `messageType`      | `string`       | (OBLIGATORIO) Tipo de mensaje, deben ser las primeras 3 letras del tipo en mayusculas         | `ENC` (Encuesta) *opciones validas abajo*                                         |
| `link`    | `string`       | (OBLIGATORIO) Link para el CTA de la notificacion               | `https://ejemplo.com.ar/encuesta`                                 |
| `dateMsg`        | `string`       | (OBLIGATORIO) La fecha de envio del mensaje, debe ir con el mismo formato que el ejemplo              | `17/03/2022 08:25:30 PM UTC`                                         |
| `endMsgDate`       | `string`       | La fecha de vencimiento del mensaje en string o null si no debe tener fecha de vencimiento, debe ir con el mismo formato que el ejemplo. "YYYYMMDD"            | `20220729`                                         |
| `urlImage`      | `string`       | Url de la imagen que debe ir en la notificacion, o null si no lleva imagen     | `https://images.placeholders.dev/?width=300&height=100`  |
| `titleMsg`      | `string`       | (OBLIGATORIO) Titulo de la notificacion     | `Novedad!`  |
| `details`      | `string`       | Descripción de la notificacion     | `Implementamos un nuevo sistema de notificaciones!`  |


`messageType` opciones validas: "ENC", "OFE", "PRO", "CHE", "NOV" (Encuesta, Oferta, Promo, TokinCheck y Novedad respectivamente)

## Configuration 

To use the **external-notifications** component you should:

1. Add this to your manifest.json dependencies: `"valtech.external-notifications": "0.x"`
2. Fill the block properties (see Blocks section)

## Blocks

The blocks to include in the store theme: 

1. Block definition
```shell
"external-notifications-provider": {
    "children": [
        "external-notifications-layout"
    ]
},
```

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

| CSS Handles |
| ----------- | 
| `bell` | 
| `insideBell` | 
| `openIconContainer` | 
| `headerText` | 
| `hasNotificationsAvailable` |
| `noMoreNotificationsText` |
| `noMoreNotificationsIcon` |
| `noMoreNotificationsContainer` |
| `notificationItemContainer` |
| `notificationTitleContainer` |
| `notificationTitle` |
| `dateMsgContainer` |
| `deleteButton` |
| `messageSentDate` |
| `messageExpireDate` |
| `messageImageContainer` |
| `messageImage` |
| `notificationDescription` |
| `notificationDescriptionContainer` |
| `itemNotRead` |
| `deleted` |
| `deleteIcon` |
| `messageTypeIcon` |

<!-- DOCS-IGNORE:start -->

## Contributors

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->