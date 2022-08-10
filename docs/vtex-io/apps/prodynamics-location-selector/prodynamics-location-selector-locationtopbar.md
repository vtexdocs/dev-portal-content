---
title: "Location Modal"
slug: "prodynamics-location-selector-locationtopbar"
excerpt: "prodynamics.location-selector@0.7.42"
hidden: true
createdAt: "2022-08-04T15:40:17.047Z"
updatedAt: "2022-08-04T16:35:40.078Z"
---
El bloque `location-top-bar` se muestra una vez el usuario ha seleccionado una tienda para preferida. El componente
muestra la información relacionada con esta tienda y permite, mediante un botón tipo enlace, seleccionar una diferente
de las disponibles.

![image](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/coopi-location-top-bar.png)

---

## Uso

1. El componente está diseñado para ser incluido dentro del `header` y de forma _sticky_.

```json
{
    "sticky-layout#location-top-bar": {
        "children": [
            "location-top-bar"
        ]
    }
}
```

2. Es un caso de uso común tener un `header` también como _sticky_ por esta razón ambos bloques deberían estar en
   un `sticky-layout.stack-container`

```json
{
    "header-layout.desktop": {
        "children": [
            "sticky-layout.stack-container#header-desktop"
        ]
    },
    "sticky-layout.stack-container#header-desktop": {
        "props": {
            "position": "top"
        },
        "children": [
            "sticky-layout#header-desktop",
            "sticky-layout#location-top-bar"
        ]
    }
}
```

---

## Personalización

Para editar los estilos del componente se debe hacer uso de la guía oficial de
VTEX [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)
.

| CSS Handles             |
| ----------------------- |
| `locationSelectorTopBar` |
| `locationSelectorTopBarText` |
| `locationSelectorTopBarButton` |