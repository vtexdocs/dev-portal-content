---
title: "Curbside Pickup"
slug: "vtex-curbside-pickup"
excerpt: "vtex.curbside-pickup@0.3.8"
hidden: false
createdAt: "2020-07-07T13:45:04.134Z"
updatedAt: "2022-05-31T16:20:48.774Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Curbside Pickup app allows shoppers and store staff to coordinate curbside pickup orders through email notifications.

![curbside](https://user-images.githubusercontent.com/52087100/94301877-b43bda80-ff41-11ea-9bc8-e28cc61b9246.png)

## Configuration

### Step 1 - Installing the Curbside Pickup app

Using your terminal and [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/#command-reference), log in to the VTEX account you are working on and [install](https://vtex.io/docs/recipes/store/installing-an-app) the `vtex.curbside-pickup@0.x` app.

### Step 2 - Defining the app settings 

In your VTEX account's admin, perform the following actions:

1. Access the **Apps** section and then **My Apps**. 
2. Select the **Curbside Pickup** app box.
3. Enter your [app key and token](https://developers.vtex.com/docs/getting-started-authentication#creating-the-appkey-and-apptoken) in the `App Key` and `App Token` fields.

![curbside-pickup-admin](https://user-images.githubusercontent.com/52087100/94301599-37a8fc00-ff41-11ea-8f25-33ecee833d43.png)

4. Access **Inventory & shipping** and then **Pickup points**. 
5. For each of your pickup point store locations, enter the store's email address in the **Address Line 2** field. The Curbside Pickup app will use this email to send the store pickup notifications.

> ℹ️ If the `Address Line 2` field is not available for you, use the `complement` field instead.

6. Access the new admin's **Curbside Pickup** section, immediately below Inventory & shipping.
7. In the box titled `Almost There`, click on the **PROCEED** button. This will initialize the order notification hook needed by the app and will create the following email templates:

- `curbside-ready-for-packing` - Sent to the store's email address (the one from step 5) when a curbside order is ready for handling.
- `curbside-package-ready` - Sent to the shopper when the order is ready to be picked up.
- `curbside-at-location` - Sent to the store's email address when the shopper has arrived at the pickup location.

Once the email templates are created, you may customize them as you see fit. Follow the links to the templates from the Curbside Pickup page, or navigate to `Message center > Templates` from your admin dashboard sidebar.
  
## Modus Operandi

When a pickup order has reached the `Ready For Handling` state, the Curbside Pickup adds a comment to the order timeline stating that the curbside pickup process has begun and sends an email to the staff of the physical store where the order will be picked up. 

This email contains a link that the store staff can click on when the order is packed and ready to be picked up.

Clicking on the link will add another comment to the order timeline and trigger a second email to be sent to the shopper, notifying them that their order is ready to be picked up. 

This email also contains a link that the shopper can click on once they have arrived at the store.

Clicking on the link will add a comment to the order timeline and trigger a third email to be sent to the store staff informing them that the shopper has arrived and they should bring the order out to their car. 

This email, in turn, contains a link that the store staff should click after having handed the order to the shopper.

When the store staff clicks on the link stating that the order has been handed off, the order timeline will be updated with a comment to that effect, completing the curbside pickup process and allowing the order to be invoiced as usual.

## Customization

No CSS Handles are available yet for the app customization.

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!