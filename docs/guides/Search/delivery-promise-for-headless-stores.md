---
title: "Delivery promise for headless stores (Beta)"
slug: "delivery-promise-for-headless-stores"
hidden: false
excerpt: "Learn how to implement the delivery promise feature in headless stores."
createdAt: "2025-05-14T22:18:24.684Z"
updatedAt: "2025-05-14T22:18:24.684Z"
---

>ℹ️ This feature is in closed beta, which means that only selected customers can access it for now. If you are interested in implementing it in the future, please contact our [Support](https://support.vtex.com/hc/en-us) team.

This guide details how to use the [Delivery Promise](https://help.vtex.com/en/tutorial/delivery-promise-beta--p9EJH9GgxL0JceA6dBswd) feature on headless stores, using [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) with additional facets for this purpose.

Only products that can be delivered to the provided address or picked up at pickup points are displayed, following these rules:

* For pickup points selected in the header or a specific pickup point, the system displays all available pickup points within a 50 km pickup radius configured in Checkout. There is no limit to the number of pickup points shown.

* For the nearby pickup filter, pickup points within a 10 km radius of the buyer's location are shown, with a maximum of 40 pickup points.

## Before you begin

* Make sure you have Intelligent Search installed, namely admin-search and search-resolver. Learn more at [Installing Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4mwZGH252R3CCPRim8v0F3).  
* Complete Catalog integration with Intelligent Search. Learn more at [Starting the integration with Catalog](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/2wBsO1AKTQZ04idbTKszI4).

## Using Delivery Promise parameters

The `GET` [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) endpoint from Intelligent Search API accepts path parameters referred to as facets:

```
https://{accountName}.{environment}.com.br/api/io/_v/api/intelligent-search/product_search/{facets}
```

To enable the Delivery Promise functionality, you should use the following additional query strings and facets on this request. When possible, using query strings is recommended for  better performance.

| Facet | Description | Example |
| :---- | :---- | :---- |
| `zip-code` **\[required\]** | Postal code. It can also be used as a query string. | Query string: **`?zip-code=22250040`**`&coordinates=-43.18218231201172,-22.94549560546875 ` Facet: **`/zip-code/22250040`**`/coordinates/-43.18218231201172,-22.94549560546875` |
| `coordinates` **\[required\]** | Address coordinates. To get the coordinates based on a postal code, follow the steps on [Get address by postal code](https://developers.vtex.com/docs/guides/get-address-by-postal-code) to return the coordinates in the correct and expected value inside the `geoCoordinates` object. It can also be used as a query string. | Query string: `?zip-code=22250040&coordinates=-43.18218231201172,-22.94549560546875 ` Facet: `/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875`  |
| `shipping` | Shipping method. It must always be combined with `zip-code` and `coordinates`. Possible values: `pickup-in-point delivery pickup-all pickup-nearby` | `/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875/shipping/pickup-in-point/` |
| `pickupPoint` | Pickup point ID to filter by a specific pickup point. This is used only with the `shipping/pickup-in-point` facet, besides the required parameters. It can also be used as a query string. |  Query string: `/shipping/pickup-in-point?zip-code=22250040&coordinates=-43.18218231201172,-22.94549560546875&pickupPoint=vtex-botafogo` Facet: `/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875/shipping/pickup-in-point/pickupPoint/vtex-botafogo` |

>⚠️ `zip-code` and `coordinates` are **required** to filter product availability according to the shopper’s location and are integral to any request using Delivery Promise functionality. This means you must use them when filtering by shipping method and pickup point.

### Filtering by location

Here is an example of a basic Delivery Promise search using only postal code and coordinates, which are the required facets:

```
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875
```

### Filtering by shipping method

To filter the search by a shipping method, you must use the `shipping` parameter and some additional optional parameters, depending on the type of filter you want to implement.

The possible filters are:

* [Delivery to the shopper’s ZIP code](#delivery-to-the-shopper’s-zip-code)  
* [Pickup at a specific location](#pickup-at-a-specific-location)  
* [Pickup at a nearby location](?tab=t.0#heading=h.qzpibergwrec)

Learn more about each of them in the following sections.

#### Delivery to the shopper’s ZIP code {#delivery-to-the-shopper’s-zip-code}

Filters the search for products that can be delivered to the zip code entered by the buyer.

Parameters: `/shipping/delivery`

Example:

```
https://{{accountName}}.myvtex.com.br/api/io/_v/api/intelligent-search/product_search/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875/shipping/delivery
```

#### Pickup at a specific location {#pickup-at-a-specific-location}

Filters the search for products that can be picked up at a specific pickup point selected by the buyer. 

Parameters: `/shipping/pickup-in-point/pickupPoint/{pickupPointId}`

>ℹ️ To first fetch the list of pickup points for the store, follow the [List pickup points by location](https://developers.vtex.com/docs/guides/list-pickup-points-by-location) guide and [API reference](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points).

Example:

```
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875/shipping/pickup-in-point/pickupPoint/vtex-botafogo
```

#### Pickup at a nearby location

Filters the search for products that can be picked up at pickup points located within a radius of up to 50 km from the shopper, within the same pickup radius limit as the Checkout.

Parameters: `/shipping/pickup-in-point/pickup-nearby`

Example:

```
https://{{accountName}}.myvtex.com.br/api/io/_v/api/intelligent-search/product_search/zip-code/22250040/coordinates/-43.18218231201172,-22.94549560546875/shipping/pickup-in-point/pickup-nearby 
```

## Implementing sidebar filters

>⚠️ The delivery promise filters are part of a beta feature and may be subject to breaking changes. If you choose to customize this functionality, ensure your implementation can adapt to updates.

In headless implementations, you must manually retrieve and render filters using VTEX Intelligent Search APIs. For example, inside a filter sidebar, where you want users to refine results based on shipping method or pickup location.

You can retrieve available filters using the `GET` [Get facets](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) endpoint and use the response to build a custom filter UI in your headless storefront. For example, mapping `name: "pickup-in-point"` to a checkbox labeled **Pickup in store**.

>⚠️ Delivery-related filters (e.g. delivery, pickup-in-point) are included in the `facets` response. These are tied to the user's session and shipping context ([segment token](https://developers.vtex.com/docs/api-reference/session-manager-api#post-/api/sessions)). Make sure the segment and shipping data are initialized correctly for this to work.

Example request:

```
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