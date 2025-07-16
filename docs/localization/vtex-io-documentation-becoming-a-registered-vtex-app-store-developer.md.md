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

As a developer, you can share your own solutions with other VTEX users in the **VTEX App Store**, so they can also leverage them to grow their business.

To become a VTEX App Store seller, follow these steps:

1. Express interest to our team.
2. Sign a commercial agreement.
3. Register as a VTEX App Store seller.

## Instructions

### Step 1 - Expressing your interest

To publish your application or integration on the VTEX App Store, complete the [Application form](https://vtex.com/us-en/partners/).

This form helps our team understand the best approach and prioritize publication requests.

### Step 2 - Signing our commercial agreement

If the form is complete and the team agrees that the application is suitable for the VTEX App Store, the next step is to sign a commercial agreement with VTEX.

This contract, provided by the VTEX team, grants VTEX distribution rights over the app. Additionally, it enrolls your account in the VTEX [Partner Program](https://vtex.com/en-us/partners/) if you're not already a member.

> ℹ️ The Partner Program provides access to a VTEX account, allowing you to test and develop new apps and receive tech support from the VTEX partner team.

### Step 3 - Registering as a VTEX App Store seller

The App Store is a marketplace where developers who want to distribute their apps should register as sellers.

This [seller-marketplace configuration](https://help.vtex.com/tutorial/configuring-the-marketplace-between-vtex-stores--tutorials_6520) is done through the `vtex.app-store-seller` app.

Follow the steps below to register as a new seller on the VTEX App Store:

1. In your terminal, log in to your VTEX account by running the `vtex login {accountName}` command. Replace the values between curly brackets with your account name.
2. Run `vtex install vtex.app-store-seller@0.x` to install the `vtex.app-store-seller` app.
3. Access the VTEX Admin of the account in which you're working.
4. In `Installed apps`, go to `Seller setup` and complete the required fields.
5. Select the sales channel you intend to use to connect to the App Store.
6. Choose an affiliate ID made up of three consonants:

![submitting-seller-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-1.png)

![submitting-seller-2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer-2.png)

After submitting your request to become a seller, you can track its status until it's approved by our team. This approval is required to publish your app successfully in the VTEX App Store.
