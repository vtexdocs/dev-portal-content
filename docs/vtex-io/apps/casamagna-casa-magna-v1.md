---
title: "Casa Magna - Vtex IO"
slug: "casamagna-casa-magna-v1"
excerpt: "casamagna.casa-magna@1.1.4"
hidden: true
createdAt: "2022-07-22T14:12:05.482Z"
updatedAt: "2022-08-02T15:23:39.415Z"
---
_Tienda de casamagna creada en la plataforma Vtex IO_

### Comenzando 🚀
_Se debe clonar el repositorio con el comando 'clone'_

`$ git clone https://gitlab.com/palmeraMarketing/casa-magna/vtex.io.git`

_Ejecutar entorno de desarrollo_

```
vtex login casamagna
vtex use dev
vtex link
visitar el link de desarrollo {workspacename}--casamagna.myvtex.com ---> en este caso el workspace es dev
```

### Despliegue
[Guia para desplegar apps](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-new-app-version-publicly-available)
[video de guia ver minuto 2:36:00](https://www.youtube.com/watch?v=M2kDKO8hU28)

### Tutorial
Para entender como funcionan las cosas [VTEX IO](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1/)

### Estructura

```sh
├── assets      --> Fuentes
├── docs        --> Documentos
├── react       --> Componentes personalizados
├── sitemap 
├── store       --> Tienda
|   ├── blocks  --> Bloques vtex IO
|   │   ├── faq
|   │   ├── footer
|   │   ├── header
|   │   ├── pdp
|   │   ├── home
|   │   ├── product-summary
|   │   ├── terms
├── styles      --> Estilos
├── manifest.json   --> Config de la tienda, dependencias , versionamiento etc
└── package.json
```

### Dependencias
Todos los componentes de la tienda que ve en este documento también son de código abierto. Listo para la producción, puede encontrar esas aplicaciones en esta organización de GitHub.

Store framework is the baseline to create any store using _VTEX IO Web Framework_.
- [tienda](https://github.com/vtex-apps/store/blob/master/README.md)

Store GraphQL es un middleware para acceder a todas las APIs de VTEX.

- [GraphQL](https://github.com/vtex-apps/store-graphql/blob/master/docs/README.md)

### Tienda de aplicaciones de componentes

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

### Aplicaciones pixel

 - [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
 - [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)

### Versionado 📌

Mira los [tags en este repositorio](https://gitlab.com/palmeraMarketing/casa-magna/vtex.io/-/tags).

---
⌨️ por [PLM Group](https://gitlab.com/palmeraMarketing) 😊