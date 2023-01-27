---
title: "Implementing reCAPTCHA in integrations"
slug: "implementing-recaptcha-in-integrations"
hidden: false
createdAt: "2021-08-03T21:56:05.910Z"
updatedAt: "2022-09-05T16:48:05.147Z"
---
In order to have your implementation validate users with reCAPTCHA, they should first obtain the appropriate key from VTEX’s Checkout API and then use that key to display the actual reCAPTCHA widget on their UI. Once the shopper correctly solves the validation, the integration receives a token that should be sent in the request that places the order.

>⚠️ You must have a [Beta environment](https://help.vtex.com/pt/tutorial/acessar-o-ambiente-beta-pelo-dominio-myvtex-com--3BHM289568gcSwk2O80Asu) and use [Checkout V6](https://help.vtex.com/pt/tutorial/ativar-o-checkout-v6--7qVqv3ptRvpVVplrvg8ruH) to test the feature.

> ℹ️️ In order to simulate an untrustworthy session, try accessing the shopping cart’s link through an anonymous browser window. reCAPTCHA validation will probably be required.

## Getting the reCAPTCHA key

There are two different ways of placing orders via API. It can be done through the [orderForm transaction endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) or the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders).

The first is based on a pre-existing `orderForm`, while the latter requires passing all of the order’s information on the request body. Because of that difference, different integrations must use different methods to obtain the reCAPTCHA key.


### orderForm transaction

This method of creating orders is based on existing `orderForm`, meaning a payment method has already been selected and VTEX already knows if reCAPTCHA validation is needed.

Whenever reCAPTCHA validation applies, according to your `recaptchaValidation` [configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm), the Checkout API should respond with a `recaptchaKey` field similar to this:

```json
{
    ...,
    "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-"
}
```


### Place order

If a reCAPTCHA validation token is necessary for a given order and this request is made without it, you should get an error response with the `recaptchaKey` in the `fields` object, like in the example below.

```json
{
    "fields": {
        "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-"
    },
    "operationId": "749dt09-34d3-4b5b-b244-978473d0d373",
    "error": {
        "code": "CHK0082",
        "message": "ReCAPTCHA necessário. Tente novamente passando o token reCAPTCHA junto com a chave fornecida.",
        "exception": null
    }
}
```


## Displaying the reCAPTCHA widget

Having obtained the `recaptchaKey`, you can pass it as the `siteKey` property when displaying the validation widget as described in the [reCAPTCHA v2 documentation](https://developers.google.com/recaptcha/docs/display).

Since reCAPTCHA application may vary according to payment method, we recommend that the integration is prepared to render the validation widget after the payment selection step.


## Final validation

After the shopper successfully solves the validation, the integration should receive a response token. This token should be included in the API request that places the order, along with the `recaptchaKey`, be it with the [orderForm transaction endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) or the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders). The example below works for both cases.

```json
{
    ...,
    "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-",
    "recaptchaToken": "03AERD8Xp5arKO6-vS76sxlAFIMqCQwHOp2XTKO-DF7HcNZZVVZGJrCmHGIBCywHstiaoOpsdmAUp5pIRVD0hOwSydYvubdor45EmSH37QuBbD4qmKfjyatKTMLpsIfmXSy40kmooZ2_TZAlVH0jnKBH5avX1BdYM4qN2uihVPjlRI1RX6ze05PG3ZDn9RQmjqHLot5jDX16nSLMauiZgCqhFPPZaKXz5qNXi2irsuM6xDIfoju50wKp9fJkDmY5eyT4_1iqEVOYkGjMq8hAorY2B6KmaiqxOYWwOPwyrPYP1sFbELO2teGeFYCuxqjOSi7Zq22xEYqQhWGeFHmu4L0ydfhbk3cHnHEyYdQpr3gaG-wHK2dVI1cMD6MYYiLwDfxZ_LgdruW7O-fT12WZCtZhUrwrefaw53hQ"
}
```


## Handling errors

The reCAPTCHA token is valid for only one attempt. So in case of error during validation, the widget has to be displayed again to the shopper, in order to get a new token. The key used to display the validation widget after the error may vary depending on the error and order placement method, as described below.


### orderForm transaction

In case of internal error (`status 500`), the widget has to be displayed using the `recaptchaKey` from the latest updated `orderForm`.

If validation fails (`status 403`), the API returns the same error `CHK0082` as mentioned above. Note that the `recaptchaKey` returned in the error may be different than the one used previously. Be sure to use the latest one received.


### Place order

In case of internal error (`status 500`), the widget has to be displayed again. The `recaptchaKey` that was used the first time may be used this time.

If validation with the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) fails (`status 403`), the API returns the same error `CHK0082` as mentioned above. Note that the `recaptchaKey` returned in the error may be different than the one used previously. Be sure to use the latest one received.

>⚠️ If you are implementing a headless checkout in your store or even carrying out order creation tests via API, reCAPTCHA in active mode can block order completion requesting the reCAPTCHA validation key that is not possible to generate only via API, its only possible to generate displaying the reCAPTCHA widget.\n \nTo bypass the reCAPTCHA key validation and be able to create the order via API without having to display the widget and solve the reCAPTCHA, the authentication keys (appKey and appToken) used to create the orders need to have the [\"Shopping cart full access\"](https://help.vtex.com/en/tutorial/perfis-de-acesso--7HKK5Uau2H6wxE1rH5oRbc#) role assigned.
