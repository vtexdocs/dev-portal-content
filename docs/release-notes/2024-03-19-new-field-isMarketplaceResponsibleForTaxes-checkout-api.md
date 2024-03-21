---
title: "Tax Service"
slug: "2024-03-19-new-field-isMarketplaceResponsibleForTaxes-checkout-api"
type: "improvement"
createdAt: ""
hidden: false
excerpt: "Introducing a new field, isMarketplaceResponsibleForTaxes, in the Checkout API orderForm. Easily determine tax calculation responsibility between marketplace and seller."
---

We have added a new field, `isMarketplaceResponsibleForTaxes`, to the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api#overview) `orderForm`. This feature determines whether the marketplace or the seller is responsible for calculating taxes for the products.

For more information on how to use this field, please refer to the [Tax Service Specification](https://developers.vtex.com/docs/guides/tax-services-specification) article.

>ℹ️ This is important for US merchants who must comply with some legislation regarding tax redemption.