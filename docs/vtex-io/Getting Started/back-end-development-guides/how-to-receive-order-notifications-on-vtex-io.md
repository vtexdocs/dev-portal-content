---
title: "Receiving Order Notifications"
slug: "how-to-receive-order-notifications-on-vtex-io"
hidden: false
createdAt: "2020-10-08T02:06:13.811Z"
updatedAt: "2021-03-25T14:45:50.605Z"
---
## Recipe

1. Choose a workspace on your account that you'll work on. Let's suppose we're using the workspace `oms`.
2. Clone this repository [https://github.com/vtex-apps/orders-feed-example](https://github.com/vtex-apps/orders-feed-example)
3. Go to `https://{accountName}.myvtex.com/admin/apps/vtex.orders-broadcast/setup`
4. Change the `Target Workspace` variable to the name of the workspace you have created previously.
5. Now you can link this app (`vtex.orders-feed-example`) in your desired workspace and receive order status updates.
6. Now, if you finish an order on the account's Store, you'll see the notifications pop up on the console. You can start your development extracting the listener code from the cloned app to your application.
7. If you want more details check out the [readme on the example app](https://github.com/vtex-apps/orders-feed-example/blob/master/docs/README.md)

*Example running on account cliqueretire and workspace lucis:*

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Getting%20Started/back-end-development-guides/ead1c53-events.png)