---
title: "Translating Catalog content"
excerpt: "Overwrite automatic message translations from the Catalog with a more representative content of your store."
slug: "catalog-internationalization"
hidden: false
createdAt: "2020-08-31T17:18:54.238Z"
updatedAt: "2024-10-04T15:19:12.970Z"
---

In this guide, you will learn how to overwrite an automatic message translation from the Catalog, such as a product name or a product description, with a more specific and representative content of your store.

Catalog messages are translatable text strings related to a store's catalog, stored as external data in the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview), which manages a store’s sales channels, categories, brands, products, SKUs, and specifications.

The following list includes the settings from the Catalog API that are translatable, meaning they can automatically be translated into different languages based on the user’s locale.

- **[Category](https://help.vtex.com/en/tutorial/category-registration-fields--5Z7RrvW41yumyQCmk2iqoG):** Name, keywords (similar words), page title (tag title), meta tag description, and the URL slug (cross-border stores only).
- **[Brand](https://help.vtex.com/en/tutorial/brand-registration-fields--37Ky7lTbEkiWIAYA80EMyI):** Name, keywords (similar words), page title (tag title), meta tag description, and the URL slug (cross-border stores only).
- **[Product](https://help.vtex.com/en/tutorial/product-registration-fields--4dYXWIK3zyS8IceKkQseke):** Name, keywords (substitute words), page title (tag title), description, short description, meta tag description, and the URL slug (cross-border stores only).
- **[SKU](https://help.vtex.com/en/tutorial/sku-registration-fields--21DDItuEQc6mseiW8EakcY):** Name.
- **[SKU or product specification](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP):** Name, description, and values.
- **[Category group](https://help.vtex.com/en/tutorial/creating-category-groups--tutorials_246):** Name.

Considering literal translations and cultural factors, you may want to overwrite automatic translations with specific and representative content of your store. This can be done through the `catalog-graphql` app, which is the GraphQL interface of the Catalog API, by following the instructions below.

## Instructions

To translate text messages from your store's catalog, follow these steps:

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.
2. In the Admin VTEX, access **Store Setting > Storefront > GraphQL IDE**.
3. From the dropdown list, choose the `vtex.catalog-graphql` app.
4. Click on  *Query Variables* at the bottom of the page.

  ![graphql-ide](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/graphql-ide.gif)

5. According to your scenario, check the following sections ([category](#category), [brand](#brand), [product](#product), [SKU](#SKU), [SKU or product specification](#SKU-or-product-specification), [specification values](#specification-values)) for orientations on how to fill in the main text box and the *Query Variables* section.
6. After adjusting your query, click the play button to run the declared mutation. The expected response is a boolean value indicating `true`.

Below, see an example of the complete process of the automatic translation of a product name:

![graphql-ide-catalog](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/graphql-ide-catalog.gif)

## Translatable settings

Below, learn how to fill in the main text box and the *Query Variables* section when configuring your catalog translation.

### Catalog

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args:CategoryInputTranslation, $locale:Locale){
  translateCategory(category:$args,locale:$locale)
}
```

#### Query Variables

Fill in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args":{
    "id": "3",
    "name": "Eletrônicos",
    "title": "Casa - Eletrônicos",
    "description": "Esta é a descrição da categoria Eletrônicos",
    "keywords": [
        "eletronicos",
        "utensílios"
    ],
    "linkId": "eletronicos"
  },
  "locale": "pt-BR" 
}
```

- `id`: Category ID. Every category in your store has a unique ID that can be found under *Catalog > Categories* in the admin VTEX.
- `name`: Category name.
- `title`: Category page meta title.
- `description`: Detailed description of the category.
- `keywords`: Object containing the translations of **each** substitute word of the category.
- `linkId`: The `textLink` (unless your store is cross-border, it must **not** be translated).
- `locale`: Target translation locale.

  > ℹ️ If you have a cross-border store, the `linkId` serves as the category URL slug. The [Rewriter](https://developers.vtex.com/docs/guides/rewriter) app will automatically create an alias using the translated slug for each target locale, storing it in the `resolveAs` field for that locale’s internal route. For example, a category with the slug `eletronics` at `http://{storename}.com/us/eletronics/d` could have the translated slug `eletronicos` for the `pt-BR` binding, as in `http://{storename}.com/br/eletronicos/d`.

### Brand

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args:BrandInputTranslation, $locale:Locale){
  translateBrand(brand:$args,locale:$locale)
}
```

#### Query Variables

Fill in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args":{
    "id": "2000057",
    "name": "Calvin Klein",
    "text": "Esta é uma descrição da marca.",
    "siteTitle": "Calvin Klein",
    "keywords": "calvin klain"
  },
  "locale": "pt-BR" 
}
```

- `id`:  Brand ID. Every brand in your store has a unique ID that can be found under *Catalog > Brands* in the admin VTEX.
- `name`: Brand name.
- `text`: Brand description (meta tag description).
- `siteTitle`: Brand page title (tag title).
- `keywords`: Object containing the translations of **each** substitute word of the brand.
- `locale`: Target translation locale.

### Product

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args:ProductInputTranslation, $locale:Locale){
  translateProduct(product:$args,locale:$locale)
}
```

#### Query Variables

Fill in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args":{
    "id": "45",
    "name": "Câmera Retrô",
    "description": "Esta é uma descrição genérica deste produto.",
    "shortDescription": "Esta é uma breve descrição genérica deste produto.",
    "title": "Câmera Retrô - Store Components",
    "metaTagDescription": "Compre os melhores produtos em nossa loja",
    "linkId": "black-steel-film-camera",
    "keywords": [
      "lomografia",
      "vintage"]
 },
  "locale": "pt-BR" 
}
```

- `id`: Product ID. Every product in your store has a unique ID that can be found under *Catalog > Products and SKUs* in the admin VTEX.
- `name`: Product name.
- `description`: Product description.
- `shortDescription`: Additional short description.
- `title`: Page title (tag title)
- `metaTagDescription`: Description (meta tag description).
- `keywords`: Object containing the translations of **each** substitute word of the product.
- `linkId`: The `textLink` (unless your store is cross-border, it must **not** be translated).
- `locale`: Target translation locale.

  > ℹ️ If you have a cross-border store, the `linkId` serves as the product URL slug. The [Rewriter](https://developers.vtex.com/docs/guides/rewriter) app will automatically create an alias using the translated slug for each target locale, storing it in the `resolveAs` field for that locale’s internal route. For example, a product with the slug `blue-top-retro-camera` at `http://{storename}.com/us/blue-top-retro-camera/p` could have the translated slug `camera-retro-azul` for the `pt-BR` binding, as in `http://{storename}.com/br/camera-retro-azul/p`.

### SKU

#### Mutation

Fill in the main text box with the following mutation command:

```
mutation translate($args:SKUInputTranslation, $locale:Locale){
  translateSKU(sku:$args,locale:$locale)
}
```

#### Query Variables

Filll in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args":{
    "id": "46",
    "name": "Mixer Retro - Marrom"
  },
  "locale": "pt-BR" 
}
```

- `id`: SKU ID. Every product in your store has a unique ID that can be found under *Catalog > Products and SKUs* in the admin.
- `name`: SKU name.
- `locale`: Target translation locale.

### SKU or product specification

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args:FieldInputTranslation, $locale:Locale){
  translateField(field:$args,locale:$locale)
}
```

#### Query Variables

Fill in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args":{
    "fieldId": "31",
    "name": "Cor"
  },
  "locale": "pt-BR" 
}
```

- `fieldId`: Product or SKU specification field ID. Every product or SKU specification in your store has a unique ID that can be found following this [orientation for SKU specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/6UjLHdAT5YLuflki10SXLr?locale=en) or this [orientation for product specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4fcdmJzQ6QYA9zWf3bLWin).
- `name`: Specification name.
- `locale`: Target translation locale.

### Specification values

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args:FieldValueInputTranslation, $locale:Locale){
  translateFieldValues(fieldValues:$args,locale:$locale)
}
```

#### Query Variables

Fill in the *Query Variables* section with the desired translations of each parameter.

```json
{
  "args": {
    "fieldId": "31",
    "fieldValuesNames":[
        {
          "id":"91",
          "name":"Azul"
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

- `fieldId`: Product or SKU specification field ID. Every product or SKU specification in your store has a unique ID that can be found following this [orientation for SKU specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/6UjLHdAT5YLuflki10SXLr?locale=en) or this [orientation for product specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4fcdmJzQ6QYA9zWf3bLWin).
- `fieldValuesNames`: An object containing
- `id`: Specification value ID.
- `name`: Specification value name.
- `locale`: Target translation locale.

  > Specification values ID can be found by running the following query:
  > 
  > ```gql
  >query{
  >  fieldValues(fieldId:"24"){
  >    fieldValueId
  >    value
  >  }
  >}
  >```
  >
  > Where `fieldId` is the specification ID found following the guide [Products and SKU Specifications](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/6UjLHdAT5YLuflki10SXLr?locale=en).

### Category group

#### Mutation

Fill in the main text box with the following mutation command:

```gql
mutation translate($args: GroupInputTranslation, $locale:Locale) {
  translateGroup(group: $args, locale:$locale)
}
```

#### Query Variables

Fill in the Query Variables section with the desired translations of each parameter.

```json
{
  "args":{
    "groupId": "14",
    "name": "Cores"
  },
  "locale": "pt-BR" 
}
```

- `groupId`: Category group ID.
- `name`: Category group name.
- `locale`: Target translation locale.

  > Category group IDs can be found by running the following query:
  >
  >```gql
  >query{
  >  groupsByCategory(categoryId:1){
  >    id
  >    name
  >  }
  >}
  >```
  >
  > Where `categoryId` is the ID of the category related to that group.
