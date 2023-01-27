---
title: "Subscriptions API - v2 - Overview"
slug: "subscriptions-api-v2-overview"
hidden: true
createdAt: "2020-01-02T05:18:04.374Z"
updatedAt: "2021-02-10T19:01:53.494Z"
---

> ⚠️ This API is deprecated. Please use Subscriptions API - v3 instead.

This documentation describes the available REST APIs for **VTEX Subscription System**.

With Subscriptions you can set up regularly scheduled deliveries in order to  improve revenue and also reduce your store's bounce rate and churn.

All requests need authorization (VTEX ID authentication token or VTEX Appkey and Apptoken headers).

To read more about the Subscriptions feature, check our article [Setting up Subscription v2](https://help.vtex.com/tutorial/como-configurar-assinatura-v2--1FA9dfE7vJqxBna9Nft5Sj).

A **Subscription** is the representation in the system for an item (SKU) purchased with a given frequency, and the amount of units that will be used in that recurring purchase. There are a series of steps to configure the Subscriptions module in your store, you can check them [here](https://help.vtex.com/tutorial/how-to-configure-subscriptions%20--1FA9dfE7vJqxBna9Nft5Sj). After you installed the Subscriptions module, you should configure an SKU in your store to be available for Subscription orders. You do that by adding a subscription attachment to the chosen SKU. In this attachment, you will define the details around that subscription, like the permitted frequency of purchase, for example.

Currently, our system can only generate a subscription by starting from the **original order** that the client does in the checkout. This original order must include an SKU that had a Subscription attachment to it.

The **Subscription Group** is the entity shown by the system's APIs, that represents one or more items (SKUs) subscribed. Every subscribed item is part of a subscription group. All items in a group possess the same attributes that generate a recurring order. These attributes include: the subscriber's data, payment method, period and frequency.

For example, a client made an order, adding 5 items in the checkout. All of the items possess the same SKU Attachment, turning them into items viable for subscription. In this case, if the client determines the same frequency for all five items under the subscription, 5 subscriptions will be created, under 1 group. Thus, the API allows that any alteration in the group is reflected in all items, without the need to make single alterations in each item individually.
