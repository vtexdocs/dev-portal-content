---
title: "Google Tag Manager"
slug: "plwhirlpool-gtm-whirlpool"
excerpt: "plwhirlpool.gtm-whirlpool@0.1.75"
hidden: true
createdAt: "2022-07-11T09:46:40.092Z"
updatedAt: "2022-08-09T10:17:09.071Z"
---
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

The VTEX Google Tag Manager app is a first party integration to the [Google Tag Manager solution](https://tagmanager.google.com).

![google-tag-manager-app](https://user-images.githubusercontent.com/52087100/84321347-55e11c80-ab49-11ea-9445-24eec6a07785.png)

## Configuration

It is possible to install the VTEX native GTM app in your store either by using App Store or the VTEX IO Toolbelt.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the Google Tag Manager box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **GTM ID** in the `Google Tag Manager` field.
4. Click on **Save**.

:information_source: Access the [Google Tag Manager page](https://tagmanager.google.com/)</a> and login to you account in order to find out what is your account **GTM ID**. The number your should use is the one provided by the `Container ID` column.

### Using VTEX IO Toolbelt

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.google-tag-manager@2.x` app. You can confirm that the app has now been installed by running `vtex ls` again.
2. Access the **Apps** section in your account's admin page and look for the Google Tag Manager box. Once you find it, click on the box.
3. Fill in the `Google Tag Manager` field with your **GTM ID**.
4. Click on **Save**.

:information_source: Access the [Google Tag Manager page](https://tagmanager.google.com/)</a> and login to you account in order to find out what is your account **GTM ID**. The number your should use is the one provided by the `Container ID` column.

After installing the app, you are ready to use your GTM as usual by accessing your account dashboard directly on the [Google Tag Manager](https://tagmanager.google.com/) page.

## Restrictions

In order to avoid performance problems and unforeseen behavior, our VTEX IO Google Tag Manager solution uses the native GTM **blacklist** feature. You can read more about this feature on the [Google Developer Guide](https://developers.google.com/tag-manager/web/restrict).

We, by default, blacklist the `html` ID, which automatically blocklists all the tags, variables and triggers of the type `customScripts`. The main consequence of this blocklist is that **Custom HTML tags will not be triggered**.

:warning: The HTML blacklist is VTEX Google Tag Manager app's default. If you want to disable this restriction go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@2.x/setup` and check the toggle below.

<img src="https://user-images.githubusercontent.com/11340665/103930428-7c762e80-50fd-11eb-9cab-bc9e542b4dbf.png">

Most of the widely used Custom HTML tags are integrations with third-party services, like Customer Chat, Analytics, Remarketing, and Pixel tags. If your store needs a Custom HTML for one of those cases, the integration can either be done by transforming the tags into a [VTEX IO Pixel App](https://vtex.io/docs/apps/pixel/) or by removing this restriction.

Check out below the full list of tags and variables that are blocked, by default, in VTEX IO Google Tag Manager solution below:

### Blocked tags

- Custom HTML Tag - `html`
- Eulerian Analytics Tag - `ela`
- SaleCycle JavaScript Tag  - `scjs`
- Upsellit Global Footer Tag - `uslt`
- Upsellit Confirmation Tag - `uspt`

### Blocked variables

- Custom JavaScript Variable - `jsm`

Check out a list with all the GTM available tags on the [Google Developer Guide](https://developers.google.com/tag-manager/devguide).

<!-- DOCS-IGNORE:start -->

## Contributors ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->