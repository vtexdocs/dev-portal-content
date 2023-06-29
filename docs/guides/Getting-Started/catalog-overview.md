---
title: "Catalog"
slug: "catalog-overview"
hidden: false
createdAt: "2021-03-26t15:35:50.014z"
updatedAt: "2022-09-27t21:01:32.508z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by filling out [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

Catalog is your store's administration module for configuring the features related to your ecommerce products to make them available for customers on your website. This overview article goes over what you can accomplish with the VTEX Catalog, including relevant links to our developer documentation about this topic.

## Understanding Catalog architecture

On VTEX, [Categories](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf) are the way products are organized, generically dividing items available in your store. Usually, they have three levels: department, category, and subcategory.

Each [product](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru) is associated with a category and a [brand](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh), and has at least one [Stock Keeping Unit (SKU)](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA), which corresponds to each product variation – each physical unit in stock.

Categories are associated with [specification](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP) groups, which group the product and SKU specifications that will be applied to all items associated with the category. All specifications must be completed for items to be active in your store.

![VTEX Catalog architecture](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/d54af4780304904cfb383ed60497ac3f200db383/docs/guides/Getting%20Started/catalog-architecture.png)

## Setting up your catalog

One of the first steps for new stores is to upload products to VTEX, whether from your ERP, back-office system, or other sources. See the links below for an overview of the integration flow and detailed guides about each step of the process. 

### Integration flow

These links provide a general overview of the steps in the integration flow between a back office system and a VTEX store catalog.

1.  [Back office (ERP/PIM/WMS)](https://developers.vtex.com/docs/guides/erp-integration-guide)
2.  [Setting up the catalog](https://developers.vtex.com/docs/guides/erp-integration-set-up-catalog)
3.  [Importing products](https://developers.vtex.com/docs/guides/erp-integration-import-products)
4.  [Updating / deleting information](https://developers.vtex.com/docs/guides/erp-integration-updating-and-deleting-information)
5.  [Catalog](https://developers.vtex.com/docs/guides/catalog-integration)
6.  [Catalog API - Overview](https://developers.vtex.com/docs/api-reference/catalog-api#overview)

> Looking for storefront Catalog content? Read our [Customizing your storefront](#customizing-your-storefront) guides.

### Configuring initial settings (MANDATORY)

Access the following links to see details about each step and API call while uploading products to your VTEX Catalog. All these steps are **required** and must be completed in the order below, regardless of whether you are connecting to VTEX through an external system.

#### 1. Categories

Categories arrange your product assortment in hierarchical levels of product classification. The category system makes a customer search for a product easier and keeps your catalog organized. The three main category levels are called department, category, and subcategory.

*   [Categories](https://developers.vtex.com/docs/guides/categories)
*   [Catalog API - Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-)

#### 2. Brands

A brand is an attribute that helps your end customers identify a product and the company behind it.

*   [Brands](https://developers.vtex.com/docs/guides/brands)
*   [Catalog API - Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list)

#### 3. Specifications

Specifications are additional properties that can be added to your store products or SKUs. On VTEX, you must first create a specification group linked to a category and then include the desired specification fields that will be replicated in all products or SKUs in the category.

When a group is created in a department or a category, it will be replicated in all the sublevels of that department or category, following an "inheritance" logic. Therefore, to create a specification group applicable to one category only, you must create it at that category level.

*   [Specifications](https://developers.vtex.com/docs/guides/specifications)
*   [Catalog API - Specification group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-)
*   [Catalog API - Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-)
*   [Product specifications](https://developers.vtex.com/docs/guides/product-specifications)
*   [Catalog API - Product specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification)
*   [SKU specifications](https://developers.vtex.com/docs/guides/sku-specifications)
*   [Catalog API - SKU specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)

#### 4. Products

A product is a generic definition of an item available in your store, such as a shirt.

*   [Products](https://developers.vtex.com/docs/guides/products)
*   [Catalog API - Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds)
*   [Alternative API requests](https://developers.vtex.com/docs/guides/alternative-api-requests)
*   [Implementing product color variation](https://developers.vtex.com/docs/guides/how-to-implement-product-color-variation)

#### 5. SKUs

A SKU, short for "stock keeping unit", represents a physical unit or variation of a product, such as a medium blue shirt. SKUs are the items that stores keep in stock and that end customers actually buy.

*   [SKUs](https://developers.vtex.com/docs/guides/skus)
*   [Catalog API - SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids)

### Enriching your catalog (MANDATORY)

After the initial product upload, you must enrich them with the required information before selling them. The steps below are **required** for any product to be available in your store. See the following points for more details.

#### 6. Completing specifications

You need to complete the specifications of each product and SKU based on the fields and values you have created.

*   [Updating SKU specifications with the Catalog API](https://developers.vtex.com/docs/guides/updating-sku-specifications-with-catalog-api)
*   [Catalog API - Specification value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-)

#### 7. Adding images to SKUs

Every SKU needs at least one image to be active in your store.

*   [Images](https://developers.vtex.com/docs/guides/images)
*   [Catalog API - SKU file](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file)

#### 8. Activating SKUs

Read the following guide to understand how to activate SKUs and make them available in your store.

*   [How to activate a SKU](https://developers.vtex.com/docs/guides/skus#activating-an-sku)

### Adding optional settings

Once you have all the required information, there are optional settings you can configure to enhance your catalog. See the following links for more information.

#### Attachments

An attachment is an optional and free product customization. It is used to add information to a SKU.

*   [Catalog API - Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-)
*   [Catalog API - SKU attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment)

#### Assembly options

An assembly option is an attachment for complex cases, such as product customization, where you need to manage different product combinations, quantity, additional items, costs, and product inventory and display these options on the product page.

*   [Assembly options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH)
*   [Assembly Options app](https://developers.vtex.com/docs/guides/assembly-options-app)

#### Services

A service is an extra that may come with a product, optionally and at a cost. It is used to assign an additional service to a SKU, such as gift packaging, customization, or special warranty deals.

*   [Catalog API - SKU service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-)
*   [Catalog API - SKU service attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment)
*   [Catalog API - SKU service type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype)
*   [Catalog API - SKU service value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue)

#### Kits

A kit is a set of SKUs that are sold together, a SKU composed of one or more SKUs.

*   [Catalog API - SKU kit](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-kit)

#### Collections

A collection is a group of two or more SKUs that may or may not have common features to be displayed on your store product pages. You can create collections using grouping criteria such as special dates, launches, or best-selling products. You can create collections using either Legacy CMS Portal or Collections beta.

**Legacy CMS Portal**

*   [Catalog API - Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-)
*   [Catalog API - Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-/subcollection)
*   [Catalog API - Category subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/category)
*   [Catalog API - Brand subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/brand)
*   [Catalog API - SKU subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit)

**Collections Beta**

*   [Catalog API - Collections beta](https://developers.vtex.com/docs/api-reference/catalog-api/#get-/api/catalog_system/pvt/collection/search)

#### Trade policies (sales channels)

When operating with multiple trade policies, you can define which products will be available on each trade policy.

*   [How trade policies work](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)
*   [Catalog API - Trade policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy)

## Customizing your storefront

To understand how to build your storefront and display your product assortment, read the articles in this section. The rest of this guide focuses on Admin related settings and actions.

### VTEX IO

Learn how to build Catalog related pages in your storefront using VTEX IO.

*   [Building a horizontal product summary](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-horizontal-product-summary)
*   [Building a product details page](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-product-details-page)
*   [Building a shelf](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-shelf)
*   [Configuring custom images for the SKU selector](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-custom-images-for-the-sku-selector)
*   [Creating a product availability form](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-product-availability-form)
*   [Rendering a badge on top of a product](https://developers.vtex.com/docs/guides/vtex-io-documentation-rendering-a-badge)
*   [Translating Catalog content](https://developers.vtex.com/docs/guides/catalog-internationalization)

Find more information in our [Storefront implementation guides](https://developers.vtex.com/docs/guides/storefront-implementation).

## Integrating with external marketplaces or sellers

Learn more about integrating with non-VTEX marketplaces or sellers through the following documentation.

### External Marketplace

If you are an external marketplace that wishes to integrate with VTEX sellers, you can see the links below to learn how to develop a custom connector to connect with VTEX's architecture and sellers' catalogs.

*   [External Marketplace Integration Guide](https://developers.vtex.com/docs/guides/external-marketplace-integration-guide)
*   [Catalog Integration](https://developers.vtex.com/docs/guides/external-marketplace-integration-catalog)
*   [Catalog logs](https://developers.vtex.com/docs/guides/external-marketplace-integration-logs)
*   [Get product list for an initial load](https://developers.vtex.com/docs/guides/external-marketplace-integration-product-load)
*   [How to get a new product to offer in the marketplace](https://developers.vtex.com/docs/guides/external-marketplace-integration-new-products)
*   [How to get product updates](https://developers.vtex.com/docs/guides/external-marketplace-integration-product-updates)
*   [Product and Category Mappings](https://developers.vtex.com/docs/guides/external-marketplace-integration-catalog-mapping)

### External Seller

See the documentation below to understand how to integrate an external seller’s offers into your catalog if you act as a VTEX marketplace.

*   [External Seller Integration Guide](https://developers.vtex.com/docs/guides/external-seller-integration-guide)
*   [Catalog management for VTEX Marketplace](https://developers.vtex.com/docs/guides/external-seller-integration-vtex-marketplace-operation)
