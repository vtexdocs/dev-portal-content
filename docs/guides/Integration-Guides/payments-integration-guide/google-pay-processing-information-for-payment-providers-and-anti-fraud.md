---
title: "Google Pay: processing information for payment providers and anti-fraud"
slug: "google-pay-processing-information-for-payment-providers-and-anti-fraud"
hidden: false
createdAt: "2022-06-22T00:00:00.000Z"
updatedAt: ""
---

Purchase transactions made through Google Pay are sent to payment providers and anti-fraud with the same payload structure present in a purchase made through credit or debit cards on VTEX.

The payment method indicated in the transaction is the card brand used in the purchase. If the provider wishes to have the "Google Pay" information present in the transaction, it is necessary to request it from [VTEX Support](https://help.vtex.com/support). After implementing the request, the `paymentOrigin` field will be sent filled in as "Google Pay" whenever the transaction is made through this digital wallet.

Similarly, when providers choose to process DPAN cards, after contacting VTEX Support, transactions will be sent with two additional fields: `cryptogram` and `eci` (filled only in purchases with Visa cards).
