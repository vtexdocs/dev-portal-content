---
title: "B2B session data"
slug: "b2b-session-data"
hidden: false
createdAt: "2026-06-26T00:00:00.000Z"
updatedAt: "2026-07-29T00:00:00.000Z"
excerpt: "Learn how to retrieve and interpret B2B session data enriched by the Shopper Session app, including payment methods, catalog access, and addresses."
---

> ⚠️ This feature is only available to stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available for selected accounts.

The `vtex_session` cookie stores a snapshot of the buyer's session state. For B2B stores, this session is enriched with organization and contract data by the Shopper Session app, covering payment methods, catalog access, and available addresses. This enrichment is available under the `public.facets` and `shopper` namespaces.

This guide explains how to retrieve and interpret that data.

## Retrieving session data

To retrieve the current B2B session data for a logged-in buyer, send a `GET` [Get Session](https://developers.vtex.com/docs/api-reference/session-manager-api#get-/api/sessions?endpoint=get-/api/sessions) request including the `public.facets` and `shopper` namespaces:

```html
GET /api/sessions?items=public.facets,shopper.scopes,shopper.defaults,shopper.firstName,shopper.lastName
Cookie: vtex_session=<current-session-token>
```

**Response example:**

```json
{
  "namespaces": {
    "public": {
      "facets": {
        "value": "productClusterIds=138;productClusterIds=139;productClusterIds=141;productClusterIds=not:140"
      }
    },
    "shopper": {
      "scopes": {
        "value": {
          "vtex.checkout": {
            "creditCards": "visa,mastercard"
          },
          "vtex.payments": {
            "paymentSystemIds": "1,2,3"
          },
          "vtex.catalog": {
            "collectionIds": "138,139,141",
            "excludeCollectionIds": "140"
          },
          "vtex.master-data": {
            "AD": [
              {
                "ids": ["addr-1", "addr-2"]
              }
            ],
            "customFieldValues": [
              {
                "field": "name",
                "value": "customField1",
                "ids": ["field-1", "field-2"]
              }
            ]
          }
        }
      },
      "defaults": {
        "value": {
          "shippingAddress": "default-address-id",
          "paymentMethod": "default-payment-method"
        }
      },
      "firstName": {
        "value": "John"
      },
      "lastName": {
        "value": "Doe"
      }
    }
  }
}
```

## shopper.scopes sub-namespaces

The `shopper.scopes` value is divided into sub-namespaces, each representing a different area of the buyer's organization scope.

| Sub-namespace | Description |
| ----- | ----- |
| `vtex.checkout` | Credit card types (`creditCards`) allowed for the buyer's organization. |
| `vtex.payments` | Payment system IDs (`paymentSystemIds`) available to the buyer based on their contract. |
| `vtex.catalog` | Collection IDs the buyer has access to (`collectionIds`), and excluded collection IDs (`excludeCollectionIds`), restricting the product catalog to what is permitted by their contract. |
| `vtex.master-data` | Address IDs associated with the buyer's organization unit (`AD`), and custom organization fields (`customFieldValues`). |

## public.facets

The `public.facets` value embeds the buyer's catalog access as a query string in the `productClusterIds` format, prefixing excluded collections with `not:`. For example, `productClusterIds=138;productClusterIds=not:140` grants access to collection `138` and excludes collection `140`.

## shopper.defaults, firstName, and lastName

- `shopper.defaults` holds the buyer's default values, such as `shippingAddress` and `paymentMethod`.
- `shopper.firstName` and `shopper.lastName` hold the buyer's name.

## Session data expiration and refresh

This session data is a snapshot taken at session creation time. If the buyer's contract changes after the session is created (for example, a new address is added or a credit limit is updated), the session data will not reflect those changes until a new session is created or the session is explicitly refreshed.

By default, the `vtex_session` cookie has a fixed **5-day expiration**.

## Learn more

- [Session Manager API](https://developers.vtex.com/docs/api-reference/session-manager-api)
- [VTEX Session overview](https://developers.vtex.com/docs/guides/sessions-system-overview)
