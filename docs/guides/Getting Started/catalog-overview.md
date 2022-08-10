---
title: "Catalog"
slug: "catalog-overview"
hidden: false
createdAt: "2021-03-26T15:35:50.014Z"
updatedAt: "2022-08-03T21:00:34.961Z"
---
[block:callout]
{
  "type": "info",
  "body": "📣 Help us improve our documentation! Share your feedback by filling out this [form](https://forms.gle/yhHFzcZ3EFRjmam49)."
}
[/block]
This overview article goes over what you can accomplish with the VTEX Catalog, including relevant links to our developer documentation about this topic.

<br>

## Setting up your catalog

One of the first steps for new stores is making an initial load of products into VTEX, whether from your ERP, back office system or other methods. See the links below for an overview of this integration flow and for detailed guides on each step of the process.


### Overview of the integration flow

The links below provide a general view of the integration flow between a back office system and a VTEX store’s Catalog.

* [Back office (ERP/PIM/WMS)](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-guide)
* [Set up catalog](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-catalog)
* [Import products](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-products)
* [Updating / deleting information](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-updating-and-deleting-information)
* [Catalog](https://developers.vtex.com/vtex-rest-api/docs/catalog-integration)
* [Catalog API - Overview](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-overview)


### Step-by-step guides

See the links below for details on each step and API call during the process of loading products into your VTEX Catalog. All these steps are required and should be performed in the order below, whether you are connecting to VTEX through an external system or not.


#### Categories

Categories organize your product assortment by working as hierarchical levels of product classification. The organization by category makes a customer’s search for a product easier and keeps your catalog organized. The three main category levels are called Department, Category, and Subcategory.

* [Categories](https://developers.vtex.com/vtex-rest-api/docs/categories)
* [Create a category](https://developers.vtex.com/vtex-rest-api/docs/create-a-category)
* [Catalog API - Category](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-category-tree)


#### Brands

A brand is an attribute that helps your end customers to identify a product and the business behind it.

* [Brands](https://developers.vtex.com/vtex-rest-api/docs/brands)
* [Catalog API - Brand](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list)


#### Products

A product is a generic definition of something that is available for purchase in your store, such as a shirt.

* [Products](https://developers.vtex.com/vtex-rest-api/docs/products)
* [Catalog API - Product](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-products-skus)
* [Alternative API requests](https://developers.vtex.com/vtex-rest-api/docs/alternative-api-requests)
* [How to implement product color variation](https://developers.vtex.com/vtex-rest-api/docs/how-to-implement-product-color-variation)


#### SKUs

SKU stands for Stock Keeping Unit, which represents the physical unit of the product, that is, each variation of the product, such as a blue medium shirt. SKUs are the items that stores keep in stock and that end customers actually buy.

* [SKUs](https://developers.vtex.com/vtex-rest-api/docs/skus)
* [Catalog API - SKU](https://developers.vtex.com/vtex-rest-api/reference/listallskuids)


#### Specifications

Specifications are additional properties that can be included in your store's products or SKUs. At VTEX, these specifications are associated with categories and are called fields.

* [Specifications](https://developers.vtex.com/vtex-rest-api/docs/specifications)
* [How to create a specification](https://developers.vtex.com/vtex-rest-api/docs/how-to-create-a-specification)
* [Catalog API - Specification Group](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-group-categoryid)
* [Catalog API - Specification](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-specification-specificationid)
* [Product specifications](https://developers.vtex.com/vtex-rest-api/docs/product-specifications)
* [Catalog API - Product Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-product-specification)
* [SKU specifications](https://developers.vtex.com/vtex-rest-api/docs/sku-specifications)
* [Catalog API - SKU Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-specification)

<br>

## Enriching your catalog

After an initial load of products, you must enrich them with the required information before selling them. See the links below for more details.


### Filling in specifications

It is necessary to fill in the specifications for each product and SKU, according to the fields and values you have created.

* [Updating SKU Specifications with Catalog API](https://developers.vtex.com/vtex-rest-api/docs/updating-sku-specifications-with-catalog-api)
* [Catalog API - Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id)


### Adding images to SKUs

Every SKU needs at least one image to be active in your store.

* [Images](https://developers.vtex.com/vtex-rest-api/docs/images)
* [Catalog API - SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file)


### Activating SKUs

* [How to activate an SKU](https://developers.vtex.com/vtex-rest-api/docs/how-to-activate-an-sku)

<br>

## Adding optional configurations

Once you have all the required information, there are optional settings you can make to enhance your Catalog. See the following links for more information.


### Adding attachments

An attachment is the optional and cost-free customization of a product. It's used to add information to an SKU.

* [Catalog API - Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-attachment)
* [Catalog API - SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment)


### Setting up assembly options

An assembly option is an attachment for complex scenarios, such as product customization, in which you need to manage different product combinations, quantity, additional items, costs, and product inventory management and display these options in the product page.

* [Assembly Options app](https://developers.vtex.com/vtex-developer-docs/docs/assembly-options-app)


### Adding services

A service is an item that may come with a product, optionally and with cost. It is used to assign an additional service to an SKU, such as gift packaging, customization or special warranty deals.

* [Catalog API - SKU Service](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-sku-service)
* [Catalog API - SKU Service Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-service-attachment)
* [Catalog API - SKU Service Type](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-service-type)
* [Catalog API - SKU Service Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-service-value)


### Creating kits

A kit is a set of SKUs that are sold together, that is, an SKU composed of one or more SKUs.

* [Catalog API - SKU Kit](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-kit)


### Creating collections

A collection is a group of two or more SKUs that may or may not have common features to be displayed on your store's product pages. You can create collections using grouping criteria such as commemorative dates, launches, or best-selling products. It is possible to create collections using either [Legacy CMS Portal](#legacy-cms-portal) or [Collection Beta](#collection-beta).


#### Legacy CMS Portal

* [Catalog API - Collection](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-collection)
* [Catalog API - Subcollection](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid)
* [Catalog API - Category Subcollection](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-subcollection-category)
* [Catalog API - Brand Subcollection](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-subcollection-brand)
* [Catalog API - SKU Subcollection](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-sku)


#### Collection Beta

* [Catalog API - Collection Beta](https://developers.vtex.com/vtex-rest-api/reference/get-allcollections)


### Associating products and SKUs to trade policies

When operating with multiple [trade policies](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV), you can define which products will be available on each trade policy.

* [Catalog API - Trade Policy](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-trade-policy)


### Integrating your catalog with an external marketplace 

If you are an [external marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide) that wishes to integrate with VTEX sellers, you can see the links below to learn how to develop a custom connector to connect with VTEX's architecture and sellers’ catalogs.

* [Catalog Integration](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-catalog)
* [Catalog logs](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-logs)
* [Get product list for an initial load](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-load)
* [How to get a new product to offer in the marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-new-products)
* [How to get product updates](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-product-updates)
* [Product and Category Mappings](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-catalog-mapping)


### Integrating an external seller’s catalog

See the links below to understand how to integrate an [external seller](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-guide)’s offers into your catalog if you act as a VTEX marketplace.

* [Catalog management for VTEX Marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-vtex-marketplace-operation)


### Optimizing the storefront to display your catalog

Read the following documentation to understand how to build your storefront and showcase your assortment of products.

* [Building a horizontal Product Summary](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-horizontal-product-summary)
* [Building a Product Details Page](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-product-details-page)
* [Building a Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-shelf)
* [Configuring custom images for the SKU Selector](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-configuring-custom-images-for-the-sku-selector)
* [Creating a product availability form](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-product-availability-form)
* [Rendering a badge on top of a product](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-rendering-a-badge)
* [Translating Catalog content](https://developers.vtex.com/vtex-developer-docs/docs/catalog-internationalization)