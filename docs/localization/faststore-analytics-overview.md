---
title: Analytics
slug: faststore-analytics-overview
createdAt: 2024-11-05T18:10:15.623Z
updatedAt: ""
---

The Analytics module manages events on a website. The module is composed of two main functions:

- [`sendAnalyticsEvent`](/TBD): Fires events in the browser. Events fired using this function are shared only with the website's origin. The event is wrapped and sent to the [Window object](https://developer.mozilla.org/en-US/docs/Web/API/Window) via standard `postMessage` calls.
- [`useAnalyticsEvent`](/TBD): Intercepts fired events and usually communicates with an analytics provider.

![Analytics module](https://vtexhelp.vtexassets.com/assets/docs/src/analyticsmodule___37ad6fdb1e969835206b6d4b91461529.png)

> ⚠️ Events sent via the Analytics module are not automatically sent to any analytics provider (e.g., Google Analytics). To connect with a provider, configure the [`useAnalyticsEvent`](LINK) hook.

The Analytics module supports sending and receiving different events, allowing you to implement custom event types and override default ones.

Additionally,  the Analytics module offers built-in [ecommerce event](https://support.google.com/analytics/answer/14434488?hl=en) types based on the [Google Analytics 4 (GA4) data model](https://developers.google.com/analytics/devguides/collection/ga4/reference/events).

## List of native event types

The Analytics module comes with native types based on [ecommerce events](https://support.google.com/analytics/answer/14434488?hl=en). All event types are available for use and extension. Here is a list of events natively supported by the Analytics module:

| Type | Parameters |
| --- | --- |
| `add_payment_info` | `currency`, `value`, `coupon`, `payment_type`, and `items` |
| `add_shipping_info` | `currency`, `value`, `coupon`, `shipping_tier`, and `items` |
| `add_to_cart` | `currency`, `value`, and `items` |
| `add_to_wishlist` | `currency`, `value`, and `items` |
| `begin_checkout` | `currency`, `value`, `coupon`, and `items` |
| `login` | `method` |
| `page_view` | `page_title`, `page_location`, and `send_page_view` |
| `purchase` | `currency`, `transaction_id`, `value`, `affiliation`, `coupon`, `shipping`, `tax`, and `items` |
| `refund` | `currency`, `transaction_id`, `value`, `affiliation`, `coupon`, `shipping`, `tax`, and `items` |
| `remove_from_cart` | `currency`, `value`, and `items` |
| `search` | `search_term` |
| `select_item` | `item_list_id`, `item_list_name`, and `items` |
| `select_promotion` | `item_list_id`, `item_list_name`, and `items` |
| `share` | `method`, `content_type`, and `item_id` |
| `signup` | `method`, `content_type`, and `item_id` |
| `view_cart` | `currency`, `value`, and `items` |
| `view_item` | `currency`, `value`, and `items` |
| `view_item_list` | `item_list_id`, `item_list_name`, and `items` |
| `view_promotion` | `items` |

Each event exports at least two types: one for the event parameters and one for the event type itself. For example, the `add_to_cart` event has two exported types: `AddToCartParams<T extends Item = Item>` and `AddToCartEvent<T extends Item = Item>`.

Some types are [common](https://github.com/vtex/faststore/blob/main/packages/sdk/src/analytics/events/common.ts) to all events, such as the `Item` type. These types are particularly useful when overriding `Item` properties or a whole `Item` itself.

## Google Analytics 4

Google Analytics is the industry-leading analytics solution that most ecommerce websites use, and the Analytics module was designed with this in mind. All the helper functions and hooks in the module use the [Google Analytics 4 (GA4) data model](https://developers.google.com/analytics/devguides/collection/ga4/reference/events) by default. This allows you to use [code hinting](#code-hinting) tools to receive suggestions of GA4 events and their recommended properties while coding.

To send the events to Google Analytics, use the [`useAnalyticsEvent`](/TBD) hook. The hook must listen to events from [`sendAnalyticsEvents`](/TBD) and add them to the `dataLayer` (recommended for Google Tag Manager) or call the `gtag` function directly (for `gtag` script implementations).

## Code hinting

By leveraging the type definitions in the Analytics module, you can use [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) suggestions for code hinting.

![IntelliSense](https://vtexhelp.vtexassets.com/assets/docs/src/intellisense___44c8c3c8f2687f88e787ce38f867901c.png)
