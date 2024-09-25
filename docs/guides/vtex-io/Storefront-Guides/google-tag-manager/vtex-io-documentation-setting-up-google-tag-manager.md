---
title: "Setting up Google Tag Manager"
slug: "vtex-io-documentation-setting-up-google-tag-manager"
hidden: false
createdAt: "2020-06-03T16:02:44.272Z"
updatedAt: "2022-12-13T20:17:44.813Z"
category: "Storefront development"
excerpt: "Steps on how to track and analyze data from your store using Google Analytics 4"
seeAlso:
  - "/docs/guides/google-tag-manager"
  - "/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app"
  - "/docs/apps/vtex.search#app-behavior-improving-search-experience"
---

Once you have installed the [VTEX IO Google Tag Manager app](https://developers.vtex.com/docs/guides/google-tag-manager), set it up in your store by configuring all the necessary variables, triggers, and tags.

In this guide, you will learn how to track and analyze data from your store using Google Analytics 4. Specifically, you will:

- Set up GA4 events by downloading and importing a container file, adding necessary tags, triggers, and variables, and editing the Measurement ID field with your Google tag ID.

- Test that the GA4 Configuration tag is firing correctly on every page and ensure that the GA4 Event tags accurately track user actions such as viewing a product or adding a product to the cart.

- Verify that the events are arriving and the reports are being filled with data by accessing the Google Analytics' DebugView  and Reports.

- Use the available events that Pixel Apps can listen to and new events that GA4 has introduced to start tracking various user actions such as product impressions, add to cart, order placed, and more.

## Before you begin

Before proceeding any further, make sure you have the following requisites:

1. Installed and configured the VTEX Google Tag Manager app. For more information, refer to [Installing Google Tag Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-google-tag-manager).

2. Created A Google Analytics 4 (GA4) Configuration tag using your Measumerent ID in [Google Tag Manager (GTM)](https://tagmanager.google.com/). For more information, refer to the following Google article [Set up the Google Analytics 4 Configuration tag](https://support.google.com/tagmanager/answer/9442095).

## Instructions

### Step 1 - Setting up GA4 events

Once the GA4 Configuration tag is created, set up all GA4 events as follows:

1. Download the <a href="https://developers.vtex.com/container-template.json" download>container file</a>. This container adds all the necessary tags, triggers, and variables.

2. Import the container file by following Google’s [Import a container guide](https://support.google.com/tagmanager/answer/6106997?#import). This will add all the necessary tags, triggers, and variables to the workspace.

    ![import-container](https://vtexhelp.vtexassets.com/assets/docs/src/new-ga4-tags-variables___b2619df57689429d97a8abd56a5f7d83.png)

3. In the GTM container, go to the GA4 Configuration tag, and edit the **Measurement ID** field with your Google Tag ID ( G- ID).

> ℹ️ To find your Google Tag ID, refer to [Find your Google tag ID article](https://support.google.com/analytics/answer/9539598?sjid=16676572490197811169-SA#find-G-ID)

### Step 2 - Testing Tags in Google Tag Manager

To test that the GA4 Configuration tag is firing correctly for every page, use the [Preview mode](https://support.google.com/tagmanager/answer/6107056) in Google Tag Manager (GTM). Additionally, verify if the GA4 Event tags are firing accurately for user actions such as viewing a product or adding a product to the cart.

### Step 3 - Testing Events sent to Google Analytics 4

To verify if the events are arriving and the reports are being filled with data, access the Google Analytics Admin and use the [DebugView](https://support.google.com/analytics/answer/7201382) to verify if the events are arriving and the [Reports](https://support.google.com/analytics/answer/9212670) are being filled with data.

![gtm-debug-view](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-debug-view___e2dc572dcc33e2e23e81749583226ec8.png)

To see the available events that GA4 can track, refer to the [Overview of Events in Google Analytics 4](#overview-events) section.

## Overview events

This section provides a list of events that GA4 can track.This section also explains the `view_promotion` event, which is usually attached to the promotion banners carousel displayed by the Slider Layout block.

### View Promotion

The [GA4 view_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_promotion) expects to receive the product’s name or ID associated with it.

This event is commonly attached to the promotion banners carousel displayed by the Slider Layout block. For example, you can use the Site Editor to configure the `Product ID` and `Product Name`. To access the Site Editor, in the VTEX Admin, go to **Storefront > Site Editor**.

![gtm-site-editor-fields](https://vtexhelp.vtexassets.com/assets/docs/src/gtm-site-editor___bc52365aafad63deb5bfed1d74f307c0.png)

### Supported events

Check out the available events that [Pixel Apps](https://developers.vtex.com/docs/guides/pixel-apps) can listen to and their equivalent names in UA and GA4:

| VTEX                   | UA                                                                                              | GA4                                                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| vtex:promoView         | [promoView](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-impressions)     | [view_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_promotion)       |
| vtex:promotionClick    | [promoClick](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-clicks)         | [select_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#select_promotion)   |
| vtex:productImpression | [impressions](https://developers.google.com/tag-manager/enhanced-ecommerce#product-impressions) | [view_item_list](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_item_list)       |
| vtex:productClick      | [click](https://developers.google.com/tag-manager/enhanced-ecommerce#product-clicks)            | [select_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#select_item)             |
| vtex:productView       | [detail](https://developers.google.com/tag-manager/enhanced-ecommerce#details)                  | [view_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_item)                 |
| vtex:addToCart         | [add](https://developers.google.com/tag-manager/enhanced-ecommerce#add)                         | [add_to_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#add_to_cart)             |
| vtex:removeFromCart    | [remove](https://developers.google.com/tag-manager/enhanced-ecommerce#remove)                   | [remove_from_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#remove_from_cart)   |
| vtex:viewCart          | Not applicable                                                                                  | [view_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_cart)                 |
| vtex:beginCheckout     | checkout                                                                                        | [begin_checkout](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#refund)               |
| vtex:addShippingInfo   | Not applicable                                                                                  | [add_shipping_info](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#add_shipping_info) |
| vtex:addPaymentInfo    | Not applicable                                                                                  | [add_payment_info](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#add_payment_info)   |
| vtex:orderPlaced       | [purchase](https://developers.google.com/tag-manager/enhanced-ecommerce#purchases)              | [purchase](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#purchase)                   |
| vtex:refund            | Not applicable                                                                                  | [refund](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#refund)                       |
| vtex:search            | Not applicable                                                                                  | [search](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#search)                       |
| vtex:share             | Not applicable                                                                                  | [share](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#share)                         |
| vtex:addToWishlist     | Not applicable                                                                                  | [add_to_wishlist](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#add_to_wishlist)     |

### Partially-supported events

The following events are not fully supported yet. Although the GTM app will listen and format them into GA4, their VTEX event triggers have not been implemented yet:

| VTEX        | GA4                                                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------------------|
| vtex:login  | [login](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#login)     |
| vtex:signUp | [sign_up](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#sign_up) |
