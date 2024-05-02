---
title: "Cross-border stores"
slug: "vtex-io-cross-border-stores"
hidden: false
createdAt: "2020-08-31T17:27:09.759Z"
updatedAt: "2021-05-04T18:04:25.359Z"
category: "Storefront Development"
---
A Cross-border store is a special case of a [multistore](https://help.vtex.com/en/tutorial/creating-multi-store-multi-domain--tutorials_510?locale=en).

Every VTEX account can have multiple stores, meaning that the same VTEX Admin can be used to manage more than one store. These accounts are named multistore or multidomain.

This feature is mostly used by stores that have different brands and business models, needing multiple operational environments.

Broadening this concept, it's also possible for a cross-border store that has different approaches in each country it operates to become a VTEX multistore.

In a multidomain environment, each store can be set up independently. That means layouts, products, prices, and logistics, for example, can vary for each local store depending on its domain.

Considering the cross-border business model, it's possible for a single VTEX account to manage multiple stores, such as: `http://{storename}.com/en`, `http://{storename}.com/pt`.
[block:callout]
{
  "type": "info",
  "body": "To set up a multidomain environment, please open a [ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) expressing your desire to become a cross-border store."
}
[/block]

## Essential concepts

To better understand what's behind a VTEX cross-border multistore, it's essential to comprehend the following two key concepts: **bindings** and **[trade policies](https://help.vtex.com/en/tutorial/what-is-a-sales-policy--563tbcL0TYKEKeOY4IAgAE)**.

In VTEX, the process of establishing a link between a web site, a store name, and a trade policy is known as binding.

This process results in the creation of a new store, which can be identified by a property also named `binding`.

Hence, keep in mind that every VTEX store has a unique `binding` used as an identifier. This is useful, for example, to filter routes of a specific store from a multidomain VTEX account.
[block:callout]
{
  "type": "info",
  "body": "To check the `binding` value of your stores, follow [this guide](https://developers.vtex.com/docs/guides/checking-your-stores-binding-id)"
}
[/block]
Once the binding concept is familiar, it's possible to advance to trade policies.

Trade policies are the set of configurations of a store's catalog, prices, and logistics strategy. Therefore, if, for example, the Spain store's pricing diverges from the France store's one, a new trade policy must be created.

That also means that, if two stores share the same logistics, catalog, and prices, the same trade policy can be used.