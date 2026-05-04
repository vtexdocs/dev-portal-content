---
title: "Orders: Custom data now visible in the VTEX Admin"
slug: "2026-05-08-orders-custom-data-now-visible-in-the-vtex-admin"
type: "added"
createdAt: "2026-05-08T13:00:00.000Z"
updatedAt: "2026-05-08T13:00:00.000Z"
excerpt: "VTEX Admin now shows information about custom fields and apps."
---

We added support for displaying custom order data inside the VTEX Admin so you can view store-level custom fields and app-specific information directly from the order details page.

## What has changed?

Before, custom data attached to orders in OMS, including store custom fields (`customFields`) and per-app payloads (`customApps`), was only accessible through API calls. Now, when custom data exists on an order, both the order details page and print view inside the VTEX Admin display the information in collapsible groups, one for custom fields and one for app payloads.

## Why did we make this change?

In order to give merchants and store operators a complete view of order information without leaving the VTEX Admin, we developed custom data visibility in the order details page and print view. The data is only rendered if the order contains `customData`.

## What needs to be done?

To view custom order data in the VTEX Admin, contact [VTEX Support](https://supporticket.vtex.com/support) and request this feature for your account.
