---
title: "Translating Catalog content"
excerpt: "Learn how to overwrite automatic message translations from the Catalog."
slug: "catalog-internationalization"
hidden: false
createdAt: "2020-08-31T17:18:54.238Z"
updatedAt: "2025-11-18T18:56:38.330Z"
---

In this guide, you'll learn how to overwrite an automatic message translation from your store's Catalog, such as product names and descriptions. By following these instructions, you can provide more specific content in different languages.

Catalog messages are translatable text strings associated with your store's catalog. These messages are stored externally within the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview), which manages your store's sales channels, categories, brands, products, SKUs, and specifications.

Below is a list of Catalog API settings that automatically translate based on the user's locale:

- **[Category](https://help.vtex.com/en/tutorial/category-registration-fields--5Z7RrvW41yumyQCmk2iqoG):** Name, keywords (similar words), page title (tag title), meta tag description, and the URL slug (cross-border stores only).
- **[Brand](https://help.vtex.com/en/tutorial/brand-registration-fields--37Ky7lTbEkiWIAYA80EMyI):** Name, keywords (similar words), page title (tag title), meta tag description, and the URL slug (cross-border stores only).
- **[Product](https://help.vtex.com/en/tutorial/product-registration-fields--4dYXWIK3zyS8IceKkQseke):** Name, keywords (similar words), page title (tag title), description, short description, meta tag description, and URL slug (cross-border stores only).
- **[SKU](https://help.vtex.com/en/tutorial/sku-registration-fields--21DDItuEQc6mseiW8EakcY):** Name.
- **[SKU or product specification](https://help.vtex.com/en/docs/tracks/specifications-concept-definition):** Name, description, and values.

To ensure accuracy and brand consistency, you can customize VTEX's automatic translations to reflect cultural nuances or specific terminology that align with your brand. This process involves following the [instructions](#instructions) provided below, using the `catalog-graphql` app, which serves as the GraphQL interface for the Catalog API.

>ℹ️ If your store uses catalog translation overrides via Messages service (`vtex.messages`), you can check if a manual translation exists by running a query in Messages GraphQL. Learn more in the section [Checking catalog message translations](https://developers.vtex.com/docs/guides/vtex-io-documentation-overwriting-the-messages-app#checking-catalog-message-translations) of the Overwriting the Messages app guide. 

## Instructions

To translate text messages from your store catalog, follow these steps:

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.
2. In the Admin VTEX, go to **Store Settings > Storefront > GraphQL IDE**.
3. From the dropdown list, choose the `vtex.catalog-graphql` app.
4. Click _Query variables_ at the bottom of the page.

![graphql-ide](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/graphql-ide.gif)

5. Based on your scenario, check the sections ([category](#category), [brand](#brand), [product](#product), [SKU](#sku), [SKU or product specification](#sku-or-product-specification), [specification values](#specification-values)) for orientations on how to complete the main text box and the _Query variables_ section.
6. After adjusting your query, click the play button to run the declared mutation. The expected response is a boolean value indicating `true`.

Below is an example of the complete process of the automatic translation of a product name:

![graphql-ide-catalog](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/graphql-ide-catalog.gif)

## Translatable settings

See how to complete the main text box and the _Query variables_ section when configuring your catalog translation.

### Category

#### Mutation

Complete the main text box with the following mutation command:

```gql
mutation translate($args:CategoryInputTranslation, $locale:Locale){
  translateCategory(category:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

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

- `id`: Category ID. Every category in your store has a unique ID, which can be found under Catalog > Categories in the VTEX Admin.
- `name`: Category name.
- `title`: Meta title for the category page.
- `description`: Detailed description of the category.
- `keywords`: Object containing the translations of **each** similar word for the category.
- `linkId`: The `textLink` (must **not** be translated unless your store is cross-border).
- `locale`: Target translation locale.

  > ℹ️ If you have a cross-border store, the `linkId` serves as the category URL slug. The [Rewriter](https://developers.vtex.com/docs/guides/rewriter) app will automatically create an alias using the translated slug for each target locale and store it in the `resolveAs` field for that locale's internal route. For example, a category with the slug `eletronics` at `http://{storename}.com/us/eletronics/d` could have the translated slug `eletronicos` for the `pt-BR` binding, as in `http://{storename}.com/br/eletronicos/d`.

### Brand

#### Mutation

Complete the main text box with the following mutation command:

```gql
mutation translate($args:BrandInputTranslation, $locale:Locale){
  translateBrand(brand:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

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

- `id`:  Brand ID. Every brand in your store has a unique ID that can be found under _Catalog > Brands_ in the VTEX Admin.
- `name`: Brand name.
- `text`: Brand description (meta tag description).
- `siteTitle`: Brand page title (tag title).
- `keywords`: Object containing the translations of **each** similar word for the brand.
- `locale`: Target translation locale.

### Product

#### Mutation

Complete the main text box with the following mutation command:

```gql
mutation translate($args:ProductInputTranslation, $locale:Locale){
  translateProduct(product:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

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

- `id`: Product ID. Every product in your store has a unique ID, which can be found under _Catalog > Products and SKUs_ in the VTEX Admin.
- `name`: Product name.
- `description`: Product description.
- `shortDescription`: Additional short description.
- `title`: Page title (tag title)
- `metaTagDescription`: Description (meta tag description).
- `keywords`: Object containing the translations of **each** similar word for the product.
- `linkId`: The `textLink` (must **not** be translated unless your store is cross-border).
- `locale`: Target translation locale.

  > ℹ️ If you have a cross-border store, the `linkId` serves as the product URL slug. The [Rewriter](https://developers.vtex.com/docs/guides/rewriter) app will automatically create an alias using the translated slug for each target locale and store it in the `resolveAs` field for that locale's internal route. For example, a product with the slug `blue-top-retro-camera` at `http://{storename}.com/us/blue-top-retro-camera/p` could have the translated slug `camera-retro-azul` for the `pt-BR` binding, as in `http://{storename}.com/br/camera-retro-azul/p`.

### SKU

#### Mutation

Complete the main text box with the following mutation command:

```
mutation translate($args:SKUInputTranslation, $locale:Locale){
  translateSKU(sku:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

```json
{
  "args":{
    "id": "46",
    "name": "Mixer Retro - Marrom"
  },
  "locale": "pt-BR" 
}
```

- `id`: SKU ID. Every product in your store has a unique ID, which can be found under _Catalog > Products and SKUs_ in the VTEX Admin.
- `name`: SKU name.
- `locale`: Target translation locale.

### SKU or product specification

#### Mutation

Complete the main text box with the following mutation command:

```gql
mutation translate($args:FieldInputTranslation, $locale:Locale){
  translateField(field:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

```json
{
  "args":{
    "fieldId": "31",
    "name": "Cor"
  },
  "locale": "pt-BR" 
}
```

- `fieldId`: The ID for a product or SKU specification. Every product or SKU specification in your store has a unique ID, which can be found following the instructions for [SKU specifications](https://help.vtex.com/docs/tutorials/adding-sku-specifications-or-fields) or [product specifications](https://help.vtex.com/docs/tutorials/adding-specifications-or-product-fields).
- `name`: Specification name.
- `locale`: Target translation locale.

### Specification values

#### Mutation

Complete the main text box with the following mutation command:

```gql
mutation translate($args:FieldValueInputTranslation, $locale:Locale){
  translateFieldValues(fieldValues:$args,locale:$locale)
}
```

#### Query variables

Complete the _Query variables_ section with the desired translations for each parameter.

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

- `fieldId`: The ID for a product or SKU specification. Every product or SKU specification in your store has a unique ID, which can be found following the instructions for [SKU specifications](https://help.vtex.com/docs/tutorials/adding-sku-specifications-or-fields) or [product specifications](https://help.vtex.com/docs/tutorials/adding-specifications-or-product-fields).
- `fieldValuesNames`: An object containing:
- `id`: Specification value ID.
- `name`: Specification value name.
- `locale`: Target translation locale.

  > You can retrieve ID values by running the following query:
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
  > Where `fieldId` is the specification ID, which you can find by following the guide [Products and SKU Specifications](https://help.vtex.com/en/docs/tracks/specifications-concept-definition).
