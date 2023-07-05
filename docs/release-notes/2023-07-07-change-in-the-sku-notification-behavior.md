---
title: "Change in the SKU notification behavior"
slug: "2023-07-07-change-in-the-sku-notification-behavior"
excerpt: "From September 2023, we will no longer allow price and inventory changes to be notified using the Change Notification with SKU ID endpoint."
hidden: false
createdAt: "2023-07-07T15:54:00.000Z"
type: "deprecated"
---

From September 2023, we will no longer allow price and inventory changes to be notified using the [Change Notification with SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-skuId-) endpoint. This means that integrations that use this endpoint to notify marketplaces about price and inventory updates may have issues after the change, and it will be necessary to adapt them to use [Marketplace API](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price) endpoints.

## What will change?

The [Change Notification with SKU ID](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog_system/pvt/skuseller/changenotification/-skuId-) endpoint will no longer notify VTEX marketplaces about price and inventory changes. It will only about changes in SKU catalog information, such as name, description, and measurements. 

From September 2023, only the Marketplace API endpoints will be available to send price and inventory notifications:

* [Notify marketplace of price update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price)
* [Notify marketplace of inventory update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory)

## What needs to be done?

Make sure your integrations use Marketplace API endpoints to notify VTEX marketplaces of price and inventory updates before September 2023.