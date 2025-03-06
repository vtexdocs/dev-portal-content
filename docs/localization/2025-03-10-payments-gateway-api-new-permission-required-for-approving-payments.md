---
title: "Payments Gateway API: New permission required for approving payments"
slug: "2025-03-10-payments-gateway-api-new-permission-required-for-approving-payments"
type: "added"
createdAt: "2025-02-07T17:08:52.219Z"
updatedAt: ""
hidden: false
excerpt: "From April 1, 2025, a new permission is required to access payment notification endpoints in the Payments Gateway API."
---

We're introducing a new permission model for the payment notification endpoints in the Payments Gateway API, used exclusively for manual approval of payments:

* `GET` [Send payment notification with payment ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/payments/pvt/payments/-paymentId-/payment-notification)
* `POST` [Send payment notification with payment ID, date, and value paid](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/pvt/payments/-paymentId-/payment-notification)

After **April 1, 2025**, users or API keys must have a role with the new *Payments Notification* resource to call these endpoints. The new *Payments Notifier* predefined role is available for this purpose.

## What has changed?

* **New License Manager resource:** *Payments Notification*

  Required to access the [`GET`](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/payments/pvt/payments/-paymentId-/payment-notification) or [`POST`](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/pvt/payments/-paymentId-/payment-notification) payment notification endpoints on the Payments Gateway API, after **April 1, 2025**.

* **New predefined role:** *Payments Notifier*

  Includes the new *Payments Notification* resource.
  By default, this role will only be assigned to the **Sponsor** user.

## What needs to be done?

Only accounts that currently use the [`GET`](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/payments/pvt/payments/-paymentId-/payment-notification) or [`POST`](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/pvt/payments/-paymentId-/payment-notification) payment notification endpoints in the Payments Gateway API or plan to do so are affected by this change.

The Sponsor user for these accounts must assign the *Payments Notifier* role to users and API keys that need access to payment approval notifications via the Payments Gateway API. The deadline for this action is **April 1, 2025**.
