---
title: "Fabiola Molina Store components"
slug: "fabiolamolina-store-components"
excerpt: "fabiolamolina.store-components@1.0.0"
hidden: true
createdAt: "2022-07-25T19:12:57.986Z"
updatedAt: "2022-07-27T13:16:15.787Z"
---
## Configuração

1. Add a `fabiolamolina.store-components` app como dependencia no `manifest.json` :

```diff
 "dependencies ": {
+  "fabiolamolina.store-components": "0.x"
 }
```

Agora você esta pronto para usar os seguintes blocos

| Block name               | Description                                                                           |
| -------------------      | ------------------------------------------------------------------------------------- |
| `section-layout`         | Esse bloco permite ao lojista remover uma sessão de uma pagina pelo site editor.      |
| `slider-multimedia`      | Esse bloco permite criar uma lista de banners multimedia( imagem ou video).           |
| `slider-multimedia-item` | Esse bloco é equivalente a 1 item que compoem o slider-multimedia ( imagem ou video). |
| `list-rich-text` | Bloco que cria uma list context para rich text |

### `section-layout` props

| Prop name | Type   | Description                                               | Default value |
| --------- | ------ | --------------------------------------------------------- | ------------- |
| `active`  | `bool` | Caso a sessao esteja inativa, não será exibida na loja    | `true`        |

### `slider-multimedia` props

| Prop name      | Type     | Description                             | Default value |
| -------------- | -------- | --------------------------------------- | ------------- |
| `sliderLayout` | `object` | Objeto de configuração do slider layout | `null`        |
| `items`        | `array`  | Array de `slider-multmediaítem`         | `[]`        |

- `sliderLayout` object:

Veja na [documentação do componente slider layout](https://vtex.io/docs/components/all/vtex.slider-layout@0.22.1/#configuration)

### `slider-multimedia-item` props

| Prop name      | Type     | Description                                        | Default value      |
| -------------- | -------- | -------------------------------------------------- | ------------------ |
| `mediaType`    | `Enum`   | Enum para definir o tipo de media                  | `image` ou `video` |
| `Image`        | `object` | Objeto de imagem definido para o app `store-image` | `null`             |
| `Video`        | `object` | Objeto de video definido para o app `store-video`  | `null`             |
| `Link`         | `object` | Objeto de link definido para o video               | `null`             |

Veja na [documentação do componente Store Image](https://vtex.io/docs/components/all/vtex.store-image@0.14.2/#configuration)

Veja na [documentação do componente Store Video](https://vtex.io/docs/components/all/vtex.store-video@1.4.3/#configuration)

**Exemplo de uso**

```json
"slider-multimedia#main-full-banner":{
 "title":"Slide Full banner",
 "props": {
  "blockClass": "fullbanner",
  "sliderLayout":{
   "itemsPerPage": {
    "desktop": 1,
    "tablet": 1,
    "phone": 1
   },
   "infinite": true,
   "showNavigationArrows": "never",
   "showPaginationDots": "always",
   "blockClass": "full-banner"
  },
  "items":[
   {
    "mediaType":"image",
    "Image":{
     "src":"assets/banners/home/banner-home-002.png",
     "link":{
      "url":"#image-01"
     }
    }
   },
   {
    "mediaType":"video",
    "Video":{
     "src":"https://www.youtube.com/watch?v=8-KpLN57wOc",
     "autoPlay":true
    },
    "Link":{
     "url":"#video-01"
    }
   },
   {
    "mediaType":"image",
    "Image":{
     "src":"assets/banners/home/banner-home-001.png",
     "link":{
      "url":"#image-02"
     }
    }
   }
  ]
 }
}
```

### `list-rich-text` props

| Prop name  | Type     | Description                                          | Default value  |
| ---------- | -------- | ---------------------------------------------------- | -------------- |
| `texts`    | `Array`  | Array com as proprieadades do componente `rich-text` | `[]`           |
| `sliderLayout` | `object` | Objeto de configuração do slider layout | `null`        |


Veja na [documentação do componente Rich text](https://vtex.io/docs/components/all/vtex.rich-text@0.15.1/#configuration)

**Exemplo de uso**

```json
{
  
  "list-rich-text#home-exemplo": {
    "children":["slider-layout#home-exemplo"],
    "props": {
      "sliderLayout": {
      "itemsPerPage": 1,
      "infinite": true,
      "blockClass": "carousel"
    },
      "texts": [
        {
          "text": "texto 01"
        },
        {
          "text": "texto 02"
        }
      ]
    }
  }
}
```


## Customização

Use esse handles de CSS para customização.
[Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)

| CSS Handles      |
| ---------------- |
| `.sectionLayout` |
| `.image`         |
| `.videoWrap`     |
| `.link`          |
| `.video`         |

Leia mais sobre as apps:

- [Slider Layout](https://vtex.io/docs/components/all/vtex.slider-layout/)
- [Store Image](https://vtex.io/docs/components/general/vtex.store-image)
- [Store Video](https://vtex.io/docs/components/all/vtex.store-video/)
- [Render runtime](https://vtex.io/docs/components/general/vtex.render-runtime)