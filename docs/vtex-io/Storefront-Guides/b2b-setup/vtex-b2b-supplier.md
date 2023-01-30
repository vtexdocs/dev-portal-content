---
title: "B2B Supplier"
slug: "vtex-b2b-supplier"
hidden: true
createdAt: "2021-10-06T16:52:02.214Z"
updatedAt: "2022-04-26T20:10:07.224Z"
---

The **B2B Supplier** app allows you, as a supplier, to enable customers to sign up and log in as Buyer Organizations in your store. It enables components related to authentication and authorization of users and Buyer Organizations.

## Installation

To install the **B2B Supplier** app, you must follow the steps below.

1. Run the following command on your CLI:

    ```sh
    vtex install vtex.b2b-supplier
    ```

2. Add the app as a dependency in your theme’s `manifest.json` file, as follows:

    ```json
    "dependencies": {
    "vtex.b2b-supplier": "0.x"
    }
    ```

3. Declare the following blocks in a given theme template or inside another block from the theme.

| Block name | Description |
| ----------- |  ----------- |
| `b2b-supplier.sign-up-button` | Renders a `Sign up` button that leads users to the form where they can sign up as a Buyer Organization. |
| `b2b-supplier.approved-status` | Renders an alert informing the Buyer Organization user of their approval status in your store. |

After the installation, it will be possible for buyers to Sign up as a Buyer Organization in your store or for you to create and manage Buyer Organizations via API.

>⚠️ Remember that every time a new Buyer Organization signs up, it is necessary for the supplier to approve their access on Master Data.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `container` |
| `button` |
| `label` |
