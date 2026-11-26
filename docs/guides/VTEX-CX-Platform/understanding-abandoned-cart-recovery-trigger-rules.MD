---
title: "Understanding abandoned cart recovery trigger rules"
slug: "understanding-abandoned-cart-recovery-trigger-rules"
excerpt: "Learn why the WhatsApp abandoned cart recovery message from VTEX CX Platform is sent in some situations and blocked in others."
hidden: false
createdAt: "2026-08-31T00:00:00.000Z"
updatedAt: "2026-08-31T00:00:00.000Z"
---

The abandoned cart recovery feature of VTEX CX Platform sends a WhatsApp message to a customer who added items to a cart in your store and didn't complete the purchase.

A common question is why the message wasn't sent in a specific situation. This happens because the trigger depends on two sequential stages, and a failure in either of them prevents the message from being sent. The stages are:

1. [Your store sends the cart data to VTEX CX Platform](#stage-1-sending-the-cart-data).
2. [VTEX CX Platform evaluates whether to trigger the message](#stage-2-evaluating-whether-to-trigger-the-message).

Most abandoned carts stop at the first stage, so they're never evaluated for a trigger.

In this article, you'll learn when the abandoned cart recovery message is sent, when it's blocked, and which rules define this behavior.

> ℹ️ This feature is different from the native [Abandoned cart](https://help.vtex.com/en/docs/tutorials/setting-up-abandoned-carts) feature, which sends emails and is configured through Master Data. Both features are independent and can run at the same time.

## Overview

The trigger goes through two sequential stages:

| Stage | Where it happens | What it decides |
| :---: | :--- | :--- |
| Sending the cart data | On your store's pages | Whether the cart data is sent to CX Platform. |
| Evaluating whether to trigger the message | In VTEX CX Platform | Whether the cart is registered and whether the WhatsApp message is triggered. |

If Stage 1 doesn't send the data, Stage 2 doesn't happen. In that scenario, there's no record of the cart in CX Platform, so there's nothing to evaluate, since the cart doesn't appear in reports or in the execution history.

## Stage 1: Sending the cart data

For the recovery flow to work, your store needs to send the cart data to VTEX CX Platform. On the regular website, this is done automatically by a script that runs on your store's pages and watches the customer's cart.

The script is served at:

```bash
https://cdn.cloud.weni.ai/agentic-cx.js
```

> ℹ️ If your store operates storefronts beyond the website, such as a mobile app or a headless frontend, the script described in this section doesn't run there. Use [Integrating with the abandoned cart webhook](https://developers.vtex.com/docs/guides/integrating-with-the-abandoned-cart-webhook) to notify VTEX from your own backend instead. The eligibility rules described in this article, such as the abandonment time and the minimum cart value, apply the same way regardless of which path registers the cart.

The script attempts to send the cart data at the following moments:

- When any page of the store loads.
- When the customer adds an item to the cart.
- When the cart (order form) is updated, with a limit of one attempt every 3 seconds.
- Every 15 minutes, while the customer's session remains active.

> ℹ️ You can also enable this feature inside the VTEX Admin. To learn more, read the [Introduction to VTEX CX Platform](https://help.vtex.com/docs/tutorials/introduction-to-cx) article.

### Data required

The script needs to gather all the four following items to send the cart data:

| Data | Description |
| :---: | :--- |
| VTEX account | Store account the cart belongs to. |
| Cart (order form) | Identifier of the customer's cart in the store. |
| Name | Customer's name, used to personalize the message. |
| Phone number | Customer's phone number, used to send the WhatsApp message. |

To get the name and phone number, the script checks the following sources, in this order:

1. The profile data already filled in the cart (order form).
2. The customer's profile in the store.
3. The customer's session in the store.

If none of these sources has the name and the phone number, the script doesn't send the data and the recovery cart message isn't triggered.

### Stage 1 scenarios

| Scenario | Status of the cart data |
| :---: | :--- |
| A customer adds items to the cart without providing a name or a phone number. | Not sent. |
| A customer with a name and a phone number in their profile adds a product to the cart without going to checkout. | Sent. |
| A customer fills in only the email at checkoutm without providing a name or a phone number. | Not sent. |
| A customer fills in the name and phone number at checkout and navigates to another page of the store. | Sent on the next attempt. |
| A customer updates their name and phone number in their account profile, and the data becomes available in the sources the script checks. | Sent on the following attempts. |

## Stage 2: Evaluating whether to trigger the message

This stage only happens if Stage 1 sent the data successfully. Here, VTEX CX Platform decides whether to register the cart and whether to trigger the WhatsApp message.

The trigger is blocked in the following situations:

| Rule for blocking the trigger | Description |
| :---: | :--- |
| Same cart within 15 days | The specific cart (order form) already had a successful trigger in the last 15 days, even if the customer added, removed or edited items. |
| Identical cart within 24 hours | The same phone number already received a trigger with the same items in the last 24 hours. |
| Phone cooldown | The minimum time, in hours, the same phone number must wait after receiving a trigger before it can receive another one. This feature is off by default. You can configure it from `1` to `168` (7 days). |
| Value below the minimum | The cart value didn't reach the configured minimum value. The default value is R$ 50. |
| Empty cart | The cart has no items. |
| Cart without an email | The customer's email isn't filled in the cart. |
| Order already purchased | The purchase was completed before the check ran. |
| Cart abandonment time hasn't been reached. | The cart has to be abandoned for longer than its abandonment time to trigger the message. The default time is 60 minutes. |
| Invalid data | The data sent is invalid. |

### Stage 2 scenarios

| Scenario | Status of the recovery cart message trigger |
| :---: | :--- |
| Data sent with name, phone number, and cart; abandonment time reached; no blocking rule applies. | Triggers. |
| A cart already had a trigger, and the customer comes back and adds products to the same cart. | Doesn't trigger, because of the 15-day block. |
| The same cart is renewed several times on the same day. | Tends to generate a single trigger. |
| Different carts on the same day, with the cooldown off. | More than one trigger can happen, unless the items are identical within 24 hours. |
| Different carts on the same day, with the cooldown on. | After the first trigger, the following ones tend to be blocked. |
| The customer abandons a cart again the next day, with a different cart and different items, and the cooldown off. | Can trigger. |
| The customer corrects their phone number. | The previous record stays active, and a new record is created with the new phone number. Two carts can exist, and whichever triggers first can block the other one through the 15-day rule. |

To track the performance of the abandoned cart recovery feature, see the dashboard described in [Introduction to CX](https://help.vtex.com/docs/tutorials/introduction-to-cx).
