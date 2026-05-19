---
title: "Gathering delivery promise information"
slug: "gathering-delivery-promise-information"
hidden: false
createdAt: "2026-03-05T00:00:00.000Z"
updatedAt: "2026-03-05T00:00:00.000Z"
excerpt: "Learn how to retrieve the delivery zones, pickup points, and delivery suggestions needed to display delivery promise information in your storefront."
seeAlso:
 - "/docs/guides/delivery-promise"
 - "/docs/guides/delivery-promise-suggestions-api-headless-integration"
 - "/docs/guides/setting-up-delivery-promise-components"
 - "/docs/guides/delivery-promise-for-headless-stores"
 - "/docs/guides/faststore/features-delivery-promise"
 - "https://help.vtex.com/docs/tutorials/delivery-promise-faq"
---

>ℹ️ This feature is in beta, and we are actively working to improve it. If you have any questions, please contact [our Support](https://help.vtex.com/en/support).

[**Delivery Promise**](https://developers.vtex.com/docs/guides/delivery-promise) is VTEX's solution that lets shoppers see only the products they can actually buy, taking into account product availability and the shipping methods valid for their delivery address. The [Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api) builds on this by surfacing the most relevant delivery and pickup options directly in the storefront, such as the fastest delivery available or the nearest pickup point.

This guide walks you through the data you need to collect before rendering any UI: the available delivery zones, the available pickup points, and the resulting delivery promise suggestions for a shopper's location.

## Delivery zones

Use the [`POST` Search delivery zones](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/delivery-zones/_search/v2) endpoint to retrieve the following information:

- Delivery zone IDs
- Delivery zones hash
- Country code

Response example:

```json
{
   "deliveryZoneIds": [
         "BRA_COUNTRY",
         "BRA_REGION_NORDESTE",
         "BRA_SUBSTATE_PB_INTERIOR"
   ],
   "deliveryZonesHash": "c3e1a42f7b9d4e81aafe24ba6e7b120f",
   "countryCode": "BRA"
}
```

Use the `deliveryZonesHash` value when you search for delivery suggestions.

## Delivery pickup points

To retrieve the available pickup points for the shopper, use the [`POST` Search pickup points](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/pickuppoints/_search) endpoint.

Response example:

```json
{
   "pickupPointDistances": [
         {
            "pickupId": "fulfillmentqa_vtexsp",
            "distance": 4.990988731384277,
            "pickupName": "VTEX SP",
            "isActive": true,
            "address": {
               "city": "São Paulo",
               "neighborhood": "Itaim Bibi",
               "number": "4440",
               "postalCode": "04538-132",
               "street": "Avenida Brigadeiro Faria Lima",
               "state": "SP"
            },
            "businessHours": [
               {
                     "dayOfWeek": 0,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 1,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 2,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 3,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 4,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 5,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               },
               {
                     "dayOfWeek": 6,
                     "openingTime": "00:00:00",
                     "closingTime": "23:59:00"
               }
            ]
         }
      ],
   "pickupPointsHash": "b92e64d0a08f4c6785e6d0319cbad19a"
}
```

Use the `pickupPointsHash` value when you search for delivery suggestions.

## Delivery Promise suggestions

Use the [`POST` Search delivery suggestions](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/delivery-promise-suggestions/_search) endpoint with the `deliveryZonesHash` and `pickupPointsHash` values in the request body to gather the delivery promise suggestions that will be presented in your storefront. You can use this endpoint for batch processing and for scenarios that involve multiple products.

The following example response illustrates the data you can expect:

```json
{
      "suggestions": [
            {
                  "productId": "123",
                  "suggestions": {
                  "delivery": [
                        {
                              "id": "express-delivery",
                              "name": "Express Delivery",
                              "slaTimeTarget": {
                              "from": 0,
                              "to": 4,
                              "unit": "h"
                              },
                              "conditions": [
                              "fastest"
                              ]
                        },
                        {
                              "id": "standard-delivery",
                              "name": "Standard Delivery",
                              "slaTimeTarget": {
                              "from": 1,
                              "to": 3,
                              "unit": "d"
                              },
                              "conditions": []
                        }
                  ],
                  "pickup": [
                        {
                              "id": "store-downtown",
                              "name": "Downtown Store",
                              "slaTimeTarget": {
                              "from": 0,
                              "to": 2,
                              "unit": "h"
                              },
                              "conditions": [
                              "nearest"
                              ]
                        }
                  ]
                  }
            }
      ]
}
```
