---
title: "Conversion"
slug: "conversion"
excerpt: "Track when an ad leads to a purchase."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

Conversion tracking is crucial for measuring ad campaign effectiveness in VTEX Ads. This guide explains how to properly send conversion events when users complete purchases after interacting with your advertisements.

## Conversion event rules

- Conversion events should be sent when an order is closed.
- Each conversion requires both `user_id` and `session_id` for proper attribution.
- Events must include complete order information including items and customer details, as detailed in `POST` [Track conversions](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/conversion).
- Prices must be sent per unit. Don't multiply the `price` or `promotional_price` by the `quantity`.
- All customer identifiers (email, phone, etc.) must be hashed for privacy.

> 🚧 Don't construct event URLs manually. Always use the URL provided from the `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) request.
>
> This is extremely important to ensure long-term stability of the integration, because the parameters of the event URL may change over time, but the integration itself does not.

## Sending a conversion event

Use the `POST` [Track conversions](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/conversion) endpoint to send conversion events. Check the endpoint documentation for detailed information about all available fields.

Request example:

```json
POST https://events-api.ads.vtex.com/v1/beacon/conversion HTTP/1.1
accept: application/json
content-type: application/json

{
  "channel": "ecommerce",
  "publisher_id": "xxx",
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499",
  "order_id": "123",
  "email_hashed": "xyz",
  "items": [
    {
      "sku": "12221",
      "seller_id": "1234",
      "product_id": "4567",
      "quantity": 1,
      "price": 2000.00,
      "promotional_price": 1899.00
    },
    {
      "sku": "12222",
      "seller_id": null,
      "product_id": "4568",
      "quantity": 2,
      "price": 500.00,
      "promotional_price": 400.00
    }
  ],
  "created_at": "2023-01-01T09:20:00Z"
}
```

Sucessful response example:

>ℹ️ A successful response will have HTTP code 202.

```json
{
 "messages": [
  "conversion will be processed soon"
 ]
}
```

Failed response example:

>ℹ️ A failed response will have HTTP code 422. The error message follows the [RFC 8927](https://datatracker.ietf.org/doc/rfc8927/) format.

```json
[
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'user_id'",
        "params": {
            "missingProperty": "user_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'order_id'",
        "params": {
            "missingProperty": "order_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'publisher_id'",
        "params": {
            "missingProperty": "publisher_id"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'items'",
        "params": {
            "missingProperty": "items"
        },
        "schemaPath": "#/required"
    },
    {
        "instancePath": "",
        "keyword": "required",
        "message": "must have required property 'created_at'",
        "params": {
            "missingProperty": "created_at"
        },
        "schemaPath": "#/required"
    }
]
```
