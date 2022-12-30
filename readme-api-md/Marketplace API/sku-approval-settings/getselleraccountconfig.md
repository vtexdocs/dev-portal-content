---
title: "Get Seller's Approval Settings"
slug: "getselleraccountconfig"
excerpt: "This endpoint retrieves the current Received SKUs approval settings applied to a specific seller. Its response includes: \n\n- `sellerId`: A string that identifies the seller in the marketplace. \n\n- `accountId`: Marketplace’s account ID. \n\n- `accountName`: Marketplace’s account name. \n\n- `mapping`: Mapping of SKU and product Specifications. \n\n- `matchFlux`: This field determines the type of approval configuration applied to SKUs received  from a seller. The possible values include:  \n\n`default`, where the Matcher reviews the SKU, and approves it based on its score. \n\n`manual`, for manual approvals through the Received SKU UI and Match API. \n\n`autoApprove`, for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score."
hidden: false
createdAt: "2021-11-09T18:52:06.554Z"
updatedAt: "2021-11-22T17:02:54.623Z"
---
