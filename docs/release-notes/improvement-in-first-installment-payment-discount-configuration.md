---
slug: "improvement-in-first-installment-payment-discount-configuration"
title: "Improvement in first installment payment discount configuration"
createdAt: 2021-12-14T18:55:36.844Z
hidden: false
type: "added"
---

![Payments](https://img.shields.io/badge/-Payments-blueviolet)

VTEX allows stores to [Configure discounts for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt#). In order to do this, you must set the Checkout configuration parameter `paymentSystemToCheckFirstInstallment`. 

Before, it was necessary to contact VTEX support in order to change this configuration, but now any store can set it directly, using the [Checkout configuration API request](https://developers.vtex.com/vtex-rest-api/reference/configuration#updateorderformconfiguration). To do this, you may send the `paymentSystemToCheckFirstInstallment` field as the ID of the desired payment system (string).
[block:callout]
{
  "type": "warning",
  "body": "This configuration receives only one payment system."
}
[/block]
Learn more: 
- [Configure discounts for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt#)
- [Using Checkout API to set a discount](https://developers.vtex.com/vtex-rest-api/docs/using-checkout-api-to-set-a-discount).