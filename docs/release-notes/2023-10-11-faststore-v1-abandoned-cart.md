---
title: "FastStore v1: Fixed abandoned cart tracking"
slug: "2023-10-11-faststore-v1-abandoned-cart"
type: "fixed"
excerpt: "Introducing a solution for precise abandoned cart tracking and analytics data on FastStorev1"
createdAt: "2023-10-11T00:00:00.000Z"
---

We have implemented a solution to ensure correct tracking and monitoring of abandoned carts and analytics data for stores currently on [FastStorev1](https://v1.faststore.dev/docs). Stores using this version of FastStore must update their project code with the new `VTEX_METADATA` object.

> ⚠️ This change only affects stores using [FastStore v1](https://v1.faststore.dev/docs).

## What has changed?

Before, stores faced issues with tracking abandoned carts, as they were receiving a `null` value. This resulted in an inability to track whether customers completed their purchases or not when they added items to their carts. As a result, sending cart reminders or notifications was a challenge.

Now, by implementing the `VTEX_METADATA` object, you can set the correct account information, ensuring proper tracking of abandoned carts and analytics data for Return Customer (RC) and Activity Flow (AF) analytics trackers from VTEX.

## What needs to be done?

Stores using [FastStore v1](https://v1.faststore.dev/docs) must define the `VTEX_METADATA` object to ensure the correct behavior. To do so, open your FastStore project code and follow the steps below:

1. In the `src/sdk/analytics/index.tsx` file, add the highlighted code:

    ```tsx
    if (typeof window !== 'undefined') {
        window.dataLayer = window.dataLayer ?? []
        window.VTEX_METADATA = {
            account: storeConfig.api.storeId,
            renderer: 'faststore',
        }
    }
    ```

2. In the `src/typings/global.d.ts` file, add the highlighted code:

    ```ts
    declare module '*.scss';
    declare module '*.png';

    interface Window extends Window {
        dataLayer: any[];
        VTEX_METADATA: {
            account: string,
            renderer: "faststore"
        };
        sendrc: (eventName: string, eventValues?: any) => void
    }
    ```

3. In the terminal, run `yarn dev` to sync the changes.

After syncing the changes, you can test the solution by checking the information in the following topics:

- **Check if `VTEX_METADATA` has been defined:**

  1. Access the provided localhost URL in your browser.
  2. Open the Dev Tools terminal, go to the **Console** tab, and check if the `window.VTEX_METADATA` is defined in the console, as illustrated in the image below.

  ![console-object](https://vtexhelp.vtexassets.com/assets/docs/src/console-vtex-metadata___f1d9f78c17949decc87f22266ac3285d.gif)

- **Check if the data captured by Return Customer (RC) is updating the records in Master Data:**

   Refer to the topic [Is the data captured by RC updating the records in Master Data?](https://help.vtex.com/en/tutorial/setting-up-abandoned-carts--tutorials_740#is-the-data-captured-by-rc-updating-the-records-in-master-data).
