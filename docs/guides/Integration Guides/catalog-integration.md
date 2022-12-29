---
title: "Catalog"
slug: "catalog-integration"
hidden: false
createdAt: "2021-12-06T20:34:13.795Z"
updatedAt: "2022-11-22T17:07:53.138Z"
---

VTEX Catalog architecture is based on five fundamental concepts:

- [Category](https://developers.vtex.com/vtex-rest-api/docs/categories)
- [Brand](https://developers.vtex.com/vtex-rest-api/docs/brands)
- [Product](https://developers.vtex.com/vtex-rest-api/docs/products)
- [SKU](https://developers.vtex.com/vtex-rest-api/docs/skus)
- [Specification](https://developers.vtex.com/vtex-rest-api/docs/specifications) ([product](https://developers.vtex.com/vtex-rest-api/docs/product-specifications) and [SKU](https://developers.vtex.com/vtex-rest-api/docs/sku-specifications) attributes)

Before uploading your entire catalog to VTEX it is very important to think carefully about your desired catalog structure. The way you structure your catalog and product specifications can have a great impact on site navigation, order integration and other aspects of your store.

In VTEX, the category tree is the backbone of the Catalog. Categories represent the way you organize your products so that the user can easily find the desired products.

When organized into categories, products can be classified hierarchically. Usually in up to three levels: department, category, and subcategory.

VTEX Intelligent Search doesn't have a limit of category levels. Category works as an attribute. On the other hand, running under Classic CMS, we strongly suggest using a maximum of three levels.

For a product to be made available in your store, it must:

- Be part of a brand, a category.
- Have at least one active SKU.

**Brands** are also an important aspect to consider, as it is very common for clients to search for products using them as a keyword. When brands are associated with products, you can use them as filters in your store navigation.

VTEX Catalog structure requires that an SKU can only be created after defining product information since the SKU itself is the product variation. Therefore, we can say that an SKU is the physical unit of a product in stock.

VTEX Catalog architecture also includes specifications, which are a category’s registered properties that attribute specific characteristics to products and SKUs linked to it.

Such specifications are, for example, SKU voltage, size, or color.

An example of a VTEX Catalog architecture blueprint is found below:
![VTEX Catalog architecture example](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/catalog-integration-0.png)

## Integration flow

Catalog integration must follow a specific workflow. The registers are related to each other, so following the correct order below is crucial:

1. Department and Categories
2. Specifications Fields
3. Brand
4. Products
5. SKUs
6. Product/SKU Specifications

## Registering products

VTEX provides three different ways to register products to a catalog:

1. **API Integration:** the collection with all methods can be found at the following link: [Catalog API Overview](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-overview).
2. **Spreadsheets:** there are two possible ways to import a spreadsheet with your  Catalog information.  They are:
   a. **Google Drive Import:** import the Catalog from a single Google Drive file. See the [google-import app details](https://github.com/vtex-apps/google-import)
   b. **Classic Method:** import the Catalog using multiple files (product, SKU, specification, image)
3. **Manual input:** [Catalog data is loaded manually into VTEX Admin panel](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1ROhz3Y7mfSMmCO1I1GxEL), by filling out each field.

In order to import your products, it is possible that you have to use more than one method, depending on how the data is structured and what types of software are used in your operation.
