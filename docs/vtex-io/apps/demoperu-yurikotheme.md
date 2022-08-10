---
title: "Store Theme IT Globers"
slug: "demoperu-yurikotheme"
excerpt: "demoperu.yurikotheme@0.1.0"
hidden: true
createdAt: "2022-07-10T00:00:30.941Z"
updatedAt: "2022-07-10T00:00:30.941Z"
---
IT Globers Store Theme es un modelo básico de tienda basado en VTEX IO Store Framework.

Debe usarse solo cuando desee iniciar un nuevo tema de tienda sin ninguna configuración preestablecida.

While Store Theme gives developers a ready-to-go default store front structure, the IT Globers Store Boilerplate Theme will enable you to build you store freely from scratch.

## Previsualización

Screenshot del home del sitio.
<!-- Por favor incluya un screenshot del home del sitio en el que está trabajando. Ejemplo
![store-theme-default](https://user-images.githubusercontent.com/1354492/63937047-e8d81c80-ca37-11e9-86fc-61e88847bbfb.png)-->

## Configuración

### Paso 1 -  Configuración básica

Ingrese a la [guía básica de configuración](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1) de VTEX IO y siga los pasos. 

Al final de la configuración, debería tener instalada la interfaz de línea de comandos de VTEX (Toolbelt) junto con un workspace para desarrolladores en el que pueda trabajar.

### Paso 2 - Clonación del repositorio de IT Globers Store Theme.

Use este repositorio como [plantilla](https://github.com/itglobers/itglobers-store-theme-es/generate) para crear un repositorio de forma local para poder comenzar a trabajar de manera efectiva en él

Luego, acceda al directorio del repositorio usando su terminal.

### Paso 3 - Editando el archivo `Manifest.json`


Una vez en el directorio del repositorio, es hora de editar el archivo `manifest.json` de Store Theme de IT Globers. 

Una vez estemos en el archivo, deberá remplazar los valores de `vendor` y `account`. `vendor` es el nombre de la cuenta en la que estamos trabajando y `account` es lo que desee colocar de nombre para su tema. Por ejemplo:

```json
{
  "vendor": "itglobers",
  "name": "store-theme",
}
```

### Paso 4 -  Instalando las apps requeridas

Para usar Store Framework y trabajar en el tema de su tienda, es necesario tener  `vtex.store-sitemap` y `vtex.store` instalados.

Ejecute `vtex list` y compruebe si esas aplicaciones ya están instaladas. 

Si no es así, ejecute el siguiente comando para instalarlos: `vtex install vtex.store-sitemap vtex.store -f`

### Paso 5 - Desinstalar cualquier tema existente

Al correr `vtex list`, puede verificar si hay algún tema instalado.

Es común tener ya instalado un `vtex.store-theme` cuando inicia el proceso de desarrollo front de la tienda.

Por lo tanto, si lo encuentra en la lista de la aplicación, copie su nombre y utilícelo junto con el comando `vtex uninstall`. Por ejemplo:

```json
vtex uninstall vtex.store-theme
```

### Paso 6 - Ejecute y obtenga una vista previa de su tienda

Entonces ha llegado el momento de cargar todos los cambios que realizó en sus archivos locales a la plataforma. Para eso, use el comando `vtex link`.

Si el proceso se ejecuta sin errores, se mostrará el siguiente mensaje: `App linked successfully`. Luego, ejecute el comando `vtex browse` para abrir una ventana del navegador con su tienda vinculada.

Esto le permitirá ver los cambios aplicados en tiempo real, a través de la cuenta y el espacio de trabajo en el que está trabajando.

## Dependencies

odos los componentes de la tienda que ve en este documento también son de código abierto. Listo para producción, puede encontrar esas aplicaciones en esta organización de GitHub.

Store framework es la base para crear cualquier tienda usando _VTEX IO Web Framework_.
- [Store](https://github.com/vtex-apps/store/blob/master/README.md)

### Store component dependencies
- [Header](https://github.com/vtex-apps/store-header/blob/master/docs/README.md)
- [Footer](https://github.com/vtex-apps/store-footer/blob/master/docs/README.md)
- [Slider Layout](https://github.com/vtex-apps/slider-layout/blob/master/docs/README.md)
- [Shelf](https://github.com/vtex-apps/shelf/blob/master/docs/README.md)
- [Telemarketing](https://github.com/vtex-apps/telemarketing/blob/master/docs/README.md)
- [Menu](https://github.com/vtex-apps/menu/blob/master/docs/README.md)
- [Login](https://github.com/vtex-apps/login/blob/master/docs/README.md)
- [Minicart](https://github.com/vtex-apps/minicart/blob/master/docs/README.md)
- [Category Menu](https://github.com/vtex-apps/category-menu/blob/master/docs/README.md)
- [Product Summary](https://github.com/vtex-apps/product-summary/blob/master/docs/README.md)
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb/blob/master/docs/README.md)
- [Search Result](https://github.com/vtex-apps/search-result/blob/master/docs/README.md)
- [Product Details](https://github.com/vtex-apps/product-details/blob/master/docs/README.md)
- [Store Components](https://github.com/vtex-apps/store-components/blob/master/docs/README.md)
- [Order Placed](https://github.com/vtex-apps/order-placed/blob/master/docs/README.md) 

### Dependencias Peer store component 

### Dependencias Custom component