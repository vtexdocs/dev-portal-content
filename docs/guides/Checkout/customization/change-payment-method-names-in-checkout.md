---
title: "Change payment method names in Checkout"
slug: "change-payment-method-names-in-checkout"
hidden: false
createdAt: "2022-07-25T13:06:05.839Z"
updatedAt: "2022-10-20T17:35:59.686Z"
---
The name or description of payment methods can be modified by your store's CSS entered at Checkout. Typically, CSS customization is the responsibility of the agency hired by the store for this purpose. However, for this case, several simple ways to change them are described below.

- **Change the name of the payment method**: [image-replacement](http://css-tricks.com/css-image-replacement/) technique can be used;
- **Change the description of the payment method**: enter the following code on your CSS:

`.bankInvoicePaymentGroup .payment-description { font-size: 0; }.bankInvoicePaymentGroup .payment-description:after { font-size: 13px; content: "{Text here}" }`

- Change the name of the delivery phase: enter the following code on your CSS:

`.shipping-data .accordion-toggle span { font-size: 0: }.shipping-data .accordion-toggle span:after { content: "{Text here}"; }`

>⚠️ Note that you should be very careful about any CSS or JavaScript changes in your store. If it's not properly done, this kind of customization can compromise your store's conversion rate and the security of your checkout.
