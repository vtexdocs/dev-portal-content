---
title: "Enable partial cancellation for Debit or Credit Direct sales"
slug: "enable-partial-cancellation"
hidden: false
createdAt: "2021-12-08T14:33:24.216Z"
updatedAt: "2021-12-08T14:34:08.806Z"
---
By default, inStore does not show the `Cancel order` in the [Order placed page](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/TrTtmCGVLTaCSmowGFYDI) when the selected payment method is Debit Direct sale or Credit Direct sale. It only shows the `Cancel total order` button by default in these cases.

If you want to enable partial cancellation of orders — the ability to cancel individual packages — for these payment methods, you must edit the `checkout-instore-custom.js` file as described below. Check out the [How to customize inStore guide](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) for further information on how to access this file.


## Prerequisites

To enable this functionality, make sure that you meet the following prerequisites:

* Having Debit Direct sale or Credit Direct sale configured as payment conditions, as described in the [inStore - Payments](https://help.vtex.com/en/tracks/instore-payments--43B4Nr7uZva5UdwWEt3PEy/2liigRors32hzqBNs2M1Oa) guide.
* Create the filters that define which payment methods will be displayed on inStore, as described in the [Define payment methods displayed on inStore](https://developers.vtex.com/vtex-rest-api/docs/define-payment-methods-displayed-on-instore) guide.

## Edit the `checkout-instore-custom.js` file

To enable partial cancellation for these payment methods, the `payments` object within `window.INSTORE_CONFIG` must contain the following property:
[block:parameters]
{
  "data": {
    "0-0": "`partialCancellationEnabled`",
    "0-1": "array",
    "0-2": "You should add payment conditions that will have partial cancellation enabled on inStore in this array",
    "h-0": "Property",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 1
}
[/block]

The indication of each payment condition is made by the payment condition ID. Check the section on [Where to find the payment condition ID](https://developers.vtex.com/vtex-rest-api/docs/define-payment-methods-displayed-on-instore#where-to-find-the-payment-condition-id) in the [Define payment methods displayed on inStore ](https://developers.vtex.com/vtex-rest-api/docs/define-payment-methods-displayed-on-instore)guide for more details.

In the example code below, partial cancellation will be enabled for Debit Direct Sale (whose ID is `44`) and Credit Direct Sale (whose ID is `45`).

``` javascript
window.INSTORE_CONFIG = {
 payments: {
   partialCancellationEnabled: [
     '44', // Debit Direct Sale
     '45', // Credit Direct Sale
   ],
 }
}
```