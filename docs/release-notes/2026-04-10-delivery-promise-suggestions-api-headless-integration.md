---
title: "Delivery Promise Suggestions API: New headless integration guide and API"
slug: "2026-04-10-delivery-promise-suggestions-api-headless-integration"
type: added
excerpt: "The new Delivery Promise Suggestions API provides real-time delivery and pickup suggestions for headless storefronts, with a comprehensive integration guide to enhance the shopping experience."
createdAt: "2026-04-10T00:00:00.000Z"
updatedAt: "2026-04-10T00:00:00.000Z"
hidden: false
---

The new [Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api) enables you to display real-time delivery promises and pickup options directly on product listing and detail pages, creating meaningful visual indicators for shoppers.

>ℹ️ This API is in beta, and we are actively working to improve it. If you have any questions, please contact [our Support](https://help.vtex.com/en/support).

## What has been added?

The [Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api) provides four endpoints to help you gather and display delivery information:

**Logistics Shipping:**
- `POST` [Search delivery zones](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/delivery-zones/_search/v2): Retrieves available delivery zones based on location information (postal code, coordinates, and country).
- `POST` [Search pickup points](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/pickuppoints/_search): Finds available pickup points near a given address with distance constraints.

**Delivery Promise Suggestions:**
- `POST` [Search delivery suggestions](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/delivery-promise-suggestions/_search): Retrieves delivery and pickup suggestions for a batch of products (up to 20 products).
- `GET` [Get delivery suggestions](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#get-/api/delivery-promise-suggestions): Retrieves suggestions using query parameters, supporting caching and browser optimizations.

## Why did we make this change?

This API extends the [Delivery Promise](https://developers.vtex.com/docs/guides/delivery-promise) solution to headless storefronts, enabling you to:

- Display only products available for the shopper's location with valid shipping methods.
- Highlight the most relevant delivery and pickup options directly on the storefront.
- Provide accurate delivery time estimates using precomputed fulfillment contexts for better performance.
- Enhance the shopping experience with clear, contextual delivery promises.

## What needs to be done?

If you manage a headless storefront and want to integrate delivery promise suggestions, follow the [headless integration guide](https://developers.vtex.com/docs/guides/delivery-promise-suggestions-api-integration) to implement the API endpoints.

For more information about Delivery Promise, see:
- [Delivery Promise guide](https://developers.vtex.com/docs/guides/delivery-promise)
- [Setting up Delivery Promise components](https://developers.vtex.com/docs/guides/setting-up-delivery-promise-components)
- [Delivery Promise for headless stores](https://developers.vtex.com/docs/guides/delivery-promise-for-headless-stores)
- [Delivery Promise FAQ](https://help.vtex.com/docs/tutorials/delivery-promise-faq)
