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

> By standard, VTEX adopts the `edition-seller-` prefix in all edition apps.

2. Change the `vendor` field to your store’s account name, to become the app’s sponsor`.

> Make sure you request through VTEX Support that your store is enabled to become the app’s sponsor.

3. Set the appropriate parent edition in the `dependencies` field.

> The dependency must be published by the vendor's sponsor.

### Adding apps for sub-accounts

After configuring your manifest, you can specify apps to be installed in the sub-accounts that have this edition configured. You do that through the `edition/apps.json` file, adding an entry to the object under the `apps` key in the format:

```json
{
  "<vendor>.<name>": {
    "major": "<desired major>",
    "settings": "<initial settings>"
  },
}
```

The settings are optional and can be omitted, but they will define the initial settings that should be configured for the app when it is installed through the current edition.

E.g.: The contents of the `apps.json` file could be:

```json
{
  "apps": {
    "vtex.node-getting-started": { "major": 0 }
  }
}
```

### Testing

To test the app, make sure you have [VTEX's toolbelt](https://github.com/vtex/toolbelt) installed.

Edition apps cannot be linked, so for testing, you need to launch a pre-release version and set them on test accounts or workspaces for validation. To do so:

1. Launch a pre-release of your edition: `vtex release patch beta`.
2. Check the edition of current account/workspace: `vtex edition`.
3. Set the edition in current account/workspace: `vtex edition set <edition>@<version>`.

All the apps configured in the `apps.json` file will be automatically installed in that workspace where the edition was set. You can validate that by inspecting the `vtex ls` command output.

## Multiple marketplaces using the same edition

There is another scenario where more than one marketplace, who are under the same parent company, wish to operate with the same Seller Portal edition app.

In the example below we guide you through the architecture that enables this scenario.

### Scenario example

**Scenario:** Two separate marketplaces, with different sellers, wish to provide the same Seller Portal experience to their sellers, without the complexity of creating multiple edition apps.

We have two market places: The **MKPSeller** and the **Cosmetics2**. They are both part of the same holding, but they're different marketplace accounts.

The **MKPSeller** has created an edition app, based on our default, **vtex.edition-seller**, and added other custom pages they wish to provide for their sellers. They called the edition they sponsored the `mkpseller.edition-seller` .

They declare the default edition that VTEX has sponsored, or vtex.edition-seller as a dependency on their app’s code. This action automatically imports all the default Seller Portal apps to their edition app

```json
{
 "vendor": "mkpseller",
 "name": "edition-seller",
 "version": "0.1.0",
 "title": "MKP Seller edition apps",
 "description": "VTEX IO edition for seller accounts",
 "builders": {
   "edition": "0.x"
 },
 "dependencies": {
   "vtex.edition-seller": "0.x"
 },
 "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
}
```

Meanwhile, **Cosmetics2** also wants to create an edition app, copying **MKPseller’s** edition, since they came to the conclusion that **MKPseller's** edition fits all their needs.

Instead of creating an edition app and manually adding the desired custom pages one by one, they can simply create their app, and declare **MKPSeller's** edition as a dependency.

```json
{
 "vendor": "cosmetics2",
 "name": "edition-seller",
 "version": "0.1.0",
 "title": "Cosmetics2 edition apps",
 "description": "VTEX IO edition for seller accounts",
 "builders": {
   "edition": "0.x"
 },
 "dependencies": {
   "mkpseller.edition-seller": "0.x"
 },
 "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
}
```

For the dependency to work, **MKPSeller** must be **Cosmetics2** app’s sponsor. This means that **Cosmetics2** has an edition belonging to **MKPSeller** associated to it.

> ℹ️ To know which edition is associated with an account, on VTEX Toolbelt, run `vtex edition get` .

This way, **Cosmetics2** edition app will include everything declared in `mkpseller.edition-seller` . This means including:

* VTEX’s default apps, since they were declared as a dependency.
* The custom pages added by **MKPSeller**, since they created their custom edition.

Summing it up, to declare VTEX or another marketplace’s **Edition app** as a **dependency**, this dependency’s owner must be the app’s **sponsor**.

### Limitations for multiple marketplace architecture

The current multiple marketplace architecture has some limitations:

* The apps included in an edition can only belong to the same sponsor, or to VTEX. E.g. MKPSeller cannot add apps from Cosmetics2's edition.
* An edition cannot have more than one sponsor.
* For this architecture to work, we can only include an edition as a dependency if it belongs to the same app vendor, or to the vendor’s sponsor.
