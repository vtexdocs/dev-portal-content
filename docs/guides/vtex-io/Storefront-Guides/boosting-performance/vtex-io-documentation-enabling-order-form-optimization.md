---
title: "Enabling the orderForm optimization"
slug: "vtex-io-documentation-enabling-order-form-optimization"
hidden: false
createdAt: "2020-06-03T16:02:44.278Z"
updatedAt: "2022-12-13T20:17:44.505Z"
---

The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) object is central to every VTEX store, managing and fetching order data such as the items added to a customer's cart. This data enables store blocks to display and interact with the shopping cart and checkout information.

To manage this interaction, Store Framework stores use the `OrderFormProvider`, which exports the `orderForm` data to the store blocks.

Two versions of `OrderFormProvider` exist:

- The legacy version was historically used by older store blocks like `minicart` and `buy-button`.
- The new `OrderFormProvider` v2 is used by updated blocks such as `minicart.v2`, `add-to-cart-button`, and `checkout-cart`, and is now the default for any new native blocks.

By default, both the legacy and new `OrderFormProvider` are used to maintain compatibility with older blocks. However, this setup requires fetching two separate `orderForm` objects, which can slow down store performance.

To improve performance, you can disable the legacy `OrderFormProvider`, so your store only uses the newer `OrderFormProvider` v2. This optimization reduces unnecessary data fetching and results in smoother navigation for users.

## Before you begin 

Before enabling this optimization, ensure that none of your store's blocks depend on the legacy `OrderFormProvider`. If your store uses blocks like 
`minicart.v2` and `add-to-cart-button`, and you have no custom blocks relying on the legacy provider, it’s safe to proceed.

## Instructions

1. Access the VTEX Admin and go to **Store Settings > Storefront > Store**.
2. Navigate to the **Advanced** tab and toggle the **Enable orderForm optimization** button.

    ![enabling-pwa](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-enabling-order-form-optimization-1.png)

3. Save your changes.
