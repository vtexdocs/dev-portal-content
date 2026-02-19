---
title: "B2B Orders History (B2B Suite)"
slug: "vtex-b2b-orders-history"
hidden: false
createdAt: "2022-03-29T04:30:06.314Z"
updatedAt: "2022-08-16T16:18:50.580Z"
---

> ⚠️ This documentation applies to B2B Suite only.

> ℹ️ The **B2B Orders History** app is part of VTEX’s [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution: a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend that you use it alongside the other apps in this suite for all functionalities to work as expected.

When navigating a store, B2B customers who are members of organizations often need to view past orders placed by other users in their organization or cost center.

Considering this, the **B2B Orders History** app replaces the [default Orders page](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh#orders) in [My Account](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh) with an adapted version for the B2B scenario.

In this version of the **Orders** page, logged-in B2B customers who are members of an organization can view not only their own orders, but also orders placed by members of their organization or cost center, provided that they have the required [storefront permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions).


## Before you begin

First, make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed in your machine.

To use **B2B Orders History**, you must have the [B2B Organizations](https://developers.vtex.com/docs/guides/vtex-b2b-organizations) app installed in your store, which will enable you to group B2B users into organizations, with their own assigned payment methods, price tables, product collections, and cost centers. 

You must also have the **Storefront Permissions** app installed – it allows you to grant specific storefront roles for B2B customers in an organization. See the [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) app documentation for information on the available roles and how to customize their permissions.


## Installation

You can install the **B2B Orders History** app by running `vtex install vtex.b2b-organizations` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).


## Configuration

After installing the app, you must hide the default **Orders** page within **My Account**. To do this, follow the steps below.

1. On the VTEX Admin, access **Account Settings > Apps > My apps**.
2. In the list of apps, find **My Account** and click on its <img src="https://user-images.githubusercontent.com/77292838/160175751-b3803ff1-41f1-46d2-981a-b57693c03f79.png" width="15" alt-text="gear-icon"/> `Settings`.

    If you prefer, you can go directly to the URL `https://accountName.myvtex.com/admin/apps/vtex.my-account@1.x/setup/`

3. In the **Orders** section, deselect the **Visible** checkbox, as shown in the following image.
4. Click on `Save`.

![my-account-settings-orders](https://user-images.githubusercontent.com/77292838/160175754-67874b5b-e1e1-4baa-9209-6b6a35c024f8.png)


## How it works

Once the app is installed and **My Account** is configured, B2B customers who are members of an organization will be able to see all of their organization or cost center’s orders at **My Account > Orders** in the storefront, if they have the required permissions.

By default, only customers with the **Organization Admin** role can see all the organization’s orders. Users with the **Organization Approver** or **Organization Buyer** roles can only see their cost center’s orders. Note that if you have the [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) app you can customize these permissions in your VTEX Admin, on **Account Settings > Storefront Permissions**.