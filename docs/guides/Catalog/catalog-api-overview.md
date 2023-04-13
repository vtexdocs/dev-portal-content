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

- `GET` [Get Category Tree](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/category/tree/-categoryLevels-)
- `GET` [Get Category by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/category/-categoryId-)
- `PUT` [Update Category](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/category/-categoryId-)
- `POST` [Create Category](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/category)

### Category Specification

- `GET` [Get Specifications By Category ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listByCategoryId/-categoryId-)
- `GET` [Get Specifications Tree By Category ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/field/listTreeByCategoryId/-categoryId-)

### Brand

- `GET` [Get Brand List](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/list)
- `GET` [Get Brand List Per Page](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/pagedlist)
- `GET` [Get Brand](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/brand/-brandId-)
- `POST` [Create Brand](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/brand)
- `GET` [Get Brand and context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/brand/-brandId-)
- `PUT` [Update Brand](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/brand/-brandId-)
- `DELETE` [Delete Brand](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/brand/-brandId-)

### Specification Group

- `GET` [List Specification Group by Category](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/groupbycategory/-categoryId-)
- `GET` [Get Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/groupGet/-groupId-)
- `POST` [Create Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationgroup)
- `PUT` [Update Specification Group](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specificationgroup/-groupId-)

### Specification

- `GET` [Get Specification](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/-specificationId-)
- `PUT` [Update Specification](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specification/-specificationId-)
- `POST` [Create Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specification)

#### Specification Field

- `GET` [Get Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldGet/-fieldId-)
- `POST` [Create Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/field)
- `PUT` [Update Specification Field](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/specification/field)

#### Non Structured Specification

- `GET` [Get Non Structured Specification by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured/-Id-)
- `DELETE` [Delete Non Structured Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/specification/nonstructured/-Id-)
- `GET` [Get Non Structured Specification by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specification/nonstructured)
- `DELETE` [Delete Non Structured Specification by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/specification/nonstructured)

### Specification Value

- `GET` [Get Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/specificationvalue/-specificationValueId-)
- `PUT` [Update Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/specificationvalue/-specificationValueId-)
- `POST` [Create Specification Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/specificationvalue)

#### Specification Field Value

- `GET` [Get Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/specification/fieldValue/-fieldValueId-)
- `GET` [Get Specification Values By Field ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/specification/fieldvalue/-fieldId-)
- `POST` [Create Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/specification/fieldValue)
- `PUT` [Update Specification Field Value](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog_system/pvt/specification/fieldValue)

### Product

- `GET` [Get Product and SKU IDs](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/GetProductAndSkuIds)
- `GET` [Get Product by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-)
- `PUT` [Update Product](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-)
- `GET` [Get Product and its general context](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/productget/-productId-)
- `GET` [Get Product by RefId](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/productgetbyrefid/-refId-)
- `GET` [Get Product's SKUs by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pub/products/variations/-productId-)
- `GET` [Get Product Review Rate by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/addon/pvt/review/GetProductRate/-productId-)
- `POST` [Create Product with Category and Brand](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product)

### Product Specification

- `GET` [Get Product Specification by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/products/-productId-/specification)
- `POST` [Update Product Specification by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/products/-productId-/specification)
- `GET` [Get Product Specification and its information by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/product/-productId-/specification)
- `POST` [Associate Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/product/-productId-/specification)
- `DELETE` [Delete all Product Specifications by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification)
- `DELETE` [Delete a specific Product Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/product/-productId-/specification/-specificationId-)
- `PUT` [Associate product specification using specification name and group name](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/product/-productId-/specificationvalue)

### SKU

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

- `GET` [Get SKU Specifications](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `POST` [Associate SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `PUT` [Update SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `DELETE` [Delete all SKU Specifications](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/specification)
- `DELETE` [Delete SKU Specification](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/specification/-specificationId-)
- `PUT` [Associate SKU specification using specification name and group name](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/specificationvalue)

### SKU File

- `GET` [Get SKU Files](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `POST` [Create SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `DELETE` [Delete All SKU Files](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/file)
- `PUT` [Update SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/-skuId-/file/-skuFileId-)
- `DELETE` [Delete SKU Image File](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/file/-skuFileId-)
- `PUT` [Copy Files from an SKU to another SKU](https://developers.vtex.com/docs/api-reference/catalog-api#put-/api/catalog/pvt/stockkeepingunit/copy/-skuIdfrom-/-skuIdto-/file/)
- `DELETE` [Disassociate SKU File](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/disassociate/-skuId-/file/-skuFileId-)

### SKU Complement

- `GET` [Get SKU Complement by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement)
- `GET` [Get SKU Complements by Complement Type ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/stockkeepingunit/-skuId-/complement/-complementTypeId-)
- `GET` [Get SKU complements by type](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/complements/-parentSkuId-/-type-)
- `POST` [Create SKU Complement](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/skucomplement)
- `GET` [Get SKU Complement by SKU Complement ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog/pvt/skucomplement/-skuComplementId-)
- `DELETE` [Delete SKU Complement by SKU Complement ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/skucomplement/-skuComplementId-)

### SKU EAN

- `GET` [Get SKU by EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-)
- `GET` [Get EAN by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/stockkeepingunit/-skuId-/ean)
- `DELETE` [Delete all SKU EAN values](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/stockkeepingunit/-skuId-/ean)
- `POST` [Create SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-)
- `DELETE` [Delete SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-)

### Attachment

- `GET` [Get attachment](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/attachment/-attachmentid-)
- `PUT` [Update attachment](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog/pvt/attachment/-attachmentid-)
- `DELETE` [Delete attachment](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/attachment/-attachmentid-)
- `POST` [Create attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/attachment)
- `GET` [Get all attachments](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/attachments)

### SKU Attachment

- `POST` [Associate SKU Attachment](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/skuattachment)
- `DELETE` [Dissociate attachments and SKUs](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/skuattachment)
- `GET` [Get SKU Attachments by SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/stockkeepingunit/-skuId-/attachment)
- `DELETE` [Delete SKU Attachment by Attachment Association ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/skuattachment/-skuAttachmentAssociationId-)
- `POST` [Associate attachments to an SKU](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog_system/pvt/sku/associateattachments)

### SKU Service

- `GET` [Get SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/skuservice/-skuServiceId-)
- `PUT` [Update SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog/pvt/skuservice/-skuServiceId-)
- `DELETE` [Dissociate SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/skuservice/-skuServiceId-)
- `POST` [Associate SKU Service](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/skuservice)

### SKU Kit

- `GET` [Get SKU Kit by SKU ID or Parent SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/stockkeepingunitkit)
- `POST` [Create SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/stockkeepingunitkit)
- `DELETE` [Delete SKU Kit by SKU ID or Parent SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/stockkeepingunitkit)
- `GET` [Get SKU Kit](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/stockkeepingunitkit/-kitId-)
- `DELETE` [Delete SKU Kit by KitId](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/stockkeepingunitkit/-kitId-)

### SKU Seller

- `GET` [Get details of a seller's SKU](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/skuseller/-sellerId-/-sellerSkuId-)
- `POST` [Remove a seller's SKU binding](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog_system/pvt/skuseller/remove/-sellerId-/-sellerSkuId-)
- `POST` [Change Notification with Seller ID and Seller SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog_system/pvt/skuseller/changenotification/-sellerId-/-sellerSkuId-)
- `POST` [Change Notification with SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog_system/pvt/skuseller/changenotification/-skuId-)

### Similar Category

- `GET` [Get Similar Categories](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/product/-productId-/similarcategory/)
- `POST` [Add Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/product/-productId-/similarcategory/-categoryId-)
- `DELETE` [Delete Similar Category](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/product/-productId-/similarcategory/-categoryId-)

### Collection Beta

- `GET` [Get All Collections](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/collection/search)
- `GET` [Get All Inactive Collections](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/collection/inactive)
- `POST` [Create Collection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/collection/)
- `GET` [Get Collections by search terms](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/collection/search/-searchTerms-)
- `GET` [Import Collection file example](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/collection/stockkeepingunit/importfileexample)
- `POST` [Add products to Collection by imported file](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/collection/-collectionId-/stockkeepingunit/importinsert)
- `POST` [Remove products from Collection by imported file](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/collection/-collectionId-/stockkeepingunit/importexclude)
- `GET` [Get products from a collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/collection/-collectionId-/products)

### Legacy Collection

- `GET` [Get Collection](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/collection/-collectionId-)
- `PUT` [Update Collection](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog/pvt/collection/-collectionId-)
- `DELETE` [Delete Collection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/collection/-collectionId-)
- `POST` [Create Collection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/collection)

### Legacy Subcollection

- `POST` [Add SKU to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit)
- `DELETE` [Delete SKU from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/subcollection/-subCollectionId-/stockkeepingunit/-skuId-)
- `POST` [Associate Category to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/subcollection/-subCollectionId-/category)
- `DELETE` [Delete Category from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/subcollection/-subCollectionId-/brand/-categoryId-)
- `POST` [Associate Brand to Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/subcollection/-subCollectionId-/brand)
- `DELETE` [Delete Brand from Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/subcollection/-subCollectionId-/brand/-brandId-)
- `GET` [Get Subcollection by Collection ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/collection/-collectionId-/subcollection)
- `GET` [Get Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/subcollection/-subCollectionId-)
- `PUT` [Update Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog/pvt/subcollection/-subCollectionId-)
- `DELETE` [Delete Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/subcollection/-subCollectionId-)
- `POST` [Create Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/subcollection)
- `POST` [Reposition SKU on the Subcollection](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/collection/-collectionId-/position)

### Seller

- `GET` [Get Seller List](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/seller/list)
- `GET` [Get Seller by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/seller/-sellerId-)
- `PUT` [Update Seller](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog_system/pvt/seller)
- `POST` [Create Seller](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog_system/pvt/seller)
- `GET` [Get Seller by ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/sellers/-sellerId-)

### Supplier

- `POST` [Create Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/supplier)
- `PUT` [Update Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#put-api/catalog/pvt/supplier/-supplierId-)
- `DELETE` [Delete Supplier](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/supplier/-supplierId-)

### Trade Policy

- `GET` [Get Trade Policies by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog/pvt/product/-productId-/salespolicy)
- `POST` [Associate Product with Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#post-api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-)
- `DELETE` [Remove Product from Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#delete-api/catalog/pvt/product/-productId-/salespolicy/-tradepolicyId-)
- `GET` [List all SKUs of a Trade Policy](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel)

### Product Indexing

- `GET` [Get Product Indexed Information](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/products/GetIndexedInfo/-productId-)

### Commercial Conditions

- `GET` [Get all commercial conditions](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/commercialcondition/list)
- `GET` [Get commercial condition](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/catalog_system/pvt/commercialcondition/-commercialConditionId-)

### Gift List

- `GET` [Get Gift List](https://developers.vtex.com/docs/api-reference/catalog-api#get-api/addon/pvt/giftlist/get/-listId-)