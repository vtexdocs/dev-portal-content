---
slug: "new-customer-credits-use-conditions-endpoint"
title: "Customer Credit: New Purchase Conditions endpoint"
createdAt: 2020-08-11T14:23:14.329Z
hidden: true
type: "added"
---

![Commerce APIs](https://img.shields.io/badge/-Commerce%20APIs-brightgreen)

Each Customer Credit account has a set of use conditions configured specifically for it.

With that, the Checkout displays a personalized scenario every time that a client chooses the Customer Credit as a payment method to make a purchase.

Now, using [this new endpoint] (link), you can retrieve an account's use conditions all at once. In addition to the payment conditions, the payload also retrieves the quantity of available credit and the account identifier.
