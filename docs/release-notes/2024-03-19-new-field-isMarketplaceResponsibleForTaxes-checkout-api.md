---
title: "New tax calculation field on Checkout API"
slug: "2024-03-19-new-field-isMarketplaceResponsibleForTaxes-checkout-api"
type: "added"
createdAt: "2024-03-19T10:00:00.661Z"
hidden: false
excerpt: "Introducing new field isMarketplaceResponsibleForTaxes in the Checkout API."
---

We added the `isMarketplaceResponsibleForTaxes` property to the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api#overview) `orderForm`. This new boolean field indicates whether the marketplace should calculate product taxes (`true`) or if the calculation should be done by the seller (`false`).

This feature is crucial for merchants needing to comply with tax collection legislation. In some countries, like the US, the marketplace is the one required to calculate taxes, not the seller.

For more information about how to use this feature, please check the [Tax Service Specification](https://developers.vtex.com/docs/guides/tax-services-specification) guide.