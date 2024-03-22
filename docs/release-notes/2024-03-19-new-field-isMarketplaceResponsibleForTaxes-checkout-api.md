---
title: "Tax Service"
slug: "2024-03-19-new-field-isMarketplaceResponsibleForTaxes-checkout-api"
type: "added"
createdAt: ""
hidden: false
excerpt: "Introducing a new field, isMarketplaceResponsibleForTaxes, in the Checkout API orderForm. Easily determine tax calculation responsibility between marketplace and seller."
---

We have added the `isMarketplaceResponsibleForTaxes` property to the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api#overview) `orderForm`. This new field is a boolean that indicates whether the marketplace is responsible for calculating taxes for the products (`true`) or if the responsibility lies with the seller (`false`).

For more information on how to use it, please refer to the [Tax Service Specification](https://developers.vtex.com/docs/guides/tax-services-specification) guide.

>ℹ️ This is important for US merchants who must comply with some legislation regarding tax redemption.