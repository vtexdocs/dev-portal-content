---
title: "Customer Credit API - Overview"
slug: "customer-credit-api-overview"
hidden: false
createdAt: "2020-01-02T04:28:35.895Z"
updatedAt: "2020-09-22T17:11:32.786Z"
---
With Customer Credit your store can enable **credit payments** through the checkout. You can also control **invoices** and the **credit limits** of your clients.

Learn more about Customer Credit in our [Help Center article](https://help.vtex.com/en/tracks/customer-credit-getting-started).

All requests need the **authorization header**.

Additionally, you can find more information on installment payments for an order in the `customData`  field found in the [Get Order](https://developers.vtex.com/reference/orders#getorder) endpoint of the Orders API. This includes the number of installments, amount and due dates.

This API allows two kinds of authorization:
1. Authorization header containing the VTEX ID authentication token.
2. VTEX Appkey and Apptoken headers.