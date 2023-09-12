---
title: "New Checkout Settings for Bot Attack Protection"
slug: "2023-09-12-new-checkout-settings-for-bot-attack-protection"
type: "added"
excerpt: "Expanding protective measures against potential bot attacks."
createdAt: "2023-09-12T00:00:00.000Z"
updatedAt: "2023-09-12T00:00:00.000Z"
---

# New Checkout Settings for Bot Attack Protection

In order to enhance system security, new Checkout configuration options have been made available, expanding protective measures against potential bot attacks.

## What has changed?

The following fields have been added to your store's orderForm configuration and can be modified via the endpoint [Update an account's orderForm configuration](https://developers.vtex.com/docs/guides/update-an-account-orderform-configuration).

- `requiresLoginToPlaceOrder`: indicates whether purchases should only be completed by customers who are already authenticated in the store (via registered email).
- `minimumPurchaseDowntimeSeconds`: defines a minimum amount of time (in seconds) for a buyer to wait before making another purchase.

>⚠️ This setting is most efficient when combined with mandatory login during the checkout process (previous configuration).

cartAgeToUseNewCardSeconds: defines the minimum amount of time (in seconds) in which the cart must have been created to allow a new credit card to be applied to it.
