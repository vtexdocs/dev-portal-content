---
title: "Installing Google Tag Manager"
slug: "vtex-io-documentation-installing-google-tag-manager"
hidden: false
createdAt: "2022-02-01t13:34:01.638z"
updatedAt: "2022-12-13T20:17:44.697Z"
excerpt: "Steps to install the Google Tag Manager app in your VTEX Admin."
category: "Storefront Development"
seeAlso:
  - "/docs/guides/vtex-io-documentation-setting-up-google-tag-manager"
---

This guide provides a step-by-step guide on installing and configuring Google Tag Manager (GTM) on Store Framework stores. The guide also highlights some restrictions to avoid performance issues and unpredictable behavior, including blocklists for custom HTML tags and variables.
## Before you start

You need a Google account to use Google Tag Manager. You can use the same account if you already use Google products, such as Gmail.

If you do not have a Google account, create one at [Creating your Google account](https://accounts.google.com/signup/v2/webcreateaccount?service=analytics&continue=https%3A%2F%2Ftagmanager.google.com%2F&dsh=S1158101756%3A1642078409369040&biz=true&flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true).

> ⚠️ If you install a new version of the Google Tag Manager (GTM) app, the VTEX environment deletes the previous GTM data that was stored. Therefore, if you already have a GTM version installed in your account, review the data you have added before installing a new version of the app.

## Instructions

1. Access your VTEX **Admin** and go to **Account settings > Apps > App Store**.

2. Search for the Google Tag Manager app and click `Install`. You will be redirected to the [App Store page](https://apps.vtex.com/vtex-google-tag-manager/p). Log in to your App Store account if you are not currently logged in. ![image2](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-installing-google-tag-manager-0.gif)

3. Then, you will be redirected to the [App Store landing page](https://apps.vtex.com/). In the search field, type `Google Tag Manager`, click the app, and then click `GET APP`.

4. On the checkout page, click *check the Google Tag Manager terms and conditions*, and if you agree, click `PLACE ORDER`.

> ℹ️ GTM is a free app.

5. You’ll see a success message about the purchase. Click `GO TO INSTALL PAGE`, which will redirect you to the GTM setup page.
6. You'll see a warning message prompting you to complete the necessary settings. Scroll down and type your **GTM ID** in the Google Tag Manager field.
7. Click Save.

> ℹ️ To find your store's **GTM ID**, first, you need a container for the Google Tag Manager account. If you do not have one, follow the [create a new account and container tutorial](https://support.google.com/tagmanager/answer/6103696?hl=en#install) and, then, get the GTM ID from the `Container ID` column of the container.

Once you have installed the app, see the [Setting up Google Tag Manager documentation](/docs/guides/vtex-io-documentation-setting-up-google-tag-manager) and learn how to set up the variables, triggers, and tags required for the app to work.

## Restrictions

To avoid performance problems and unpredictable behavior, the VTEX IO Google Tag Manager solution uses the native GTM blacklist feature. You can read more about this feature in the [Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/restrict). By default, the HTML ID is blocked, automatically blocking all the tags, variables, and triggers of type `customScripts`. The main consequence of this blacklist is that custom HTML tags will not be triggered. **The HTML blacklist is the VTEX Google Tag Manager app default.** If you want to disable this restriction, go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@3.x/setup` and check the toggle below.

![restrictions](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-installing-google-tag-manager-1.png)

Most of the widely used custom HTML tags are integrations with third-party services, like Customer Chat, Analytics, Remarketing, and Pixel tags. If your store needs custom HTML for any of those cases, the integration can either be done by transforming the tags in a [VTEX IO Pixel app](/docs/guides/pixel-apps) or by removing this restriction. See below the full list of tags and variables that are blocked by default in the VTEX IO Google Tag Manager solution:

**Blocked tags**

- Custom HTML Tag - html
- Eulerian Analytics Tag - ela
- SaleCycle JavaScript Tag - scjs
- Upsellit Global Footer Tag - uslt
- Upsellit Confirmation Tag - uspt

**Blocked variables**

- Custom JavaScript Variable - jsm

See a list with all the available GTM tags on [the Google Developer Guide](https://developers.google.com/tag-platform/tag-manager/web/datalayer).
