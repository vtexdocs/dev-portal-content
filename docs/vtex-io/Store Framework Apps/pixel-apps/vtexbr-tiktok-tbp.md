---
title: "TikTok for Business"
slug: "vtexbr-tiktok-tbp"
excerpt: "vtexbr.tiktok-tbp@1.2.0"
hidden: false
createdAt: "2022-04-14T23:35:51.398Z"
updatedAt: "2022-05-19T20:07:12.467Z"
---
> �The integration with TikTok is available only for stores in *Brazil*.

The TikTok for Business app allows merchants to easily connect their stores to TikTok, using it as a channel to drive sales and market products sold in their ecommerce.

The app includes the following features:

* Connecting TikTok For Business and Ads Manager accounts with your VTEX account.
* Syncing products in your catalog with TikTok.
* Inserting the [TikTok Pixel](#tiktok-pixel) in your store.
* Managing TikTok Ads from the VTEX Admin.


## Before you start

Before installing the app, make sure you have read about its compatibility and requirements in the following sections.


### Compatibility

TikTok for Business is fully compatible with stores using [VTEX IO](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/4yB9wSl79cArd68aRBnBZ2) and partially compatible with stores using [Legacy CMS](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj) or [Headless CMS](https://faststore.dev/tutorials/cms/0#vtex-headless-cms).

In VTEX IO stores, installing and configuring TikTok for Business causes the TikTok Pixel to be inserted automatically. On the other hand, stores using the Legacy CMS or Headless CMS need to configure the TikTok Pixel manually. Refer to the [Manual TikTok Pixel configuration](#manual-tiktok-pixel-configuration) section for more information on this.


### Requirements

To be able to configure the TikTok for Business app in your VTEX store, you need to meet the following requirements:

* Having a [TikTok Business account](https://ads.tiktok.com/help/article?aid=13288).
* Having [Admin permission](https://ads.tiktok.com/help/article?aid=238947046829056266&lang=en) in TikTok Business Center.
* Having a [TikTok Ads Manager account](https://ads.tiktok.com/help/article?aid=9678) linked to your business account.


## Installation

You can install TikTok for Business on the [VTEX App Store](https://apps.vtex.com/).

After installation, the app settings will be available in the VTEX Admin, under **Marketplace > TikTok**. For some versions of the VTEX Admin, the page can be found at **Apps > My Apps > TikTok**.


## Configuration

You must configure the TikTok for Business app through the VTEX Admin. Please check out the documentation about the [Integration with TikTok](https://help.vtex.com/en/tracks/tiktok-integration--1r0yJSO11nrer1YVu3WTFd/7Dwfwu1aHMp1aR1yvej5nv) for instructions on this process.

In case you are using the Legacy CMS or Headless CMS, you need to configure the TikTok Pixel manually as well. Read the following sections for more information on this.


## TikTok Pixel

The TikTok Pixel is a JavaScript code snippet that you can include on your store's website, which allows you to track various actions of your websites visitors and share them with TikTok. These actions are called Pixel events  see the [Supported Pixel events](#supported-pixel-events) section to learn more.

In VTEX IO stores, the TikTok Pixel is automatically inserted when you install and configure TikTok for Business. In Legacy CMS or Headless CMS stores, you need to configure it manually. Refer to the [Manual TikTok Pixel configuration](#manual-tiktok-pixel-configuration) section for more information on this.

### Supported Pixel events

TikTok Pixel supports the following events:

| **Event** | **Description** |
|:---:|:---:|
| 'ViewContent' | When a visitor views any page in your store. |
| 'AddToCart' | When a visitor adds a product to the cart. |
| 'PlaceAnOrder' | When a visitor places an order. |

For more information on TikTok Pixel events, read TikToks documentation on [Standard Events and Parameters](https://ads.tiktok.com/help/article?aid=10028&lang=en).


### Manual TikTok Pixel configuration

> � This configuration applies only to [Legacy CMS](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj) and [Headless CMS](https://faststore.dev/tutorials/cms/0#vtex-headless-cms) stores. If your store is built with [VTEX IO](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/4yB9wSl79cArd68aRBnBZ2), skip this section.


To insert the TikTok Pixel manually, you must follow the instructions in the TikTok documentation, more specifically in [Option 2: Install the pixel using Developer Mode](https://ads.tiktok.com/help/article?aid=10000357#:~:text=to%20create%20events.%C2%A0-,Option%202%3A%20Install%20the%20pixel%20using%20Developer%20Mode%C2%A0,-Step%201%3A%20Install) of the [Get Started with Google Tag Manager](https://ads.tiktok.com/help/article?aid=10000357#:~:text=TikTok%20Pixel%20Partners.-,Get%20Started%20with%20Google%20Tag%20Manager,-There%20are%20two) guide.


## Disconnecting from TikTok

Merchants can disable the integration between their store and TikTok at any time, by following the instructions on [Disconnecting TikTok from your store](https://help.vtex.com/en/tracks/tiktok-integration--1r0yJSO11nrer1YVu3WTFd/24SfBYkRkKMaetgjLDKgaP#disconnecting-tiktok-from-your-store).

In case their TikTok user access token is revoked (deactivated or invalid), the integration will be disconnected automatically. The `access_token` is the token that bears the authorization of the TikTok user.

Once disconnected, your integration with TikTok stops completely: the TikTok Pixel and the integration with your store's catalog are deactivated. Therefore, you will no longer be able to send new products to TikTok and update products on the TikTok catalog automatically.

On the other hand, existing products are not deleted from the TikTok catalog by VTEX, which means they continue to appear on TikTok. For this to stop, you need to manually delete the products in [TikTok Catalog Manager](https://ads.tiktok.com/help/article?aid=10001005).

After disconnecting, it is possible to reactivate the integration at any time by repeating the steps described in [Configuring the integration with TikTok for Business in the VTEX Admin](https://help.vtex.com/en/tracks/tiktok-integration--1r0yJSO11nrer1YVu3WTFd/4AEUg7pEdX1beOaQhFf0wC).


**Upcoming documentation:**

 - [Feature/error toast](https://github.com/vtex-apps/tiktok-tbp/pull/88)