---
slug: "improvements-on-marketplace-api"
title: "Improved field descriptions on Marketplace API"
createdAt: 2021-05-26T19:33:00.000Z
hidden: false
type: "improved"
---

![Commerce APIs](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/improvements-on-marketplace-api-0.png)

We have improved our Marketplace API documentation on the following endpoints:

[Match multiple received SKUs](https://developers.vtex.com/vtex-rest-api/reference/match-received-skus-1#match-multiple-received-skus):

- We have corrected the `skuSpecification` fields that were documented as mandatory, but are actually optional.
- We have corrected the request's body type. It is an array of objects, and not a single object.
- We have improved descriptions of the `matchId`, `matcherId` and `version` fields, pointing out what calls to perform to retrieve their value.

[Get Suggestions API](https://developers.vtex.com/vtex-rest-api/reference/get-suggestions-1):

- We have added the `type` parameter to this endpoint, pointing out whether the SKU suggestion was sent for the first time (new), or if it's an update to suggestions previously sent (update).
