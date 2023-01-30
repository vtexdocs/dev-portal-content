---
title: "Buyer Organization Supplier"
slug: "vtex-buyer-org-supplier"
hidden: true
createdAt: "2021-10-07T18:58:23.596Z"
updatedAt: "2022-02-04T20:56:01.083Z"
---

The Buyer Organization Supplier app is responsible for storing Buyer Organization data in the Profile System. This app provides an endpoint that receives a [Buyer Organization](https://github.com/vtex-apps/buyer-org-supplier/blob/ec15a9b202f48c4ab94095b02348e70eebde5583/node/typings/buyerOrgService.d.ts) and adds a new user in the Profile System with the given data.

## [Optional] Customization

If you want to customize the data that will be stored in the Profile System, follow the steps in this section. If you would rather use the default behavior, skip to the [Installation](#installation) section.

1. Clone the app [repository](https://github.com/vtex-apps/buyer-org-supplier).
2. Change the `vendor` in the `manifest.json` file to the name of the account where you are logged in.
3. Make the desired changes in the [`createBuyerOrg.ts`](https://github.com/vtex-apps/buyer-org-supplier/blob/main/node/routes/createBuyerOrg.ts) file. This file must inform the data you want to store in the Profile System. It will receive the informed Buyer Organization data and save this information in the Profile System database.
    >⚠️ Do not change the `path` in the `service.json` file, or the Buyer Organization sign up process will fail.

4. Create a fork of the repository.
5. [Publish the app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-publishing-an-app).

## Installation

Follow the steps below to install the app.

1. Run the following command on your CLI. If you opted to customize the app, replace `{vendor}` with the value you set for the `vendor` in the `manifest.json` file before. If you prefer to use the default app behavior, replace `{vendor}` with `vtex`.

    ```
    vtex install {vendor}.buyer-org-supplier
    ```

    >⚠️ Do not install both the default and customized versions of the app, or the Buyer Organization sign up process will fail.

2. Add the app as a dependency in your theme’s `manifest.json` file, as shown below. Once again, if you opted to customize the app, replace `{vendor}` with the value you set for the `vendor` in the `manifest.json` file before. If you prefer to use the default app behavior, replace `{vendor}` with `vtex`.

    ```json
    "dependencies": {
        "{vendor}.buyer-org-supplier":  "0.x"
    }
    ```
