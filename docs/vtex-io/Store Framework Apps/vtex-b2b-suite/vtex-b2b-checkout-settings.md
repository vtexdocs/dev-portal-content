---
title: "B2B Checkout Settings"
slug: "vtex-b2b-checkout-settings"
excerpt: "vtex.b2b-checkout-settings@1.4.3"
hidden: false
createdAt: "2021-11-10T15:03:55.029Z"
updatedAt: "2022-09-15T21:01:11.033Z"
---

>ℹ The **B2B Checkout Settings** app is part of VTEX’s [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution, a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend that you use it alongside the other apps in this suite for all functionalities to work as expected.

In B2B commerce, it is often necessary to provide customized options during checkout, such as:

* Making specific payment methods available for each organization or cost center.
* Providing pre-filled addresses.
* Including a purchase order number in the order.
* Offering the option to create an order quote before making an actual purchase.

The **B2B Checkout Settings** app works alongside other **B2B Suite** apps to extend the checkout experience for users who are members of organizations, adding all the above possibilities to the checkout page.


## Before you start

First, make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed in your machine.

To use **B2B Checkout Settings**, you must have the [B2B Organizations](https://developers.vtex.com/docs/guides/vtex-b2b-organizations) app installed in your store, which will enable you to group B2B users into organizations, with their own assigned payment methods, price tables, product collections, and cost centers. 

You must also have the [Storefront Permissions](https://developers.vtex.com/docs/guides/vtex-storefront-permissions) app installed – it allows you to grant specific storefront roles for B2B users in an organization. See the **Storefront Permissions** app documentation for information on the available roles and how to customize their permissions.


## Installation

You can install this app by running `vtex install vtex.b2b-checkout-settings` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

After this command, the app will be installed in your VTEX Admin, and B2B store administrators can access it on **Store Setup** > **B2B Checkout Settings**.


## How it works

Considering B2B stores often need similar customizations, **B2B Checkout Settings** provides a ready-to-use customized checkout page for B2B scenarios.

Once **B2B Checkout Settings** is installed in your account, every script contained in its [`checkout-ui-custom` folder](https://github.com/vtex-apps/b2b-checkout-settings/tree/master/checkout-ui-custom) will be automatically linked to your store. The app will customize your checkout page with the functionalities described below. You will also be able to [configure](#configuration) the app on **Store Setup** > **B2B Checkout Settings**.


>ℹ The behavior of the checkout page in VTEX stores is customizable through JavaScript code. In case you need additional customization, we recommend that you use [Checkout UI Custom](https://apps.vtex.com/vtex-checkout-ui-custom/p) if you prefer using the VTEX Admin interface or [Checkout UI Settings](https://developers.vtex.com/docs/guides/vtex-checkout-ui-settings) if you prefer a code-only option.


### Restricted access to checkout

This app automatically checks users’ roles within the organization by communicating with the **B2B Organizations** app, and validates if the user has the required permissions to access checkout, by communicating with the Storefront Permissions app.

By default, users with any storefront role can access checkout, except for users with the **Organization Buyer** role. Any attempt to proceed to checkout without the required permission will result in a notification with the following message: _You don’t have access to the checkout_.

Note that if you have [Storefront Permissions UI](https://developers.vtex.com/docs/guides/vtex-storefront-permissions-ui) installed, you can customize these permissions on the VTEX Admin by accessing **Account Settings > Storefront Permissions**.


### Cost Center addresses

The **B2B Checkout Settings** app communicates with the **B2B Organizations** app and automatically lists the [Cost Center addresses](https://developers.vtex.com/docs/guides/vtex-b2b-organizations#cost-center-details) associated with the user during checkout:

| ![cost-center-details-addresses](https://raw.githubusercontent.com/vtex-apps/b2b-checkout-settings/master/docs/images/cost-center-details-addresses.png) |
|-|
|**Cost Center Details** page, displaying two options of addresses associated with the cost center in question |

| ![shipping](https://raw.githubusercontent.com/vtex-apps/b2b-checkout-settings/master/docs/images/shipping.png) |
|-|
| **Cost Center Details** page, displaying two options of addresses associated with the cost center in question | Checkout page for an user associated with this organization and cost center |


### Purchase order number field

A purchase order (PO) is a commercial agreement between a buyer company and a B2B store, authorizing the payment for products or services to be delivered in the future within a specific time frame.

Having a purchase order number allows B2B customers to pay for authorized purchases by referencing this number. The purchase order is authorized and issued in advance by the company that is making the purchase.

Using **B2B Checkout Settings**, it is possible to enable an optional **Reference or PO Number** field for customers to insert this information during the checkout.

![purchase-order](https://raw.githubusercontent.com/vtex-apps/b2b-checkout-settings/master/docs/images/purchase-order.png)

See the [Configuration](#configuration) section to understand how to enable or disable this button.

## Configuration

To change app settings, in the VTEX Admin go to **Store Setup** > **B2B Checkout Settings**.

![b2b-checkout-settings](https://raw.githubusercontent.com/vtex-apps/b2b-checkout-settings/master/docs/images/b2b-checkout-settings.png)

You can use the toggle button to activate or deactivate the available settings:

* **Show Purchase Order Number Field:** enabling this will add the **Reference or PO Number** input field to the checkout page. This will allow users to insert a purchase order number during checkout.
* **Show 'Create a Quote' Button:** enabling this will add the `Create a Quote` button to checkout, which allows users to create a quote using the current contents of their cart.

> ⚠️ You should only enable the `Create a Quote` button if your store has the [B2B Quotes & Carts](https://developers.vtex.com/docs/guides/vtex-b2b-quotes) app installed. Check the **B2B Quotes** app documentation for more information on how order quotes work.