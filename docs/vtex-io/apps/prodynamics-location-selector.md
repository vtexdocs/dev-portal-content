---
title: "Location Selector prodynamics"
slug: "prodynamics-location-selector"
excerpt: "prodynamics.location-selector@0.7.42"
hidden: true
createdAt: "2022-07-15T20:12:09.643Z"
updatedAt: "2022-08-04T16:35:39.982Z"
---
## Descripción

Componente que determina la ubicación del usuario y filtra el catálogo de productos de acuerdo a la geolocalización
(latitud y longitud) del mismo. También permite establecer una de las tiendas con cobertura a la ubicación dada como
predeterminada. Además almacena las direcciones de los usuarios por correo, sin ser requerido el registro en la tienda
de los mismos.

---

## Configuración

Antes de empezar debemos considerar que esta aplicación usa servicios propios para la consulta y almacenamiento de
direcciones, también extiende la información de las tiendas para almacenar su geolocalización. Todo esto haciendo uso de
la [versión 2 de Master Data](https://developers.vtex.com/vtex-rest-api/reference/master-data-api-v2-overview) por esto
es necesario crear mediante el _API de VTEX_ las entidades definidas en `~/node/schemas/` también encontrará el esquema
requerido para crear la entidad de [VTable](https://help.vtex.com/tutorial/vtable--35ygHE0Ohaw46Si2MSEAE4) que permite
administrar la lista de tiendas.

---

## Instalación

Para empezar a usar la aplicación lo primero es agregar la dependencia al `manifest.json`.

```json
  {
  "dependencies": {
    "prodynamics.location-selector": "0.x"
  }
}
```

La aplicación trabaja con estado centralizado en un contexto que deberá encapsular todos los componentes que hacen parte
de esta aplicación por esta razón es necesario extender todas las interfaces de la tienda y agregar el contexto como un
bloque al rededor (`around`) de estas. Para ello en el archivo `store/interfaces.json` deberá extender las interfaces
nativas así:

```json
{
  "store.home.custom": {
    "around": [
      "locationWrapper"
    ],
    "after": [
      "location-modal"
    ]
  }
}
```

Debe extenderse **cada una** de las interfaces de la tienda pues sin el `locationWrapper` el componente no funciona.

> _Nota:_ El bloque `location-modal` está definido en la extensión de la interfaz sin embargo y si se prefiere puede ser
> invocado dentro del `footer`.

---

## Componentes

Luego de agregar la dependencia `prodynamics.location-selector` las siguientes aplicaciones estarán ahora disponibles.
Incluyendo el componente no-visual que se integró en el proceso de instalación anterior.

- [Location Modal](LocationModal.md)
- [Location Selector](LocationSelector.md)
- [Location Top Bar](LocationTopBar.md)

## Hooks

### useLocationModal
El hook `useLocationModal` controla el estado de visibilidad del modal (`<LocationModal />`) y del tooltip
`<LocationTooltip />` que contiene el selector de ubicación. Para usar el hook de estado es necesario importarlo del
app así:

```typescript jsx
import React from 'react'
import { useLocationModal } from 'prodynamics.location-selector'

function CustomComponent() {
    const locationModalState = useLocationModal()
    return <div>Location State</div>
}
```

Donde la constante `locationModalState` tiene las siguientes propiedades:

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| isModalOpen | `boolean` | Indica si el modal es visible |
| isTooltipOpen | `boolean` | Indica si el tooltip es visible |
| setModalVisibility | `Function` | Establece la visibilidad del modal |
| setTooltipVisibility | `Function` | Establece la visibilidad del tooltip |
| state | `LocationState` | Describe el estado del selector de ubicación y del selector de seller |
| dispatch | `Dispatch<LocationPayload>` | Establece el objeto `state` a través de su reducer |

El tipo `LocationState` tiene las siguientes propiedades:

| Nombre | Tipo |
| --- | --- |
| user | `UserAddress` |
| seller | `SelectedSeller` |
| allSellers | `string[]` |
| modal | uno entre `"user-modal"` o `"seller-modal"` |

Y los tipos `UserAddress` y `SelectedSeller` a su vez tienen las siguientes propiedades:

```typescript
type UserAddress = {
  id?: string
  userEmail: string
  address: string
  latitude: string
  longitude: string
}

type SelectedSeller = {
  id?: string
  name: string
  address: string
  account?: string
  latitude?: string
  longitude?: string
}
```