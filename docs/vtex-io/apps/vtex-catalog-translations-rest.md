---
title: "Catalog Translations Rest"
slug: "vtex-catalog-translations-rest"
excerpt: "vtex.catalog-translations-rest@1.0.0"
hidden: true
createdAt: "2022-08-03T14:46:14.982Z"
updatedAt: "2022-08-03T14:46:14.982Z"
---
Rest API that allows both the translation of each entity of the catalog in particular, as well as the massive translation of them.

You can download the Postman Collection from this ([link](https://github.com/vtex-apps/catalog-translations-rest/blob/development/docs/VTEX%20-%20Catalog%20Translation%20API.postman_collection.json)).

Check ([this](https://developers.vtex.com/vtex-developer-docs/docs/catalog-internationalization)) documentation for more information.

## Routes

### Authentication

Each route must include in the headers either:

| **Header** | **Type** |
| ---------- | -------- |
| `AppKey`   | string   |
| `AppToken` | string   |

Or:

| **Header**           | **Type** | **Description**                     |
| -------------------- | -------- | ----------------------------------- |
| `authorizationToken` | string   | VTEX Auth Cookie for authorization. |

Every translation entity must have this two properties:

| **Property** | **Type** | **Description**                                  |
| ------------ | -------- | ------------------------------------------------ |
| `args`       | object   | Translation information for the specific entity. |
| `locale`     | string   | Translation language (ex: 'fr-FR').              |

Example:

```json
    {
        "args": {
          {...}
        },
        "name": "{locale}"
    }
```

#### Category

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/category`

| **args**    | **Type** |
| ----------- | -------- |
| id          | string   |
| name        | string   |
| title       | string   |
| description | string   |
| keywords    | [string] |
| linkId      | string   |

```json
{
  "args": {
    "id": "3",
    "name": "Elêtronicos",
    "title": "Casa - Elêtronicos",
    "description": "Esta é a descrição da categoria Eletrônicos",
    "keywords": ["eletronicos", "utensílios"],
    "linkId": "eletronicos"
  },
  "locale": "pt-BR"
}
```

#### Brand

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/brand`

| **args**  | **Type** |
| --------- | -------- |
| id        | object   |
| name      | string   |
| text      | string   |
| siteTitle | string   |
| keywords  | string   |

```json
{
  "args": {
    "id": "2000057",
    "name": "Calvin Klein",
    "text": "Esta é uma descrição da marca.",
    "siteTitle": "Calvin Klein",
    "keywords": "calvin klain"
  },
  "locale": "pt-BR"
}
```

#### Product

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/product`

| **args**           | **Type** |
| ------------------ | -------- |
| id                 | string   |
| name               | string   |
| title              | string   |
| description        | string   |
| shortDescription   | string   |
| keywords           | [string] |
| metaTagDescription | string   |
| linkId             | string   |

```json
{
  "args": {
    "id": "45",
    "name": "Câmera Retrô",
    "description": "Esta é uma descrição genérica deste produto.",
    "shortDescription": "Esta é uma breve descrição genérica deste produto.",
    "title": "Câmera Retrô - Store Components",
    "metaTagDescription": "Compre os melhores produtos em nossa loja",
    "linkId": "black-steel-film-camera",
    "keywords": ["lomografia", "vintage"]
  },
  "locale": "pt-BR"
}
```

#### Sku

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/sku`

| **args** | **Type** |
| -------- | -------- |
| id       | string   |
| name     | string   |

```json
{
  "args": {
    "id": "46",
    "name": "Mixer Retro - Marrom"
  },
  "locale": "pt-BR"
}
```

#### Sku or Product Specification

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/sku-specification`

| **args** | **Type** |
| -------- | -------- |
| id       | string   |
| name     | string   |

```json
{
  "args": {
    "fieldId": "31",
    "name": "Cor"
  },
  "locale": "pt-BR"
}
```

#### Specification Values

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/specification-values`

| **args**        | **Type**                           |
| --------------- | ---------------------------------- |
| fieldId         | string                             |
| fieldValueNames | [{ id: `string`, name: `string` }] |

```json
{
  "args": {
    "fieldId": "31",
    "fieldValuesNames": [
      {
        "id": "91",
        "name": "Azul"
      },
      {
        "id": "92",
        "name": "Vermelho"
      }
    ]
  },
  "locale": "pt-BR"
}
```

#### Category Group

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/category-group`

| **args** | **Type** |
| -------- | -------- |
| groupid  | string   |
| name     | string   |

#### Bulk Translate

Bulk Translate allows to make a massive translation of the above entities. For each of these, the same structure presented above must be respected.

It is necessary to specify an email where you will receive a report on the translations done and will be notified in case there has been an error in any specific translation.

`POST`

`https://{environment}--{accountName}.myvtex.com/v0/catalog-translation/bulkTranslate`

```json
{
  "notificationEmail": "",
  "categories": [],
  "brands": [],
  "products": [],
  "skus": [],
  "skusProductsSpecifications": [],
  "specificationValuesData": [],
  "categoriesGroupsData": []
}
```