---
title: "Set a discount using the Checkout API"
slug: "set-a-discount-using-the-checkout-api"
hidden: false
createdAt: "2020-08-03T18:41:16.434Z"
updatedAt: "2022-10-20T17:36:22.970Z"
---

One of the most used customer attraction strategies in ecommerce is applying a discount to the cash price when choosing a specific payment method. Commonly, the discount price is visible only at the checkout payment stage after the user has already chosen the payment method that grants the discount.

This Checkout configuration sets the discount price and links it to a payment method. To configure, follow the steps below:

1. Use the [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) endpoint to enter the desired payment method ID in the `paymentSystemToCheckFirstInstallment` property.

2. To get the payment method ID, access Settings in the **Payments** module. The ID of the condition you want to use is on the right side of the screen in the **Payments Settings > Payments Conditions** section.

![Payment condition](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/set-a-discount-using-the-checkout-api-0.png)

3. After updating `paymentSystemToCheckFirstInstallment`, you can [Simulate a shopping cart](https://developers.vtex.com/docs/guides/simulate-a-shopping-cart). Thus, you will be able to verify that the chosen payment method has been updated with the discount in the cash payment option in the `installmentOptions` section, within `paymentData`.

```json
"paymentData":{
    "installmentOptions":[
   	 {
   		 "paymentSystem":"6",
   		 "paymentName":"Boleto Bancário",
   		 "paymentGroupName":"bankInvoicePaymentGroup",
   		 "value":10000,
   		 "installments":[
   			 {
   				 "count":1,
   				 "hasInterestRate":false,
   				 "interestRate":0,
   				 "value":9000,
   				 "total":9000,
   			 }
   		]
   	}
  ]
}
```

For more information, check [Configuring a discount for orders prepaid in full](https://help.vtex.com/en/tutorial/configurar-desconto-de-preco-a-vista--7Lfcj9Wb5dpYfA2gKkACIt).
