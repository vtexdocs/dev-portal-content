---
title: "FAQ: ERP Integration"
slug: "faq-erp-integration"
hidden: false
createdAt: "2020-09-21T22:45:41.805Z"
updatedAt: "2021-06-21T13:53:23.523Z"
---

## 1. How should you treat order cancelations in the integration?

When filtering Feed or Hook events by status, you can monitor events with the status `cancelation-request`. This way, whenever a customer requests cancelation the integration is notified and the store can check if the order is already on its way to the carrier or can still be canceled.

VTEX’s [order flow](https://help.vtex.com/tutorial/order-flow-on-the-oms--tutorials_196#) includes a `window-to-cancel`, which is a time period you can set during which the order has not yet gone to handling and the customer may cancel with minimal consequence to the store.

You can also set up your integration to check again and see if the order has been canceled before it goes to shipping. At this point, if it has not been canceled, the store can invoice and ship it.

## 2. Why doesn't the feed always return all available messages in the queue?

This is because of VTEX’s distributed data structure which allows different processes to run in parallel providing a high-performance system. For performance reasons, we use [Standard Queues at AWS’s Simple Queue Services](https://aws.amazon.com/pt/sqs/features/).

## 3. Why does the feed send out duplicate events?

This can happen because of VETX’s distributed data structure which allows different processes to run in parallel providing a high-performance system.

Also, there are cases in which an order can receive the same status twice in regards to different events. Consider, for instance, an order that is split between two sellers of a marketplace. Each seller is going to invoice part of the order, generating two different events with the status `invoiced`. In cases like this, the integration must be prepared to deal with this possibility.

## 4. Feed or Hook, which should I use?

See our [Feed v3 API guide](https://developers.vtex.com/docs/guides/orders-feed).

## 5. Order is locked in `Ready for Handling`. What do I do?

Access our this [article on how to solve orders locked in `Ready for Handling`](https://help.vtex.com/faq/meus-pedidos-estao-travados-em-pronto-para-manuseio--frequentlyAskedQuestions_771#).