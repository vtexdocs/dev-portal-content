---
title: "Storefront Permissions UI"
slug: "vtex-storefront-permissions-ui"
excerpt: "vtex.storefront-permissions-ui@1.1.1"
hidden: false
createdAt: "2021-08-12T01:05:10.534Z"
updatedAt: "2022-11-14T14:14:48.952Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

**Storefront Permissions UI** provides an interface for the [Storefront Permissions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions) app, which is part of VTEX’s [B2B Suite](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-suite) solution, a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships.

B2B customers often play distinct roles within their organization, such as professional buyer, manager, or supervisor. Each role is associated with a different set of permissions, depending on the actions the user needs to perform.

This app communicates with the backstage **Storefront Permissions** app and provides the following features for this scenario:

* [Roles management](#roles-management): allow VTEX Admin users to manage B2B roles and associated app permissions through an interface.
* [Theme blocks configuration](#theme-blocks-configuration): enable conditional theme blocks so that only users with the required permissions can access determined parts of the content in your storefront.

We recommend that you use it alongside the other apps in the [B2B Suite](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-suite) for all functionalities to work as expected.


## Before you start

Make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install) installed in your machine.


## Installation

You can install the app by running `vtex install vtex.storefront-permissions-ui` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

After this command, the app will be installed in your VTEX Admin, and you can access it on **Account Settings** > **Storefront Permissions**.

> ℹ Installing **Storefront Permissions UI** has the effect of automatically installing the [Storefront Permissions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions) app as a dependency, in case it is not already installed.

## Roles management

To manage roles and their respective app permissions using the Storefront Permissions UI, follow the steps below after installing the app.

1. At the VTEX Admin, navigate to **Account Settings** > **Storefront Permissions**.
2. Click on one of the [available storefront roles](#available-storefront-roles).
3. Click on one of the listed apps.

    > ℹ Only apps that are integrated with **Storefront Permissions** will be on the list – check our [Storefront Permissions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions#advanced-app-integration-optional) documentation for more information.

4. Select which permissions you want to enable for the role, as illustrated below.
5. Once you are done, click on `Save`.

![storefront-permissions-ui](https://raw.githubusercontent.com/vtex-apps/storefront-permissions-ui/master/docs/images/storefront-permissions-ui.gif)

After associating roles with the desired permissions, you may then assign roles to users. To learn more about this, read our [B2B Organizations documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-organizations#users).


### Available storefront roles

In the following table, you can see the available storefront roles, their key used for identification in the app’s code, and their description.


| **Role** | **Key** | **Description** |
|---|---|---|
| Store Admin | `store-admin` | Store administrator, that is, a user who has access to the VTEX Admin. |
| Sales Admin | `sales-admin` | Sales administrator user who can manage all sales users. |
| Sales Manager | `sales-manager` | Sales manager user who can manage sales users in the same organization, as well as assist or impersonate buyers during navigation or purchase. |
| Sales Representative | `sales-representative` | Sales representative user who can assist or impersonate buyers in the same cost center during navigation or purchase.  |
| Organization Admin | `customer-admin` | Main organization user who manages the organization information, as well as its members and cost centers. |
| Organization Approver | `customer-approver` | Organization user who can take a saved cart or quote that was created by an **Organization Buyer** and use it to place an order. |
| Organization Buyer | `customer-buyer` | Organization user who has the ability to add items to cart. If the **B2B Quotes** app is installed, they are also able to save their cart for future use or create a quote. |


## Theme blocks configuration

If you only want users with roles that have the required permissions to be able to access determined parts of the content in your storefront, you can also configure conditional blocks in your store’s theme. These types of blocks allow you to validate information in order to display or hide content in your storefront.

In case you need more information on how to start building your own theme, read our [documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-1-basicsetup) before you proceed.

If you are experienced in developing and customizing your store’s theme, follow the steps below to declare the conditional blocks enabled by **Storefront Permissions UI**.

1. Open your store theme app’s repository in your local files.
2. In the `manifest.json` file, under `dependencies`, add `"vtex.storefront-permissions-ui": "1.x"`, like in the example below.

    ```json
     "dependencies": {
       "vtex.storefront-permissions-ui": "1.x"
      },
    ```

3. Now, you can use the `check-permission`, `allowed-content` and `disallowed-content` blocks on any files you want in your store’s theme. See more information on these blocks below.

    | **Block name** | **Description** |  |
    |---|---|---|
    | `check-permission` | Checks if the current user has the required permissions to access the content wrapped with this block.<br>You can wrap content blocks with check-permission when declaring them to validate if the user has the required permissions to see that content. Example: `check-permission#carousel` |  |
    | `allowed-content` | Allows you to define on children blocks the content that will be shown for allowed users – users with roles that have the required permissions to view the block. |  |
    | `disallowed-content` | Optional block that allows you to define on children blocks the content that will be shown for disallowed users – users with roles that do not have the required permissions to view the block. |  |
    

    This component will check if the user has permission to see the `allowed-content`, otherwise they will see the `disallowed-content`.
    
    The `check-permission` block has a prop named `roles`, which lets you define an array of roles that are allowed to see the blocks defined under the children blocks of `allowed-content`.
    
    | **Prop name** | **Type** | **Description** | **Required** | **Example** |
    |---|---|---|---|---|
    | `roles` | array of strings | List of the allowed roles, identified by their key. Learn more about each role and its key in the [Available storefront roles](#available-storefront-roles) section. | true | `["store-admin", "sales-admin"]` |


#### Example

In the example below, in a store’s home, a carousel with banners will only be visible to logged in users with the `store-admin` or `sales-admin` roles. Users with other roles will see a warning message (`**You don't have access to this content**`) instead.

```diff
{
  "store.home": {
    "blocks": [
+     "check-permission#carousel",
      "shelf#home",
      "info-card#home",
      "rich-text#question",
      "rich-text#link"
    ]
  },
+  "check-permission#carousel": {
+    "props": {
+      "roles": ["store-admin", "sales-admin"]
+    },
+    "blocks": ["allowed-content#carousel","disallowed-content#carousel"]
+  },
+  "allowed-content#carousel": {
+    "children": ["carousel#home"]
+  },
+  "disallowed-content#carousel": {
+    "children": ["rich-text#disallowed"]
+  },
+  "rich-text#disallowed": {
+    "props": {
+      "text": "**You don't have access to this content**"
+    }
+  },
  "carousel#home": {
    "props": {
      "autoPlay": false,
      "banners": [
        {
          "image": "https://storecomponents.vteximg.com.br/arquivos/banner-principal.png",
          "mobileImage": "https://storecomponents.vteximg.com.br/arquivos/banner-principal-mobile.jpg"
        },
        {
          "image": "https://storecomponents.vteximg.com.br/arquivos/banner.jpg",
          "mobileImage": "https://storecomponents.vteximg.com.br/arquivos/banner-principal-mobile.jpg"
        }
      ],
      "height": 720,
      "showArrows": true,
      "showDots": true
    }
  },
```