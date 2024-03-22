---
title: "New field for tax calculation on Checkout API"
slug: "2024-03-19-new-field-isMarketplaceResponsibleForTaxes-checkout-api"
type: "added"
createdAt: ""
hidden: false
excerpt: "Introducing a new field, isMarketplaceResponsibleForTaxes, in the Checkout API."
---

We have added the `isMarketplaceResponsibleForTaxes` property to the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api#overview) `orderForm`. This new field is a boolean that indicates whether the marketplace is responsible for calculating taxes for the products (`true`) or if the responsibility lies with the seller (`false`).

This feature is essential for merchants needing to comply with legislation regarding tax redemption. In certain countries, such as the US, tax calculation responsibility falls on the marketplace rather than the seller.

For more information on how to use it, please refer to the [Tax Service Specification](https://developers.vtex.com/docs/guides/tax-services-specification) guide.