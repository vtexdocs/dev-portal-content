---
title: "FastStore: Coupons persist through store cart validation"
slug: "2025-08-06-faststore-store-coupons"
type: fixed
excerpt: "Coupons remain applied after store cart updates"
createdAt: "2025-08-06T09:50:00.214Z"
updatedAt: "2025-08-06T10:00:00.214Z"
hidden: false
---

Applied coupons now remain in the store cart after any cart interaction, such as refreshing the page or adding new items.

## What has changed?

Previously, applied coupons in the cart would disappear after a page refresh or any interaction.
This happened because the `marketingData` object, which holds coupon information and other session data (such as UTMs), was overwritten during cart interaction, causing applied coupons to be removed from the cart.

Now, when a user refreshes the page or adds a new item, existing coupon information within `marketingData` is combined with any new session data instead of being overwritten. This ensures that the previously applied coupons and other `marketingData` properties such as UTMs are preserved.

## Why did we make this change?

Losing applied coupon codes during cart validation could lead to abandoned carts and lost sales. This fix ensures that `marketingData` is combined rather than overwritten. The update eliminates this friction point, contributing to a better customer journey.

## What needs to be done?

To implement the fix for persistent coupons in the cart, update your store project to the latest version. To do this, follow these steps:

1. Open your project in a code editor.

2. Open a terminal and run the following command to update the FastStore packages to the latest version:

```bash
yarn upgrade -L --scope @faststore
```

No further configuration is required. The new cart validation logic, ensuring coupons are preserved, is automatic once you upgrade your project version. To test whether the `marketingData` object contains coupon tracking and UTM data, follow the instructions available at [Validating UTM tracking in FastStore](https://developers.vtex.com/docs/guides/faststore/seo-validating-utm-tracking-in-faststore#instructions).
