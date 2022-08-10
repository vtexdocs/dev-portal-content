---
title: "MINICART PRODUCT LIST / BUY THERMOMETER / FLAGS TARJETAS / GENERAL FLAGS"
slug: "tiendasjumboqaio-metro-minicart"
excerpt: "tiendasjumboqaio.metro-minicart@2.0.20"
hidden: true
createdAt: "2022-07-22T16:51:36.620Z"
updatedAt: "2022-08-08T20:29:50.495Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

**Minicart**
App para mostrar el minicart, donde se categorizan los productos con filtros.

**Buy thermometer**
App para mostrar un target de valor a alcanzar para recibir envio gratis.

**Flags TARJETAS**
App para mostrar valores cuando se paga con una tarjeta en especifico.

**General Flags**
App para mostrar flags varias segun nombre recibido por *PROMOCION*

## Configuration 

### **Minicart**

**Esta app incluye el termometro**

Se debe pasar el bloque `minicart-product-list-jumbo`
A este se le deben pasar los siguientes childrens en la **posicion respectiva**:
1. minicart-summary
2. Boton de finalizar compra y/o LINK de ir a cart.
3. y 4. HASTA **2** flex .row de footers.

Y por props se le debe pasar el ID de la promocion de la cual saca el valor min de compra.


*EJEMPLO*

```
"minicart-product-list-jumbo": {
    "title": "Minicart Jumbo",
    "props": {
      "promId": "24982570-1dd4-405c-85d7-966ad7bd14be"
    },
    "children": [
      "minicart-summary",
      "link.product#cart",
      "flex-layout.row#minicart-footer2",
      "flex-layout.row#minicart-footer3"
    ]
  }
```

Y por props se le debe pasar el ID de la promocion de la cual saca el valor min de compra. (si no llega no se muestra)

### `minicart-product-list-jumbo` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `promId`      | `string`       | ID de la promocion         | ``        |


### **Buy thermometer**

### `minicart-thermometer` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `promId`      | `string`       | ID de la promocion         | ``        |


### **Flags TARJETAS**

Se debe agergar el bloque `flag-product-tarjetas`

### `flag-product-tarjetas` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `productId`      | `string`       | ID del producto (opcional) / utiliza contexto/graphql.         | ``        |
| `small`      | `boolean`       | Mostrar las flags y texto mas pequeño.         | false        |

### **General Flags**
Se debe agergar el bloque `general-flags` utiliza contexto/graphql


## Customization

Se puede inspeccionar las clases respectivas para editar los diseños desde el theme-io

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
[Hector Ruiz](https://github.com/hruiz13)
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->

----