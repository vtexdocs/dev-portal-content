---
title: "External Marketplace"
slug: "external-marketplace"
hidden: false
createdAt: "2021-07-01T15:01:30.107Z"
updatedAt: "2022-02-03T21:32:07.282Z"
---
In this section, you will find the endpoints involved in the VTEX integration between an external marketplace and a VTEX seller.

[block:parameters]
{
  "data": {
    "0-0": "[VTEX Mapper Registration](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/connector/register)",
    "1-0": "[Send Category Mapping to VTEX Mapper](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-mapper#post-/api/mkp-category-mapper/categories/marketplace/-id-)",
    "2-0": "[Place fulfillment order](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders)",
    "3-0": "[Authorize dispatch for fulfillment order](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders/-orderId-/fulfill)",
    "h-0": "Request",
    "h-1": "From",
    "h-2": "To",
    "0-1": "External marketplace",
    "1-1": "External marketplace",
    "2-1": "External marketplace",
    "3-1": "External marketplace",
    "0-2": "VTEX system",
    "1-2": "VTEX system",
    "2-2": "VTEX Seller",
    "3-2": "VTEX Seller"
  },
  "cols": 3,
  "rows": 4
}
[/block]
For a detailed explanation of the steps required to develop a custom connector to become an external marketplace for VTEX sellers, check out our complete [External Marketplace Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).