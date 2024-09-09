---
title: "Enabling the Order Form optimization"
slug: "vtex-io-documentation-enabling-order-form-optimization"
hidden: false
createdAt: "2020-06-03T16:02:44.278Z"
updatedAt: "2022-12-13T20:17:44.505Z"
---

Every VTEX store uses the `orderForm` object to **record and fetch data from a user's order**, including each item added to the cart.

To give store page blocks access to information stored on any VTEX `orderForm` and thereby be able to render it,  Store Framework always worked with an `OrderFormProvider` in each store page that, behind the scenes, exports user data to every Store Framework block.
Through our constant effort of building the store Checkout using the VTEX IO Store Framework, a **new** `OrderFormProvider` was created, making the former a **legacy**.

The new `OrderFormProvider` v2 is already used by `minicart.v2`, the `add-to-cart-button`, the `checkout-cart` and it will be used by any native block that will be developed in Store Framework from now on. However, important native blocks that are older, such as the `minicart` and `buy-button`, still consume `orderForm` data that was exported by the legacy `OrderFormProvider`.

To ensure **backward-compatibility** is reinforced in Store Framework,  **both** `OrderFormProvider`s, the legacy and the new one, remain on store pages, exporting `OrderForm` data to their respective blocks.

This comes with a performance cost since it means every store is now fetching **two** different `orderForm`s to use in each of the `OrderFormProvider`s working behind the scenes.

To avoid this unnecessary overhead, it is possible to disable the legacy `OrderFormProvider` and allow your store to only use the newer one. Enabling this should result in a smoother navigation experience for your users.

> ⚠️ This setting must be enabled with **caution**, since it may cause harm to your store if any of its blocks still need the legacy `orderFormProvider` to properly function. In case your store already uses the `minicart.v2` and the `add-to-cart-button` blocks, and there are no custom blocks that depend on the legacy provider, there should be no issues regarding the optimization.

Find out how to enable the Order Form optimization in the steps below.

## Instructions

1. In the VTEX Admin, access **Store Settings > Storefront > Store**.

2. In the **Advanced** tab, toggle the **orderForm optimization** button.

    ![enabling-pwa](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-enabling-order-form-optimization-1.png)

3. Save your changes.
