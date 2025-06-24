---
title: "Becoming a registered VTEX App Store developer"
slug: "vtex-io-documentation-becoming-a-registered-vtex-app-store-developer"
hidden: false
createdAt: "2021-11-12T20:06:26.255Z"
updatedAt: "2025-06-24T13:23:53.214Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store"
---

[**VTEX App Store**](https://apps.vtex.com/) is a marketplace for VTEX IO plug-and-play solutions.

As a developer, you can share your own solutions with other VTEX users in **VTEX App Store** so they can also leverage their business.

To become a VTEX App Store seller, follow these steps:

1. Express interest to our team.
2. Sign a commercial agreement.
3. Register as a VTEX App Store seller.

## Instructions

### Step 1 - Expressing your interest

Fill out the [Application form](https://vtex.com/us-en/partners/) to publish your application or integration on VTEX App Store.

The form helps our team understand the best approach and prioritize the publication demands.

### Step 2 - Signing our commercial agreement

If the form is complete and the team agrees that the application is suitable for the VTEX App Store, the next step is to sign a commercial agreement with VTEX.

This contract, provided by the VTEX team, grants VTEX distribution rights over the app. Additionally, it enrolls your account in the VTEX **Network Partner Program** if you're not already a member.

> ℹ️ The [Network Partner Program](https://network.vtex.com/terms_of_use) provides access to a VTEX account, allowing you to test and develop new apps and receive tech support from the VTEX partner team.

### Step 3 - Registering as a VTEX App Store seller

The App Store is a marketplace where developers who want to distribute their apps should register as sellers.

This [seller-marketplace configuration](https://help.vtex.com/tutorial/configuring-the-marketplace-between-vtex-stores--tutorials_6520) is done through the `vtex.app-store-seller` app.

Follow the steps below to register as a new seller on VTEX App Store:

1. In your terminal, log in to your VTEX account by running the `vtex login {accountName}` command. Replace the values between curly brackets based on your account name.
2. Run `vtex install vtex.app-store-seller@0.x` to install the `vtex.app-store-seller` app.
3. Access the admin of the VTEX account in which you're working.
4. In `Installed apps`, access `Seller setup` and fill out the required fields.
5. Select the sales channel you intend to use to connect to the App Store.
6. Choose an affiliate ID, made up of 3 consonants:

![submitting-seller-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-1.png)

![submitting-seller-2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-2.png)

After submitting the request to be a seller, you can check its status until our team approves it. This approval is required to publish your app successfully in the VTEX App Store.
