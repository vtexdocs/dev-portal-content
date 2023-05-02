---
title: "Configuring Google Analytics 4 Configuration tag in Google Tag Manager"
slug: "vtex-io-documentation-configuring-ga-in-gtm"
hidden: false
createdAt: "2022-02-01T13:34:01.638Z"
updatedAt: "2023-05-02T20:17:44.697Z"
excerpt: "In this guide, you will learn how to track and analyze data from your store using Google Analytics 4"
category: "Storefront Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-installing-google-tag-manager"
---

In this guide, you will learn how to track and analyze data from your store using Google Analytics 4. Specifically, you will:

- Set up GA4 events by downloading and importing a container file, adding necessary tags, triggers, and variables, and editing the Measurement ID field with your Google tag ID.


- Test that the GA4 Configuration tag is firing correctly on every page and ensure that the GA4 Event tags accurately track user actions such as viewing a product or adding a product to the cart.


- Verify that the events are arriving and the reports are being filled with data by accessing the Google Analytics' DebugView  and Reports.


- Use the available events that Pixel Apps can listen to and new events that GA4 has introduced to start tracking various user actions such as product impressions, add to cart, order placed, and more.

## Before you start
Before proceeding any further, make sure you have the following requisites:

1. Installed and configured the VTEX Google Tag Manager app. For more information, refer to [Installing Google Tag Manager](/docs/guides/vtex-io-documentation-installing-google-tag-manager).

2. Created A Google Analytics 4 (GA4) Configuration tag using your Measumerent ID in [Google Tag Manager (GTM)](https://tagmanager.google.com/). For more information, refer to the following Google article [Set up the Google Analytics 4 Configuration tag](https://support.google.com/tagmanager/answer/9442095).

## Step-by-step

### Step 1 - Setting up GA4 events

Once the GA4 Configuration tag is created, set up all GA4 events as follows:
1. Download the [container file](https://gist.githubusercontent.com/filipewl/6fab5e75ae938487fe780b1ce213970f/raw/e9bf3db528bca7a07851512e378e53ac7d8ba08d/gtm-ga4-container-template.json). This container adds all the necessary tags, triggers, and variables.

2. Import the container file by following Google’s [Import a container guide](https://support.google.com/tagmanager/answer/6106997?#import). This will add all the necessary tags, triggers, and variables to the workspace.

![import-container](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-import-container___755c64280e03b4df0105de7722099c65.png)

3. In the GTM container, go to the GA4 Configuration tag, and edit the **Measurement ID** field with your Google Tag ID ( G- ID).

> ℹ️ To find your Google Tag ID, refer to [Find your Google tag ID article](https://support.google.com/analytics/answer/9539598?sjid=16676572490197811169-SA#find-G-ID)

### Step 2 - Testing Tags in Google Tag Manager
To test that the GA4 Configuration tag is firing correctly for every page, use the [Preview mode](https://support.google.com/tagmanager/answer/6107056) in Google Tag Manager (GTM). Additionally, verify if the GA4 Event tags are firing accurately for user actions such as viewing a product or adding a product to the cart. 

### Step 3 - Testing Events sent to Google Analytics 4
To verify if the events are arriving and the reports are being filled with data, access the Google Analytics Admin and use the [DebugView](https://support.google.com/analytics/answer/7201382) to verify if the events are arriving and the [Reports](https://support.google.com/analytics/answer/9212670) are being filled with data.

![gtm-debug-view](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-debug-view___e2dc572dcc33e2e23e81749583226ec8.png)