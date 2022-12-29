---
title: "Delivery Window Blocker"
slug: "delivery-window-blocker-app"
excerpt: "vtex.delivery-window-blocker@2.2.1"
hidden: false
createdAt: "2022-07-13T18:41:39.206Z"
updatedAt: "2022-07-13T18:41:39.206Z"
---
A delivery window is a time frame during which packages are sent to customers, configured within a [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140). The **Delivery Window Blocker** app provides an interface on VTEX Admin for you to manually block or unblock scheduled delivery windows, and set up weekly recurrent blocking. The app is available for all VTEX stores.

> ⚠️ The **Delivery Window Blocker** app is compatible with the native solution, which is the [Delivery capacity](https://help.vtex.com/en/tutorial/managing-delivery-capacity--2y217FQZCjD0I1n62yxVcz) configurations in the [Scheduled delivery](https://help.vtex.com/en/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) feature. Note that actions performed by the app will override delivery capacity settings.

For example, a delivery window blocked by the app will not be automatically unblocked by configurations made in the delivery capacity feature. It will be necessary to unblock the delivery window through the app.

## Installation

You can install the **Delivery Window Blocker** app using [VTEX App Store](https://apps.vtex.com/vtex-delivery-window-blocker/p) or [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). Once installed, the app settings will appear in your VTEX Admin, under **Orders > Inventory & shipping**. 

> If using the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), you will find them under **Apps > Installed Apps**.

### VTEX App Store

Once you are logged in your VTEX App Store’s account, follow these steps:

1. In the VTEX App Store, go to the app page [Delivery Window Blocker](https://apps.vtex.com/vtex-delivery-window-blocker/p).
2. Click on `GET APP`.
3. In your cart in the VTEX App Store, click on `PLACE ORDER`.
4. Click on `GO TO INSTALL PAGE`.
5. In the VTEX Admin, click on `INSTALL`.

### VTEX IO CLI

Using your terminal and [VTEX IO CLI](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/#command-reference), log in to the account you are working on and [install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.delivery-window-blocker` app.

## How it works

The **Delivery Window Blocker** app enables you to perform the following actions:

- [Block a delivery window on demand](#block-a-delivery-window-on-demand)
- [Set up a recurrent blocking time](#set-up-a-recurrent-blocking-time)
- [Unblock a delivery window on demand](#unblock-a-delivery-window-on-demand)

> ℹ️ Through the Delivery **Window Blocker** app you can access a [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) and edit delivery window’s configurations. This can be done by selecting a shipping policy and clicking on <i class="fas fa-pencil-alt"></i> **EDIT SHIPPING POLICY**.

![block_delivery_window_1](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/delivery-window-blocker-app-0.png)

### Block a delivery window on demand

Blocking a delivery window means it will not be displayed for the customer at checkout. To block a window, do the following:

1. In your VTEX Admin, go to **Orders > Inventory & shipping > Delivery window blocker**.

    For the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), go to **Apps > Installed Apps > Delivery window blocker**.
    
2. Open the **Block on demand** tab.
3. Click on `Shipping policy: Name` <i class="fas fa-angle-down"></i> and select the desired [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140).
4. Click on `APPLY`.
5. Click on `Date: MM/DD/YYYY` <i class="fas fa-angle-down"></i> and select the start and end date to block the delivery window.
6. Click on `APPLY`.
7. In the row with the given delivery window, in the **Actions** column, click on the menu icon <i class="fas fa-ellipsis-v"></i>.
8. Select the `Block window` option.
9. Click on `BLOCK`.

![block_delivery_window_2](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/delivery-window-blocker-app-1.png)

### Set up a recurrent blocking time

To block a delivery window on a weekly basis, do the following:

1. In your VTEX Admin, go to **Orders > Inventory & shipping > Delivery window blocker**.

    For the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), go to **Apps > Installed Apps > Delivery window blocker**.

2. Open the **Recurrent blocking** tab. 
3. Click on `Shipping policy: Name` <i class="fas fa-angle-down"></i> and select the desired shipping policy.
4. Click on `APPLY`.
5. Click on `+SET RECURRENT BLOCKING`.
6. In the modal, fill in the day and hour during which the delivery window will be blocked.
7. Click on `CONFIRM`. 

![block_delivery_window_3](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/delivery-window-blocker-app-2.gif)
 
### Unblock a delivery window on demand

Unblocking a delivery window means it will be displayed for customers on checkout. If you wish to unblock a window, follow these steps:

1. In your VTEX Admin, go to **Orders > Inventory & shipping > Delivery window blocker**.

    For the [New VTEX Admin](https://content.vtex.com/join-new-admin-beta-program-en/), go to **Apps > Installed Apps > Delivery window blocker**.

2. Open the **Block on demand** tab. 
3. Click on `Shipping policy: Name` <i class="fas fa-angle-down"></i> and select the desired shipping policy.
4. Click on `APPLY`.
5. In the row with the given delivery window, in the **Actions** column, click on the menu icon <i class="fas fa-ellipsis-v"></i>.
6. Select the `Unblock window` option.
7. Click on `UNBLOCK`.

Unblocking delivery windows that were set up as recurrent blocking times works in a similar way. The difference is that on step 1 you will select the **Recurrent blocking** tab, and on step 4 you will select `Remove recurrent blocking`.

![block_delivery_window_4](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/delivery-window-blocker-app-3.png)