---
title: "Seller Portal Edition App"
slug: "seller-portal-edition-app"
hidden: false
createdAt: "2022-03-14T23:06:52.335Z"
updatedAt: "2022-03-14T23:15:05.749Z"
---

The [Seller Portal](https://help.vtex.com/en/tutorial/seller-portal-primeiros-passos--6w1vBdRH2uuBGmUqgNQjwK) is a VTEX platform edition used by sellers to connect and sell their products on VTEX marketplaces. What differentiates it from a regular VTEX Admin is the curation of pages: we have selected only the key pages from VTEX’s Admin that fit the most with a seller’s operations.

That selection is possible because Seller Portal is actually a VTEX IO app. All pages available on the Seller Portal are declared in an Edition App, built using VTEX IO. This means that all sellers added to the marketplace’s Seller Portal, will see the same experience, which is defined in the edition app.

In this guide, we will go over some key concepts around the Edition App’s architecture and point out how marketplaces can configure their own Edition App, to create a customized Seller Portal.

## App sponsor

Every Seller Portal account is created from a VTEX IO Edition App, which is defined by its **sponsor**. The sponsor is the entity responsible for defining which pages will be included in that edition. In the code, they are defined as the app’s vendor. The `vendor` field represents the sponsor and the `name` field, the seller’s edition app.

```json
{
  "vendor": "vtex",
  "name": "edition-seller",
}
```

> ℹ️ It is not possible to create edition apps without a VTEX account as the sponsor.

Two entities can become an Edition app’s sponsor: VTEX or a VTEX marketplace.

### VTEX as the sponsor

In default Seller Portal environments, VTEX is the sponsor of the edition. This means that VTEX is responsible for:

* Selecting which pages would be included in Seller Portal’s default environment.
* Creating the edition app that will become the default Seller Portal.

VTEX has therefore defined its own edition for the Seller Portal, which includes the default pages that come within an account.

### Marketplace as the sponsor

It is also possible for marketplaces to create their own custom editions of Seller Portal, by becoming sponsors of their own edition app. When a marketplace wishes to select extra pages to be included in the seller’s experience, they can create their custom editions of Seller Portal by becoming sponsors of a an edition app.

Marketplaces that choose to be sponsors of their own edition app usually want:

* To have all the default pages that come with VTEX’s Seller Portal edition included for their sellers, in an easy and quick way.
* To automatically add specific pages that are not included in VTEX’s default edition, to all their sellers using Seller Portal.

The edition app sponsored by the marketplace should become the app’s sponsor and add VTEX’s edition as a “dependency” field. We will go over the step by step process of building your app in the [Configuring your Edition App](#configuring-your-edition-app) section of this article.

> ℹ️ To sponsor an app, please open a ticket to VTEX Support, so your account can be enabled as a sponsor.

### App dependencies

Making VTEX’s edition app a `dependency` automatically includes all of VTEX’s default pages, updates and bug fixes. In this way, you don’t have to manually include all apps in the default experience, they can just import what is in VTEX’s edition.

Once VTEX’s edition is declared as a dependency, you can add your own desired pages in the edition/apps.json file.

```json
{
  "dependencies": {
    "vtex.edition-seller": "0.x"
  },
}
```

Every **Edition App** has a **dependency** declared, which imports pages from another edition app.

![Composable Seller Portal - How does Edition work](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/seller-portal-edition-app-0.jpg)

## Configuring your Edition App

To configure your Edition app, follow these steps:

### Cloning the repository

1. Open the terminal and use the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) to log in to the desired VTEX account.
2. To clone this repository run `vtex init`.
3. Choose the `edition app` option.

If you don't have VTEX Toolbelt installed, you can also clone it manually:

 `git clone https://github.com/vtex/edition-hello edition-hello`

 `cd edition-hello`

### Defining the Manifest

After cloning the repository, follow the instructions below to configure your app:

1. In the `manifest.json`, change the `name` to your preferred choice.
By standard, VTEX adopts the `edition-seller-` prefix in all edition apps.

2. Change the `vendor` field to your store’s account name, to become the app’s sponsor`.
Make sure you request through VTEX Support that your store is enabled to become the app’s sponsor.

3. Set the appropriate parent edition in the `dependencies` field.
The dependency must be published by the vendor's sponsor.
