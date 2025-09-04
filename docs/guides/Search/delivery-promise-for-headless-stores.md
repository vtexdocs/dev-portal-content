---
title: "Delivery promise for headless stores (Beta)"
slug: "delivery-promise-for-headless-stores"
hidden: false
excerpt: "Learn how to implement the delivery promise feature in headless stores."
createdAt: "2025-05-14T22:18:24.684Z"
updatedAt: "2025-05-14T22:18:24.684Z"
---

>ℹ️ This feature is in closed beta, which means that only selected customers can access it. If you are interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

This guide details how to use the [Delivery Promise](https://help.vtex.com/en/tutorial/delivery-promise-beta--p9EJH9GgxL0JceA6dBswd) feature on headless stores, using the [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) with additional facets.

With Delivery Promise enabled, only products that can be delivered to the provided address or picked up at pickup points are displayed, following these rules:

* The system displays all available pickup points within the 50 km radius configured in Checkout. This applies when the customer selects pickup in the header or a specific pickup point. There’s no limit to the number of pickup points displayed.

* For the nearby pickup filter, the system displays pickup points within a 10 km radius of the buyer's location, up to 40 pickup points.

## Before you begin

* Make sure you have Intelligent Search installed, namely admin-search and search-resolver. Learn more in [Installing Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4mwZGH252R3CCPRim8v0F3).
* Complete Catalog integration with Intelligent Search. Learn more in [Starting the integration with Catalog](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/2wBsO1AKTQZ04idbTKszI4).

## Using Delivery Promise parameters

The `GET` [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) endpoint from Intelligent Search API accepts path parameters referred to as facets:

```txt
https://{accountName}.{environment}.com.br/api/io/_v/api/intelligent-search/product_search/{facets}
```

To enable the Delivery Promise functionality, you should use the following additional query strings and facets on this request. We recommend using query strings when possible for better performance.

| Query string / Facet | Description | Example |
| :---- | :---- | :---- |
| `zip-code` **\[required\]** | Postal code. | Query string: **`?zip-code=22250040`**`
| `shipping` | Shipping method. It must always be combined with `zip-code`. Possible values: `pickup-in-point delivery pickup-all pickup-nearby` | `/shipping/pickup-in-point/?zip-code=22250040` |
| `pickupPoint` | Pickup point ID to filter by a specific pickup point. This is used only with the `shipping/pickup-in-point` facet, besides the required parameters.|  Query string: `/shipping/pickup-in-point?zip-code=22250040&pickupPoint=vtex-botafogo` |
| `hideUnavailableItems` | When set to `true`, this query parameter ensures only products actually available for delivery or pickup are returned. If omitted, products with the `showIfNotAvailable` property set to `true` in Catalog may appear even if unavailable. | Query string: `?hideUnavailableItems=true` |

>⚠️ `zip-code` is **required** to filter product availability based on the shopper’s location and is integral to any request using Delivery Promise. You must use it when filtering by shipping method and pickup point.

>⚠️ To ensure only products that are available for delivery or pickup are returned, you must include the `hideUnavailableItems=true` query parameter in your requests. If this parameter is omitted, the search engine will include products with the `showIfNotAvailable` property set to `true` in the Catalog module even if they are not available for delivery or pickup. For example, product `649553` may appear in results if it has `showIfNotAvailable` enabled, unless you explicitly set `hideUnavailableItems=true`.

### Filtering by location

Here is an example of a basic Delivery Promise search using only postal code:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search?zip-code=22250040
```

### Filtering by shipping method

To filter the search by a shipping method, you must use the `shipping` parameter and some additional optional parameters, depending on the type of filter you want to implement.

The possible filters are:

* [Delivery to the shopper’s postal code](#delivery-to-the-shoppers-zip-code)
* [Pickup at a specific location](#pickup-at-a-specific-location)
* [Pickup at a nearby location](?tab=t.0#heading=h.qzpibergwrec)

Learn more about each of them in the following sections.

#### Delivery to the shopper’s ZIP code

Filters the search for products that can be delivered to the postal code entered by the buyer.

Parameters: `/shipping/delivery`

Example:

```txt
https://{{accountName}}.myvtex.com.br/api/io/_v/api/intelligent-search/product_search/shipping/delivery?zip-code=22250040
```

#### Pickup at a specific location

Filters the search for products that can be picked up at a specific pickup point selected by the buyer.

Parameters: `/shipping/pickup-in-point/pickupPoint/{pickupPointId}`

>ℹ️ To first fetch the list of pickup points for the store, follow the [List pickup points by location](https://developers.vtex.com/docs/guides/list-pickup-points-by-location) guide and [API reference](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points).

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/shipping/pickup-in-point/pickupPoint/vtex-botafogo?zip-code=22250040
```

#### Pickup at a nearby location

Filters the search for products that can be picked up at pickup points located within a radius of up to 50 km from the shopper, within the same pickup radius limit as the Checkout.

Parameters: `/shipping/pickup-in-point/pickup-nearby`

Example:

```txt
https://{{accountName}}.myvtex.com.br/api/io/_v/api/intelligent-search/product_search/shipping/pickup-in-point/pickup-nearby?zip-code=22250040
```

## Implementing sidebar filters

>⚠️ The delivery promise filters are a beta feature and may be subject to breaking changes. If you customize this functionality, ensure your implementation can adapt to updates.

In headless implementations, you must manually retrieve and render filters using the VTEX Intelligent Search APIs — for example, in a filter sidebar where users can refine results by shipping method or pickup location.

You can retrieve available filters using the `GET` [Get facets](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) endpoint and use the response to build a custom filter UI in your headless storefront. For example, mapping `name: "pickup-in-point"` to a checkbox labeled **Pickup in store**.

>⚠️ Delivery-related filters (for example, delivery and pickup-in-point) are included in the `facets` response. These are tied to the user's session and shipping context ([segment token](https://developers.vtex.com/docs/api-reference/session-manager-api#post-/api/sessions)). Make sure the segment and shipping data are initialized correctly for this to work.

Example request:

```txt
GET https://{{accountName}}.myvtex.com/_v/api/intelligent-search/facets/?query=moisturizer
```

Example response:

```json
{
  "facets": [
    {
      "name": "Shipping Method",
      "values": [
        { "id": "delivery", "name": "Delivery", "quantity": 142 },
        { "id": "pickup-in-point", "name": "Pickup in Store", "quantity": 37 }
      ]
    },
    {
      "name": "Pickup Location",
      "values": [
        { "id": "vtex-botafogo", "name": "VTEX Botafogo", "quantity": 12 },
        { "id": "vtex-sp", "name": "VTEX Sao Paulo", "quantity": 8 }
      ]
    }
  ]
}
```
