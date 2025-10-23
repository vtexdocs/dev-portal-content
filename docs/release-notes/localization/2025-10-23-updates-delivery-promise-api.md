---
title: "Delivery Promise Notification API: New endpoint to update delivery promises for external sellers"
slug: "2025-10-23-updates-delivery-promise-api"
type: added
excerpt: "A new endpoint lets marketplaces update delivery promises (SLAs) for an external seller's item via the Delivery Promise Notification API."
createdAt: "2025-10-23T11:00:00.000Z"
updatedAt: "2025-10-23T11:00:00.000Z"
hidden: false
---

We updated the [Delivery Promise Notification API](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api) with a new `PATCH` endpoint that lets marketplaces update delivery promises (SLAs) for an external seller’s item in near real time. This keeps shipping estimates accurate across the storefront and reduces customer friction caused by outdated delivery information.  

## What has changed?

- New endpoint: `PATCH` [Update delivery promises for an external seller’s item](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api#patch-/delivery-promises/external-sellers/-sellerId-/items/-itemId-).
 - New `deliveryZoneIds`: Added new `deliveryZoneIds` values to the `PUT` [Update product availability endpoint](https://developers.vtex.com/docs/api-reference/delivery-promise-notification-api#put-/delivery-promises/external-sellers/-sellerId-/products).  

## Why did we make this change?

This change improves the accuracy and timeliness of delivery information shown to shoppers. With this endpoint, marketplaces can promptly adjust SLAs for external sellers’ offers when logistics inputs change, reducing customer friction and preventing outdated delivery promises from being shown.

## What needs to be done?

If you integrate with the Delivery Promise Notification API:

- Review the updated schema and examples.
- Update your marketplace integration to call the new endpoint whenever delivery-related inputs for an external seller’s item change.
- For more information about this feature, see the [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise) guide.
