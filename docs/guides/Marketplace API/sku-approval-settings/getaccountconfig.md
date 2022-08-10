---
title: "Get Account's Approval Settings"
slug: "getaccountconfig"
excerpt: "This endpoint retrieves the current approval settings of a marketplace's Received SKUs module. Its response includes: \n\n- `Score`: Matcher scores for approving and rejecting SKUs received from sellers. \n\n- `Matchers`: All Matchers configured on the marketplace, and their respective details. \n\n- `SpecificationsMapping`: Mapping of product and SKU specifications, per seller. \n\n- `MatchFlux`: This field determines the type of approval configuration applied to SKUs received from a seller. The possible values include:  \n\n`default`, where the Matcher reviews the SKU, and approves it based on its score. \n\n`manual`, for manual approvals through the Received SKU UI, or Match API. \n\n`autoApprove`, for every SKU received from a given seller to be approved automatically, regardless of their Matcher Score."
hidden: false
createdAt: "2021-11-09T18:52:06.553Z"
updatedAt: "2022-04-28T14:20:24.836Z"
---
