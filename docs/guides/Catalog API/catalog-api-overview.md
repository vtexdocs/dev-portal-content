---
title: "Catalog API - Overview"
slug: "catalog-api-overview"
hidden: false
createdAt: "2019-12-20T02:25:40.558Z"
updatedAt: "2022-08-08T21:09:09.766Z"
---
[block:callout]
{
  "type": "info",
  "body": "Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.",
  "title": "Onboarding guide"
}
[/block]
Methods for collecting product/SKU catalog data, categories, brands and other information. All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.


[block:api-header]
{
  "title": "Index"
}
[/block]
- [Product](ref:catalog-api-product) - Here you can consult, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).
- [Product Specification](ref:catalog-api-product-specification) - You can consult, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).
- [SKU](ref:catalog-api-sku) - Here you can consult, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).
- [SKU Complement](ref:catalog-api-sku-complement) - You can consult, create, or update an SKU Complement. An SKU Complement is a new SKU that has a Parent SKU.
- [SKU EAN](ref:catalog-api-sku-ean) -  Here you can consult, create, or update an SKU unique identification code (barcode).
- [SKU Attachment](ref:catalog-api-sku-attachment) - You can consult, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [SKU File](ref:catalog-api-sku-file) - Here you can consult, create, or update an SKU File. An SKU File is an image associated with an SKU.
- [SKU Kit](ref:catalog-api-sku-kit) - You can consult, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).
- [SKU Seller](ref:catalog-api-sku-seller) - Here you can consult and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [SKU Service](ref:catalog-api-sku-service) - You can create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).
- [SKU Service Attachment](ref:catalog-api-sku-service-attachment) - Here you can associate or disassociate an Attachment to an SKU Service.
- [SKU Service Type](ref:catalog-api-sku-service-type) - You can create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.
- [SKU Service Value](ref:catalog-api-sku-service-value) - Here you can create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.
- [SKU Specification](ref:catalog-api-sku-specification) - You can consult, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).
- [SKU Subcollection](ref:catalog-api-sku-subcollection) - Here you can can consult, create, or delete an SKU Subcollection. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).
- [Category](ref:catalog-api-category) - You consult, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).
- [Similar Category](ref:catalog-api-similar-category) - Here you can create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).
- [Category Specification](ref:catalog-api-category-specification) - You can consult all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).
- [Category Subcollection](ref:catalog-api-category-subcollection) - Here you can associate or disassociate  a subcollection to a category.
- [Brand](ref:catalog-api-brand) - You can consult, create, update, or delete a Brand. A brand is a product property. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).
- [Brand Subcollection](ref:catalog-api-brand-subcollection) - Here you can associate or disassociate a subcollection to a brand.
- [Attachment](ref:catalog-api-attachment) - You can consult, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [Collection Beta](ref:collection-beta) - The new [Beta Collections module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to engineer new endpoints that create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).
- [Collection](ref:catalog-api-collection) - Here you can consult, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).
- [Collection CMS](ref:collection-cms) - Here you can create a Collection CMS. A collection is a group of items. For more information, check [this article](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#).
- [Subcollection](ref:catalog-api-subcollection) - You can can consult, create, update, or delete a Subcollection. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).
- [Specification](ref:catalog-api-specification) - Here you can consult, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).
- [Specification Field](ref:catalog-api-specification-field) - You can consult, create, or update a Specification Field. A specification field allows you to present more detailed items. 
- [Specification Field Value](ref:catalog-api-specification-field-value) - Here you can consult, create, or update a Specification Field Value. 
- [Specification Value](ref:catalog-api-specification-value) - You can consult, create, or update a Specification Value.
- [Specification Group](ref:catalog-api-specification-group) - Here you can consult, create, or update a Specification Group.
- [Non Structured Specification](ref:catalog-api-non-structured-specification) - You can consult or delete a Non Structured Specification.
- [Sales Channel](ref:catalog-api-sales-channel) - Here you can consult Sales Channel.
- [Seller](ref:catalog-api-seller) - You can consult, create, or update a Seller. A seller is the _product owner_. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [Supplier](ref:catalog-api-supplier) - Here you can consult, create, or update a Supplier.
- [Trade Policy](ref:catalog-api-trade-policy) - You can create, update, or delete a Trade Policy. Trade policy is required when one of the above factors is different among the sale channel. For more information, check [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).
- [Product Indexed](ref:catalog-api-product-indexed) - Here you can consult Product Indexed information.
[block:api-header]
{
  "title": "Common parameters"
}
[/block]
| Parameter name              | Description                                                                             |
|---------------------------|-----------------------------------------------------------------------------------------|
| `{{accountName}}`         | Store account name                                                                      |
| `{{environment}`          | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |
| `{{X-VTEX-API-AppKey}}`   | Located in the headers of the requests, user authentication key                         |
| `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password                         |