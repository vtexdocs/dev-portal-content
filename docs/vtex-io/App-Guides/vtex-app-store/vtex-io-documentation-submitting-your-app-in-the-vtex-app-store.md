---
title: "Submitting your app to the VTEX App Store"
slug: "vtex-io-documentation-submitting-your-app-in-the-vtex-app-store"
hidden: false
createdAt: "2020-09-11T19:35:00.561Z"
updatedAt: "2022-12-13T20:17:44.608Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-business-guidelines-app-monetization"
 - "/docs/guides/vtex-io-documentation-business-guidelines-marketing-assets"
 - "/docs/guides/vtex-io-documentation-design-guidelines"
 - "/docs/guides/vtex-io-documentation-engineering-guidelines"
---

To share your solutions in the VTEX App Store, you must follow our homologation process:

1. Check out our business, design and engineering guidelines.
2. Send the app's data for validation.
3. Wait for the App homologation.

## Before you start

Before submitting your app to the VTEX App Store, you must be a registered VTEX App Store developer. For more information, check [this guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer) and follow the necessary steps.

You should also have already [set your app's billing model](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-your-apps-billing-model) and [prepared it for distribution](https://developers.vtex.com/docs/guides/vtex-io-documentation-preparing-your-app-distribution).

## Step by step

### Step 1 - Checking out our business, design and engineering guidelines

To submit and publish your app on VTEX App Store, you must follow our business, design and engineering guidelines. These guidelines guarantee the standard of quality, viability and usability of all apps made available to our tenants through the VTEX App Store, so it is important that you are aware of them before submitting your extension for the homologation process. You can check in [Business guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-business-guidelines-vtex-app-store), [Design guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-design-guidelines), [Engineering guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-engineering-guidelines).

### Step 2 - Sending the app data for validation

Once you've configured the app assets, it is time to submit the app's data for evaluation by the app store development team. First of all, you'll need to meet the following prerequisites:

- Have a [**GitHub**](https://github.com/) account (since your project evaluation during the homologation process is made through Pull Requests).
- [Publish your app on the VTEX IO development platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/). Remember to publish the app in the VTEX account in which you are working and in a [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/) that can be tested by the team.
- [Deploy your app on the VTEX IO development platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available#step-6---deploying-the-app-stable-version).

With the first two prerequisites met, you're ready to send you app through to VTEX's homologation process:

1. Using your CLI, [log into the VTEX account](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#logging-into-your-vtex-account) in which the app was published.
2. Access the folder containing your app.
3. Run `vtex plugins add submit` plugin in the [VTEX CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

> ⚠️ The `vtex plugins add submit` plugin will only work if the VTEX IO CLI is updated to version 3.x that has a plugin-based architecture. Check out the [Updating VTEX IO'S CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-update) and [Managing plugins documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) for more information.

4. Then, run `vtex submit`. You can also specify which version your want to submit by running `vtex submit {vendor}.{name}@{version}`.

After step 4 , a GitHub repository will be automatically created and a Pull Request link will be displayed on your CLI.

> ℹ️ You'll be added to the repository with your GitHub handle and will have read-only permissions to be able to follow your app's review process. Comments can be followed in the same repository and after performing adjustments, any new app version can be submitted following the step 2 above, thereby creating a new `branch` containing the new version in the same repository.

![submitting-github-terminal](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store-0.png)

When a branch has the adjustments it needs, you should open a *Pull Request* to the VTEX team.

![submitting-github-pr](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store-1.png)

### Step 3 - Waiting for the app homologation

Once the app data has been sent in the PR, our product team will validate it in order to approve and merge it.

This process, called homologation, will ensure that any published application has a clear value proposition, is safe, stable, aligned with VTEX's brand and business guidelines and is in compliance with the company's business, design and technology standards.

Therefore, the **3 main criteria** taken into account by the VTEX product team are:

- **Business**  - Whether the app has a business model with viable and sustainable pricing and accomplishes what it sets out to do.
- **UX**  - Whether the app offers a good user experience, following VTEX Styleguide rules.
- **Security and performance**  - Whether the app's performance is safe and efficient.

You can find more details on how these criteria will be assessed in our [Homologation requirements for the VTEX App Store](https://developers.vtex.com/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store).

>ℹ The SLA for the homologation process is 45 days from [the moment the app data is sent for validation](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store#step-2-sending-the-app-data-for-validation).

When an app fulfills the above-mentioned criteria, the PR will be approved and your new app version is ready to be released and made available in the VTEX app store.

Notice the following: once everything is approved, a product (which effectively is your app) will be automatically created in your store catalog. Do not remove our change it - this product is what integrates your app to the VTEX App Store marketplace.

## Frequently Asked Questions

### Does the homologation process occur only for apps to be published on the App Store?

Yes. For an app to be eligible for publication in the App Store, it must be [public](https://developers.vtex.com/docs/guides/vtex-io-documentation-10-making-your-app-publicly-available) – meaning it should be available for all VTEX accounts to install or purchase.

In technical terms, this translates to having a [billing model set up for the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-your-apps-billing-model#setting-the-app-as-public). The homologation process must occur for new apps and new major versions of apps.

### Which type of apps goes through a homologation process (Storefront apps, Admin apps, Backend apps and Pixel apps, Private apps, Public app, Single account, Multi-account)?

All apps must go through the homologation process before they're published to the App Store. The type of functionality (storefront, admin, backend, pixel) does not make any difference. Only public apps, that can be installed on multiple accounts, are eligible – if you want your app to be private to your organization and installed on a single account, you can [install it](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) directly.

### Which category does an Edition app go into? And does it also go through a homologation process?

[Edition apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) work as app bundles – they make it easier to guarantee a set of apps will be installed on certain accounts. Only one Edition app can be set per account, and most accounts use the default alternatives that are provided by VTEX:

- `vtex.edition-business`: all apps required to build a store with our legacy [CMS](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC).
- `vtex.edition-store`: all apps required to build a store with Store Framework.

Merchants with advanced requirements might wish to develop their own Edition apps. To do so they must fulfill the [requirements to become a Sponsor Account](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account), but no homologation process is required since Edition apps are not installed or set through the App Store.

### Do custom and non-custom apps (non-boilerplate apps) also go through a homologation process?

Only apps meant to be published in the App Store must go through the homologation process.

### How much time does it take for an app homologation process to complete? Do we have a formal SLA?

The SLA is 45 days from [the moment the app data is sent for validation](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store#step-2-sending-the-app-data-for-validation).
