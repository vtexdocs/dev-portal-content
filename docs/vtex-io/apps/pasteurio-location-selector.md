---
title: "Selector de Ubicación"
slug: "pasteurio-location-selector"
excerpt: "pasteurio.location-selector@0.14.2"
hidden: true
createdAt: "2022-07-12T19:23:17.636Z"
updatedAt: "2022-07-12T19:23:17.636Z"
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
    "pasteurio.location-selector": "0.x"
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

Luego de agregar la dependencia `coopidrogas.location-selector` las siguientes aplicaciones estarán ahora disponibles.
Incluyendo el componente no-visual que se integró en el proceso de instalación anterior.

- [Location Modal](LocationModal.md)
- [Location Selector](LocationSelector.md)