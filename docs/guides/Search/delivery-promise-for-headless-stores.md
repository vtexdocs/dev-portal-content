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

* The system displays all available pickup points within the 50 km radius configured in Checkout. This applies when the customer selects pickup in the header or a specific pickup point. There’s no limit to the number of pickup points displayed. To enable this functionality, you must fetch the complete list of pickup points using the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points). Retrieving this list is a mandatory dependency for the Delivery Promise feature in headless stores.
* For the nearby pickup filter, pickup points within a 10 km radius of the buyer's location are shown, with a maximum of 40 pickup points.

## Before you begin

* Make sure you have Intelligent Search installed, namely admin-search and search-resolver. Learn more at [Installing Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4mwZGH252R3CCPRim8v0F3).
* Complete Catalog integration with Intelligent Search. Learn more at [Starting the integration with Catalog](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/2wBsO1AKTQZ04idbTKszI4).

## Using Delivery Promise parameters

The `GET` [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-) endpoint from Intelligent Search API accepts path parameters referred to as facets:

```txt
https://{accountName}.{environment}.com.br/api/io/_v/api/intelligent-search/product_search/{facets}
```

To enable the Delivery Promise functionality, you should use the following additional query strings and facets on this request. When possible, using query strings is recommended for better performance.

| Query string / Facet | Description | Example |
| :---- | :---- | :---- |
| `zip-code` **\[required\]** (query string) | Postal code. | **`?zip-code=22250040`** |
| `shipping` (facet) | Shipping method. It must always be combined with `zip-code`. Possible values: `pickup-in-point`, `delivery`, `pickup-all`, `pickup-nearby` | `/shipping/pickup-in-point/?zip-code=22250040` |
| `pickupPoint` (query string) | Pickup point ID to filter by a specific pickup point. This is used only with the `shipping/pickup-in-point` facet, besides the required parameters. |  `/shipping/pickup-in-point?zip-code=22250040&pickupPoint=vtex-botafogo`  |
| `delivery-options` (facet) | [Delivery Option](https://help.vtex.com/en/tutorial/delivery-options-beta--1fRDJFcHCtpTnk7GNyaRDY) ID or IDs to be filtered. The ID can be obtained in the VTEX Admin, at **Shipping > Delivery Options**. It must always be combined with `zip-code`. Multiple entries of this filter can be used in the request to search for multiple Delivery Options. | **`/delivery-options/express-option-id`**`?zip-code=22250040` |
| `dynamic-estimate` (facet) | The Dynamic Estimate filter selects Delivery Options that can meet the requested delivery or pickup timeframe. It must always be used together with `zip-code` and `shipping`. Possible values: `same-day`, `next-day`. It dynamically identifies which Delivery Options for the given `zip-code` and `shipping` facet can meet the requested timeframe, and then filters the search as if those Delivery Options had been manually passed as filters. | `/shipping/delivery/dynamic-estimate/same-day?zip-code=22250040` |
| `hideUnavailableItems` (query string) | Controls whether the search returns only available products or both available and unavailable ones. When set to `true`, only products with stock are returned; when set to `false`, the API includes unavailable products as well. A product is considered unavailable when `availableQuantity = 0`, while `availableQuantity = 10000` indicates that the product is available. Retailers may choose to show unavailable items for commercial reasons (for example, to signal that they carry those products even if temporarily out of stock), while the recommended default is `true`. This facet also allows merchants to expose a shopper-facing filter such as "show only in-stock products."<br><br> If `hideUnavailableItems` is omitted, products with the `ShowIfNotAvailable` property set to `true` in the Catalog may appear even if unavailable. Learn more about the `ShowIfNotAvailable` property in the [Catalog API reference](https://developers.vtex.com/docs/api-reference/catalog-api?endpoint=get-/api/catalog_system/pvt/sku/stockkeepingunitbyid/-skuId-). | `?hideUnavailableItems=true` |

>⚠️ `zip-code` is **required** to filter product availability according to the shopper’s location and is integral to any request using Delivery Promise functionality. This means you must use it when filtering by shipping method and pickup point.

>⚠️ To ensure only products that are available for delivery or pickup are returned, you must include the `hideUnavailableItems=true` query parameter in your requests. If this parameter is omitted, the search engine will include products with the `ShowIfNotAvailable` property set to `true` in the Catalog module even if they are not available for delivery or pickup. For example, product `649553` may appear in results if it has `ShowIfNotAvailable` enabled, unless you explicitly set `hideUnavailableItems=true`. Learn more about the `ShowIfNotAvailable` property in the [Catalog API reference](https://developers.vtex.com/docs/api-reference/catalog-api?endpoint=get-/api/catalog_system/pvt/sku/stockkeepingunitbyid/-skuId-).

For more information on facet options apart from the ones directly related to Delivery Promise, go to `GET` [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-).

### Filter combinations

When shoppers apply filters, the API combines them according to the following rules:

* **Facets of the same type → OR (union):** when multiple values of the same facet are applied, the API returns the union of all products matching any of those values.  
* **Facets of different types → AND (intersection):** when different facet types are combined, the API returns only the products that satisfy all selected facet conditions simultaneously.

This results in the following behavior when using Delivery Options and Dynamic Estimates:

* **Multiple Delivery Options → OR (union):** the API returns all products that match any of the delivery options selected by the shopper.  
* **Dynamic Estimate \+ Delivery Option → AND (intersection):** the API returns only the products that satisfy both the selected dynamic estimate and the chosen delivery option.

### Filtering by location

Here is an example of a basic Delivery Promise search using only postal code:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search?zip-code=22250040
```

### Filtering by shipping method

To filter the search by a shipping method, you must use the `shipping` parameter and some additional optional parameters, depending on the type of filter you want to implement.

The possible filters are:

* [Delivery to the shopper’s ZIP code](#delivery-to-the-shopper's-zip-code)
* [Pickup at a specific location](#pickup-at-a-specific-location)
* [Pickup at a nearby location](#pickup-at-a-nearby-location)

Learn more about each of them in the following sections.

#### Delivery to the shopper’s ZIP code

Filters the search for products that can be delivered to the zip code entered by the buyer.

Parameters: `/shipping/delivery`

Example:

```txt
https://{{accountName}}.myvtex.com.br/api/io/_v/api/intelligent-search/product_search/shipping/delivery?zip-code=22250040
```

#### Pickup at a specific location

Filters the search for products that can be picked up at a specific pickup point selected by the buyer.

Parameters: `/shipping/pickup-in-point/pickupPoint/{pickupPointId}`

>ℹ️ We are working on an endpoint that will simplify retrieving pickup points directly. For now, to fetch the list of pickup points for the store and their IDs, follow the [List pickup points by location](https://developers.vtex.com/docs/guides/list-pickup-points-by-location) guide and [API reference](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points).

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/shipping/pickup-in-point/pickupPoint/vtex-botafogo?zip-code=22250040
```

#### Pickup at a nearby location

Filters the search for products that can be picked up at pickup points located within a radius of up to 50 km from the shopper, within the same pickup radius limit as the Checkout.

Parameters: `/shipping/pickup-in-point/pickup-nearby`

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/shipping/pickup-in-point/pickup-nearby?zip-code=22250040 
```

### Filtering by Delivery Options

Delivery Options  are the set of choices a merchant provides to shoppers, describing how and when an order can be delivered, along with relevant metadata such as estimated delivery time.

Before you can display Delivery Option filters, it is necessary to:

* Enable the Delivery Options feature by contacting [our Support](https://help.vtex.com/en/support).  
* Create the Delivery Options for your store in the VTEX Admin following the instructions in the [Delivery Options](https://help.vtex.com/docs/tutorials/delivery-options-beta) guide.

To filter by a Delivery Option, use the `delivery-options` parameter. Its value must be the ID for one of the Delivery Options configured on your store.

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/delivery-options/express-option-id?zip-code=22250040
```

You can also filter for multiple Delivery Options by including multiple entries for the `delivery-options` parameter on the request.

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/delivery-options/one-week-option-id/delivery-options/one-day-option-id?zip-code=22250040
```

### Filtering by Dynamic Estimates

Dynamic Estimates for the delivery or pickup of a product are computed in real-time when searching. They are based on the store’s logistics operations, time of day and any product properties that might affect them. The possible values are *Same-day Delivery* and *Next-day Delivery*.

To filter by a Dynamic Estimate, you must use the `dynamic-estimate` parameter.

#### Same-day Delivery

Filters the search for products that can be delivered or picked up at the provided `zip-code` on the **same day**.

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/dynamic-estimate/same-day?zip-code=22250040
```

#### Next-day Delivery

Filters the search for products that can be delivered or picked up at the provided `zip-code` on the **next day**.

Example:

```txt
https://{{accountName}}.myvtex.com/api/io/_v/api/intelligent-search/product_search/dynamic-estimate/next-day?zip-code=22250040
```

## Implementing sidebar filters

>⚠️ The delivery promise filters are part of a beta feature and may be subject to breaking changes. If you choose to customize this functionality, ensure your implementation can adapt to updates.

In headless implementations, you must manually retrieve and render filters using VTEX Intelligent Search APIs. For example, inside a filter sidebar, where you want users to refine results based on shipping method or pickup location.

You can retrieve available filters using the `GET` [Get facets](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-) endpoint and use the response to build a custom filter UI in your headless storefront. For example, mapping `name: "pickup-in-point"` to a checkbox labeled **Pickup in store**.

>⚠️ Delivery-related filters (e.g. delivery, pickup-in-point) are included in the `facets` response. These are tied to the user's session and shipping context ([segment token](https://developers.vtex.com/docs/api-reference/session-manager-api#post-/api/sessions)). Make sure the segment and shipping data are initialized correctly for this to work.

**Example request:**

```txt
GET https://{{accountName}}.myvtex.com/_v/api/intelligent-search/facets/?query=moisturizer
```

**Example response:**

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
