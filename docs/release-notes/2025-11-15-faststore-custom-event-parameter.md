---
title: "FastStore: New parameter for custom analytics events"
slug: "2025-11-15-faststore-custom-event-parameter"
type: improved
excerpt: "The sendAnalyticsEvent function now supports the isEcommerceEvent parameter, allowing developers to send custom analytics events without the GA4 ecommerce structure."
createdAt: "2025-11-15T00:00:00.219Z"
updatedAt: "2025-11-15T00:00:00.219Z"
hidden: false
tags:
    - FastStore
---

The [`sendAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) function in FastStore now supports the new `isEcommerceEvent` parameter, giving developers more flexibility when sending custom analytics events to Google Analytics 4.

## What has changed?

Previously, all events sent via `sendAnalyticsEvent` were automatically wrapped in an `ecommerce` object. This structure follows the Google Analytics 4 ecommerce events format.

While this approach worked well for commerce-related events such as add-to-cart and purchase, it wasn’t suitable for custom events that track non-commerce activities like newsletter interactions, user actions, or feature usage.

The new `isEcommerceEvent` parameter lets developers choose how events are structured:

- **Custom events:** Set `isEcommerceEvent: false` to send parameters at the top level, following the GA4 custom events format.
- **Ecommerce events:** Keep the default `isEcommerceEvent: true` to send data inside the `ecommerce` object.

## Why did we make this change?

This update enhances the flexibility of the Analytics module, enabling developers to send custom events that align with the recommended Google Analytics 4 event formats.

Custom events tracking non-commerce activities, such as user preferences, content interactions, or feature usage, now follow the appropriate GA4 structure, resulting in more accurate data and clearer reporting.

## What needs to be done?

To use the `isEcommerceEvent`, follow these steps:

1. Add the `isEcommerceEvent: false` parameter to your `sendAnalyticsEvent` calls for custom events.
2. Structure your event parameters according to your analytics requirements.

For detailed examples and implementation guidance, refer to the [sendAnalyticsEvent](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) and the [Sending custom events](https://developers.vtex.com/docs/guides/faststore/analytics-sending-custom-events) guides.
