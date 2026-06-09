---
slug: 2026-06-12-orders-custom-data-now-generally-available
type: added
title: "Orders: Custom data in the VTEX Admin is now generally available"
excerpt: "Custom order data, including custom fields and app payloads, is now visible in the VTEX Admin for all stores."
createdAt: 2026-06-12T15:00:00.000Z
updatedAt: 2026-06-12T15:00:00.000Z
---

The VTEX Admin order details page now displays custom order data for all stores. Merchants and store operators can view store-level custom fields (`customFields`) and per-app payloads (`customApps`) directly from the order details page and print view, with no additional setup required.

## What has changed?

Previously, this feature was available in open beta and required stores to contact [VTEX Support](https://support.vtex.com/) to enable it. Now, custom order data is available to all stores by default. When an order contains `customData`, both the order details page and print view display the information in collapsible groups, one for custom fields and one for app payloads.

## Why did we make this change?

In order to give all merchants and store operators a complete view of order information without leaving the VTEX Admin, we made custom data visibility generally available. This eliminates the need to rely on API calls or manual enablement to access order-level custom data.

## What needs to be done?

No action is required. Custom order data is now automatically visible in the order details page and print view of the VTEX Admin for all stores that have `customData` attached to their orders.

To learn more, see [Orders: Custom data now visible in the VTEX Admin](https://developers.vtex.com/updates/release-notes/2026-05-08-orders-custom-data-now-visible-in-the-vtex-admin).
