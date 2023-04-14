---
title: "Catalog API - Overview"
slug: "catalog-api-overview"
hidden: false
createdAt: "2019-12-20T02:25:40.558Z"
updatedAt: "2022-08-08t21:09:09.766z"
---

> Check out the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It combines all our Developer Portal documentation about Catalog and focuses on the developer's journey.

The Catalog API provides methods for collecting product/SKU catalog data, categories, brands, and other information. All content between `{{}}` keys must be replaced with the correct data before performing the request.

[block:api-header]
{
  "title": "Index"
}
[/block]

- [Product](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds) - Retrieve, create, or update a product. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).
- [Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification) - Retrieve, create, or update additional information of a product.  For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).
- [SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids) - Retrieve, create, or update a SKU. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).
- [SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement) - Retrieve, create, or update a SKU complement. A SKU complement is a new SKU with a parent SKU.
- [SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) - Retrieve, create, or update a SKU unique identification code (barcode).
- [SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment) - Retrieve, create, or update a SKU attachment. An attachment is used to add custom information about the item. For more information, read [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file) - Retrieve, create, or update an SKU file. A SKU file is an image linked to a SKU.
- [SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit) - Retrieve, create, or update a SKU kit. A kit is a SKU composed of one or more SKUs. For more information, read [this article](https://help.vtex.com/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28?locale=en).
- [SKU Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-) - Retrieve and delete a SKU seller. An SKU Seller is a seller linked to a SKU. For more information, read [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-) - Retrieve, update, or delete a SKU service. A service is an item that may come with a product, which is optional and has a cost. For more information, read [this article](https://help.vtex.com/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y?locale=en).
- [SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment) - Link or unlink an attachment to a SKU service.
- [SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype) - Create, update, or delete a SKU service type. A service type is the behavior configuration of a service.
- [SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue) - Create, update, or delete a SKU service value. The service value is how much the customer will be charged for the service.
- [SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification) - Retrieve, create, or delete a SKU specification. A SKU specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).
- [Legacy Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit) - Retrieve, create, or delete a SKU, brand, or category from a subcollection, as well as create, delete, and update subcollections. A subcollection is a group type associated with a collection. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).
- [Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-) - Retrieve, create, or update a category. A category is a hierarchical level of product classification. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).
- [Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/) - Create and delete a similar category related to a product. This way, the product will be shown in both categories (main and similar).
- [Category Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-) - Retrieve all specifications by category. For more information about specifications, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).
- [Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list) - Retrieve, create, update, or delete a brand. A brand is a product property. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).
- [Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-) - Retrieve, create, or update an attachment. An attachment is used to add custom information about an item. For more information, read [this article](https://help.vtex.com/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm?locale=en).
- [Collection Beta](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search) - The new [Collections (beta) module](https://help.vtex.com/announcements/new-beta-collections-module-easily-create-and-manage-product-collections--6KvFxylC5SNsbVm8L8XZpZ#) launch allowed us to build new endpoints to create and manage collections. For more information, read [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye?&utm_source=autocomplete#).
- [Legacy Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-) - Retrieve, create, update, or delete a collection. A collection is a group of items. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca?locale=en).
- [Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-) - Retrieve, create, or delete a specification. A specification is used to create site browsing filters and to differentiate SKUs and products within the product page. For more information, read [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).
- [Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-) - Retrieve, create, or update a specification field. A specification field allows you to display more detailed items.
- [Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-) - Retrieve, create, or update a specification field value.
- [Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-) - Retrieve, create, or update a specification value.
- [Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-) - Retrieve, create, or update a specification group.
- [Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-) - Retrieve or delete a non-structured specification.
- [Sales Channel](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list) - Retrieve the sales channel.
- [Seller](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list) - Retrieve, create, or update a seller. A seller is the _product owner_. For more information, read [this article](https://help.vtex.com/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w?locale=en).
- [Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier) - Retrieve, create, or update a supplier.
- [Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy) - Create, update, or delete a trade policy. A trade policy is required when one of the above factors is different among the sales channel. For more information, read [this article](https://help.vtex.com/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE?locale=en).
- [Product Indexing](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-) - Retrieve product indexed information.
- [Commercial Conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list) - Retrieve commercial conditions added to the store.

[block:api-header]
{
  "title": "Common parameters"
}
[/block]
| Parameter name            | Description                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------- |
| `{{accountName}}`         | Store account name                                                                      |
| `{{environment}}`         | The environment that will be called. Change to vtexcommercestable or vtexcommmercebeta. |
| `{{X-VTEX-API-AppKey}}`   | Located in the request headers, user authentication key.                                |
| `{{X-VTEX-API-AppToken}}` | Located in the request headers, authentication password.                                |
