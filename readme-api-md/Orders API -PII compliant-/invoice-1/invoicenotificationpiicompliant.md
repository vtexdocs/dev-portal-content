---
title: "Order invoice notification"
slug: "invoicenotificationpiicompliant"
excerpt: "Once the order is invoiced, the seller should use this request to send the invoice information to the marketplace.\n\nWe strongly recommend that you always send the object of the invoiced items. With this practice, rounding errors will be avoided.\n\nIt is not allowed to use the same `invoiceNumber` in more than one request to the Order Invoice Notification endpoint.\n\nBe aware that this endpoint is also used by the seller to send the order tracking information. This, however, should be done in a separate moment, once the seller has the tracking information.\n\r\n\r> The `Notify invoice` resource is needed to use this API request. This is included in `OMS - Full access` and `IntegrationProfile - Fulfillment Oms`, among other default roles available in the Admin. Learn more about the [License manager roles and resources](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#)."
hidden: true
createdAt: "2022-04-26T15:47:38.591Z"
updatedAt: "2022-04-26T15:47:38.591Z"
---
