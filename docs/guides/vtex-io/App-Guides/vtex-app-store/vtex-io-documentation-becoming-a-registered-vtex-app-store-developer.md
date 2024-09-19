---
title: "Becoming a registered VTEX App Store developer"
slug: "vtex-io-documentation-becoming-a-registered-vtex-app-store-developer"
hidden: false
createdAt: "2021-11-12T20:06:26.255Z"
updatedAt: "2022-12-13T20:17:44.104Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store"
---

>⚠ From the [release of Extensions Hub](https://developers.vtex.com/updates/release-notes/extensions-hub-our-new-place-to-promote-apps-and-partners-inside-vtex-admin), we changed our terms of service to enable VTEX partners to promote and sell their apps in the App Store. Thus, we created an addendum in the contract with partners, considering the app monetization and the new payment flow.
>
> Due to changes in our internal procedures, we applied temporary restrictions related to publishing apps in the App Store:
>
> - Partners that already have published apps and still did not sign the new contract with the addendum must sign it as soon as possible.
> - Only partners that already signed the new contract can publish apps as usual, following the [homologation process](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store).
> - We are not accepting new partners for publishing apps in the App Store.

The [**VTEX App Store**](https://apps.vtex.com/) is a marketplace for VTEX IO plug-and-play solutions.

As a developer, you can **share your own solutions** with other VTEX users in the [**VTEX App Store**](https://apps.vtex.com/) so they can also **leverage their business**.

For that, you must register as a VTEX App Store seller by taking the following steps:

1. Express your interest to our team.
2. Sign our commercial agreement.
3. Register as a VTEX App Store seller.

## Instructions

### Step 1 - Expressing your interest

Fill out the [Application form](https://vtex.com/us-en/partners/) to **share your interest** in publishing your application or integration on the VTEX App Store.

The form will help our team to understand the best approach and prioritize the publication demands.

### Step 2 - Signing our commercial agreement

If the form was correctly filled out and the team agrees that the application is suitable for the VTEX App Store, the next step is to sign a commercial agreement with VTEX.

This contract, provided by the VTEX team to you, will grant VTEX distribution rights over the app. In addition, it is going to sign your account up to the VTEX **Network Partner Program** if you are not already a member.

> ℹ️ The [Network Partner Program](https://network.vtex.com/terms_of_use) provides access to a VTEX account, allowing you to test and develop new apps and have access to tech support from the VTEX partner team.

### Step 3 - Registering as a VTEX App Store seller

The App Store is a **Marketplace**. Therefore, partners looking to distribute their apps should register as a  **seller** there.

This [structure](https://help.vtex.com/tutorial/configuring-the-marketplace-between-vtex-stores--tutorials_6520) (seller - marketplace) configuration is done through the `vtex.app-store-seller` app.

Follow the steps below to register as a new seller on VTEX App Store:

1. Logged into the VTEX account in which you are working, run `vtex install vtex.app-store-seller@0.x` in your terminal.
2. Access the admin of the VTEX account in which you're working.
3. In `Installed apps`, access `Seller setup` and fill out the required fields.
4. Select the sales channel you intend to use to connect to the App Store.
5. Choose an affiliate ID, made up of 3 consonants:

![submitting-seller-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-1.png)

![submitting-seller-2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-2.png)

After submitting the request to be a seller, you can check its `status` until our team approves it. This approval is required in order to complete the next steps and be able to successfully publish your app in the VTEX App Store.
