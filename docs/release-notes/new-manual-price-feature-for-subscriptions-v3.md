---
slug: 'new-manual-price-feature-for-subscriptions-v3'
title: 'New Manual Price feature for Subscriptions v3'
createdAt: 2022-05-10T20:00:04.576Z
hidden: false
type: 'added'
excerpt: "You can now enable the Manual Price feature for [Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/subscriptions-v3-migration-guide)."
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

You can now enable the Manual Price feature for [Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/subscriptions-v3-migration-guide), which allows you to:

- Apply a manual price to each subscription item, instead of the current price applied.
- Maintain the same manual price for every future recurrent order from that subscription, if desired.

To make this possible, we have added an endpoint to the Subscriptions API v3:

- post [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1)

We also added these properties to the following endpoints:

| Property name | Endpoints to which the property was added |
|---------------|-------------------------------------------|
| `manualPriceAllowed` | get [Get Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/getsettings-1); post [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1)
| `useItemPriceFromOriginalOrder` | get [Get Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/getsettings-1); post [Edit Subscription Settings](https://developers.vtex.com/vtex-rest-api/reference/editsettings-1)
| `manualPrice` |post [Add item to subscription](https://developers.vtex.com/vtex-rest-api/reference/post_api-rns-pub-subscriptions-id-items); patch [Edit item on subscription](https://developers.vtex.com/vtex-rest-api/reference/patch_api-rns-pub-subscriptions-id-items-itemid)

To learn more about the feature and how to enable it, please refer to the documentation below.

- [Enabling Manual Prices for Subscriptions v3](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-prices-for-subscriptions-v3) guide.
- [Subscriptions API v3 reference](https://developers.vtex.com/vtex-rest-api/reference/subscriptions-api-v3-overview).
