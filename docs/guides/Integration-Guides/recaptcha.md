---
title: "reCAPTCHA"
slug: "recaptcha"
hidden: false
createdAt: "2021-08-03T21:49:23.639Z"
updatedAt: "2022-05-10T14:20:43.993Z"
---
reCAPTCHA is a tool used to determine if a given action is performed by a real user or malicious automation. Therefore, it is particularly helpful in preventing ecommerce fraud. 

This guide shows you how to implement this feature in checkout integrations. To learn more about this type of validation in VTEX stores, see this [article on reCAPTCHA](https://help.vtex.com/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP) on our help center.
[block:callout]
{
  "type": "info",
  "body": "VTEX uses reCAPTCHA v2. Learn more about it in the official [reCAPTCHA v2 documentation](https://developers.google.com/recaptcha/docs/display) provided by Google."
}
[/block]
To configure reCAPTCHA verification, follow the steps below:

1. Make a `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).

2. Make a `POST` request using the endpoint [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) with the same data obtained in the GET request, just modifying the  `recaptchaValidation` parameter to one of the following values:
   - `"never"`: no purchases are validated with reCAPTCHA.
   - `"always"`: all purchases are validated with reCAPTCHA.
   - `"vtexCriteria"`: only some purchases are validated with reCAPTCHA in order to minimize friction and improve shopping experience. VTEX’s algorithm determines which sessions are trustworthy and which should be validated with reCAPTCHA. This is the recommended option.

3. Make a new `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm) to confirm activation.

This configuration is valid for the entire account. It is not possible to activate reCAPTCHA for a limited number of [bindings](https://help.vtex.com/en/tutorial/o-que-e-binding--4NcN3NJd0IeYccgWCI8O2W#).
>❗ If you activate reCAPTCHA for your account, it is important to note that any integrations that deal with placing orders should be able to handle the validation. That is, integrations should display the validation to the user and send the appropriate response token to VTEX once they solve it successfully. If reCAPTCHA is required for a given order, it can not be placed without validation. However, if your store uses VTEX’s native UI, it is already capable of handling reCAPTCHA.

Learn more about the [applicable cases](https://developers.vtex.com/vtex-rest-api/docs/applicable-cases) and [how to implement reCAPTCHA for Checkout integrations](https://developers.vtex.com/vtex-rest-api/docs/implementing-recaptcha-in-integrations).
