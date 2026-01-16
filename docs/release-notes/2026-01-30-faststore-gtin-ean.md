---  
title: "FastStore: Improved SEO and data reliability with EAN-based GTIN in product structured data"   
slug: "2026-01-30-faststore-gtin-ean"   
type: "fixed"   
createdAt: "2026-01-16T00:00:00.000Z"   
updatedAt: ""   
excerpt: "FastStore now accurately populates the Global Trade Item Number (GTIN) field in product structured data using the European Article Number (EAN), leading to improved SEO compliance and data reliability."  
tags:  
    - FastStore
---

FastStore has improved how the Global Trade Item Number (GTIN) field is populated in product structured data. This update ensures that product pages display standardized product identifiers, helping search engines better index your products and potentially qualify for rich results in Google Search.

## What has changed?

Previously, the GTIN field in product structured data was populated using the product's Reference code from [the Catalog](https://help.vtex.com/docs/tutorials/adding-or-editing-skus#identifiers). With this update, FastStore now prioritizes the European Article Number (EAN) for the GTIN field whenever an EAN value is available. If no EAN exists, the system falls back to using the Reference code.

![ean-and-reference-code-admin](https://vtexhelp.vtexassets.com/assets/docs/src/image1-ean___3314df0c0e9088ddb97cf770b7d75847.gif)

This change affects the [JSON-LD structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) on the product pages, which search engines use to understand and display product information.

## Why did we make this change?

The previous implementation didn't use the standardized EAN code for GTIN, which could affect:  
**SEO performance**: Search engines prefer standardized product identifiers.  
**Product discoverability**: Accurate GTINs help search engines match products across sources.  
**Rich results eligibility**: Google requires valid GTINs for [product rich results](https://developers.google.com/search/docs/appearance/structured-data/product).

Using EAN values makes your product structured data more accurate and compliant with search engine requirements.

## What needs to be done?

No migration is required. This update is automatically applied to all FastStore projects.

> ⚠️ If you rely on custom logic or integrations for structured data, review your storefront implementation to ensure EAN values are correctly populated for SKUs where GTIN is critical.

To confirm that the GTIN field is using EAN values correctly, follow these steps:

1. Open a product page in your store.  
2. Right-click on the page and select **Inspect** (or press `F12`).  
3. In the **Elements** tab, press `Ctrl+F` (or `Cmd+F` on Mac) and search for `"gtin"`.  
4. Verify the value matches the EAN configured in your [Catalog](https://help.vtex.com/en/docs/tutorials/adding-or-editing-skus#identifiers).

The structured data should look like this:

![gtin-field](https://vtexhelp.vtexassets.com/assets/docs/src/image2-gtin___11bcb80e6f143229a4fe3c13b42c5f89.png)

> ⚠️ Products without EAN will fall back to using the Reference code. You can create an EAN for a SKU by following the [Create SKU EAN API reference](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-).
