---
title: "Google Tag Manager (Beta)"
slug: "vtex-io-documentation-setting-up-google-tag-manager-beta"
hidden: true
createdAt: "2023-04-18T16:41:44.272Z"
updatedAt: "2023-04-18T16:41:44.813Z"
category: "Storefront Development"
excerpt: "Step-by-step to install and configure the Google Tag Manager app (Beta)"
seeAlso:
 - "/docs/guides/google-tag-manager"
 - "/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app"
 - "/docs/guides/vtex-io-documentation-setting-up-google-analytics-search-tracking"
---
> ⚠️ The new version of the VTEX Google Tag Manager is currently in beta. If you agree to use this version, please report any issues you find in the [Issue section on GitHub](https://github.com/vtex-apps/google-tag-manager/issues).

## Before you start

Create a Google Analytics 4 (GA4) property using the GA4 Setup Assistant. This property collects data in parallel with your existing Universal Analytics property. To create the GA4 property. Follow [Google’s official guide](https://support.google.com/analytics/answer/9744165#zippy=%2Cin-this-article).

> ⚠️ Take note of the *Measurement ID*, also known as [*G- ID*](https://support.google.com/analytics/answer/9539598#find-G-ID), as it will be used later to set up the Google Analytics 4 tag in Google Tag Manager.

## Installing Google Tag Manager (Beta)

1. Open the VTEX CLI and enter your store’s account:

```bash
```bash
    vtex login {account-name}
```

> ⚠️ Replace `{account-name}` with your store's account name, for example, `vtex login storecomponents`.

1. Create a new development workspace for testing purposes.



 vtex use {workspace-name}
```

1. Install the Google Tag Manager app by running the following command:


1. Install the Google Tag Manager app by running the following command:
    vtex install vtex.google-tag-manager@3.3.2.beta
```

Once the installation is complete, you should see a successful message.
Once the installation finished you should see a successful message.
Once the installation is complete, you should see a successful message.

### Enabling the GA4 setting in the GTM app


### Enabling the GA4 setting in the GTM app

2. Check the box **Send Google Analytics 4 Events** and click on `Save`.

![gtm-app-one](https://user-images.githubusercontent.com/67270558/232889771-bdb8c814-4d89-42a3-b48d-4d3cae29f57c.png)

## Configuring Google Analytics 4 Configuration tag in Google Tag Manager


## Configuring Google Analytics 4 Configuration tag in Google Tag Manager

To ensure data flows from your store to Google Analytics, create a Google Analytics 4 configuration tag using Measumerent ID in [Google Tag Manager](https://tagmanager.google.com/). To create the tag see the following article [Set up the Google Analytics 4 Configuration tag](https://support.google.com/tagmanager/answer/9442095).

Once the Google Analytics 4 Configuration tag is created, set up each GA4 event as follows:

1. Download the [container file](https://gist.githubusercontent.com/filipewl/6fab5e75ae938487fe780b1ce213970f/raw/e9bf3db528bca7a07851512e378e53ac7d8ba08d/gtm-ga4-container-template.json). This container adds all the necessary tags, triggers, and variables.

2. Import the container file by following Google’s [Import a container guide](https://support.google.com/tagmanager/answer/6106997?#import). It will add all the necessary tags, triggers, and variables.

![import-container](https://user-images.githubusercontent.com/67270558/232900478-36277198-bc4a-40f2-a7e3-f54b73270fe9.png)

3. In the GTM app, in the GA4 Configuration tag, edit the **Measurement ID** field.

> ℹ️ Your measurement ID usually starts with `G-`. To find your Google tag ID, refer to [Find your Google tag ID article](https://support.google.com/analytics/answer/9539598?sjid=16676572490197811169-SA#find-G-ID)

### Testing Tags in Google Tag Manager

To test that the Google Analytics: GA4 Configuration tag is firing correctly for every page, use the [Preview mode](https://support.google.com/tagmanager/answer/6107056) in Google Tag Manager (GTM). Additionally, verify that the Google Analytics: GA4 Event tags are firing accurately for user actions such as viewing a product or adding a product to the cart.

### Testing Events sent to Google Analytics 4

To verify if the events are arriving and the reports are being filled with data, access the Google Analytics Admin and use the [DebugView](https://support.google.com/analytics/answer/7201382) to verify if the events are arriving and the [Reports](https://support.google.com/analytics/answer/9212670) are being filled with data.

![DebugView](https://user-images.githubusercontent.com/67270558/232895238-979567b3-38a8-491b-92f8-7c84691d7ccc.png)

## Overview Events

### View Promotion

The [GA4 view_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#view_promotion) expects to receive the product’s name or ID associated with it.

This event is commonly attached to promotion banners carousel displayed by the Slider Layout block, for example, and you can use the Site Editor to configure the `Product ID` and `Product Name`.

### Supported Events

Check out the available events that [Pixel Apps](https://developers.vtex.com/docs/guides/pixel-apps) can listen to and their equivalent names in UA and GA4:

| VTEX | UA | GA4 |
| ---- | -- | --- |
| vtex:promoView | [promoView](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-impressions) | [view_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_promotion) |
| vtex:promotionClick | [promoClick](https://developers.google.com/tag-manager/enhanced-ecommerce#promo-clicks) | [select_promotion](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#select_promotion) |
| vtex:productView | [detail](https://developers.google.com/tag-manager/enhanced-ecommerce#details) | [view_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_item) |
| vtex:productImpression | [impressions](https://developers.google.com/tag-manager/enhanced-ecommerce#product-impressions) | [view_item_list](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#view_item_list) |
| vtex:productClick| [click](https://developers.google.com/tag-manager/enhanced-ecommerce#product-clicks) | [select_item](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#select_item) |
| vtex:addToCart | [add](https://developers.google.com/tag-manager/enhanced-ecommerce#add) | [add_to_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#add_to_cart) |
| vtex:removeFromCart | [remove](https://developers.google.com/tag-manager/enhanced-ecommerce#remove) | [remove_from_cart](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#remove_from_cart) |
| vtex:cartLoaded | [checkout](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce#checkout) | [begin_checkout](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm#begin_checkout) |
| vtex:orderPlaced | [purchase](https://developers.google.com/tag-manager/enhanced-ecommerce#purchases) | [purchase](https://developers.google.com/analytics/devguides/collection/ga4/reference/events#purchase) |

### New Events

Other than the events listed above, GA4 has new events that stores can start tracking. The full list can be found [here](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm).

The GTM app listens to the following events and send them in the GA4 format:

| VTEX | GA4 |
| ---- | --- |
| vtex:addPaymentInfo| add_payment_info |
| vtex:addShippingInfo | add_shipping_info |
| vtex:login| login |
| vtex:signUp| sign_up |
| vtex:viewCart | view_cart |
| vtex:beginCheckout | begin_checkout |
| vtex:refund | refund |
| vtex:addToWishlist | add_to_wishlist |
| vtex:search | search |
| vtex:share | share |