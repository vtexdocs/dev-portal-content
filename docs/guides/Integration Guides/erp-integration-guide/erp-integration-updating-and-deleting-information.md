---
title: "Updating / deleting information"
slug: "erp-integration-updating-and-deleting-information"
hidden: false
createdAt: "2020-03-11T20:58:09.117Z"
updatedAt: "2022-02-03T13:51:21.641Z"
---
As you may have noticed when browsing through our [API Reference](https://developers.vtex.com/reference) in the previous steps of this guide, most of the endpoints used have `PUT` / `DELETE` counterparts. These endpoints may be used as needed in your migration scripts or integration middleware to update and delete information. Check the links below to learn more.


## Product updates
You may use automations that trigger API requests to your VTEX catalog whenever there are changes to you ERP catalog. Another alternative is to use one of the different [methods of importing or editing products manually](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-products#import-product).

Your store's catalog may go through different kinds of changes, but in each case, your operation must be prepared to handle them and register them to VTEX.


### New products or SKUs
In case you have new products or SKUs, you may follow the [product import flow](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-products#import-product) mentioned in this guide.
[block:callout]
{
  "type": "warning",
  "body": "Before importing new items make sure your [catalog is setup](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-catalog) to receive the new item when it comes to [category](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-catalog#create-departments-categories-and-subcategories), [brand](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-catalog#create-departments-categories-and-subcategories) and [specifications](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-catalog#create-departments-categories-and-subcategories)."
}
[/block]
To learn more, see our [Catalog API reference](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-overview) and these detailed integration guides:
- [Categories](https://developers.vtex.com/vtex-rest-api/docs/categories)
- [Brands](https://developers.vtex.com/vtex-rest-api/docs/brands)
- [Specifications](https://developers.vtex.com/vtex-rest-api/docs/specifications)
- [Products](https://developers.vtex.com/vtex-rest-api/docs/products)
- [SKUs](https://developers.vtex.com/vtex-rest-api/docs/skus)


### Updating existing products or SKUs
See these guides:
- [Update a product](https://developers.vtex.com/vtex-rest-api/docs/products#update-a-product)
- [Update an SKU](https://developers.vtex.com/vtex-rest-api/docs/skus#update-sku)


### Deactivating old products or SKUs
If you want a product or SKU to be removed from the catalog shown in your storefront, you may deactivate them. To do this, use the [Update product](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-product) or [Update SKU](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-sku) API request setting the `IsActive` field as `false`.


## Pricing updates
To perform ongoing pricing updates, you may use the same method described previously in this guide: [Import prices](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-prices#set-base-price).


## Inventory updates
To perform ongoing inventory updates, you may follow the same flow mentioned previously in this guide: [Update SKU Inventory](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-import-inventory#update-sku-inventory).


## Feedback
[block:callout]
{
  "type": "success",
  "title": "Let us know what you think",
  "body": "Congratulations in completing all the steps in this integration guide :tada:\n\nIf you found it helpful, please let us know by clicking the :thumbsup: icon below! Otherwise, feel free to make suggestions in the `Feedback` button on the top of the page, after you click the :thumbsdown: icon."
}
[/block]