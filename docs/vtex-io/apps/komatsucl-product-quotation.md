---
title: "Quick Search"
slug: "komatsucl-product-quotation"
excerpt: "komatsucl.product-quotation@0.0.2"
hidden: true
createdAt: "2022-08-04T08:41:23.100Z"
updatedAt: "2022-08-08T22:45:06.175Z"
---
Componente encargado de realizar búsqueda de productos con base en especificaciones de producto configuradas como
filtros. El primer filtro funciona como un auto-completar del buscador nativo.

Las especificaciones se deben indicar vía _props_ sobre el componente, una vez instalada la aplicación debería ver un
componente **como la imagen** pero sin estilos.

![Captura](https://raw.githubusercontent.com/cristianbarreto-bs/images/main/komatsu-quick-search-desktop.png)

## Configuration

Para usar la aplicación debe contar con las ID's de especificación que usura como filtros, recuerde que el primer filtro
siempre será un buscador de productos. Teniendo este en mente solo debería:

1. Agregar la aplicación como dependencia en el archivo `manifest.json` de su tema;
2. Declara el bloque `quick-search`

Recuerde que los filtros se aplican en relación con el funcionamiento
de [VTEX Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search/).

## Customization

| CSS Handles |
| ----------- | 
| `quickSearchWrapper` | 
| `quickSearchForm` | 
| `quickSearchTitle` | 
| `quickSearchTitleIcon` | 
| `filterWrapper` |

La aplicación usa el [Selector](https://styleguide.vtex.com/#/Components/%F0%9F%91%BB%20Experimental/Select) de
paquete `vtex.styleguide@9.x`, considere esto si requiere estilizar los selectores