---
title: "Receiving Order Notifications"
slug: "how-to-receive-order-notifications-on-vtex-io"
hidden: false
createdAt: "2020-10-08T02:06:13.811Z"
updatedAt: "2021-03-25T14:45:50.605Z"
excerpt: Learn how to receive real-time order status notifications
---

This guide explains how to receive real-time order status notifications from VTEX using the `vtex.orders-broadcast` app and a sample listener application. By following these steps, you’ll be able to set up a workspace, configure the broadcast app, and start receiving notifications when orders are placed in your store.

## Before you begin

- A VTEX IO account with [workspace permissions](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace).
- [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed.
- Basic familiarity with linking apps on VTEX IO.

## Instructions

1. Choose a workspace on your account that you'll work on. Let's suppose we're using the workspace `oms`.
2. Clone the [Orders Feed Example](https://github.com/vtex-apps/orders-feed-example) repository to your local environment:
      ```bash
      git clone https://github.com/vtex-apps/orders-feed-example
      ```
3. In your browser, open the Orders Broadcast configuration page: `https://{accountName}.myvtex.com/admin/apps/vtex.orders-broadcast/setup`
4. Change the `Target Workspace` variable to the name of the workspace you have created previously.
5. Now you can link the `vtex.orders-feed-example` app in your desired workspace and receive order status updates.
6. Now, if you finish an order on the account's Store, you'll see the notifications pop up on the console. You can start your development by extracting the listener code from the cloned app and adding it to your application.

> For more information about customizing the listener, check the [example app's README](https://github.com/vtex-apps/orders-feed-example/blob/master/docs/README.md)

Example running on account `cliqueretire` and workspace `lucis`:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-receive-order-notifications-on-vtex-io-0.png)
