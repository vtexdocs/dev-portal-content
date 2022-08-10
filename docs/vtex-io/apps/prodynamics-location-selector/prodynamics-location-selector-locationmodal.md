---
title: "Location Modal"
slug: "prodynamics-location-selector-locationmodal"
excerpt: "prodynamics.location-selector@0.7.42"
hidden: true
createdAt: "2022-08-04T15:40:17.035Z"
updatedAt: "2022-08-04T16:35:40.263Z"
---
El bloque `location-modal` se encarga de guiar al usuario en una serie de pasos que le permiten dos cosas según el
estado de la aplicación:

1. Establecer la su ubicación mediante la API de Google Places ingresando su dirección o con la ayuda de Google Maps
2. Seleccionar como preferida alguna de las tiendas disponibles para su ubicación

![image](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/coopi-location-modal-1.png)
![image](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/coopi-location-modal-2.png)

---

## Uso

1. Se debe llamar este bloque de forma que esté disponible en todas las páginas del sitio una única vez sin importar que
   se trate de la versión de _escritorio_ o la versión _móvil_, para ellos existen diferentes estrategias para este caso
   lo haremos dentro de una fila del `footer`

```json
{
    "footer-row#location-modal": {
        "children": [
            "location-modal"
        ]
    }
}
```

2. Ahora agregamos nuestra fila al `footer` para _escritorio_ y _móvil_:

```json
{
    "footer-layout.desktop": {
        "children": [
            "footer-row#location-modal"
        ]
    },
    "footer-layout.mobile": {
        "children": [
            "footer-row#location-modal"
        ]
    }
}
```

> _Nota:_ También se puede emplear como se indica en el documento principal, es decir, como bloque `after` de todas
> las interfaces que se extienden.

---

## Personalización

Para editar los estilos del componente se debe hacer uso de la guía oficial de
VTEX [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)
.

| CSS Handles             |
| ----------------------- |
| `locationSelectorModalBody` |
| `locationSelectorModalBodyMin` |
| `locationSelectorModalBodySmall` |
| `locationSelectorModalBanner` |
| `locationSelectorModalMap` |
| `locationSelectorModalButtonAlt` |
| `locationSelectorModalButton` |
| `locationSelectorModalHead` |
| `locationSelectorModalHeadTitle` |
| `locationSelectorModalForm` |
| `locationSelectorModalLink` |
| `locationSelectorModalBodyText` |
| `locationSelectorModalButtonGhost` |
| `locationSelectorModalAddressInput` |
| `locationSelectorModalAddressContainer` |
| `locationSelectorModalConfirmText` |
| `locationSelectorModalConfirmTitle` |
| `locationSelectorModalConfirmContainer` |
| `locationSelectorSellerItem` |
| `locationSelectorSellerName` |
| `locationSelectorSellerTabs` |
| `locationSelectorSellerList` |
| `locationSelectorModalButtonAltLight` |
| `locationSelectorModalButtonAltSelected` |