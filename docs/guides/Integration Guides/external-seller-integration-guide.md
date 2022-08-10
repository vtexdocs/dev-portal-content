---
title: "External Seller"
slug: "external-seller-integration-guide"
hidden: false
createdAt: "2020-09-01T13:42:40.894Z"
updatedAt: "2020-09-01T23:36:28.475Z"
---
In our native multi-seller architecture, VTEX stores decouple different aspects of an e-commerce operation in order to clearly divide responsibilities between marketplace and seller.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4e90638-VTEX_Seller_and_VTEX_Marketplace.png",
        "VTEX Seller and VTEX Marketplace.png",
        800,
        400,
        "#f9ebf0"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
This allows VTEX stores to become marketplaces themselves or become sellers in other VTEX stores without requiring any additional development. Store settings connect the marketplace subsystem of a store to the seller subsystem of another. 
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6b348a4-VTEX_Seller_and_VTEX_Marketplace_2.png",
        "VTEX Seller and VTEX Marketplace 2.png",
        1000,
        400,
        "#f6ecf0"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
This behavior can be leveraged in endless combinations. VTEX accounts can both set up a marketplace storefront to sell products from multiple sellers, including their own, and distribute products to multiple other marketplaces. This creates our [collaborative commerce](https://vtex.com/en/blog/strategy/collaborative-commerce-imperative-why-digital-first-collaboration-is-at-the-core-of-todays-business-success/) network.
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/944d4c2-External_Seller.png",
        "External Seller.png",
        1000,
        400,
        "#e1d7dd"
      ],
      "sizing": "80"
    }
  ]
}
[/block]
However, there may be a strategic partner for your business operating outside our collaborative commerce network. This guide presents the steps needed to develop a **custom connector to sell products from an external seller in your storefront**.