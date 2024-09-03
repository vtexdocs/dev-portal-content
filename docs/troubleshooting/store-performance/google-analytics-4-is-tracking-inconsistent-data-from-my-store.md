---
title: "Google Analytics 4 is tracking inconsistent data from my store"
slug: "google-analytics-4-is-tracking-inconsistent-data-from-my-store"
hidden: false
createdAt: "2024-09-03T14:22:52.165Z"
updatedAt: ""
excerpt: "If Google Analytics 4 is not accurately traciing data, try server-side tagging and configuring a VTEX IO Pixel app."
tags:
  - performance
  - analytics
  - ga4
---

**Keywords:** GA4 | performance | analytics

After configuring [Google Analytics 4 (GA4)](https://developers.vtex.com/docs/guides/google-tag-manager), your store may experience issues with inconsistent data tracking.

Due to General Data Protection Regulation (GDPR) restrictions, some companies are updating their operating systems, browsers, and devices to block events triggered during shopper navigation, which is the main reason behind this problem.

## Solution

To solve this problem, follow the instructions below.

### Step 1 - Setting up server-side tagging

Server-side tagging shifts tag processing from the client side to the server environment. This enhances website performance by reducing client-side code, improves data security by managing sensitive information on the server, and provides greater control over data collection.

Acting as an intermediary between users and data vendors, server-side tagging enables faster page loads, stronger security policies, better privacy, and more durable cookies, all while using familiar Google Tag Manager tools.

To configure server-side tagging, follow Google's [Server-Side Tag Manager](https://developers.google.com/tag-platform/tag-manager/server-side) documentation.

### Step 2 - Creating a VTEX IO Pixel app

Follow the instructions in the [Pixel apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps) guide to develop your own Pixel app.

After creating the Pixel app, add the Google Tag Manager (GTM) script passing the correct container code and the server URL (which holds the server-side tag manager configuration) that will trigger the events for Google.

### Step 3 - Setting up the native GTM app

Keep the native [GTM app](https://developers.vtex.com/docs/guides/google-tag-manager) installed in your store, but pass a **fake container code** to the app.

To access the GTM app settings, go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@3.5.4/setup/`, replacing `{accountName}` with your VTEX account name. In the `Enter the ID (GTM-XXXX) from your Google Tag Manager` field, add the fake container code.

![gtm-fake-container](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/store-performance/gtm-fake-container.png)

### Step 4 - Setting up the store checkout

Remove the container code from the store checkout configuration.

Go to `https://{accountName}.myvtex.com/admin/portal/#/sites/default/checkout/`, replacing `{accountName}` with your VTEX account name, to access your store checkout configuration.

![checkout-settings-gtm](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/store-performance/checkout-settings-gtm.png)

Insert the GTM script with the correct container and the server URL into the JavaScript tab within the [Checkout UI Custom app](https://developers.vtex.com/docs/apps/vtex.checkout-ui-custom) and click `Publish` to track the events triggered on the store checkout pages.

![checkout-custom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/store-performance/checkout-custom.png)

The expected behavior is that your store's analytics data should be consistent and reflect user interactions.

After following these steps, if the error continues, open a [support ticket](https://help.vtex.com/support).

## Learn more

- [Configuring Google Tag Manager](https://help.vtex.com/tutorial/integration-with-google-tag-manager--frequentlyAskedQuestions_616)
- [How to customize the Checkout UI Custom in the Admin](https://help.vtex.com/tutorial/how-to-customize-the-checkout-ui-custom-in-the-admin--548aDBJciQu97Vh0BhEiWx)
