---
title: "Teste"
slug: "teste"
hidden: true
excerpt: "Learn how to implement the delivery promise feature in headless stores."
createdAt: "2025-05-14T22:18:24.684Z"
updatedAt: "2025-05-14T22:18:24.684Z"
---

TESTE DO CALLOUT


>ℹ️ **Retrieving available pickup points**
>
> To retrieve the list of available pickup points with their IDs, distances, addresses, and business hours, use the `GET` [Get pickup point availability](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/api/intelligent-search/v0/pickup-point-availability/productClusterIds/-productClusterIds-/trade-policy/-tradePolicy-) endpoint from Intelligent Search API. This endpoint returns pickup points based on product availability (product cluster/collection), sorted by distance from the provided coordinates.
>
> You can call this endpoint in two ways:
>
> - **With country and ZIP code:** Provide the country and ZIP code to retrieve pickup points based on location.
>
>   ```txt
>   GET https://api.vtexcommercestable.com.br/api/intelligent-search/v0/pickup-point-availability/productClusterIds/{productClusterIds}/trade-policy/{tradePolicy}?zip-code={zipCode}&an={accountName}&coordinates={coordinates}&country={country}
>   ```
>
> - **With delivery zones and pickups hashes:** Alternatively, provide pre-computed hashes (`deliveryZonesHash` and `pickupsHash`) for faster lookup.
>
>   ```txt
>   GET https://api.vtexcommercestable.com.br/api/intelligent-search/v0/pickup-point-availability/productClusterIds/{productClusterIds}/trade-policy/{tradePolicy}?deliveryZonesHash={deliveryZonesHash}&pickupsHash={pickupsHash}&an={accountName}
>   ```
