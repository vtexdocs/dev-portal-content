---
title: "Activity Flow: Flexible cart event capture in the dataLayer"
slug: "2026-07-08-activity-flow-flexible-cart-event-capture-in-the-datalayer"
type: "improved"
excerpt: "The Activity Flow Web Script data-layer plugin now captures add-to-cart events reliably across storefronts and analytics setups."
createdAt: "2026-07-08T00:00:00.000Z"
tags:
  - Activity Flow
  - Intelligent Search
---

The [Activity Flow](https://developers.vtex.com/docs/guides/activity-flow) Web Script data-layer plugin now captures add-to-cart events reliably across any storefront and analytics setup. This provides a complete and trusted conversion-to-add-to-cart signal across accounts, serving as the north-star metric for measuring search impact directly before checkout.

## What has changed?

Previously, add-to-cart measurement relied on product listing page (PLP) and product detail page (PDP) click-through as a proxy. This approach had two key distortions: it missed sessions that landed directly on a PDP without going through a PLP, and it ignored add-to-cart actions that happened on the PLP itself, which is common in grocery and similar verticals.

On top of that, event capture broke when stores used a different naming convention, ran Google Analytics 4 (GA4) and Google Analytics Universal (GAU) simultaneously, or loaded the Activity Flow script more than once.

Now, the data-layer plugin addresses these limitations with the following improvements:

- Expanded compatibility to stores using only GAU, which were previously unsupported.
- Cart events are captured regardless of naming convention, including `add_to_cart`, `addToCart`, `add-to-cart`, `add_to_cart_v2`, and other common variations.
- Automatic filtering of duplicate cart events when GA4 and GAU run simultaneously.
- Elimination of duplicate events caused by multiple Activity Flow script loads.
- Improved reliability of cart event collection without requiring store-specific customizations.

## Why did we make this change?

To replace the PLP and PDP proxy with a more accurate conversion signal, we've improved how the Web Script reads cart events from the `dataLayer`.

This change accounts for direct-to-PDP sessions and PLP-level add-to-cart actions, broadens compatibility across Store Framework, FastStore, headless, and custom storefront implementations, and ensures a single Activity Flow event is generated for each user cart action. It also reduces maintenance effort by supporting new cart event naming conventions without requiring code changes, making the Activity Flow Web Script more resilient to different analytics implementations across storefronts.

## What needs to be done?

The cart event capture mechanism depends on cart events being available in the `dataLayer`, since the Activity Flow Web Script reads them from `window.dataLayer` to generate Activity Flow events. Therefore, for this feature to work properly, your storefront must expose cart events in the `dataLayer`.

No extra action is required for stores using VTEX native storefront solutions - FastStore, Store Framework, or CMS Portal (Legacy) - where Activity Flow is installed by default.

If you use a headless storefront, make sure the [Activity Flow Web Script](https://developers.vtex.com/docs/guides/installing-activity-flow-in-headless-stores) is installed and loaded only once per page. Once the script is in place, the improved cart event capture applies automatically.

To learn more about Activity Flow, see [VTEX Activity Flow](https://developers.vtex.com/docs/guides/activity-flow).
