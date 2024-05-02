---
title: "Assembly Options"
slug: "assembly-options-app"
hidden: false
createdAt: "2022-06-23T14:21:02.843Z"
updatedAt: "2022-06-23T14:21:02.843Z"
---
> ⚠ This app is available only for stores developed in [VTEX IO](https://vtex.com/br-pt/store-framework/).

At VTEX, [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) consist on creating [attachments](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm) for complex scenarios, where it is necessary to offer various combinations of SKUs, quantities, additional items and costs.

The **Assembly Options** app provides an interface on VTEX Admin to create and manage product customization options available to customers in a specific store.  This experience aims to offer a simple and easy-to-use alternative to the [manual configuration](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#attachments) available through **Catalog > Attachments** using a certain attachment syntax.

## Before you begin

To use Assembly Options, you must first install and configure [Product Customizer](https://developers.vtex.com/docs/guides/vtex-product-customizer) in your store.

We also recommend reading our [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) documentation for more information on this feature.

## Installation

> ⚠ When this app is installed in a [seller account](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w), the Assembly Option is displayed at checkout. To display it on the product page, you must install the app in a [marketplace account](https://help.vtex.com/tutorial/what-is-a-marketplace--680lLJTnmEAmekcC0MIea8#).

You can install the app for free in the [VTEX App Store](https://apps.vtex.com/vtex-admin-assembly-options/p) or using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), by running `vtex install vtex.admin-assembly-options@2.x` in your terminal.

After the installation, you can find the app's interface on VTEX Admin, by accessing *Products > Assembly options* or  by going directly to the URL `{accountName}.myvtex.com/admin/assembly-options/`, replacing `{accountName}` with your VTEX account.

This app installs Assembly Options GraphQL as a dependency. Learn more about it by accessing the [assembly-options-graphql](https://github.com/vtex/assembly-options-graphql) repository.

## How the app works

The app inserts a new menu in the VTEX Admin, which you can access on _Products > Assembly options_.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-0.png)

The Assembly Options interface allows you to:

<details>
<summary>View a list of existing Assembly Options.</summary>

![Listing](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-1.gif)
</details>

<details id="search">
<summary>Search for Assembly Options.</summary>

![Search](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-2.gif)
</details> 

<details id="filters">
<summary>Filter Assembly Options by Status.</summary>

![Filter](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-3.gif)
</details>

<details id="creation">
<summary>Create Assembly Options.</summary>

![Creation2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-4.gif)
</details>

<details id="edition">
<summary>Edit Assembly Options.</summary>

![Edit](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-5.gif)
</details>

<details id="deletion">
<summary>Delete Assembly Options.</summary>

![Delete](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/assembly-options-app-6.gif)
</details>

For more information on how to use this interface, read our user guide [Assembly Options app](https://help.vtex.com/en/tutorial/assembly-options-app--54mWg37mojrqOgCA79iqqk).