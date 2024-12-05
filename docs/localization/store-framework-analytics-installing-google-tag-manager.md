---
title: "Installing Google Tag Manager"
slug: "store-framework-analytics-installing-google-tag-manager"
hidden: false
createdAt: "2022-02-01t13:34:01.638z"
updatedAt: "2024-11-18T16:28:11.922Z"
excerpt: "Discover the steps to install the Google Tag Manager app in your Store Framework store."
---

This guide provides instructions for managing Analytics on Store Framework stores by installing and configuring [Google Tag Manager (GTM)](https://tagmanager.google.com/). It also outlines restrictions to avoid performance issues and unpredictable behavior, such as blocklists for custom HTML tags and variables.

## Before you begin

> ⚠️ This app is only available for stores built with [Store Framework](https://developers.vtex.com/docs/guides/store-framework). For stores built with Legacy CMS Portal, see [Configuring Google Tag Manager](https://help.vtex.com/en/tutorial/how-to-setup-google-analytics-in-vtex-store--G2P0rmSrEiqCcmUMyUUwG#configuring-google-tag-manager).

If you have already installed the Google Tag Manager app, go to the [Create a Google Analytics 4 property](#create-a-google-analytics-4-property) step to create the property and follow along.

<Steps>

### Have a Google account

You need a Google account to use Google Tag Manager (GTM). If you already use Google products like Gmail, you can use the same account.

If you do not have an account for a Google product, create one by following Google's guide on [Creating your Google account](https://accounts.google.com/signup/v2/webcreateaccount?service=analytics&continue=https%3A%2F%2Ftagmanager.google.com%2F&dsh=S1158101756%3A1642078409369040&biz=true&flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true).

### Have a GTM Container

To use a GTM ID in your store, you need a GTM container. If you do not have one, follow the steps in the [Create a new account and container tutorial](https://support.google.com/tagmanager/answer/6103696?hl=en#install).

After creating a container, find its GTM ID in the `Container ID` column. Note this ID, as you will need it later in the installation process.

### Create a Google Analytics 4 property

Create a Google Analytics 4 (GA4) property using the GA4 Setup Assistant. This property collects data alongside your existing Universal Analytics (UA) property. To create the GA4 property, follow [Google’s official guide](https://support.google.com/analytics/answer/9744165#zippy=%2Cin-this-article).

### Take note of GTM settings

Take note of the Measurement ID, also known as [*G- ID*](https://support.google.com/analytics/answer/9539598#find-G-ID), as it will be used later to set up the GA4 tag on GTM.

</Steps>

## Instructions

1. In VTEX **Admin**, go to **Apps > Extensions Hub > App Store**.

2. Search for the Google Tag Manager app and click `Get App`.

   ![installing-gtm](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/installing-gtm.gif)

3. You will be redirected to the [App Store page](https://apps.vtex.com/vtex-google-tag-manager/p). If you are not currently logged in, log in to your account.

   ![gtm-on-app-store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/gtm-on-app-store.gif)

4. After logging in, you will be redirected to the [App Store landing page](https://apps.vtex.com/). In the search field, type `Google Tag Manager`, click the app, and then click `GET APP`.

5. On the checkout page, click `PLACE ORDER`.

> ℹ️ GTM is a free app.

6. You will see a success message about the purchase. Click `GO TO INSTALL PAGE` to be redirected to the GTM setup page in VTEX admin.

7. On the GTM setup page in VTEX admin, click `INSTALL.`

   ![google-tag-manager](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-tag-manager.gif)

8. The GTM app settings page will open for you to complete with the necessary information.
In the Google Tag Manager field, add your **GTM ID**. 
Check the box **Send Google Analytics 4 Events**

> ℹ️ To find your store's **GTM ID**, you first need to have a container for the Google Tag Manager account. If you do not have one yet, follow the [create a new account and container tutorial](https://support.google.com/tagmanager/answer/6103696?hl=en#install). Once you have created it, you can find the GTM ID in the `Container ID` column of the container.

![gtm-new-field](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-new-field___bf665f34409d6d7cbcfc79239e277ee0.png )

9. Click `SAVE`.

Once you have installed the app and check the box **Send Google Analytics 4 Events**, see the [Configuring Google Analytics 4 Configuration tag in Google Tag Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager) documentation and learn how to set up the variables, triggers, and tags necessary for the app to work.

## Restrictions

To avoid performance problems and unpredictable behavior, the VTEX IO Google Tag Manager solution uses the native GTM blacklist feature. Learn more in the [Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/restrict). By default, the HTML ID is blocked, which automatically blocks all tags, variables, and triggers of type `customScripts`.

The main consequence of this blacklist is that custom HTML tags will not be triggered. **The HTML blacklist is the default setting in the VTEX Google Tag Manager app**. To disable this restriction, go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@3.x/setup` and check the toggle below.

>⚠ Replace {accountName} with your store account name.

![restrictions](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-installing-google-tag-manager-1.png)

The most commonly used custom HTML tags are integrations with third-party services, such as Customer Chat, Analytics, Remarketing, and Pixel tags. If your store requires custom HTML for any of these cases, the integration can either be done by transforming the tags into a VTEX IO [Pixel app](https://developers.vtex.com/docs/guides/vtex-io-documentation-pixel-app) or by removing this restriction.

Below is the full list of tags and variables that are blocked by default in the VTEX IO Google Tag Manager solution:

**Blocked tags**

- Custom HTML Tag - html
- Eulerian Analytics Tag - ela
- SaleCycle JavaScript Tag - scjs
- Upsellit Global Footer Tag - uslt
- Upsellit Confirmation Tag - uspt

**Blocked variables**

- Custom JavaScript Variable - jsm

See a list with all the available GTM tags on [the Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/datalayer).
