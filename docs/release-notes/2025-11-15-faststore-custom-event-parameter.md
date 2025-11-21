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

The [`sendAnalyticsEvent`](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) function in FastStore now supports a new `isEcommerceEvent` parameter, giving developers more flexibility when sending custom analytics events to Google Analytics 4.

## What has changed?

Previously, all events sent via `sendAnalyticsEvent` were automatically wrapped in an `ecommerce` object. This structure follows the Google Analytics 4 ecommerce events format.

While this was ideal for commerce-related events (add to cart, purchase, etc.), it wasn't suitable for custom events tracking non-commerce activities like newsletter, user interactions, or feature usage.

With the new `isEcommerceEvent` parameter, developers can now:

- **Set `isEcommerceEvent: false`** for custom events to send parameters at the top level, following the GA4 custom events format.
- **Keep the default `isEcommerceEvent: true`** (or omit the parameter) for ecommerce events to maintain the nested `ecommerce` object structure.

### Event structure comparison

**Custom event with `isEcommerceEvent: false`:**

```typescript
sendAnalyticsEvent({
  name: 'newsletter_signup',
  isEcommerceEvent: false,
  params: {
    method: 'footer_form',
    user_type: 'new_visitor'
  }
})
```

Sends to dataLayer as:

```json
{
  "event": "newsletter_signup",
  "method": "footer_form",
  "user_type": "new_visitor"
}
```

**Ecommerce event (default behavior):**

```typescript
sendAnalyticsEvent({
  name: 'add_to_cart',
  params: {
    currency: 'USD',
    value: 29.99,
    items: [{ item_id: '12345' }]
  }
})
```

Sends to dataLayer as:

```json
{
  "event": "add_to_cart",
  "ecommerce": {
    "currency": "USD",
    "value": 29.99,
    "items": [{ "item_id": "12345" }]
  }
}
```

## Why did we make this change?

This change improves the Analytics module's flexibility by allowing developers to send custom events that properly align with Google Analytics 4 event structures.

Custom events tracking non-commerce activities (like user preferences, content interactions, or feature usage) now follow the recommended GA4 format, improving data accuracy and reporting capabilities.

## What needs to be done?

To use the `isEcommerceEvent`, follow these steps:

1. Add the `isEcommerceEvent: false` parameter to your `sendAnalyticsEvent` calls for custom events.
2. Structure your event parameters according to your analytics requirements.

For detailed examples and implementation guidance, refer to the [sendAnalyticsEvent](https://developers.vtex.com/docs/guides/faststore/analytics-send-analytics-event) and the [Sending custom events](https://developers.vtex.com/docs/guides/faststore/analytics-sending-custom-events) guides.
