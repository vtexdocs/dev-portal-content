---
title: "Submitting your app to the VTEX App Store"
excerpt: "Learn how to submit your app for distribution in the VTEX App Store."
slug: "vtex-io-documentation-submitting-your-app-in-the-vtex-app-store"
hidden: false
createdAt: "2020-09-11T19:35:00.561Z"
updatedAt: "2025-07-07T17:30:00.000Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-business-guidelines-app-monetization"
 - "/docs/guides/vtex-io-documentation-business-guidelines-marketing-assets"
 - "/docs/guides/vtex-io-documentation-design-guidelines"
 - "/docs/guides/vtex-io-documentation-engineering-guidelines"
---

Learn how to successfully submit your app for distribution in the VTEX App Store by following this guide. The VTEX App Store is a marketplace where VTEX clients can discover and install applications that enhance their ecommerce experience. Before your app can be featured in the VTEX App Store, it must pass the homologation process, which involves evaluation in three key areas: business, user experience (UX), and security/performance. This process applies to all apps, regardless of their functionality, such as storefront, admin, backend, or pixel.

> ⚠️ Keep in mind that the homologation process may take 45 days from [the moment the app data is sent for validation](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store#step-2-sending-the-app-data-for-validation).

> [Edition apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) do not need to be published in the App Store. Instead, accounts that wish to develop their own Edition apps must fulfill the [requirements to become a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account).

## Before you begin

### Technical requirements

To complete this guide, you will need:

- **[GitHub](https://github.com/) account:** The app homologation is conducted via GitHub and Pull Requests (PR). Ensure you have a GitHub account.
 - **VTEX IO CLI `3.x`:** Ensure that the VTEX IO CLI is updated to version `3.x`. For instructions, refer to [Updating VTEX IO'S CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-update).

### App prerequisites

Before proceeding with the homologation process, ensure your app meets these prerequisites:

- [**Set up your app's billing model**](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-your-apps-billing-model): To be eligible for publication in the App Store, your app must have a billing model set up. This allows it to be publicly available for all VTEX accounts. If you want your app to be private to your organization and installed on a single account, you do not need to go through the process detailed in this guide and can [install it](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) directly in your account.
- [**Publish your app on the VTEX IO development platform**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/): Publish your app using the VTEX account corresponding to your  `vendor` account and in a [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/) that the VTEX team can test.
- [**Deploy your app on the VTEX IO development platform.**](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available#step-6---deploying-the-app-stable-version)
  
### App Store prerequisites

Finally, before submitting your app to the VTEX App Store, ensure you've completed the following steps:

- [**Become a registered VTEX App Store developer**](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer): To submit an app to the VTEX App Store, you need to be a registered VTEX App Store developer.
- [**Prepared your app for distribution**](https://developers.vtex.com/docs/guides/vtex-io-documentation-preparing-your-app-distribution): Ensure your app adheres to VTEX's [business](https://developers.vtex.com/docs/guides/vtex-io-documentation-business-guidelines-vtex-app-store), [design](https://developers.vtex.com/docs/guides/vtex-io-documentation-design-guidelines), [marketing](https://developers.vtex.com/docs/guides/vtex-io-documentation-business-guidelines-marketing-assets), and [engineering](https://developers.vtex.com/docs/guides/vtex-io-documentation-engineering-guidelines) guidelines. These guidelines guarantee the standard of quality, viability, and usability of all apps made available through the VTEX App Store, so you must be aware of them before submitting your extension for the homologation process.

## Instructions

### Step 1 - Submitting the app for validation

1. Open the terminal and [log in to the VTEX account](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#logging-into-your-vtex-account) corresponding to the app's `vendor` account using the [VTEX IO CLI `3.x`](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).
2. Change to your app's directory.
3. Install the `submit` plugin:
   ```sh
   vtex plugins add submit
   ```
4. Submit your app for the homologation process by running the following command. You can also specify which version to submit by running `vtex submit {vendorAccount}.{appName}@{appVersion}`.
   ```sh
   vtex submit
   ```
5. When prompted, enter the GitHub username that will manage the homologation process. In the following, provide the workspace URL the VTEX team can use to test your app.

![submitting-github-terminal](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store-0.png)

### Step 2 - Managing the homologation process

After completing these steps above, a GitHub repository will be automatically created for your app, and you will be prompted with a PR link in the terminal (e.g., `https://github.com/vtex-reviews/{vendorAccount}.{appName}`). The specified GitHub account will be added to the repository with read-only permissions to follow your app's review process. Comments and adjustments can be made in the same repository. 

> The homologation process applies to both new apps and new major versions of apps. A new branch will be created in the repository for each new app version.

You can work on improvements in a new branch. When the branch has the necessary adjustments, open a PR to the VTEX team for review.

![submitting-github-pr](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store-1.png)

### Step 3 - Waiting for the app homologation

After opening the PR, the VTEX team will validate it for approval and merging. The PR will be approved when the app fulfills the [VTEX App Store guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store) and your new app version will be ready to be released and made available in the VTEX App Store.

> ⚠️ Please note that after the homologation process is completed, a product will be automatically created in your store catalog. Do not remove or modify it, as this product is what integrates your app with the VTEX App Store marketplace.
