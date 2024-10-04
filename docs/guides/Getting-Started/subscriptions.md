---
title: "Subscriptions"
slug: "subscriptions"
hidden: false
createdAt: "2023-01-11T18:18:00.000Z"
updatedAt: "2024-04-10T18:18:00.000Z"
---

> **Help us improve our documentation!** Tell us about your experience with this article by filling out [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

[Subscriptions](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453) is the VTEX solution for customers to make recurrent purchases on a regular schedule, determining the orders’ products and frequency. This overview article presents what you can accomplish with **Subscriptions** and gathers relevant documentation on the subject.

## Understanding Subscriptions

**Subscriptions** is an app developed by VTEX to facilitate recurring sales for a store. It works as an automatic scheduler, executing a repurchase at the frequency requested by the customer.

To enable **Subscriptions** for customers, merchants have to [create subscription plans](https://help.vtex.com/en/tutorial/creating-a-subscription-plan--1qGRoFczm98Wgt81f9mUqC) to associate the products valid for subscriptions and the frequencies available for recurrent orders.

Once the [Subscriptions module is configured](#setting-up-subscriptions-mandatory), the merchant can generate, edit and manage customers’ recurrent orders, and [create subscription promotions](https://help.vtex.com/tutorial/creating-a-subscription-promotion--3ROT13HYNeUIv0plDqgNed).

The composition of a subscription is as the following:

![subscription-composition](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Subscriptions/subscriptions-v3-migration-guide-2_51.PNG)

Every subscription order has an execution count called cycle. The cycle determines the position of an order counting from when the shopper subscribed. The original order that creates the subscription corresponds to 0, the first subscription order corresponds to 1, the second corresponds to 2, and so on.

Customers can create a subscription during checkout or on their [My Account](https://help.vtex.com/en/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh) page, and the communication between merchants and customers regarding subscriptions is made in the **Email Templates** module through [transactional emails](https://help.vtex.com/en/tutorial/transactional-emails-for-subscriptions-orders--2NYHqHMRqZ43Cn6s84ZCB5).

> This module may process personal or sensitive information. Learn more about how VTEX handles data privacy at our [Data privacy](https://developers.vtex.com/docs/guides/data-privacy) guide.

## Setting up Subscriptions (mandatory)

To install the **Subscriptions** module, merchants have to contact [our Support](https://help.vtex.com/support). After that, they have to follow the configuration steps described in [How to configure Subscriptions in your store](https://help.vtex.com/en/tutorial/how-to-configure-subscriptions-in-your-store--1FA9dfE7vJqxBna9Nft5Sj).

After the installation, merchants have to [create subscription plans](https://help.vtex.com/en/tutorial/creating-a-subscription-plan--1qGRoFczm98Wgt81f9mUqC) to associate the products valid for subscriptions and the frequencies available for recurrent orders.

We highly recommend creating subscription plans in the **Subscriptions** module of your VTEX Admin, although it is also possible to create them as [catalog attachments](https://help.vtex.com/tutorial/how-to-create-a-subscription-attachment-via-the-catalog-module--2bUuKyPflA8cOGLv8OvaKK).

**In Admin:** Orders > Order Management > Subscriptions > Dashboards

**In Redesigned Admin:** Orders > Subscriptions > Dashboards

## Managing Subscriptions

In this section, you will find content about controlling and editing the **Subscriptions** settings of your store, and about updating, retrieving data and removing subscription orders.

### Settings

You can edit the **Subscriptions** settings of your store and retrieve information about them.

* [POST - Edit Subscriptions settings](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/settings)
* [GET - Get Subscription Settings](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/settings)

### Plans

It is possible to list and retrieve information about **Subscription plans**.

* [GET - List plans](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pvt/plans)
* [GET - Get plan details](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pvt/plans/-id-)

### Subscriptions

You can update settings, edit items and retrieve information about a given subscription.

* [POST - Create subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pub/subscriptions)
* [PATCH - Update subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#patch-/api/rns/pub/subscriptions/-id-)
* [GET - Get subscription details](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pub/subscriptions/-id-)
* [GET - List subscriptions](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pub/subscriptions)
* [PATCH - Edit item on subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#patch-/api/rns/pub/subscriptions/-id-/items/-itemId-)
* [POST - Add item to subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pub/subscriptions/-id-/items)
* [DELETE - Remove item from subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#delete-/api/rns/pub/subscriptions/-id-/items/-itemId-)

### Cycles

Cycles are the execution count of subscription orders. The cycle determines the position of an order counting from when the shopper subscribed.

You can retrieve information about cycles and rerun cycles that present errors, which will reprocess the order.

* [GET - Get cycle details](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pub/cycles/-cycleId-)
* [GET - List cycles](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pub/cycles)
* [POST - Retry cycle](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pub/cycles/-cycleId-/retry)

### Communication

The communication between stores and shoppers about subscription orders happens via [transactional emails](https://help.vtex.com/en/tutorial/transactional-emails-for-subscription-orders--2NYHqHMRqZ43Cn6s84ZCB5). It is possible to retrieve the conversation messages sent to a shopper regarding a subscription order.

* [GET - Get conversation messages](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pub/subscriptions/-subscriptionId-/conversation-message)

## Enabling manual prices

When using **Subscriptions**, stores might need to configure prices manually. By [enabling the Manual Price feature for Subscriptions](https://developers.vtex.com/docs/guides/enabling-manual-prices-for-subscriptions-v3#setting-a-manual-price-in-a-subscription-item), merchants can apply a manual price on each subscription item, overriding the current price, and maintain the same manual price for future recurrent orders from a given subscription.

## Simulating prices

It is possible to simulate a subscription order price at checkout, getting information about items and shipping costs.

* [POST - Calculate the current prices for a specific subscription](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pub/subscriptions/-id-/simulate)
* [POST - Calculate the current prices for the provided subscription template](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pub/subscriptions/simulate)

## Configuring pickup points for subscription orders

>ℹ️ The feature pickup points for subscription orders is in beta and available only for stores using the **Checkout V6**.

A [pickup point](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) is a physical location where shoppers can pick up their orders instead of having them delivered to their addresses, and merchants can [configure pickup points for subscription orders](https://help.vtex.com/tutorial/pickup-points-for-subscription-orders-beta--csIqB6iBh4QNIFdEj0nVv). The requirements are the following:

* Have the [Subscriptions module](https://help.vtex.com/en/tutorial/how-to-configure-subscriptions-in-your-store--1FA9dfE7vJqxBna9Nft5Sj) installed.
* Have pickup points configured.
* Associate to pickup points for subscription orders only carriers that do not have a [delivery windows](https://help.vtex.com/pt/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) configured.
* Have items in stock at the subscription cycle date.

## Controlling reports

You can generate reports about subscription orders using templates to filter orders. When you create a template, you determine which criteria will be used for filtering: order status, creation date, scheduled date, among others.

* [GET - List report templates](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pvt/reports)
* [GET - Get report document details](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#get-/api/rns/pvt/reports/-reportName-/documents/-documentId-)
* [POST - Generate report](https://developers.vtex.com/docs/api-reference/subscriptions-api-v3#post-/api/rns/pvt/reports/-reportName-/documents)
