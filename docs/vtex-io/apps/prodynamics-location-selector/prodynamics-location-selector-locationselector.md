---
title: "Location Selector"
slug: "prodynamics-location-selector-locationselector"
excerpt: "prodynamics.location-selector@0.7.42"
hidden: true
createdAt: "2022-08-04T15:40:17.069Z"
updatedAt: "2022-08-04T16:35:40.235Z"
---
El bloque `location-selector` se encarga de abrir el componente `location-modal`, también presenta al usuario las
opciones seleccionadas, incluye el tooltip que indica cuando aún no se selecciona una ubicación. También incluye un
botón para cambiar entre las diferentes vistas del modal o eliminar el filtro de tienda seleccionado.

![image](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/coopi-location-selector.png)

![image](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/coopi-location-selector-2.png)

---

## Uso

1. El bloque debe ser llamado dentro del `header`. Para el caso de la vista _móvil_ el bloque cuenta con una
   funcionalidad para mostrar solo un icono en lugar del selector. Lo primero es agregar el selector regular

```json
{
    "header-layout.mobile": {
        "children": [
            "flex-layout.row#1-mobile",
            "flex-layout.row#2-mobile"
        ]
    },
    "flex-layout.row#1-mobile": {
        "children": [
            "location-selector"
        ]
    }
}
```

2. Ahora agregamos también la vista del selector como "solo icono" usando la propiedad `mobileMode`

```json
{
    "flex-layout.row#2-mobile": {
        "children": [
            "flex-layout.col#1-mobile"
        ]
    },
    "flex-layout.col#1-mobile": {
        "children": [
            "location-selector#simple-mobile"
        ]
    },
    "location-selector#simple-mobile": {
        "props": {
            "mobileMode": "icon",
            "hideTooltip": true
        }
    }
}
```

| Propiedad | Tipo     | Descripción | Valor por defecto  |
| --------- | -------- | ----------- | -------------- |
| `mobileMode`   | `MobileMode` | La forma en que se muestra el selector en móvil  | `full` |
| `hideTooltip`   | `boolean` | Ocultar el tooltip del selector | `false` |
| `placeholder`   | `string` | El texto de ayuda que se muestra cuando aún no selecciona ubicación | `none` |

> `MobileMode` será un `string` que puede ser `"full"` o `"icon"` y de ser `"icon"` debería usarse la propiedad `hideTooltip`
> como `true`

---

## Personalización

Para editar los estilos del componente se debe hacer uso de la guía oficial de
VTEX [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)
.

| CSS Handles             |
| ----------------------- |
| `changeSellerLink` |
| `changeLocationText` |
| `changeLocationIcon` |
| `changeLocationInput` |
| `changeLocationWrapper` |
| `changeLocationContainer` |
| `changeLocationLabel` |
| `changeSellerContainer` |
| `changeSellerText` |
| `removeSellerButton` |
| `locationInfoTooltip` |
| `locationInfoTooltip--scrolled` |
| `locationInfoTooltipTitle` |
| `locationInfoTooltipText` |
| `locationInfoTooltipButton` |
| `locationInfoTooltipIcon` |
| `locationInfoTooltipCloseButton` |