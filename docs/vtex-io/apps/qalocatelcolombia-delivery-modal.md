---
title: "jumbo-delivery-modal"
slug: "qalocatelcolombia-delivery-modal"
excerpt: "qalocatelcolombia.delivery-modal@0.0.1"
hidden: true
createdAt: "2022-07-28T23:20:24.239Z"
updatedAt: "2022-07-28T23:20:24.239Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Delivery Modal es una app personalizada encargada de settear el whitelabel que atenderá la orden del cliente dependiendo de su ubicación y método de envío (domicilio o recogida en tienda).

## Preview
![Vista general](https://raw.githubusercontent.com/ITGlobers/jumbo-delivery-modal/main/assets/readme1.jpg?token=APBR3ASUCXGNMR7WK6SNGLDB2XFV6)

Para recogida en tienda se conecta con la lista de tiendas disponibles almacenadas en master data con sus coordenadas previamente configuradas.

![Recogida en tienda](https://raw.githubusercontent.com/ITGlobers/jumbo-delivery-modal/main/assets/readme2-tienda.jpg?token=APBR3AXOYJFN2AEFU64GOJDB2XFYU)

Para entrega a domicilio se conecta al servicio GeoCoder de servinformacion para obtener las coordenadas del cliente y settear al whitelabel correspondiente.

![Envío a domicilio](https://raw.githubusercontent.com/ITGlobers/jumbo-delivery-modal/main/assets/readme3-domicilio.jpg?token=APBR3ASLSSMMMENZLNL3W4DB2XF2O)

## Configuration 

1. Importar `tiendasjumboqaio.delivery-modal` en el archivo `manifest.json` del theme io;  

```
  "dependencies": {
    "tiendasjumboqaio.delivery-modal": "0.x",
  }
```

2. Crear el archivo .json que contendra el `modal-trigger#location` del modal. por ejemplo `modal-delivery.json` el cual contendra el siguiente codigo:

```
{
  "modal-trigger#location": {
    "props": {
      "blockClass": "location-delivery-info"
    },
    "children": [
      "delivery-info-for-trigger",
      "modal-layout#location"
    ]
  },
  "modal-header#location": {
    "props": {
      "showCloseButton": true,
      "blockClass": "delivery"
    }
  },
  "modal-layout#location": {
    "children": [
      "modal-header#location",
      "flex-layout.row#location-content"
    ],
    "props": {
      "blockClass": "main-delivery",
      "preventVerticalStretch": true
    }
  },
  "flex-layout.row#location-content": {
    "props": {
      "blockClass": "location-content"
    },
    "children": [
      "delivery-form-content"
    ]
  },
  "modal-trigger#location-validation": {
    "props": {
      "blockClass": "delivery-modal"
    },
    "children": [
      "rich-text#location-btn-trigger",
      "modal-layout#location"
    ]
  },
  "rich-text#location-btn-trigger": {
    "props": {
      "text": "COMPRAR",
      "blockClass": [
        "btn-trigger",
        "btn-trigger-location"
      ]
    }
  },
  "delivery-add-to-cart-button": {
    "children": [
      "modal-trigger#location-validation"
    ]
  },
  "delivery-add-to-cart-button#search": {
    "props": {
      "isContextSummarySearch": true
    },
    "children": [
      "modal-trigger#location-validation"
    ]
  }
}
```

3. Verificar que el bloque `delivery-form-content` se encuentre en el archivo .json creado:

```
 "flex-layout.row#location-content": {
    "props": {
      "blockClass": "location-content"
    },
    "children": [
      "delivery-form-content"
    ]
  },
```

4. El el archivo header o cualquier otro que desee, agregar el bloque `delivery-info-for-trigger` que contiene la informacion de la ubicacion setteada por el modal:

![info Trigger](https://raw.githubusercontent.com/ITGlobers/jumbo-delivery-modal/main/assets/readme4-info.jpg?token=APBR3ARXBA7FR5WTGF22YU3B2XFF6)

```
"flex-layout.col#delivery-trigger": {
    "children": [
      "delivery-info-for-trigger"
    ],
    "props": {
      "blockClass": "mobile-col-modal"
    }
  },
```

5. Reemplazar todos los botones de agregar al carrito nativos de vtex por el bloque `delivery-add-to-cart-button` que solo agrega items al carrito cuando se tiene una ubicacion configurada, de lo contrario dispara el modal:

```
"flex-layout.row#buy-button": {
    "children": [
      "delivery-add-to-cart-button"
    ]
  },
```

# Adicion de producto despues de seleccionar WL
Se realiza un desarrollo para que cuando el cliente de click en el boton de agregar producto, y se abra la modal de ubicacion, se guarda el producto el cual fue seleccionado para cuando se setee el WL y se recargue la pagina, se lea ese producto y se agregue al carrito el mismo, evitando que el usuario deba agegar nuevamente el producto.

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