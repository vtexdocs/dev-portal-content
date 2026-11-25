---
title: "Implementing transparent integration for VTEX Ads"
slug: "implementing-transparent-integration-for-vtex-ads"
hidden: false
createdAt: "2026-11-13T00:00:00.000Z"
updatedAt: "2026-11-13T00:00:00.000Z"
excerpt: "Set up transparent integration for Banner and Video ads using the VTEX Ads script and a client-side conversion beacon."
---

> ⚠️ Transparent integration only serves Banner and Video ads.

Transparent integration is a low-friction setup designed to start a **VTEX Ads** integration on your website or mobile site (`msite`) in the simplest way possible. Instead of building a full custom API integration upfront, you combine an active catalog integration with a client-side **VTEX Ads** script and a browser conversion event.

> ℹ️ For the broader **VTEX Ads** integration landscape, see [VTEX Ads](https://developers.vtex.com/docs/guides/vtex-ads).

## Before you begin

Make sure the following requirements are in place before setting up the transparent integration:

- **Catalog integration:** You have an active catalog integration following the standard **VTEX Ads** format. See [Synchronizing the catalog with VTEX Ads](https://developers.vtex.com/docs/guides/synchronizing-the-catalog-with-vtex-ads).
- **Publisher ID:** You have your `publisher_id` identifier for **VTEX Ads**, which is required in the conversion event payload.
- **Session and user parameter origins:** You know where your storefront stores `session_id` and `user_id` (cookies, `sessionStorage`, or `localStorage`).

## 1. Install the transparent integration script

Add the following script tag as early as possible inside the `<head>` tag of your website or mobile site (`msite`):

```html
<script src="https://cdn.newtail.com.br/retail-media/scripts/vtexads-magic-1.0.0.js"></script>
```

> ℹ️ The `vtexads-magic-1.0.0.js` script applies only to this transparent integration and doesn't replace `vtexads-agent.1.0.0.js`, which is documented in [VTEX Ads Script Agent](https://developers.vtex.com/docs/guides/vtex-ads-script-agent). For custom API integrations that send browser impression and click events directly, see [Ads events notification](https://developers.vtex.com/docs/guides/ads-events-notification).

### Share session and user parameter origins

For `vtexads-magic-1.0.0.js` to work properly, you must inform the **VTEX Ads** team of the origin of two parameters on your storefront:

- `session_id`
- `user_id`

These parameters are usually stored in cookies, `sessionStorage`, or `localStorage`.

## 2. Send the client-side conversion event

Trigger the conversion event on the client side after the order is created, without waiting for payment confirmation.

Use the `navigator.sendBeacon` interface to send the conversion payload as a JSON `Blob` (`application/json`) to `https://newtail-media.newtail.com.br/v1/beacon/conversion`. Because `navigator.sendBeacon` sends small amounts of data asynchronously, it transmits conversion analytics before the user navigates away from the page without affecting current page performance or the load time of the next page.

> ℹ️ This client-side `navigator.sendBeacon` flow is the authoritative conversion path for the transparent integration. Unlike the standard server-side flow in [Conversion](https://developers.vtex.com/docs/guides/conversion) and `POST` [Track conversions](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/conversion), which sends a server-side request to `events.newtail-media.newtail.com.br` when an order is closed, this integration sends a browser beacon to `https://newtail-media.newtail.com.br/v1/beacon/conversion` after order creation without payment confirmation.

```javascript
const data = {
  "publisher_id": "d4dff0cb-1f21-4a96-9acf-d9426a5ed08c",
  "user_id": "26119121",
  "order_id": "1758035060",
  "channel": "site|msite|app",
  "created_at": "2025-09-16T15:04:19.794Z",
  "items": [
    {
      "price": 12,
      "promotional_price": 10,
      "quantity": 1,
      "sku": "sku1"
    },
    {
      "price": 15,
      "promotional_price": 13,
      "quantity": 1,
      "sku": "sku2",
      "seller_id": "seller1"
    },
    {
      "price": 19,
      "promotional_price": 17,
      "quantity": 1,
      "sku": "sku3",
      "product_id": "prod3"
    },
    {
      "price": 30,
      "promotional_price": 25,
      "quantity": 2,
      "sku": "sku4",
      "product_id": "prod4",
      "seller_id": "seller2"
    }
  ]
};

const rawData = JSON.stringify(data);
const blob = new Blob([rawData], { type: 'application/json' });
const url = "https://newtail-media.newtail.com.br/v1/beacon/conversion";

const success = navigator.sendBeacon(url, blob);

if (success) {
  console.log("Beacon request successfully queued!");
} else {
  console.error("Failed to queue beacon request.");
}
```

Keep the following behavior and payload details in mind when implementing this snippet:

- **Channel value:** The `channel` field specifies the channel where the order was created (`site`, `msite`, or `app`).
- **Item fields:** Each entry in `items` includes `price`, `promotional_price`, `quantity`, and `sku`, and can optionally include `seller_id` and `product_id`.
- **Queue status:** The `navigator.sendBeacon` method returns `true` if the browser queues the request for delivery and `false` otherwise. Because `navigator.sendBeacon` doesn't return a `Promise`, you can't use `.then()` or `.catch()`. Delivery is highly likely, though not guaranteed.

## Next steps

- [Synchronizing the catalog with VTEX Ads](https://developers.vtex.com/docs/guides/synchronizing-the-catalog-with-vtex-ads): Set up or verify product and inventory synchronization for your store catalog.
- [Ads events notification](https://developers.vtex.com/docs/guides/ads-events-notification): Learn how custom integrations send browser impression and click notifications.
- [Conversion](https://developers.vtex.com/docs/guides/conversion): Review the server-side conversion `POST` flow used in full API integrations when an order is closed.
- [VTEX Ads API overview](https://developers.vtex.com/docs/api-reference/vtex-ads-api): Explore the complete REST API if you wish to implementa full VTEX Ads integration.
