---
title: "Maeztra - SKU Ghost"
slug: "amobelezaio-mz-skusimilar"
excerpt: "amobelezaio.mz-skusimilar@0.0.3"
hidden: true
createdAt: "2022-08-08T20:46:48.416Z"
updatedAt: "2022-08-09T20:02:45.662Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Aplicativo para projetos com multi sku-selector, visando resolver problemas de layouts com mais de um seletor de SKU da mesma caracteristica como Tamanho ou Cor fizemos um clique fantasma para interagir com apenas um módulo sendo os outros apenas controle visual.

## Configuracao 

A configuracao é simples, apenas iremos configurar os parametros em **defaults** :


### `selector` props

| Prop name       | Type            | Description                           |Defaultvalue           |
| --------------- | --------------- | ---------------------------------------------------------------
| `selector`      | `string`        | Qual seletor iremos assombrar         | `default vtex`        |


### `classCheck` props

| Prop name         | Type            | Description                       |Defaultvalue           |
| ------------------| --------------- | -----------------------------------------------------------
| `classCheck`      | `string`        |Checar se esta ativo o SKU         | `default vtex`        |

### `classInactive` props

| Prop name            | Type               | Description                         |Defaultvalue           |
| ---------------------| -------------------| -------------------------------------------------------------
| `classInactive`      | `string`           |Checar se esta inativo o SKU         | `default vtex`        |

### `ghostTrigger` props

| Prop name            | Type               | Description                                      |Defaultvalue           |
| ---------------------| -------------------| -------------------------------------------------------------------------
| `ghostTrigger`       | `string`           |Elemento especifico que precisamos clicar         | `default vtex`        |


## Customizacao

Para aplicar personalizações de CSS neste e em outros blocos, siga as instruções fornecidas na receita em [Usando CSS Handles para personalização de loja](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- | 
| `ulSkuGhost` | 
| `liSkuGhost` | 
| `inactive` | 
| `selected` | 
| `title` |