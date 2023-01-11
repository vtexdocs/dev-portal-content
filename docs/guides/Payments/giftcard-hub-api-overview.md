---
title: "GiftCard Hub API - Overview"
slug: "giftcard-hub-api-overview"
hidden: false
createdAt: "2020-01-02T04:28:35.508Z"
updatedAt: "2022-06-15T20:47:28.940Z"
---

> ℹ️️ Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer's journey.

The Gift Card Hub API allows interactions with all Gift Card providers registered to a store from a single point.

Gift Card providers are systems capable of providing cards to be used in the buying process.

The following is the sequence diagram that represents calls in the purchase closing process.
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/giftcard-hub-api-overview-0.png)

**Checkout + Gateway**: Systems responsible for the sale and for processing orders and payments.

**Gift Card Hub**: System responsible for managing multiple registered Gift Card providers for a store.

**Gift Card Provider**: System responsible for providing the Gift Cards available to the user not closing a purchase. This system can be implemented by third parties.
