---
title: "B2B Quotes & Carts"
slug: "vtex-b2b-quotes"
excerpt: "vtex.b2b-quotes@1.5.2"
hidden: false
createdAt: "2021-10-19T20:10:51.309Z"
updatedAt: "2022-12-02T14:51:23.888Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

> ℹ The **B2B Quotes & Carts** app is part of VTEX’s [B2B Suite](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-suite) solution: a collection of apps that allow stores to manage organizations, storefront roles and permissions, and checkout settings for B2B commerce relationships. We recommend that you use it alongside the other apps in this suite for all functionalities to work as expected.

The B2B shopping experience frequently requires the possibility for customers to request quotes and negotiate prices with sales representatives.

The **B2B Quotes & Carts** app allows customers who are part of [B2B Organizations](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-organizations) to request a quote for a shopping cart and save it for future use – including its items, product quantities and prices. This enables price negotiations between them and the store’s sales representatives, as well as order approval flows within their organization.

## Before you start

First, make sure you have the [VTEX IO CLI (Command Line Interface)](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install) installed in your machine.

Note that installing **B2B Quotes & Carts** will also result in [Storefront Permissions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions) being installed as a dependency app – it allows you to grant specific storefront roles for B2B users in an organization. This is especially useful for organizations with multiple users who have different responsibilities, such as placing orders, approving orders or managing the organization users. See the [Storefront Permissions](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions) app documentation for information on the available roles and how to customize their permissions (optional).

If you want to be able to manage roles and permissions on the VTEX Admin, you must install [Storefront Permissions UI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions-ui) as well.

Along with this app, we recommend installing [B2B Checkout Settings](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-checkout-settings), which includes quotes-related functionalities to checkout. For example, it allows you to add a `Create a Quote` button to the checkout’s shopping cart page, as well as “lock” the checkout if a quote is in use, preventing the cart contents from being changed until the order is placed.

## Installation

You can install the **B2B Quotes & Carts** app by running `vtex install vtex.b2b-quotes` in your terminal, using the [VTEX IO CLI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## How the app works

The **B2B Quotes & Carts** app enables a shared [My Quotes](#my-quotes) page for members of a B2B organization, from where it is possible to create a quote or saved cart and view existing quotes and saved carts.

It is also possible to manage each quote or saved cart’s [details](#quote-details), including the possibility to edit them, request adjustments, approve or decline them or use them to place an order.

In addition, the app enables a set of [email templates](#email-templates) to notify members of the organization of quote status changes through Message Center.

The ability to use these resources depends on having the required [storefront permissions](#storefront-permissions), as explained in the next section.

| **Permission**                                | **Default roles**                                                                                                                        |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Create Quotes and Carts**                   | Store Admin<br></br>Sales Admin<br></br>Sales Manager<br></br>Sales Representative<br></br>Organization Admin<br></br>Organization Approver<br></br>Organization Buyer |
| **Access My Cost Center's Quotes and Carts**  | Sales Representative<br></br>Organization Approver<br></br>Organization Buyer                                                                      |
| **Access My Organization's Quotes and Carts** | Sales Manager<br></br>Organization Admin                                                                                                      |
| **Access All Quotes and Carts**               | Store Admin<br></br>Sales Admin                                                                                                               |
| **Place Orders from Quotes and Carts**        | Store Admin<br></br>Sales Admin<br></br>Sales Manager<br></br>Sales Representative<br></br>Organization Admin<br></br>Organization Approver                       |
| **Decline Quotes and Carts**                  | Store Admin<br></br>Sales Admin<br></br>Sales Manager<br></br>Sales Representative<br></br>Organization Admin<br></br>Organization Approver                       |
| **Edit My Cost Center's Quotes and Carts**    | Sales Representative                                                                                                                     |
| **Edit My Organization's Quotes and Carts**   | Sales Manager                                                                                                                            |
| **Edit All Quotes and Carts**                 | Store Admin<br></br>Sales Admin                                                                                                               |

If you want to be able to manage roles and permissions for **B2B Quotes & Carts** on the VTEX Admin, you must install [Storefront Permissions UI](https://developers.vtex.com/vtex-developer-docs/docs/vtex-storefront-permissions-ui) and refer to its documentation.

### My Quotes

The **B2B Quotes & Carts** app enables the **My Quotes** page, an interface to manage quotes and saved carts in the storefront, provided that the user is logged in and has the required storefront permissions.

To access **My Quotes**, customers or sales users must follow the instructions below.

1. Access the storefront and log in.
2. Click `Hello, {name}`.
3. Click on **My Account**.
4. Go to **Quotes and Saved Carts** on the sidebar. You will see the page below.

![my-quotes](https://user-images.githubusercontent.com/77292838/161637102-66a15213-e70d-421a-9e90-5a68ddc25825.png)

> ℹ Quotes and saved carts are shown together in the same table. The differences are the following:
> _ Only quotes can have a status of **Pending** or **Revised**.
> _ Sales users are not notified when saved carts are created. \* It is possible to edit a saved cart such that it becomes a quote, as explained in [Quote Details](#quote-details).

In this page, it is possible to use the following resources:

- **Search bar**: allows you to look up specific quotes or saved carts by name.
- **Filters**: allows you to filter the displayed quotes or saved carts by _Status_, _Organization \_or \_Cost Center._ The two last options are available under `More`.
- **New quote**: allows you to create a quote or saved cart by clicking on the `New Quote` button. See more details on this in the [Creating a quote or saved cart](#creating-a-quote-or-saved-cart) section.

The list of quotes and saved carts displays the following information:

- **Ref. Name:** the quote or saved cart’s reference name.
- **Subtotal:** subtotal of the shopping cart associated with the quote or saved cart.
- **Created by:** email of the user who created the quote or saved cart.
- **Created on:** date when the quote or saved cart was created, in the MM/DD/YYYY format.
- **Expiration:** date when the quote or saved cart will expire, in the MM/DD/YYYY format.
- **Status:** current state of the quote or saved cart, including the following options:
  - **Ready**: the quote or saved cart is ready to be used to place an order.
  - **Pending**: the quote is waiting for review and adjustment by a sales user.
  - **Revised**: the quote is waiting for additional review and adjustment by a sales user.
  - **Declined**: the quote or saved cart has been declined and cannot be used to place an order.
  - **Expired**: the quote or saved cart has reached its expiration date and cannot be used to place an order.
  - **Placed**: the quote or saved cart has been used to place an order and cannot be used again.
- **Last Update:** date when the quote or saved cart was updated for the last time, in the MM/DD/YYYY format.
- **Organization:** name of the organization the quote or saved cart is associated with.
- **Cost Center:** name of the cost center the quote or saved cart is associated with.

From the list, users may click on any row or click on <img src="https://user-images.githubusercontent.com/77292838/159766633-dfcb818f-6bd7-4cd0-92dc-9c682fb50d04.png" width="10" alt-text="00-ellipsis"/> **> Details** to view and edit the [details](#quote-details) of that quote or saved cart, according to what their permissions allow.

Depending on the current user’s [storefront permissions](#storefront-permissions), the **My Quotes** page will show a list of quotes and saved carts containing one of the following:

| **Permission**                                | **Content**                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------- |
| **Access My Cost Center's Quotes and Carts**  | All quotes and saved carts created by users in the current user’s cost center.  |
| **Access My Organization's Quotes and Carts** | All quotes and saved carts created by users in the current user’s organization. |
| **Access All Quotes and Carts**               | All quotes and saved carts in the current store, regardless of organization.    |

### Creating a quote or saved cart

In order to create a quote or saved cart, it is necessary to have the **Create Quotes and Carts** [permission](#storefront-permissions). After adding products to the cart in the storefront, users with these permissions can use the contents of their cart to create a saved cart or to request a quote. They should follow the instructions below.

1. Fill in the shopping cart with the desired products.
2. Take one of the following actions to create a quote or saved cart:

   - Clicking the `Create a Quote` button during checkout, provided that **B2B Checkout Settings** is installed and this button is enabled in the app’s [configuration](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-checkout-settings#configuration).
   - Navigating to the `/b2b-quotes/create` route.
   - Clicking the `+ New` button on the **My Quotes** page.

     Any of these paths will lead to the **Create Quote** page, illustrated below.

3. Fill in the quote or saved cart’s **Name**.
4. Make sure that all the information in the **Create Quote** page is correct:
   - **Original Subtotal:** subtotal of the shopping cart before any discounts.
   - **Percentage Discount:** percentage of the discount offered by a sales representative.
   - **Quoted Subtotal:** subtotal of the quote, including any discounts offered by sales representatives.
   - **Image:** image of the selected product.
   - **Ref. Code:** reference code of the selected product.
   - **Name:** name of the product.
   - **Original Price:** original price of the product.
   - **Quoted Price:** price of the product including any discounts offered by sales representatives.
   - **Quantity:** quantity of items.
   - **Total:** total value considering the quoted price and the quantity of items.
5. Write a note in the optional **Add Note** field, if necessary.

   Notes added here will be visible as part of the quote or saved cart’s [Update History](#quote-details) and can be seen by salespeople or other members of your organization and cost center. For example, if a user wishes to request a specific discount from the B2B store’s salesperson, they may include this request as a note.

6. Click on one of the following options:

   - `Save for later`: clicking on this button will result in the creation of a saved cart. The status of the newly created saved cart will be set as **Ready**, meaning that it can immediately be used to place an order by any user within that organization or cost center who has the **Place Orders from Quotes and Carts** [permission](#storefront-permissions).
   - `Request quote`: clicking on this button will result in the creation of a quote. The status of the newly created quote will be set as **Pending**, meaning that it will need to be reviewed and adjusted by a salesperson before any special discounts can be applied.

     Note that a **Pending** quote can still be used to place an order, as it is essentially a saved cart at this point, with the original item quantities and prices from the user’s shopping cart.

The items in the table, along with the quantities and prices shown, will be saved when the quote or saved cart is created.

![create-quote](https://user-images.githubusercontent.com/77292838/161637106-44d41347-2ee4-4191-bfe9-8dc7e67c783e.png)

### Quote Details

The **Quote Details** page displays all the information about a specific quote or saved cart, as well as the available actions, depending on its status and the user’s [storefront permissions](#storefront-permissions).

Users can access this page through the storefront by going to **My Account > Quotes and Saved Carts**.

![quote-details](https://user-images.githubusercontent.com/77292838/161637111-043851a7-9215-49eb-81d3-42f5a8b3936c.png)

This page displays the following information about a specific quote:

- **Name:** reference name of the quote or saved cart.
- **Original Subtotal:** subtotal of the shopping cart before any discounts.
- **Percentage Discount:** percentage of the discount offered by a sales representative.
- **Quoted Subtotal:** subtotal of the quote, including any discounts offered by sales representatives.
- **Expiration:** date when the quote or saved cart will expire, in the MM/DD/YYYY format.
- **Status:** current state of the quote or saved cart, as in [My Quotes](#my-quotes).
- **Image:** image of the selected product.
- **Ref. Code:** reference code of the selected product.
- **Name:** name of the product.
- **Original Price:** original price of the product.
- **Quoted Price:** price of the product including any discounts offered by sales representatives.
- **Quantity:** quantity of items.
- **Total:** total value considering the quoted price and the quantity of items.
- **Update History:** includes a history of all events related to the quote, such as its creation and discounts offered, including notes if there are any.
- **Add Note:** optional field to write comments or notes. Notes added here will be visible as part of the quote or saved cart’s [Update History](#update-history). For example, if a user wishes to request a specific discount from their salesperson, they may include this request as a note.

The following actions are available, depending on the user’s storefront permissions:

| Actions                                                                                         | Required storefront permissions                                                                                                               |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [Editing a quote](#editing-a-quote)                                                             | Any of the following:<br></br>Edit My Cost Center's Quotes and Carts<br></br>Edit My Organization's Quotes and Carts<br></br>Edit All Quotes and Carts       |
| [Requesting additional adjustments to a quote](#requesting-additional-adjustments-to-a-quote)   | Any of the following:<br></br>Access My Cost Center's Quotes and Carts<br></br>Access My Organization's Quotes and Carts<br></br>Access All Quotes and Carts |
| [Declining a quote or saved cart](#declining-a-quote-or-saved-cart)                             | Decline Quotes and Carts                                                                                                                      |
| [Using a quote or saved cart to place an order](#using-a-quote-or-saved-cart-to-place-an-order) | Place Orders from Quotes and Carts                                                                                                            |

#### Editing a quote

Users with **Edit** [permissions](#storefront-permissions) – who are typically users associated with any of the Sales roles or the Store Admin role – can edit quotes in the **Quote Details** page as follows:

- Change the price or quantity of each SKU by editing them directly in the **Quoted Price** and **Quantity** columns of the product list within the quote.
- **Apply Percentage Discount:** apply a percentage discount to the entire quote by dragging the discount bar up to the desired percentage. This will override any changes made to individual product prices.
- **Expiration Date Change:** change the quote’s expiration date.
- **Add Note:** write an optional comment.

After making any of the above edits on the quote details page, the user must save the quote by clicking `Save quote`.

This will have the effect of setting the quote’s status to **Ready** and notifying any user who has previously interacted with the quote of the change via email – check [Email templates](#email-templates) for more details on this notification.

![quote-details-edit](https://user-images.githubusercontent.com/77292838/161637108-aeaeef58-296f-407a-9c00-b5ffe9d509fb.png)

> ℹ To take discounts into consideration, the **B2B Quotes and Carts** app is integrated with the [Order Authorization](https://help.vtex.com/en/tutorial/how-order-authorization-works--3MBK6CmKHAuUjMBieDU0pn) system. If there is a manual discount rule that will automatically deny a discount above a certain percent, **B2B Quotes and Carts** will not allow a discount above this amount to be applied.

#### Requesting additional adjustments to a quote

Users who lack any of the **Edit** permissions but have any of the **Access** [permissions](#storefront-permissions) can add additional notes to a quote or saved cart if its current status is **Ready**, **Pending**, or **Revised**.

If a quote is **Ready**, meaning that it has been adjusted and saved by a sales user, its status will change to **Revised** when an organization user adds notes and clicks `Submit to Sales Rep`. This is intended as a way for the organization user to request additional adjustments to pricing or quantity. All users who have previously interacted with the quote will receive a notification including the contents of the notes field – check [Email templates](#email-templates) for more details on this notification.

#### Declining a quote or saved cart

A declined quote or saved cart can no longer be edited or used to place an order. Users with the **Decline Quotes and Carts** [permission](#storefront-permissions) may decline a quote or saved cart if its current status is **Ready**, **Pending** or **Revised**. This can be done by clicking the `Decline` button on the quote details page.

All users who have previously interacted with the quote will be notified that it has been declined – check [Email templates](#email-templates) for more details on this notification.

#### Using a quote or saved cart to place an order

Users with the **Place Orders from Quotes and Carts** [permission](#storefront-permissions) may use a quote or saved cart to place an order if its current status is **Ready**, **Pending**, or **Revised**.

They can do this by clicking the `Use Quote` button on the quote details page. The user will be redirected to checkout with the contents of the quote or saved cart added to their current cart. Anything that was previously in the user’s cart will be cleared.

If the [B2B Checkout Settings](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-checkout-settings) app is installed, the checkout will be in a “locked” state until the order is placed, meaning that product quantities cannot be changed, and products cannot be added or removed. If there are not enough items in stock to meet the quantity specified in the quote or saved cart, the amount will be automatically adjusted. If a given product has no availability, checkout will allow it to be removed from the cart.

Once the order has been placed, the quote or saved cart’s status will automatically change to **Placed**, after which point it cannot be used again.

### Email templates

The **B2B Quotes & Carts** app provides a set of three email templates to be sent to B2B users, triggered automatically based on specific changes:

| Template name | Recipients                                                                                                                                                     | Trigger                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Quote created | Users with any of the following permissions:<br></br>Edit My Cost Center's Quotes and Carts<br></br>Edit My Organization's Quotes and Carts<br></br>Edit All Quotes and Carts | The quote request was created.                                                                                     |
| Quote placed  | All users who have previously interacted with the quote by editing it, requesting adjustments or approving it.                                                 | An order was placed from the existing quote.                                                                       |
| Quote updated | All users who have previously interacted with the quote.                                                                                                       | The quote was updated in any way – including changes in discounts or expiration dates, new notes added or refusal. |

If you want to view or edit any of these templates, follow the steps below.

1. In the VTEX Admin, go to **Customer > Message center > Templates**.
2. In the search bar, type `quote`.
3. Click on the template you want to view or edit.
4. Make the desired changes in the template. You can learn more about editing **Message Center** templates by reading our documentation on [How to create and edit transactional email templates](https://help.vtex.com/en/tracks/transactional-emails--6IkJwttMw5T84mlY9RifRP/335JZKUYgvYlGOJgvJYxRO).
5. Click on `Save`.

## **Configuration (optional)**

To change the app’s settings, access **Account Settings** > **B2B Quotes** in the VTEX Admin.

On this page, you can configure the following option:

- **Default expiration period (in days) for quotes and saved carts:** this field allows you to configure the default expiration date for new quotes requested by customers in your store. The default value is 30 days. The minimum value you can set is 1, and there is no maximum value.

Make sure you click on `Save Settings` after any changes.

Note that users with [storefront permissions](#storefront-permissions) to edit quotes will be able to adjust the expiration dates of individual quotes as needed.

![app-configuration](https://user-images.githubusercontent.com/6306265/163218059-903cfbcf-0077-45d2-9457-19ee0ba4d5c8.png)

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->