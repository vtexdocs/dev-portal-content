---
title: "metro-custom-cart"
slug: "tiendasjumboqaio-metro-custom-cart"
excerpt: "tiendasjumboqaio.metro-custom-cart@2.0.16"
hidden: true
createdAt: "2022-08-01T13:35:29.111Z"
updatedAt: "2022-08-01T13:35:29.111Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Custom cart es una app personalizada que contiene componentes indispensables para finalizar compra en el sitio de metro como:
- modal de ubicación.
- modal de productos sin stock.
- filtro de productos por categoria.
- promociones
- cupones de descuento
- notas al producto
- criterio de sustitución
- entre otras...

## Preview
![Custom cart image](../assets/custom-cart.jpg)

## Configuration 

1. Importar `tiendametroqaio.custom-cart` en el archivo `manifest.json` del theme io;  

```
  "dependencies": {
    "tiendametroqaio.custom-cart": "0.x"
  }
```

2. Crear una pagina personalizada que contendra la app. por ejemplo `store.custom#cart`  :

```
{
  "store.custom#cart": {
    "parent": {
      "header": "header#cart",
      "footer": "footer#cart"
    },
    "blocks": [
      "flex-layout.row#cart"
    ]
  },
  "flex-layout.row#cart": {
    "title": "Content",
    "children": [
      "flex-layout.col#cart"
    ],
    "props": {
      "blockClass": "cart"
    }
  },
  ...
  ...
```

3. Agregar el bloque `metro-cart` en el archivo creado en paso 2, por ejemplo:

```
  "flex-layout.col#cart": {
    "children": [
      "metro-cart"
    ]
  },
```


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/63118722?v=4" width="100px;" alt=""/><br /><sub><b>Daniel Acosta</b></sub></a><br /><a href="https://github.com/vtex-apps/store-theme/commits?author=hugocostadev" title="Documentation">📖</td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->