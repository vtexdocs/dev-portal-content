---
slug: "improvement-price-consistency-checkout-discounts-installments"
title: "Price consistency at Checkout with discounts applicable to a specific number of installments"
createdAt: 2021-11-11T14:05:58.063Z
hidden: false
type: "fixed"
---

<div class="badge" id="suggestions-api">Integration</div>
<br></br>

We have improved the way installments are calculated and displayed to our customers at Checkout. This change aims to provide accurate information on discounts in the appropriate contexts. 


## What has changed?
Before this change, customers could experience issues in the installments selector if there was a discount eligible only for orders paid in a limited number of installments.

This happened due to an inconsistency in the values available in [orderForms’](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview#paymentdata) `paymentData.installmentOptions` object. This object is commonly used by Checkout interfaces to display installment options for a given payment.

Since the `installmentsOptions` object does not support the type of discount mentioned above, we launched the [Cart installments API endpoint](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#getcartinstallments), which returns installment options’ values consistent with the applicable discounts, if there are any.

 
## What needs to be done?
If your store uses our Checkout API connected to a different user interface, such as a proprietary app or website, you can implement this improvement using the new [Cart installments API endpoint](https://developers.vtex.com/vtex-rest-api/reference/shopping-cart#getcartinstallments). After the implementation, price discrepancies will no longer be a problem.