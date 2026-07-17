---
title: "B2B session data"
slug: "b2b-session-data"
hidden: false
createdAt: "2026-06-26T00:00:00.000Z"
updatedAt: "2026-06-26T00:00:00.000Z"
excerpt: "Learn how to retrieve and interpret B2B session data from the shopperPolicies namespace, including payment methods, catalog access, addresses, and fulfillment restrictions."
---

> ⚠️ This feature is only available to stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available for selected accounts.

The `vtex_session` cookie stores a snapshot of the buyer's session state, including B2B scope data derived from the buyer's contract. This data is available under the `shopperPolicies` namespace and covers payment methods, catalog access, available addresses, and fulfillment restrictions.

This guide explains how to retrieve and interpret that data.

## Retrieving session data

To retrieve the current B2B session data for a logged-in buyer, send a [`Get Session`](https://developers.vtex.com/docs/api-reference/session-manager-api#get-/api/sessions?endpoint=get-/api/sessions) request including the `shopperPolicies` namespace:

```html
GET /api/sessions?items=shopperPolicies
Cookie: vtex_session=<current-session-token>
```

**Response example:**

```json
{
  "namespaces": {
    "shopperPolicies": {
      "value": {
        "vtex.checkout": {
          "customFields": [
            {
              "name": "costCenter",
              "enabled": true,
              "required": true,
              "level": "item",
              "type": "string",
              "value": "xxx"
            }
          ]
        },
        "vtex.fulfillment": {
          "restrictions": [
            {
              "name": "deliveryDayAndHours",
              "enabled": true,
              "required": true,
              "level": "address",
              "type": "string",
              "value": "monday-friday, 8am-5pm"
            }
          ]
        },
        "vtex.payments": {
          "paymentSystemIds": "101,203"
        },
        "vtex.catalog": {
          "collectionsIds": "1,5,7"
        },
        "vtex.profile": {
          "addressIds": "40692,515"
        }
      }
    }
  }
}
```

## shopperPolicies sub-namespaces

The `shopperPolicies` namespace is divided into sub-namespaces, each representing a different area of the buyer's B2B contract.

| Sub-namespace | Description |
| ----- | ----- |
| `vtex.checkout` | Custom fields that apply to the order placement workflow. Each field has a `level` (`item`, `address`, or `orderform`) indicating where it applies within the order. |
| `vtex.fulfillment` | Contract-based restrictions that apply to the fulfillment workflow, such as allowed delivery days and hours or eligible pickup points. |
| `vtex.payments` | Payment method IDs available to the buyer based on their contract. |
| `vtex.catalog` | Collection IDs the buyer has access to, restricting the product catalog to what is permitted by their contract. |
| `vtex.profile` | Address IDs associated with the buyer's profile. |

## Session data expiration and refresh

The `shopperPolicies` data is a snapshot taken at session creation time. If the buyer's contract changes after the session is created (for example, a new address is added or a credit limit is updated), the session data will not reflect those changes until a new session is created or the session is explicitly refreshed.

By default, the `vtex_session` cookie has a fixed **5-day expiration**.

## Learn more

- [Session Manager API](https://developers.vtex.com/docs/api-reference/session-manager-api)
- [VTEX Session overview](https://developers.vtex.com/docs/guides/sessions-system-overview)
