---
title: "Delivery Promise Suggestions API: New endpoint to generate delivery and pickup hashes"
slug: "2026-09-11-delivery-promise-suggestions-api-new-endpoint-to-generate-delivery-and-pickup-hashes"
hidden: false
type: "added"
createdAt: "2026-09-11T12:00:00.000Z"
excerpt: "The Delivery Promise Suggestions API now offers the Get delivery zones and pickup points hashes endpoint, which returns both the `deliveryZonesHash` and the `pickupPointsHash` in a single response. The two previous hash generation endpoints are now deprecated."
---

The **[Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api)** now offers a new operation, [Get delivery zones and pickup points hashes](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/zones/_search) (`POST /api/logistics-shipping/zones/_search`), documented in the API Reference. It returns the delivery zones and the pickup points available for a given location, along with both hashes that represent the shopper's fulfillment context.

## What has changed?

- The new operation is `POST /api/logistics-shipping/zones/_search`, listed under the `Logistics shipping` tag. The request body takes `zipCode`, `coordinate` (with `latitude` and `longitude`), and `country` (ISO 3166-1 alpha-3), all required.
- The response returns `deliveryZonesHash` and `pickupPointsHash` in a single call, plus `deliveryZoneIds` and `pickupDistances` (with `pickupId`, `distance` in kilometers, and `pickupName`).
- This is now the recommended endpoint for generating the hashes required by [Get delivery suggestions](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#get-/api/delivery-promise-suggestions), [Search delivery suggestions](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/delivery-promise-suggestions/_search), and the [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) endpoints.
- Both hashes have a time to live (TTL) of 30 minutes. After that period they expire, and requests sent with an expired hash may be rejected or return invalid responses. This expiration is now documented in the new endpoint's description and in the descriptions of the `deliveryZonesHash` field and the `pickupsHash` query parameter of the delivery suggestions endpoints.
- The [Search delivery zones](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/delivery-zones/_search/v2) (`POST /api/logistics-shipping/delivery-zones/_search/v2`) and [Search pickup points](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/pickuppoints/_search) (`POST /api/logistics-shipping/pickuppoints/_search`) endpoints are now marked as deprecated in the API Reference. They still work, but their use is no longer recommended.

## What needs to be done?

No immediate action is required because the deprecated endpoints keep working, and no existing endpoint has changed its behavior.

Still, we recommend that integrations that generate the fulfillment context hashes migrate to `POST /api/logistics-shipping/zones/_search`, replacing the two separate calls to the deprecated endpoints with a single call.

Because the hashes expire after 30 minutes, we also recommend calling this endpoint as close as possible to the moment the hashes are used, and handling the expired hash scenario by requesting new ones. There is no penalty or side effect of regenerating them.

## Learn more

- [Delivery Promise Suggestions API](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api) reference.
- [Get delivery zones and pickup points hashes](https://developers.vtex.com/docs/api-reference/delivery-promise-suggestions-api#post-/api/logistics-shipping/zones/_search) in the API Reference.
- [Intelligent Search API](https://developers.vtex.com/docs/api-reference/intelligent-search-api) reference.
