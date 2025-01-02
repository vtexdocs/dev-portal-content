---
title: "Installing Google Tag Manager"
slug: "vtex-io-documentation-installing-google-tag-manager"
hidden: false
createdAt: "2022-02-01t13:34:01.638z"
updatedAt: "2024-12-18T14:38:14.781Z"
excerpt: "Discover the steps to install the Google Tag Manager app in your Store Framework store."
---

This guide provides instructions for managing Analytics on Store Framework stores by installing and configuring [Google Tag Manager (GTM)](https://tagmanager.google.com/). It also outlines restrictions to avoid performance issues and unpredictable behavior, such as blocklists for custom HTML tags and variables.

## Before you begin

> ⚠️ This app is only available for stores built with [Store Framework](https://developers.vtex.com/docs/guides/store-framework). For stores built with Legacy CMS Portal, see [Configuring Google Tag Manager](https://help.vtex.com/en/tutorial/how-to-setup-google-analytics-in-vtex-store--G2P0rmSrEiqCcmUMyUUwG#configuring-google-tag-manager).

If you have already installed the Google Tag Manager app, go to the [Create a Google Analytics 4 property](#create-a-google-analytics-4-property) step to create the property and continue.

<Steps>

### Get a Google account

You need a Google account to use Google Tag Manager (GTM). If you already use Google products like Gmail, you can use the same account.

If you don't have an account, create one by following Google's guide on [Creating your Google account](https://accounts.google.com/lifecycle/steps/signup/workspaceinterstitial?continue=https://tagmanager.google.com/&ddm=1&dsh=S1747300419:1734533693867352&flowEntry=SignUp&flowName=GlifWebSignIn&service=analytics&TL=AE--Llz4c9wxBXCL_HUOxs0VQwkCVyn1dVQZDuQL8ZvZUnVGcbKDfXTlaI-fN0ks).

### Get a GTM container

To use a GTM ID in your store, you need a GTM container. If you don't have one, follow the [Create a new account and container](https://support.google.com/tagmanager/answer/6103696?hl=en#install) tutorial.

After creating a container, find its GTM ID in the `Container ID` column. Be sure to save this ID, as it will be required later in the installation process.

### Create a Google Analytics 4 property

Create a Google Analytics 4 (GA4) property using the GA4 Setup Assistant. This property collects data alongside your existing Universal Analytics (UA) property. To create the GA4 property, follow [Google’s official guide](https://support.google.com/analytics/answer/9744165#zippy=%2Cin-this-article).

### Take note of GTM settings

Take note of the Measurement ID, also known as [G-ID](https://support.google.com/analytics/answer/9539598#find-G-ID), as it will be used later to configure the GA4 tag on GTM.

</Steps>

## Instructions

1. In the VTEX **Admin**, go to **Apps > Extensions Hub > App Store**.

2. Search for the Google Tag Manager app and click `Get App`.

   ![installing-gtm](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/installing-gtm.gif)

3. You will be redirected to the [App Store page](https://apps.vtex.com/vtex-google-tag-manager/p). If you are not currently logged in, log in to your account.

   ![gtm-on-app-store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/gtm-on-app-store.gif)

4. After logging in, you will be redirected to the [App Store landing page](https://apps.vtex.com/). In the search field, type `Google Tag Manager`, click the app, and then click `Get App`.

5. On the checkout page, click `Place Order`.

> ℹ GTM is a free app.

6. You will see a success message about the purchase. Click `Go to Install Page` to be redirected to the GTM setup page in the VTEX admin.

7. On the GTM setup page in VTEX admin, click `Install`.

   ![google-tag-manager](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-tag-manager.gif)

8. The GTM app settings page will open for you to complete the required fields.
   In the Google Tag Manager field, add your **GTM ID**.
   Check the box for **Send Google Analytics 4 Events**.

> ℹ To find your store's **GTM ID**, you first need to create a container in your Google Tag Manager account. If you don't have one yet, follow the [Create an account and container](https://support.google.com/tagmanager/answer/6103696?hl=en#install) tutorial. Once created, you can find the GTM ID in the `Container ID` column of the container.

![gtm-new-field](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-new-field___bf665f34409d6d7cbcfc79239e277ee0.png)

9. Click `Save`.

Once you have installed the app and checked the box **Send Google Analytics 4 Events**, see [Configuring Google Analytics 4 configuration tag in Google Tag Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager) to learn how to set up the variables, triggers, and tags for the app to work.

## Restrictions

To prevent performance issues and unpredictable behavior, the VTEX IO Google Tag Manager solution uses the native GTM blacklist feature. Learn more in the [Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/restrict). By default, the HTML ID is blocked, which automatically blocks all tags, variables, and triggers of the `customScripts` type.

As a result, custom HTML tags will not be triggered. **The HTML blacklist is the default setting in the VTEX Google Tag Manager app**. To disable this restriction, go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@3.x/setup` and check the setting below.

> ⚠ Replace `{accountName}` with your store account name.

![restrictions](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-installing-google-tag-manager-1.png)

The most commonly used custom HTML tags are for integrations with third-party services, such as Customer Chat, Analytics, Remarketing, and Pixel tags. If your store requires custom HTML for any of these cases, you can integrate it by transforming the tags into a VTEX IO [Pixel app](https://developers.vtex.com/docs/guides/vtex-io-documentation-pixel-app) or by removing this restriction.

Below is the complete list of tags and variables blocked by default in the VTEX IO Google Tag Manager solution:

**Blocked tags**

- Custom HTML Tag - html
- Eulerian Analytics Tag - ela
- SaleCycle JavaScript Tag - scjs
- Upsellit Global Footer Tag - uslt
- Upsellit Confirmation Tag - uspt

**Blocked variables**

- Custom JavaScript Variable - jsm

View the complete list of available GTM tags in [the Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/datalayer).
