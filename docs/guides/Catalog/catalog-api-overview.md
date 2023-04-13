---
title: "Catalog API - Overview"
slug: "catalog-api-overview"
hidden: false
createdAt: "2019-12-20T02:25:40.558Z"
updatedAt: "2022-08-08T21:09:09.766Z"
---

Catalog API offers methods for managing and retrieving data about products and SKUs, categories, brands and other information from your store's catalog.

> Check the new [Catalog onboarding guide](https://developers.vtex.com/docs/guides/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer's journey.


## Common parameters

| Parameter name | Description |
| - | - |
| `{{accountName}}` | VTEX account name. |
| `{{environment}` | The environment that will be called. Change for vtexcommercestable or vtexcommmercebeta |
| `{{X-VTEX-API-AppKey}}` | Located in the headers of the requests, user authentication key. |
| `{{X-VTEX-API-AppToken}}` | Located in the headers of the requests, authentication password. |

All content that comes between `{{}}` keys must be replaced with the correct data before performing the request.

## Index

### Category

Retrieve, create, or update a Category. A category is a hierarchical level of product classification. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2gkZDjXRqfsq62TlAkj4uf).

- `GET` [Get Category Tree](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-)
- `GET` [Get Category by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/category/-categoryId-)
- `PUT` [Update Category](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/category/-categoryId-)
- `POST` [Create Category](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/category)

### Category Specification

Retrieve all Specifications by Category. For more information about Specification, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP).

- `GET` [Get Specifications By Category ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-)
- `GET` [Get Specifications Tree By Category ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listTreeByCategoryId/-categoryId-)

### Brand

Retrieve, create, update, or delete a Brand. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/7i3sB8fgkqUp5NoH5yJtfh).

- `GET` [Get Brand List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list)
- `GET` [Get Brand List Per Page](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/pagedlist)
- `GET` [Get Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/-brandId-)
- `POST` [Create Brand](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/brand)
- `GET` [Get Brand and context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/brand/-brandId-)
- `PUT` [Update Brand](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/brand/-brandId-)
- `DELETE` [Delete Brand](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/brand/-brandId-)

### Specification Group

Retrieve, create, or update a Specification Group.

- `GET` [List Specification Group by Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-)
- `GET` [Get Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/groupGet/-groupId-)
- `POST` [Create Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationgroup)
- `PUT` [Update Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specificationgroup/-groupId-)

### Specification

Retrieve, create, or delete a Specification. A specification is used to create site browsing filters and to differentiate SKUs and Products within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en).

- `GET` [Get Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-)
- `PUT` [Update Specification](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specification/-specificationId-)
- `POST` [Create Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specification)

#### Specification Field

Retrieve, create, or update a Specification Field. A specification field allows you to present more detailed items.

- `GET` [Get Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-)
- `POST` [Create Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/field)
- `PUT` [Update Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/specification/field)

#### Non Structured Specification

Retrieve or delete a Non Structured Specification.

- `GET` [Get Non Structured Specification by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-)
- `DELETE` [Delete Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/specification/nonstructured/-Id-)

### Specification Value

Retrieve, create, or update a Specification Value.

- `GET` [Get Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-)
- `PUT` [Update Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specificationvalue/-specificationValueId-)
- `POST` [Create Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationvalue)

#### Specification Field Value

Retrieve, create, or update a Specification Field Value.

- `GET` [Get Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-)
- `GET` [Get Specification Values By Field ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldvalue/-fieldId-)
- `POST` [Create Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/fieldValue)
- `PUT` [Update Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/specification/fieldValue)

### Product

Retrieve, create, or update a Product. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1wmX3QvQVxbKVmalhIE5Ru).

- `GET` [Get Product and SKU IDs](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds)
- `GET` [Get Product by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-)
- `PUT` [Update Product](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-)
- `GET` [Get Product and its general context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/productget/-productId-)
- `GET` [Get Product by RefId](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/productgetbyrefid/-refId-)
- `GET` [Get Product's SKUs by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/products/variations/-productId-)
- `GET` [Get Product Review Rate by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/addon/pvt/review/GetProductRate/-productId-)
- `POST` [Create Product with Category and Brand](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product)

### Product Specification

Retrieve, create, or update additional information of a Product.  For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP#product-specification).

- `GET` [Get Product Specification by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification)
- `POST` [Update Product Specification by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/products/-productId-/specification)
- `GET` [Get Product Specification and its information by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/specification)
- `POST` [Associate Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/specification)
- `DELETE` [Delete all Product Specifications by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification)
- `DELETE` [Delete a specific Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification/-specificationId-)
- `PUT` [Associate product specification using specification name and group name](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-/specificationvalue)

### SKU

Retrieve, create, or update an SKU. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3mJbIqMlz6oKDmyZ2bKJoA).

- `GET` [List all SKU IDs](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitids)
- `GET` [Get SKU and context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyid/-skuId-)
- `GET` [Get SKU by RefId](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit)
- `POST` [Create SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit)
- `GET` [Get SKU ID by Reference ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/-refId-)
- `GET` [Get SKU by Alternate ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/-alternateId-)
- `GET` [Get SKU list by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitByProductId/-productId-)
- `POST` [Retrieve SKU ID list by Reference ID list](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pub/sku/stockkeepingunitidsbyrefids)
- `GET` [Get SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-)
- `PUT` [Update SKU](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-)

### SKU Specification

Retrieve, create, or delete an SKU Specification. SKU Specification is used to create site browsing filters and to differentiate SKUs within the product page. For more information, check [this article](https://help.vtex.com/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/2NQoBv8m4Yz3oQaLgDRagP?locale=en#sku-specifications).

- `GET` [Get SKU Specifications](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `POST` [Associate SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `PUT` [Update SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `DELETE` [Delete all SKU Specifications](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `DELETE` [Delete SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/specification/-specificationId-)
- `PUT` [Associate SKU specification using specification name and group name](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/specificationvalue)

### SKU File

Retrieve, create, or update an SKU File. An SKU File is an image associated with an SKU.

- `GET` [Get SKU Files](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `POST` [Create SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `DELETE` [Delete All SKU Files](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `PUT` [Update SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/file/-skuFileId-)
- `DELETE` [Delete SKU Image File](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/file/-skuFileId-)
- `PUT` [Copy Files from an SKU to another SKU](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/copy/-skuIdfrom-/-skuIdto-/file/)
- `DELETE` [Disassociate SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/disassociate/-skuId-/file/-skuFileId-)

### SKU Complement

Retrieve, create, or update an SKU Complement. An SKU Complement is an SKU that has a Parent SKU.

- `GET` [Get SKU Complement by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement)
- `GET` [Get SKU Complements by Complement Type ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement/-complementTypeId-)
- `GET` [Get SKU complements by type](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/complements/-parentSkuId-/-type-)
- `POST` [Create SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skucomplement)
- `GET` [Get SKU Complement by SKU Complement ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/skucomplement/-skuComplementId-)
- `DELETE` [Delete SKU Complement by SKU Complement ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skucomplement/-skuComplementId-)

### SKU EAN

Retrieve, create, or update an SKU unique identification code (barcode).

- `GET` [Get SKU by EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-)
- `GET` [Get EAN by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/ean)
- `DELETE` [Delete all SKU EAN values](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/ean)
- `POST` [Create SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-)
- `DELETE` [Delete SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-)

### Attachment

Retrieve, create, or update an Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm).

- `GET` [Get attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachment/-attachmentid-)
- `PUT` [Update attachment](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/attachment/-attachmentid-)
- `DELETE` [Delete attachment](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/attachment/-attachmentid-)
- `POST` [Create attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/attachment)
- `GET` [Get all attachments](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/attachments)

### SKU Attachment

Retrieve, create, or update an SKU Attachment. An attachment is used to add custom information about the item. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm).

- `POST` [Associate SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuattachment)
- `DELETE` [Dissociate attachments and SKUs](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuattachment)
- `GET` [Get SKU Attachments by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/attachment)
- `DELETE` [Delete SKU Attachment by Attachment Association ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuattachment/-skuAttachmentAssociationId-)
- `POST` [Associate attachments to an SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/sku/associateattachments)

### SKU Service

Create, update, or delete an SKU Service. A service is an item that may come with a product, optionally, and with a cost. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-a-service--46Ha8CEEQoC6Y40i6akG0y).

- `GET` [Get SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/skuservice/-skuServiceId-)
- `PUT` [Update SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservice/-skuServiceId-)
- `DELETE` [Dissociate SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuservice/-skuServiceId-)
- `POST` [Associate SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservice)

#### SKU Service Attachment

Associate or disassociate an Attachment to an SKU Service.

- `POST` [Associate SKU Service Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetypeattachment)
- `DELETE` [Dissociate Attachment by Attachment ID or SKU Service Type ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuservicetypeattachment)
- `DELETE` [Dissociate Attachment from SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuservicetypeattachment/-skuServiceTypeAttachmentId-)

#### SKU Service Type

Create, update, or delete an SKU Service Type. A service type is the behavior configuration of a service.

- `POST` [Create SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicetype)
- `GET` [Get SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/skuservicetype/-skuServiceTypeId-)
- `PUT` [Update SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservicetype/-skuServiceTypeId-)
- `DELETE` [Delete SKU Service Type](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuservicetype/-skuServiceTypeId-)

#### SKU Service Value

Create, update, or delete an SKU Service Value. Service value is how much the customer will be charged for the service.

- `POST` [Create SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skuservicevalue)
- `GET` [Get SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/skuservicevalue/-skuServiceValueId-)
- `PUT` [Update SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/skuservicevalue/-skuServiceValueId-)
- `DELETE` [Delete SKU Service Value](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skuservicevalue/-skuServiceValueId-)

### SKU Kit

Retrieve, create, or update an SKU Kit. A kit is an SKU composed of one or more SKUs. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-a-kit--5ov5s3eHM4AqAAgqWwoc28).

- `GET` [Get SKU Kit by SKU ID or Parent SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit)
- `POST` [Create SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunitkit)
- `DELETE` [Delete SKU Kit by SKU ID or Parent SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunitkit)
- `GET` [Get SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunitkit/-kitId-)
- `DELETE` [Delete SKU Kit by KitId](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunitkit/-kitId-)

### SKU Seller

Retrieve and delete an SKU Seller. An SKU Seller is a seller associated with an SKU. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w).

- `GET` [Get details of a seller's SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-)
- `POST` [Remove a seller's SKU binding](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/remove/-sellerId-/-sellerSkuId-)
- `POST` [Change Notification with Seller ID and Seller SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-sellerId-/-sellerSkuId-)
- `POST` [Change Notification with SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-skuId-)

### Similar Category

Create and delete a Similar Category to a Product. This way the Product will be shown in both categories (main and similar).

- `GET` [Get Similar Categories](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/similarcategory/)
- `POST` [Add Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/similarcategory/-categoryId-)
- `DELETE` [Delete Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/similarcategory/-categoryId-)

### Collection Beta

The Beta Collections module provides endpoints to create and manage Collections. For more information, check [this article](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye).

- `GET` [Get All Collections](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search)
- `GET` [Get All Inactive Collections](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/inactive)
- `POST` [Create Collection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/collection/)
- `GET` [Get Collections by search terms](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/collection/search/-searchTerms-)
- `GET` [Import Collection file example](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/stockkeepingunit/importfileexample)
- `POST` [Add products to Collection by imported file](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/collection/-collectionId-/stockkeepingunit/importinsert)
- `POST` [Remove products from Collection by imported file](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/collection/-collectionId-/stockkeepingunit/importexclude)
- `GET` [Get products from a collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-/products)

### Legacy Collection

 Retrieve, create, update, or delete a Collection. A collection is a group of items. For more information, check [this article](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/4hN41yU8IPeb8HKmmaXoca).

- `GET` [Get Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-)
- `PUT` [Update Collection](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/collection/-collectionId-)
- `DELETE` [Delete Collection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/collection/-collectionId-)
- `POST` [Create Collection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/collection)

### Legacy Subcollection

Can retrieve, create, or delete an SKU, Brand or Category from a Subcollection, as well as create, delete and update subcollections. A subcollection is a group type associated with a collection. For more information, check [this article](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/3moFonW33dgOYDrU21Z1X0#group-types).

- `POST` [Add SKU to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit)
- `DELETE` [Delete SKU from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit/-skuId-)
- `POST` [Associate Category to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/category)
- `DELETE` [Delete Category from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/subcollection/-subCollectionId-/brand/-categoryId-)
- `POST` [Associate Brand to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection/-subCollectionId-/brand)
- `DELETE` [Delete Brand from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/subcollection/-subCollectionId-/brand/-brandId-)
- `GET` [Get Subcollection by Collection ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/collection/-collectionId-/subcollection)
- `GET` [Get Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/subcollection/-subCollectionId-)
- `PUT` [Update Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/subcollection/-subCollectionId-)
- `DELETE` [Delete Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/subcollection/-subCollectionId-)
- `POST` [Create Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/subcollection)
- `POST` [Reposition SKU on the Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/collection/-collectionId-/position)

### Seller

Retrieve, create, or update a Seller. For more information, check [this article](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w).

- `GET` [Get Seller List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/list)
- `GET` [Get Seller by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/seller/-sellerId-)
- `PUT` [Update Seller](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/seller)
- `POST` [Create Seller](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/seller)
- `GET` [Get Seller by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sellers/-sellerId-)

### Supplier

Retrieve, create, or update a Supplier.

- `POST` [Create Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/supplier)
- `PUT` [Update Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/supplier/-supplierId-)
- `DELETE` [Delete Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/supplier/-supplierId-)

### Trade Policy

 Create, update, or delete a [trade policy](https://help.vtex.com/en/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE).

- `GET` [Get Trade Policies by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/salespolicy)
- `POST` [Associate Product with Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-)
- `DELETE` [Remove Product from Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-)
- `GET` [List all SKUs of a Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel)

#### Sales Channel

Retrieve trade policies (also known as sales channels).

- `GET` [Get Sales Channel List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/saleschannel/list)
- `GET` [Get Sales Channel by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/saleschannel/-salesChannelId-)

### Product Indexing

Retrieve Product Indexed information.

- `GET` [Get Product Indexed Information](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetIndexedInfo/-productId-)

### Commercial Conditions

Retrieve commercial conditions registered in the store.

- `GET` [Get all commercial conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/list)
- `GET` [Get commercial condition](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/commercialcondition/-commercialConditionId-)

### Gift List

Retrieve information about gift lists registered in your store.

- `GET` [Get Gift List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/addon/pvt/giftlist/get/-listId-)