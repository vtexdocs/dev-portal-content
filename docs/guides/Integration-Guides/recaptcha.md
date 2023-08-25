---
title: "reCAPTCHA"
slug: "recaptcha"
hidden: false
createdAt: "2021-08-03T21:49:23.639Z"
updatedAt: "2023-06-16T10:20:43.993Z"
---

reCAPTCHA is a tool used to determine if a given action is performed by a real user or malicious automation. Therefore, it is particularly helpful in preventing ecommerce fraud.

This guide shows you how to implement this feature in checkout integrations. To learn more about this type of validation in VTEX stores, see this [article on reCAPTCHA](https://help.vtex.com/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP) on our help center.

>ℹ️ VTEX is integrated with reCAPTCHA enterprise, which offers two validation approaches: checkbox (equivalent to reCAPTCHA v2) and score-based (equivalent to reCATPCHA v3) . See this article on [reCAPTCHA at VTEX Checkout](https://help.vtex.com/en/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP#recaptcha-versions) to learn what version you should use depending on your storefront characteristics. You can also learn more each method: [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) or [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) with the documentation provided by Google.

To configure reCAPTCHA verification, follow the steps below:

1. Make a `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).
2. Make a `POST` request using the endpoint [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) with the same data obtained in the GET request, just modifying the  `recaptchaValidation` parameter to one of the following values:
   - `"never"`: no purchases are validated with reCAPTCHA.
   - `"always"`: all purchases are validated with reCAPTCHA. This is the recommended option if you are using score-based validation (equivalent to reCATPCHA v3).
   - `"vtexCriteria"`: only some purchases are validated with reCAPTCHA in order to minimize friction and improve the shopping experience. VTEX’s algorithm determines which sessions are trustworthy and which should be validated with reCAPTCHA. This is the recommended option if you are using checkbox validation (equivalent to reCAPTCHA v2).
3. Make a new `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm) to confirm activation.

This configuration is valid for the entire account. It is not possible to activate reCAPTCHA for a limited number of [bindings](https://help.vtex.com/en/tutorial/o-que-e-binding--4NcN3NJd0IeYccgWCI8O2W#).

>❗ If you activate reCAPTCHA for your account, it is important to note that any integrations that deal with placing orders should be able to handle the validation. If reCAPTCHA is required for a given order, it can not be placed without validation. However, if your store uses VTEX’s native UI, it is already capable of handling reCAPTCHA.
>⚠️ If you are implementing a headless checkout experience in your store or even carrying out order creation tests via API, reCAPTCHA in active mode can block order completion requesting the reCAPTCHA validation key that is not possible to generate only via API, its only possible to generate displaying the reCAPTCHA widget.

Learn more about the [applicable cases](https://developers.vtex.com/vtex-rest-api/docs/applicable-cases) and [how to implement reCAPTCHA for Checkout integrations](https://developers.vtex.com/vtex-rest-api/docs/implementing-recaptcha-in-integrations).

## reCAPTCHA score

Score-based reCAPTCHA returns a score for the user interaction at your store. Possible values are `0.1`, `0.3`, `0.7` and `0.9`, where `1.0` is is very likely a good interaction and `0.0` is very likely a bot. Learn more about [how to interpret this score](https://developers.google.com/recaptcha/docs/v3?#interpreting_the_score).

If you are implementing score-based reCAPTCHA, you have the option to set a minimum score for each [key that you create](https://developers.vtex.com/docs/guides/implementing-recaptcha-in-integrations#getting-the-recaptcha-key-for-mobile-implementations) and set a minimum score for your account.

The priority order of score application for any given purchase is:

```bash
reCAPTCHA key score > Account score > VTEX default score (0.7)
```

This means that if you set minimum scores for both your key and account, the minimum score of the key will be applied. On the other hand, if you set neither, VTEX will apply the default value of `0.7`.

Interactions that return a value lower than the minimum value applicable will not be able to place orders.

### Setting an account minimum score

To set a minimum score for your account, follow the steps below:

1. Make a `GET` request using the endpoint [Get orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).
2. Make a `POST` request using the endpoint [Update orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) with the same data obtained in the GET request, just adding or modifying the value of the field `recaptchaMinScore`, which is a decimal number.
