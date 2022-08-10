---
title: "Assembly Options app"
slug: "assembly-options-app"
excerpt: "vtex.admin-assembly-options@2.0.3"
hidden: false
createdAt: "2022-06-23T14:21:02.843Z"
updatedAt: "2022-06-23T14:21:02.843Z"
---
> ⚠ This app is available only for stores developed in [VTEX IO](https://vtex.com/br-pt/store-framework/).

At VTEX, [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) consist on creating [attachments](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm) for complex scenarios, where it is necessary to offer various combinations of SKUs, quantities, additional items and costs.


The **Assembly Options** app provides an interface on VTEX Admin to create and manage product customization options available to customers in a specific store.  This experience aims to offer a simple and easy-to-use alternative to the [manual configuration](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#attachments) available through **Catalog > Attachments** using a certain attachment syntax.



## Before you start

To use Assembly Options, you must first install and configure [Product Customizer](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-customizer) in your store.

We also recommend reading our [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH) documentation for more information on this feature.


## Installation

> ⚠ When this app is installed in a [seller account](https://help.vtex.com/en/tutorial/what-is-a-seller--5FkLvhZ3Few4CWWIuYOK2w), the Assembly Option is displayed at checkout. To display it on the product page, you must install the app in a [marketplace account](https://help.vtex.com/tutorial/what-is-a-marketplace--680lLJTnmEAmekcC0MIea8#).

You can install the app for free in the [VTEX App Store](https://apps.vtex.com/vtex-admin-assembly-options/p) or using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), by running `vtex install vtex.admin-assembly-options@2.x` in your terminal.


After the installation, you can find the app's interface on VTEX Admin, by accessing *Products > Assembly options* or  by going directly to the URL `{accountName}.myvtex.com/admin/assembly-options/`, replacing `{accountName}` with your VTEX account.

This app installs Assembly Options GraphQL as a dependency. Learn more about it by accessing the [assembly-options-graphql](https://github.com/vtex/assembly-options-graphql) repository.


    
## How the app works

The app inserts a new menu in the VTEX Admin, which you can access on _Products > Assembly options_.

![](https://i.imgur.com/os1XQBi.png)

The Assembly Options interface allows you to:


<details>
<summary>View a list of existing Assembly Options.</summary>

![Listing](https://user-images.githubusercontent.com/53904010/164768650-f85f8670-3058-4952-9a8e-af86739dc4f9.gif)
</details>

<details id="search">
<summary>Search for Assembly Options.</summary>

![Search](https://user-images.githubusercontent.com/53904010/164768723-1dc5b5cc-527f-4de0-8a11-91845c8a31bd.gif)
</details> 

<details id="filters">
<summary>Filter Assembly Options by Status.</summary>

![Filter](https://user-images.githubusercontent.com/53904010/164768777-87e44f13-c965-4d1b-9d96-24ee07fa8903.gif)
</details>

<details id="creation">
<summary>Create Assembly Options.</summary>

![Creation2](https://user-images.githubusercontent.com/53904010/165098542-946b5450-b458-48b4-9d3c-808309760d0c.gif)
</details>

<details id="edition">
<summary>Edit Assembly Options.</summary>

![Edit](https://user-images.githubusercontent.com/53904010/164768873-553f9a4b-c759-453f-8601-d490aece1155.gif)
</details>

<details id="deletion">
<summary>Delete Assembly Options.</summary>

![Delete](https://user-images.githubusercontent.com/53904010/164768964-4fb41cc8-4a39-4d5e-bd48-6ee4028d8e07.gif)
</details>

For more information on how to use this interface, read our user guide [Assembly Options app](https://help.vtex.com/en/tutorial/assembly-options-app--54mWg37mojrqOgCA79iqqk).