---
title: "GiftCard Hub API - Overview"
slug: "giftcard-hub-api-overview"
hidden: false
createdAt: "2020-01-02T04:28:35.508Z"
updatedAt: "2020-04-14T13:56:45.081Z"
---
The Gift Card Hub API allows interactions with all Gift Card providers registered to a store from a single point. 

Gift Card providers are systems capable of providing cards to be used in the buying process.

The following is the sequence diagram that represents calls in the purchase closing process.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4ac5cf6-giftcardHub.png",
        "giftcardHub.png",
        628,
        447,
        "#f8f8f8"
      ]
    }
  ]
}
[/block]
**Checkout + Gateway**: Systems responsible for the sale and for processing orders and payments.

**Gift Card Hub**: System responsible for managing multiple registered Gift Card providers for a store.

**Gift Card Provider**: System responsible for providing the Gift Cards available to the user not closing a purchase. This system can be implemented by third parties.