---
title: "Comprehensive Seller: what it is and how to use it"
slug: "comprehensive-seller-what-it-is-and-how-to-use-it"
hidden: true
createdAt: "2020-10-07T11:31:17.648Z"
updatedAt: "2020-10-07T11:51:52.614Z"
---
All VTEX stores are natively prepared to function as marketplaces, that is, to sell products from other stores: the sellers. In this model, in which the products from multiple sellers are made available to the customer in their store, VTEX needs to use previously defined criteria to select the products that will be listed in the store window.

One of those criteria is that of comprehensive sellers. In this article, we will understand in detail:
- [What is the comprehensive seller](#what-is-the-comprehensive-seller)
- [When to set a seller as comprehensive](#when-to-set-a-seller-as-comprehensive)
- [How VTEX uses this information](#how-vtex-uses-this-information)

# What is the comprehensive seller

Imagine that your store sells products from 100 different sellers across the country. Some of them are able to deliver only to the country's capital; others manage to deliver throughout the southern region; while others deliver across the whole country.

When a customer browses your store's website without providing any location information, what are the sellers whose products should show up? Showing products from sellers who deliver to a restricted region may be risky. If the customer wants to receive it anywhere else, the moment they arrive at the cart and inform the zip code, the product of that specific seller will be shown as unavailable.

To solve this problem, all sellers have the `isBetterScope` property. When this property is active (value `true`), VTEX understands that this seller is comprehensive, which means that its products can be shown in navigation contexts without a defined location.

# When to set a seller as comprehensive

A seller should only be set as comprehensive if its delivery area is relevant to the operation of the store. The most common scenario is to use this property for sellers who deliver across the country.

This is important because, in the navigation stages where the store does not yet know the customer's location, the availability and price information of the products that will be shown to that customer refer exclusively to the main seller (seller 1) and to the comprehensive sellers. If the conditions of the comprehensive sellers do not reflect conditions applicable to all or at least the majority of the customer base, there may be unfulfilled expectations.

## Example

Imagine that a customer from the North of the country entered the store and has not yet informed the zip code. Let's say your store has set a seller that delivers only to the South of the country as comprehensive (`isBetterScope = true`).

The availability and price information for this seller's products shown to that customer may not apply to their actual context. The customer will only discover this after informing the zip code, which will harm the experience.

# How VTEX uses this information

When there is still no user location information, the seller selection heuristic shows only the products of the main seller (seller 1) and comprehensive sellers.

This happens both in the shop window and in the cart and aims to prevent the customer from seeing products from sellers that they will not actually be able to deliver to their address.
[block:callout]
{
  "type": "info",
  "body": "Even if the customer's location was captured in the shop window stage and stored in the `regionId` field of the Session API, this information is not used in the cart. Therefore, upon reaching the cart, the customer will again see only the information from the main seller and the comprehensive sellers. The remaining sellers are only eligible after the customer informs the delivery zip code."
}
[/block]