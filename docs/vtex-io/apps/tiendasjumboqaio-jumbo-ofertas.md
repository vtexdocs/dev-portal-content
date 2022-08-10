---
title: "OfertasPage"
slug: "tiendasjumboqaio-jumbo-ofertas"
excerpt: "tiendasjumboqaio.jumbo-ofertas@2.0.7"
hidden: true
createdAt: "2022-07-26T15:55:25.831Z"
updatedAt: "2022-08-04T16:50:20.799Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

La app OfertasPage es una aplicación que renderiza una lista de ofertas de una tienda con una funcion que hace el llamdado a la master data. Teniendo como hijos _MenuOfertas_ y _GridOfertas_. recibiendo props del estado de la aplicación.

<img src='../assets/image/docs/folders.png'/>

llamado desde Graphql.

```grpahql
query getDocuments($acronym: String, $where: String, $fields: [String]) {
  documents(acronym: $acronym, where: $where, fields: $fields, pageSize: 500) {
    id
    fields {
      key
      value
    }
  }
}
```

Llamado a la master data para traer la ofertas

```tsx
const GETDOCUMENT = gql`
  query getDocuments($dateToFind: String!, $md: String!) {
    DocumentsNoCache(
      acronym: $md
      fields: [
        "type"
        "category"
        "discountOtherMeansPayment"
        "freeShipping"
        "imageUrl"
        "linkCard"
        "offerPrice"
        "regularPrice"
        "title"
        "TyC"
        "payGet"
        "fromPrice"
        "textPrice"
        "discountFranchise"
        "FranchiseName"
        "until"
        "publishDate"
        "id"
        "pos"
      ]
      pageSize: 500
      where: $dateToFind
    ) {
      documents {
        fields {
          key
          value
        }
      }
    }
  }
`
```

```tsx
return (
  <ApolloProvider client={client}>
    <MenuOfertas setFilter={setFilter} filter={filter} />
    <GridOfertas filter={filter} test={otra} />
  </ApolloProvider>
)
```

<img src='../assets/image/docs/ofertas.png'/>

## Configuration

1. Agrega la dependencia en el archivo de `manifest.json` ;
2. Declara el bloque en la plantilla que desees en tu tema.

### Configuration

<hr>

Importe _`tiendasjumboqaio.ofertas`_ en las dependencias del tema _`manifest.json`_

```json
"dependencies": {
"tiendasjumboqaio.ofertas": "0.x",
}
```

Adicione el bloque de _`"ofertas"`_ en cualquier plantilla de su tema.

```json
  "flex-layout.col#ofertas-t": {
    "children": [
      "ofertas#prueba"
    ],
  }
```

## GridOfertas

Componente que renderiza una lista de ofertas.

### Customization

| CSS Handles                      |
| -------------------------------- |
| `container__cards`               |
| `ofertas__card`                  |
| `wrapper__cards`                 |
| `freeShipping`                   |
| `wrapper__imgCard`               |
| `ofertas__imgCard`               |
| `ofertasTyC__card`               |
| `onlyForToday`                   |
| `links__productos`               |
| `btn__ofertasCard`               |
| `title__card`                    |
| `container__productPricing`      |
| `wrapper__productPrice`          |
| `wrapper__saleTyC`               |
| `value__saleTyC`                 |
| `decoratorsTyC`                  |
| `descriptionTyC`                 |
| `wrapper__otherPay`              |
| `value__otherPay`                |
| `decorators__OtherPay`           |
| `descriptionOtherPay`            |
| `wrapper__onlyOtherPay`          |
| `onlyOtherPay`                   |
| `value__onlyOtherPay`            |
| `decorators__onlyOtherPay`       |
| `descriptiononlyOtherPay`        |
| `wrapper__priceFrom`             |
| `wrapper__priceFrom`             |
| `title__priceFrom`               |
| `priceFrom`                      |
| `fixedDiscount`                  |
| `value__fixedDiscount`           |
| `decorators__fixedDiscount`      |
| `descriptionFixedDiscount`       |
| `wrapperPrice`                   |
| `wrapper__dtoPriceCencosud`      |
| `regularPrice__dtoPriceCencosud` |
| `otherPay__dtoPriceCencosud`     |
| `payCencusud__dtoPriceCencosud`  |
| `description__dtoPriceCencosud`  |
| `Price__dtoPriceCencosud`        |
| `ofertas__cardImg`               |
| `decorators__dtoCodensa`         |
| `value__dtoCodensa`              |
| `descriptionDtoCodensa`          |
| `value__dtoAval`                 |
| `decorators__dtoAval`            |
| `descriptionDtoAval`             |
| `value__dtoItau`                 |
| `decorators__dtoItau`            |
| `descriptiondtoItau`             |
| `value__onlyCenco`               |
| `decorators__onlyCenco`          |
| `descriptiononlyCenco`           |
| `pagueLLeve__pague`              |
| `decorators__pagueLLeve`         |
| `pagueLLeve__lleve`              |
| `priceNow`                       |
| `flagCodensa`                    |
| `colorCodensa`                   |
| `flagItau`                       |
| `colorItau`                      |
| `flagAval`                       |
| `colorAval`                      |
| `jo_hasta`                       |

Para aplicar personalizaciones CSS en este y otros bloques, siga las instrucciones dadas en la receta en [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

## MenuOfertas

Componente que renderiza un menú de filtros.

### Customization

| CSS Handles           |
| --------------------- |
| `wrapper__menu`       |
| `menu__navBar`        |
| `menu__listItems`     |
| `menu__item`          |
| `menu__wrapperItem`   |
| `menu__icon`          |
| `menu__text`          |
| `menu__buttonNext`    |
| `menu__buttonPrev`    |
| `wrapperItem__active` |
| `menu__textActive`    |

Para aplicar personalizaciones CSS en este y otros bloques, siga las instrucciones dadas en la receta en [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.hruiz.com"><img src="https://avatars.githubusercontent.com/u/75335391?v=4" width="100px;" alt=""/><br /><sub><b>Hector Ruiz</b></sub></a><br /><a href="https://github.com/hruiz13" title="Documentation">📖</a></td>
   <td align="center"><img src="https://avatars.githubusercontent.com/u/75432596?v=4" width="100px;" alt=""/><br /><sub><b>Leonardo Rincón</b></sub></a><br /><a href="https://github.com/LeoRincon" title="Documentation">📖</td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->