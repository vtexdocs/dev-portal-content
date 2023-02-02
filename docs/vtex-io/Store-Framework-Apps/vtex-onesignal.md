---
title: "OneSignal"
slug: "vtex-onesignal"
hidden: true
createdAt: "2020-06-03T15:19:50.043Z"
updatedAt: "2022-11-22T18:39:22.812Z"
---

OneSignal first party integration app. The [solution](https://onesignal.com/) provides web push notifications for customer engagement.

![notification](https://user-images.githubusercontent.com/284515/88438151-68a06f80-cdde-11ea-8624-2626d8464f5d.png)

## Configuration

It is possible to install the app in your store either by using the VTEX App Store or the VTEX IO Toolbelt.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the OneSignal box.
2. Click on the **Install** button.
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **App ID**.
4. Click on **Save**.

### Using VTEX IO CLI

1. [Install](/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.onesignal@1.x` app. You can confirm that the app has now been successfully installed by running the `vtex ls` command.
2. Access the **Apps** section in your account's admin page and look for the OneSignal box. Once you find it, click on the box.
4. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **App ID**.
5. Click on **Save**.

> ℹ️️ The App ID works as an account identifier and should be provided by the OneSignal solution.

> ⚠️ To successfully use this native integration in your store, you will need to [deactivate the native service worker provided by VTEX IO](/docs/guides/vtex-io-documentation-deactivating-the-vtex-io-native-service-worker).
