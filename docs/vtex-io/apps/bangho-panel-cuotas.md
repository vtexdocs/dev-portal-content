---
title: "Panel Cuotas"
slug: "bangho-panel-cuotas"
excerpt: "bangho.panel-cuotas@0.0.2"
hidden: true
createdAt: "2022-07-20T19:05:47.926Z"
updatedAt: "2022-08-02T15:34:29.491Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Under the app's name, you should explain the topic, giving a **brief description** of its **functionality** in a store when installed.

Next, **add media** (either an image of a GIF) with the rendered components, so that users can better understand how the app works in practice. 

![Media Placeholder](https://user-images.githubusercontent.com/52087100/71204177-42ca4f80-227e-11ea-89e6-e92e65370c69.png)

## Configuration 

In this section, you first must **add the primary instructions** that will allow users to use the app's blocks in their store, such as:

1. Adding the app as a theme dependency in the `manifest.json` file;
2. Declaring the app's main block in a given theme template or inside another block from the theme.

Remember to add a table with all blocks exported by the app and their descriptions. You can verify an example of it on the [Search Result documentation](https://vtex.io/docs/components/all/vtex.search-result@3.56.1/). 

Next, add the **props table** containing your block's props. 

If the app exports more than one block, create several tables - one for each block. For example:

### `panel-cuotas` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `descont`      | `number`       | Porcentaje de descuento          | `0`        |


| CSS Handles |
| ----------- | 
| `panelCuotas-container` | 
| `panelCuotas-title` | 
| `panelCuotas-installment` | 
| `panelCuotas-installmentIcon` | 
| `panelCuotas-installmentList` |
| `panelCuotas-interes` |
| `panelCuotas-percent` |
| `panelCuotas-valueCash` |
| `panelCuotas-boxValue` |
| `panelCuotas-formpay` |
| `panelCuotas-firstValue` |
| `panelCuotas-container-duo` |
| `vtex-shipping-conteiner` |
| `vtex-shipping-header` |
| `vtex-shipping-icon` |
| `vtex-shipping-label` |
| `vtex-shipping-options` |
| `vtex-shipping-options` |
| `vtex-shipping-children` |
| `vtex-open` |
| `vtex-close` |