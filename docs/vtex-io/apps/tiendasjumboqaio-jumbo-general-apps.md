---
title: "Jumbo-General-Apps"
slug: "tiendasjumboqaio-jumbo-general-apps"
excerpt: "tiendasjumboqaio.jumbo-general-apps@2.1.15"
hidden: true
createdAt: "2022-07-15T16:30:42.807Z"
updatedAt: "2022-08-08T15:44:19.508Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

`jumbo-general-apps` es un repositorio de varias apps personalizadas para tiendas jumbo como:

- logo-footer / logo-mobile
- página de cobertura
- tarjeta-regalo
- vendido-por
- menu-valores
- otro-seller
- regionalización
- newsletter
- tabs manager
- div-for-gtm-info
- how-pay
- banner primera compra
- catalogo
- entre otras
- Background selector
- DivGTM
- Div GTM info
- Primera compra (pop-up)

## Configuration

1. Import the `tiendasjumboqaio.jumbo-general-apps` to your theme's dependencies in the `manifest.json`;

```json
  "dependencies": {
    "tiendasjumboqaio.jumbo-general-apps": "0.x"
  }
```

2. Add the differents blocks in any template from your theme. For example:

```
 "flex-layout.col#cobertura": {
      "children": [
         "cobertura-mercado"
      ]
    },
```

`No CSS Handles are available yet for the app customization.`

<!-- DOCS-IGNORE:start -->

## CardsCatalogos

Es una app que recibe un script de tiendeo.com.co el cual contiene toda la informacion del catalogo de tiendas Jumbo.

```tsx
import React, { useEffect } from 'react'

const CardsCatalogos = () => {
  useEffect(() => {
    const script = document.createElement('script')

    script.src =
      'https://www.tiendeo.com.co/_integrations/slider.js?origin=jumbo'
    script.async = true

    document.getElementById('tiendeo_container')?.appendChild(script)

    return () => {
      document.getElementById('tiendeo_container')?.removeChild(script)
      const where = document.getElementById('__tiendeoViewerContainer')
      if (where) {
        where.style.display = 'none'
      }
    }
  }, [])

  return <div id="tiendeo_container" />
}

export default CardsCatalogos
```

Del lado del cliente se rendieriza en un landing de catalogos disponibles.

<img src='../assets/image/docs/catalogos.png'/>

### Configuration

<hr>

Importe _`tiendasjumboqaio.jumbo-general-apps`_ en las dependencias del tema _`manifest.json`_

```json
"dependencies": {
"tiendasjumboqaio.jumbo-general-apps"
}
```

Adicione el bloque de _`"cards-catalogos"`_ en cualquier plantilla de su tema.

```json
  "flex-layout.row#catalogos__body": {
    "children": ["cards-catalogos"]
  },
```

## HowPay

Es una app que recibe un slider el cual tiene una secuencia de imágenes que guían al cliente en la forma de pago, recibiendo como children el componente _'<CarPay /'_ que es el contenedor de las imágenes y textos de cada paso en la compra.

```tsx
import React from 'react'
import { useCssHandles } from 'vtex.css-handles'

import CarPay from './CardPay'

const CSS_HANDLES = ['containerSlider']

const HowPay = () => {
  const handles = useCssHandles(CSS_HANDLES)

  return (
    <div className={`${handles.containerSlider}`}>
      <CarPay />
    </div>
  )
}

export default HowPay
```

Del lado del cliente se rendieriza en un landing del paso a pasa cómo comprar.

<img src='../assets/image/docs/howpay.png'/>

### Configuration

<hr>

Importe _`tiendasjumboqaio.jumbo-general-apps`_ en las dependencias del tema _`manifest.json`_

```json
"dependencies": {
"tiendasjumboqaio.jumbo-general-apps"
}
```

Adicione el bloque de _`"how-pay"`_ en cualquier plantilla de su tema.

```json
  "store.custom#como-comprar__container": {
    "children": ["flex-layout.row#como-comprar__wrapper", "how-pay"]
  }
```

## BannerPageValores

Es una app que genera el banner principal de las páginas de valores.

```tsx
BannerValoresPage.defaultProps = {
  src: 'imagenes/valores/valores-1.png',
  alt: 'Imagen de banner de panaderia',
  title: [
    { text: 'Hola', isBig: true },
    { text: 'Hola2', isBig: true },
    { text: 'Hola3', isBig: true },
  ],
  otherClass: '',
}
```

Del lado del cliente se rendieriza un banner con el texto a mostrar que se anima con el la primera carga y con el sroll de manera vertical.

<img src='../assets/image/docs/carnes.png'/>

### Configuration

<hr>

Importe _`tiendasjumboqaio.jumbo-general-apps`_ en las dependencias del tema _`manifest.json`_

```json
"dependencies": {
"tiendasjumboqaio.jumbo-general-apps"
}
```

Adicione el bloque de _`"banner-valores-page"`_ en cualquier plantilla de su tema.

```json
...
  "flex-layout.col#text-hero-sabores": {
    "children": [
      "banner-valores-page#main-valores"
    ],
    "props": {
      "blockClass": "text-sabores-main"
    }
  },
  ...
```

### _dropdown-wrapper props_

<hr>

| Prop name    | Type     | Description                                                                                                                                                                                                                                                                                   | Default value                          |
| ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `src`        | `string` | Link de la imagen a renderizar en el banner                                                                                                                                                                                                                                                   | src : 'imagenes/valores/valores-1.png' |
| `alt`        | `string` | Texto alternativo a la imagen si no se renderiza                                                                                                                                                                                                                                              | alt: 'Imagen de banner de panaderia'   |
| `title`      | `Array`  | Es un Array de objetos que renderizara el texto del banner, cada posición cuenta con 3 props clave valor {"text": "hola", "id": "text1, "isBig": false}, text y id son claves que su valor es un string, y isBig es booleano que permite saber si ese texto ira de mayor tamaño que el resto. | title: [{ text: 'Hola', isBig: true }, |
| `otherClass` | `string` | Es un string que permite poner otra class diferentes a las que llega por los handles y personalizar cada banner a gusto.                                                                                                                                                                      | otherClass: '',                        |

**CSS Handles**

- containerBanner
- containerTitle
- labelTitle
- spanTitle
- animateText
- imageBanner
- isBig

Para aplicar personalizaciones CSS en este y otros bloques, siga las instrucciones dadas en la receta en [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

## ValoresCardImage

Es una app que genera bloque donde se renderiza una imagen con un texto que se animan segun el scroll vertial.

```tsx
ValoresCardsImage.defaultProps = {
  src: 'imagenes/valores/valores-1.png',
  alt: 'Imagen de banner de panaderia',
  title: 'Pan artesanal ',
  description: 'El mejor pan artesanal',
  blockClass: '',
  button: true,
  haveImage: true,
  haveIcon: false,
  srcIcon: '',
  altIcon: 'Icono de marca',
  isParPosition: false,
  isParStyles: false,
  labelButton: 'Llevatelo',
  linkButton: '/valores/panaderia',
  idDescription: '',
  idImage: '',
  otherClass: '',
}
```

```json
  "valores-cards-image#carnes-primer-nivel": {
    "props": {
      "idImage": "card1",
      "haveImage": false,
      "title": "Carnes de primer nivel",
      "idDescription": "description1",
      "description": "Con nuestra marca propia Cuisine & Co encuentras carnes exclusivas como la carne de res premium y la carne de búfalo. Solo necesitas una buena parrilla.",
      "button": true,
      "isParPosition": true,
      "isParStyles": true,
      "labelButton": "Disfrútala",
      "linkButton": "/valores/carnes",
      "haveIcon": true,
      "srcIcon": "assets/image/valores-page/carnes/primernivel-cuisineco-tiendas-jumbo-d.png",
      "altIcon": "Icon carnes de primer nivel",
      "blockClass": "carnes-primer"
    }
  },
```

Del lado del cliente se rendieriza una sección donde se muestra una imagen con un texto que se animan segun el scroll vertial.

<img src='../assets/image/docs/valoresImage.png'/>
<img src='../assets/image/docs/frutas.png'/>
<img src='../assets/image/docs/valoresPanaderia.png'/>

### Configuration

<hr>

Importe _`tiendasjumboqaio.jumbo-general-apps`_ en las dependencias del tema _`manifest.json`_

```json
"dependencies": {
"tiendasjumboqaio.jumbo-general-apps"
}
```

Adicione el bloque de _`"valores-cards-image"`_ en cualquier plantilla de su tema, con el alias que desee.

```json
...
  "flex-layout.row#cardImage__carnes-primer-nivel": {
    "children": ["valores-cards-image#carnes-primer-nivel"],
    "props": {
      "blockClass": "cardImage__carnes-primer-nivel"
    }
  }
  ...
```

### _dropdown-wrapper props_

<hr>

| Prop name       | Type      | Description                                                                  | Default value                          |
| --------------- | --------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| `src`           | `string`  | Link de la imagen a renderizar                                               | src : 'imagenes/valores/valores-1.png' |
| `alt`           | `string`  | Texto alternativo a la imagen si no se renderiza                             | alt: 'Imagen de banner de panaderia'   |
| `title`         | `string`  | Titulo de la sección                                                         | title: 'Pan artesanal',                |
| `blockClass`    | `string`  | Es un string que permite poner las clases a los elementos.                   | blockClass: ''                         |
| `description`   | `string`  | Es el texto que lleva como descipcíon del producto                           | description: 'El mejor pan artesanal', |
| `button`        | `boolean` | Condicional que permite mostrar o no si lleva boton la card                  | button: true,                          |
| `haveImage`     | `boolean` | Boolean que nos permite ponerle si lleva o no imagen la card                 | haveImage: true,                       |
| `haveIcon`      | `boolean` | Boolean que nos permite ponerle si lleva o no icono la card.                 | haveIcon: false,                       |
| `srcIcon`       | `string`  | Link a donde nos redirigira el icono de la card.                             | srcIcon: '',                           |
| `altIcon`       | `string`  | Texto alternativo si no se renderiza el icono                                | altIcon: 'Icono de marca',             |
| `isParPosition` | `boolean` | Permite saber si la posición es para posicionar la imagen del lado correcto. | isParPosition: false,                  |
| `isParStyles`   | `boolean` | Permite saber si la posición es para darle stilos al compoente               | isParStyles: false,                    |
| `labelButton`   | `string`  | Texto que se mostrara en el boton.                                           | labelButton: 'Llevatelo'               |
| `linkButton`    | `string`  | link al que hara redirecionamiento el boton al ser clikeado.                 | blockClass: ''                         |
| `idDescription` | `string`  | ID que nos permite hacer referencia en el DOM al texto de descripción .      | idDescription: '',                     |
| `idImage`       | `string`  | ID que nos permite hacer referencia en el DOM al texto de Imagen             | idImage: '',                           |

**CSS Handles**

- containerCardImage
- containerDescription
- valoresImage
- titleImage
- descriptionImage
- buttonImage
- isParClass
- isParTitle
- isParLink
- wrapperMarca
- imageMarca
- wrapperImg
- animateText
- isParButton
- isParDescription
- isParClassDescription
- linkImage
- iconImage

Para aplicar personalizaciones CSS en este y otros bloques, siga las instrucciones dadas en la receta en [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

## Background selector

Es una app la cual le aplica un fondo personalizable desde el site editor a los childrens que se le pasen. Tambien incluye opcion de cambiar los textos a oscuros.

<img src='../assets/image/docs/bgPanel.png'/>

### Configuration

<hr>

Adicione el bloque de _`"bg-image-selector"`_ en cualquier plantilla de su tema, con el alias que desee. Y pasele al componente los hijos que desea mostrar.

```json
...
  "store.custom#template-coleccion": {
    "blocks": [
      "bg-image-selector"
    ]
  },
  "bg-image-selector": {
    "children": [
      "flex-layout.row#coleccionContainer"
    ]
  },
  ...
```
## Div gtm y Div GTM Info

Es una app la cual genera un DIV con id: gtm-manager y gtm-info respectivamente, este ultimo incluye el EAM del producto y el SKU del producto.
Esto con el fin de ser utilizado para el google tag manager.

## Div gtm y Div GTM Info

Es una app la cual genera un DIV con id: gtm-manager y gtm-info respectivamente, este ultimo incluye el EAM del producto y el SKU del producto.
Esto con el fin de ser utilizado para el google tag manager.

### Configuration

<hr>

Adicione el bloque de _`"div-for-gtm"`_ o _`"div-for-gtm-info"`_ en cualquier plantilla de su tema, con el alias que desee.desea mostrar.

```json
...
  "flex-layout.row": {
    "children": [
      "div-for-gtm",
      "div-for-gtm-info"
    ]
  },
  ...
```

## Menu Valores

Es una app especifica para replicar el menu personalizado para la pagina de valores.

### Configuration

<hr>

Adicione el bloque de _`"menu-valores"`_ en cualquier plantilla de su tema, con el alias que desee.desea mostrar.

```json
...
  "flex-layout.row": {
    "children": [
      "menu-valores"
    ]
  },
  ...
```

## Otro Seller

Es una app para filtrar contenido a mostrar, si el producto proviene a un seller diferente de _Cencosud Colombia S.A_

### Configuration

<hr>

Adicione el bloque de _`"otro-seller"`_ en cualquier plantilla de su tema, con el alias que desee.desea mostrar.
Como children se le pasa el contenido que se quiere mostrar si es del seller Cencosud Colombia
Con la propiedad Else se le pasa el componente que se quiere mostrar si es de otro seller.

```json
...
  "otro-seller": {
    "children": [
      "product-separator",
      "condition-layout.product#payments-methods-a"
    ],
    "props": {
      "Else": "responsive-layout.desktop#content-card"
    }
  },
  ...
```
### _dropdown-wrapper props_

<hr>

| Prop name       | Type      | Description                                                                  | Default value                          |
| --------------- | --------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| `Else`          | `string`  | Componente VTEX a mostrar si es de otro seller                               | null |


## Primera compra

Es una app para mostrar una modal de primera compra. Esta es administrable desde el site editor.

<img src='../assets/image/docs/primeraCompra.png'/>
<img src='../assets/image/docs/popUp.png'/>

### Configuration

<hr>

Adicione el bloque de _`"primera-compra"`_ en cualquier plantilla de su tema, con el alias que desee.desea mostrar.
Como children se le pasa el contenido que se quiere mostrar si es del seller Cencosud Colombia
Con la propiedad Else se le pasa el componente que se quiere mostrar si es de otro seller.

```json
...
  "flex-layout.col": {
    "children": [
      "primera-compra"
    ]
  },
  ...
```

## Regionalizacion

Es una app para filtrar contenido a mostrar, si el usuario no esta en una regionalizacion con _whitelabel_ de mercado.

```json
...
  "regionalizacion#slider-home": {
    "title": "Slider General",
    "children": [
      "list-context.image-list#sliderGeneral"
    ],
    "props": {
      "Else": "list-context.image-list#slider-general-plataforma"
    }
  },
  ...
```

### _dropdown-wrapper props_

<hr>

| Prop name       | Type      | Description                                                                  | Default value                          |
| --------------- | --------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| `Else`          | `string`  | Componente VTEX a mostrar si es de otro seller                               | null |


## Tab Manager

Es una app para filtrar de mostrar tabs en caso de que no tengan contenido recibido del producto.

### _dropdown-wrapper props_

<hr>

| Prop name       | Type      | Description                                                                  | Default value                          |
| --------------- | --------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| `group`          | `string`  | especification group del item (tab) en la cual se esta utilizando                                | null |


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/63118722?v=4" width="100px;" alt=""/><br /><sub><b>Daniel Acosta</b></sub></a><br /><a href="https://github.com/deacostac" title="Documentation">📖</td>
    <td align="center"><a href="http://www.hruiz.com"><img src="https://avatars.githubusercontent.com/u/75335391?v=4" width="100px;" alt=""/><br /><sub><b>Hector Ruiz</b></sub></a><br /><a href="https://github.com/hruiz13" title="Documentation">📖</a></td>
   <td align="center"><img src="https://avatars.githubusercontent.com/u/75432596?v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Rincón</b></sub></a><br /><a href="https://github.com/LeoRincon" title="Documentation">📖</td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->