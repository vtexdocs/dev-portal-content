---
title: "Catalog multi-language integration guide"
slug: "catalog-multi-language-integration-guide"
hidden: false
excerpt: "Manage multiple languages for catalog entities."
createdAt: "2026-01-13T00:00:00.000Z"
updatedAt: "2026-01-13T00:00:00.000Z"
---

> ℹ️ This feature is in beta, which means that we are working to improve it. If you have any questions, please contact our [Support](https://support.vtex.com/hc/en-us/requests).

Learn how to integrate localized catalog content using the multi-language endpoints, and create translations for catalog entities.

## Overview

The [multi-language endpoints](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/language) enable you to:

- **Granular content management:** Retrieve and store translations for products, SKUs, categories, brands, specifications, collections, and services.
- **Automated translation workflows:** Integrate with Translation Management Systems (TMS) for automated translation.
- **Multiple storefront technologies:** Consume translations across different storefront implementations, such as Store Framework, FastStore, and headless implementations.
- **Localized experience:** Provide to customers localized shopping experiences across multiple markets.

### Locale format

All locale codes follow the IETF BCP 47 standard, for example:

- `en-US`: English (United States)
- `es-ES`: Spanish (Spain)
- `pt-BR`: Portuguese (Brazil)
- `fr-FR`: French (France)
- `de-DE`: German (Germany)

## Use cases

The multi-language feature supports various integration scenarios:

| Use case | Description |
| :--- | :--- |
| Multilingual storefront | Displays translated product names, descriptions, and specifications based on the customer's locale identified by the storefront. |
| TMS integration | Connects your Translation Management System (TMS) to automatically push and pull translations via the [Catalog API](https://developers.vtex.com/docs/api-reference/catalog-api#overview). |
| Market expansion | Seamlessly adapts your catalog for new geographic markets without duplicating products. |
| SEO optimization | Provides localized meta descriptions, keywords, and URL slugs for better search engine rankings in each market. |
| Headless commerce | Fetches translated catalog data directly for custom frontend applications. |

## Activation

Open a [support ticket](https://help.vtex.com/en/support) requesting the activation of the Catalog multi-language feature for your account. Once the VTEX team activates it, they will contact you to inform that you can start using the feature.

>❗ The simultaneous use of both the multi-Language APIs and Messages APIs (GraphQL) is not supported for catalog entities. Therefore, once the new feature is activated, you will no longer be able to manage translations using GraphQL.

## Permissions

To successfully use the multi-language feature, the user or [API key](https://developers.vtex.com/docs/guides/authentication-overview#api-keys) must have the [License Manager resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) below, otherwise they will receive a 403 error:

| Product | Category | Resource |
| :--- | :--- | :--- |
| Catalog | Content | Categories Management |

## Translation flow: from API to storefront

When you send translated content to the Catalog via the Multi-Language API, the data flows through a complete pipeline:

```mermaid
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  1. API Ingestion   │────▶│  2. Search Indexing │────▶│  3. Storefront      │
│                     │     │                     │     │     Display         │
│  PUT /language      │     │  Intelligent Search │     │  Automatic locale   │
│  endpoints          │     │  reindexes content  │     │  rendering          │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
```

### Step 1: Catalog translation ingestion

The merchant or an integrated TMS sends translations using the `PUT /language` endpoints, specifying the entity (product, SKU, category, brand, or collection) and the target locale.

The Catalog validates and stores the translated fields per locale, then emits an update event to downstream services.

### Step 2: Intelligent Search indexing

Intelligent Search receives the update event from the Catalog and reindexes the affected entities to make translated content searchable and filterable in that locale.

The indexing process runs asynchronously and typically completes within a few minutes.

### Step 3: Storefront consumption and display

Storefront solutions (Store Framework, FastStore, Checkout, and headless implementations) query Intelligent Search or Catalog at render time, automatically retrieving and displaying the translated content for the shopper's selected locale.

No manual configuration or synchronization is required—translations flow seamlessly from API ingestion to storefront display.

## Creating localized content

Use the `PUT` endpoints to create or update translations for catalog entities. The following sections provide examples for each entity type.

### Translating a product

Create or update language-specific information for a product:

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/product/{productId}/language`

**Request body:**

```json
{
  "Locale": "es-ES",
  "Name": "Camiseta Premium de Algodón",
  "Description": "Camiseta de alta calidad hecha de 100% algodón orgánico",
  "Title": "Camiseta Premium | Tu Tienda",
  "MetaTagDescription": "Compra nuestra camiseta premium de algodón orgánico",
  "DescriptionShort": "Camiseta de algodón orgánico premium",
  "Keywords": "camiseta, algodón, orgánico, premium",
  "LinkId": "camiseta-premium-algodon"
}
```

**cURL example:**

```bash
curl -X PUT "https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/product/123/language" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}" \
  -d '{
    "Locale": "es-ES",
    "Name": "Camiseta Premium de Algodón",
    "Description": "Camiseta de alta calidad hecha de 100% algodón orgánico",
    "Title": "Camiseta Premium | Tu Tienda",
    "MetaTagDescription": "Compra nuestra camiseta premium de algodón orgánico",
    "DescriptionShort": "Camiseta de algodón orgánico premium",
    "Keywords": "camiseta, algodón, orgánico, premium",
    "LinkId": "camiseta-premium-algodon"
  }'
```

### Translating a product specification

Create or update translations for product specifications (e.g., material, size):

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/products/{productId}/specification/{specificationId}/language`

**Request body:**

```json
{
  "ProductId": 123,
  "SpecificationId": 45,
  "Locale": "pt-BR",
  "Name": "Material",
  "Value": "100% Algodão",
  "Values": null
}
```

>ℹ️ Use the `Value` field for text-type specifications. Use the `Values` array for combo, radio, and checkbox specification types.

### Translating a SKU

Create or update language-specific information for a SKU:

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/stockkeepingunit/{skuId}/language`

**Request body:**

```json
{
  "Locale": "fr-FR",
  "Name": "T-shirt Premium - Bleu Marine - M",
  "MeasurementUnit": "un"
}
```

### Translating a category

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/category/{categoryId}/language`

**Request body:**

```json
{
  "Locale": "de-DE",
  "Name": "Herrenbekleidung",
  "Title": "Herrenbekleidung | Modeshop",
  "Description": "Entdecken Sie unsere Kollektion an Herrenbekleidung",
  "Keywords": "herren, bekleidung, mode, kleidung",
  "LinkId": "herrenbekleidung"
}
```

### Translating a brand

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/brand/{brandId}/language`

**Request body:**

```json
{
  "Locale": "it-IT",
  "Name": "Abbigliamento Premium",
  "Text": "Produttore leader di abbigliamento di qualità",
  "Keywords": "premium, abbigliamento, qualità, marca",
  "SiteTitle": "Abbigliamento Premium | Qualità Italiana",
  "LinkId": "abbigliamento-premium"
}
```

### Translating a collection

**Endpoint:** `PUT https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/collection/{collectionId}/language`

**Request body:**

```json
{
  "Locale": "en-US",
  "Name": "Summer Collection 2025",
  "Description": "Discover our latest summer styles and trends",
  "LinkId": "summer-collection-2025"
}
```

## Consuming localized content

There are two main approaches to consuming translated catalog data, depending on your storefront implementation.

### Option 1: Via Intelligent Search (recommended)

For most storefront implementations, **Intelligent Search is the recommended approach** for consuming translated content. When using Intelligent Search:

- Translations are automatically indexed after being saved via the Multi-Language API.
- Search results, filters, and facets display translated content based on the shopper's locale.
- No additional API calls are required—the storefront receives translated data transparently.

**When to use Intelligent Search:**

| Implementation | Use Intelligent Search? |
| --- | --- |
| Store Framework | ✅ Yes (default behavior) |
| FastStore | ✅ Yes (default behavior) |
| Headless with IS | ✅ Yes |
| Legacy CMS | ⚠️ May require additional configuration |

### Option 2: Via Catalog API (direct fetch)

For headless implementations or specific use cases where you need direct access to catalog data with translations, use the Catalog API with the `Accept-Language` header.

**Endpoint:** `GET https://{accountName}.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId}`

**Required header:**

| Header | Description | Example |
| --- | --- | --- |
| `Accept-Language` | The locale to filter by. | `en-US`, `pt-BR`, `es-ES` |

**cURL example:**

```bash
curl -X GET "https://{accountName}.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/456" \
  -H "Accept: application/json" \
  -H "Accept-Language: en-US" \
  -H "Content-Type: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}"
```

### Retrieving all translations for an entity

To retrieve all available translations for an entity, use the `GET` endpoints without the `locale` query parameter:

**Endpoint:** `GET https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/product/{productId}/language`

**Response example:**

```json
[
  {
    "Id": 123,
    "Locale": "en-US",
    "Name": "Premium Cotton T-Shirt",
    "Description": "High-quality t-shirt made from 100% organic cotton",
    "Title": "Premium T-Shirt | Your Store",
    "MetaTagDescription": "Shop our premium organic cotton t-shirt",
    "DescriptionShort": "Premium organic cotton t-shirt",
    "Keywords": "tshirt, cotton, organic, premium",
    "LinkId": "premium-cotton-tshirt",
    "Category": {
      "Id": 12,
      "Locale": "en-US",
      "Name": "Men's Clothing"
    },
    "Brand": {
      "Id": 1,
      "Locale": "en-US",
      "Name": "Premium Apparel Co."
    }
  },
  {
    "Id": 123,
    "Locale": "es-ES",
    "Name": "Camiseta Premium de Algodón",
    "Description": "Camiseta de alta calidad hecha de 100% algodón orgánico",
    "Title": "Camiseta Premium | Tu Tienda",
    "MetaTagDescription": "Compra nuestra camiseta premium de algodón orgánico",
    "DescriptionShort": "Camiseta de algodón orgánico premium",
    "Keywords": "camiseta, algodón, orgánico, premium",
    "LinkId": "camiseta-premium-algodon",
    "Category": {
      "Id": 12,
      "Locale": "es-ES",
      "Name": "Ropa de Hombre"
    },
    "Brand": {
      "Id": 1,
      "Locale": "es-ES",
      "Name": "Premium Apparel Co."
    }
  }
]
```

### Retrieving a specific locale translation

To retrieve translation for a specific locale, add the `locale` query parameter:

**Endpoint:** `GET https://{accountName}.vtexcommercestable.com.br/api/catalog/pvt/product/{productId}/language?locale=es-ES`

## Implementation by storefront type

### Store Framework implementation

For stores built with [Store Framework](https://developers.vtex.com/docs/guides/store-framework), localized content is consumed automatically:

1. **Locale detection:** The store detects the shopper's locale from the URL binding (e.g., `store.com/es-ES/`) or browser settings.
2. **Automatic translation:** Intelligent Search returns translated content for the detected locale.
3. **Component rendering:** Store Framework components (product shelf, product details, search results) display the translated content without additional configuration.

**No code changes required.** Once you submit translations via the Multi-Language API, they appear automatically in your Store Framework storefront.

### FastStore implementation

[FastStore](https://developers.vtex.com/docs/guides/faststore) implementations also benefit from automatic translation handling:

1. Configure your store's supported locales in the FastStore configuration.
2. Submit translations via the Multi-Language API.
3. FastStore fetches translated content from Intelligent Search based on the active locale.

### Headless implementation

For headless storefronts, you have two options for consuming translated content:

#### Option A: Use Intelligent Search API

Query Intelligent Search with the desired locale to receive translated results:

```bash
curl -X GET "https://{accountName}.vtexcommercestable.com.br/api/io/_v/api/intelligent-search/product_search?locale=es-ES&query=camiseta" \
  -H "Accept: application/json"
```

**Advantages:**

- Full search functionality (filters, facets, relevance)
- Cached and optimized for performance
- Consistent with other storefront implementations

#### Option B: Use Catalog API directly

Query the Catalog API with the `Accept-Language` header:

```bash
curl -X GET "https://{accountName}.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitbyid/456" \
  -H "Accept-Language: es-ES" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}"
```

**When to use direct Catalog API:**

- You need specific entity translations not available in search results.
- You're building admin tools or back-office integrations.
- You need to fetch translations for validation or synchronization.

## API reference

### Product translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/product/{productId}/language` | Retrieve product translations |
| `PUT` | `/api/catalog/pvt/product/{productId}/language` | Create or update product translation |
| `GET` | `/api/catalog/pvt/products/{productId}/specification/{specificationId}/language` | Retrieve product specification translations |
| `PUT` | `/api/catalog/pvt/products/{productId}/specification/{specificationId}/language` | Create or update product specification translation |

### SKU translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/stockkeepingunit/{skuId}/language` | Retrieve SKU translations |
| `PUT` | `/api/catalog/pvt/stockkeepingunit/{skuId}/language` | Create or update SKU translation |
| `GET` | `/api/catalog/pvt/stockkeepingunit/{skuId}/attribute/{skuAttributeId}/language` | Retrieve SKU attribute translations |
| `PUT` | `/api/catalog/pvt/stockkeepingunit/{skuId}/attribute/{skuAttributeId}/language` | Create or update SKU attribute translation |
| `GET` | `/api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId}/language` | Retrieve SKU file/image translations |
| `PUT` | `/api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId}/language` | Create or update SKU file/image translation |

### Specification translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/specificationgroup/{groupId}/language` | Retrieve specification group translations |
| `PUT` | `/api/catalog/pvt/specificationgroup/{groupId}/language` | Create or update specification group translation |
| `GET` | `/api/catalog/pvt/specification/{specificationId}/language` | Retrieve specification translations |
| `PUT` | `/api/catalog/pvt/specification/{specificationId}/language` | Create or update specification translation |
| `GET` | `/api/catalog/pvt/specificationvalue/{valueId}/language` | Retrieve specification value translations |
| `PUT` | `/api/catalog/pvt/specificationvalue/{valueId}/language` | Create or update specification value translation |

### Category translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/category/{categoryId}/language` | Retrieve category translations |
| `PUT` | `/api/catalog/pvt/category/{categoryId}/language` | Create or update category translation |

### Brand translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/brand/{brandId}/language` | Retrieve brand translations |
| `PUT` | `/api/catalog/pvt/brand/{brandId}/language` | Create or update brand translation |

### Attachment and service translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/attachment/{attachmentId}/language` | Retrieve attachment translations |
| `PUT` | `/api/catalog/pvt/attachment/{attachmentId}/language` | Create or update attachment translation |
| `GET` | `/api/catalog/pvt/skuservicetype/{skuServiceTypeId}/language` | Retrieve SKU service type translations |
| `PUT` | `/api/catalog/pvt/skuservicetype/{skuServiceTypeId}/language` | Create or update SKU service type translation |
| `GET` | `/api/catalog/pvt/skuservice/{skuServiceId}/language` | Retrieve SKU service translations |
| `PUT` | `/api/catalog/pvt/skuservice/{skuServiceId}/language` | Create or update SKU service translation |
| `GET` | `/api/catalog/pvt/skuservicevalue/{skuServiceValueId}/language` | Retrieve SKU service value translations |
| `PUT` | `/api/catalog/pvt/skuservicevalue/{skuServiceValueId}/language` | Create or update SKU service value translation |

### Collection translations

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/catalog/pvt/collection/{collectionId}/language` | Retrieve collection translations |
| `PUT` | `/api/catalog/pvt/collection/{collectionId}/language` | Create or update collection translation |

## Best practices

### Translation workflow

1. **Start with high-impact entities:** Prioritize translating products, categories, and brands before moving to specifications and attachments.
2. **Batch translations:** When integrating with a TMS, batch multiple translation updates to reduce API calls.
3. **Validate before publishing:** Use the `GET` endpoints to verify translations before they go live.

### Handling missing translations

When a translation is not available for a requested locale:

- **Intelligent Search:** Returns content in the store's default language.
- **Catalog API:** Returns only entities that have translations in the requested locale.

Consider implementing fallback logic in headless implementations to handle missing translations gracefully.

### Performance considerations

- **Cache translations:** For headless implementations, cache translated content to reduce API calls.
- **Use Intelligent Search:** Whenever possible, prefer Intelligent Search over direct Catalog API calls for better performance and caching.
- **Monitor indexing:** After bulk translation updates, allow a few minutes for Intelligent Search to reindex before validating changes on the storefront.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| Translations not appearing on storefront | Wait a few minutes for Intelligent Search to reindex. Check that the locale matches your store binding configuration. |
| `403 Forbidden` error | Verify that your application key has the `Categories Management` resource enabled. |
| `404 Not Found` error | Confirm that the entity ID (product, SKU, category, etc.) exists in the Catalog. |
| `409 Conflict` error | The translation may already exist. Use `GET` to retrieve current translations before updating. |

## Related resources

- [Catalog API reference](https://developers.vtex.com/docs/api-reference/catalog-api)
- [VTEX Intelligent Search: Multilanguage settings (Beta)](/en/tutorials/beta/intelligent-search-beta/vtex-intelligent-search-multilanguage-settings-beta)
- [API authentication using application keys](https://developers.vtex.com/docs/guides/api-authentication-using-application-keys)
- [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3)
