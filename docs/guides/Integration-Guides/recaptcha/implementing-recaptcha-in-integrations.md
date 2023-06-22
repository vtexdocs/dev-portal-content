---
title: "Implementing reCAPTCHA in integrations"
slug: "implementing-recaptcha-in-integrations"
hidden: false
createdAt: "2021-08-03T21:56:05.910Z"
updatedAt: "2023-06-16T10:20:43.993Z"
---

If your store uses integrations to place orders, such as mobile apps or proprietary web-based storefronts, follow the steps below to implement [reCAPTCHA validation](https://developers.vtex.com/docs/guides/recaptcha).

>⚠️ You must have a [Beta environment](https://help.vtex.com/pt/tutorial/acessar-o-ambiente-pelo-dominio-myvtex-com--3BHM289568gcSwk2O80Asu) and use [Checkout V6](https://help.vtex.com/pt/tutorial/ativar-o-checkout-v6--7qVqv3ptRvpVVplrvg8ruH) to test the feature.
> ℹ️️ In order to simulate an untrustworthy session, try accessing the shopping cart’s link through an anonymous browser window. reCAPTCHA validation will probably be required.

In order to have your implementation validate users with reCAPTCHA, you must first [obtain the appropriate reCAPTCHA key](#getting-the-recaptcha-key) and then use that key to [integrate reCAPTCHA on your storefront](#integrating-recaptcha-on-your-storefront). Once the shopper correctly solves the validation, the integration receives a token that must be [sent in the request that places the order](#final-validation).

>ℹ️ The implementation process may vary depending on whether you are using a mobile or web-based storefront. More details below.

## Getting the reCAPTCHA key

There are different ways of obtaining the reCAPTCHA key. See below the method that best applies to your context.

### Getting the reCAPTCHA key for mobile implementations

In order to implement reCAPTCHA validation in a mobile app that places orders, follow the steps below.

1. Create a Google Cloud project, according to the instructions in the article [Create, shut down, and restore projects](https://support.google.com/googleapi/answer/6251787).
2. Create a Google Cloud API key, according to the instructions in the article [Authenticate using API keys](https://cloud.google.com/docs/authentication/api-keys) provided by Google.
3. Get your current VTEX Checkout settings, with the [Get orderForm configuration API request](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).
4. Add your newly created reCAPTCHA key to your VTEX Checkout settings, by sending a request to the [Update orderForm configuration endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm). Use the configuration retrieved in step 2 as your request body and add your key information in this field:

```json
{
    …,
    "recaptchaKeys": [
        {
            "clientId": "{id-of-your-recaptcha-key}",
            "clientSecret": "{secret-key}",
            "projectId": "{id-of-your-google-cloud-project}",
            "label": "{key-name-in-vtex}",
            "score": "{recaptcha-v3-score}"
        }
    ],
    …
}
```

- `recaptchaKeys`: array of objects with keys information.
- `clientId`: ID of your reCAPTCHA key.
- `clientSecret`: API key.
- `projectId`: ID of your Google Cloud project. If you do not have your project ID at hand, check the Google Cloud documentation to learn how to [locate your project ID](https://support.google.com/googleapi/answer/7014113)
- `label`: use this field to identify your key. We recommend that you indicate the mobile platform in which you intend to use the key (e.g., `android-001`).
- `score`: [reCAPTCHA v3 score](https://developers.vtex.com/docs/guides/recaptcha#recaptcha-v3-score) (optional).

After completing this steps, see how you can [integrate reCAPTCHA](#integrating-mobile-apps) on your storefront.

>⚠️ If you have multiple integrations (e.g., an app for Android and another for iOS), create one key for each and register each one as an object in the `recaptchaKeys` array.

### Getting the reCAPTCHA key in web-based implementations

If you are implementing a web-based storefront, you must get the reCAPTCHA key from the checkout API you use to place the order.

There are two different ways of placing orders via API. It can be done through the [orderForm transaction endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) or the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders).

The first is based on a pre-existing shopping cart (`orderForm`), while the latter requires passing all of the order’s information in a single request body. Because of that distinction, different integrations must use different methods to obtain the reCAPTCHA key.

At this stage you must choose a key compatible with your desired implementation:

- `recaptchaKey`: if you are integrating with [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display).
- `recaptchaKeyV3`: if you are integrating with [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3).

>ℹ️ Learn more about the different versions of [reCAPTCHA for VTEX Checkout](https://help.vtex.com/en/tutorial/recaptcha-no-checkout--18Te3oDd7f4qcjKu9jhNzP).

#### orderForm transaction key

This method of creating orders is based on existing `orderForm`, meaning a payment method has already been selected and VTEX already knows if reCAPTCHA validation is needed.

Whenever reCAPTCHA validation applies, according to your `recaptchaValidation` [configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm), the Checkout API should respond with a `recaptchaKey` field similar to this:

```json
{
    ...,
    "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-",
            "recaptchaKeyV3": "6LfnCR8mAAAAAGfsca_MuJ4oXTWJWOJ4TkPFOXzT"
}
```

Now you can use this key to [display the reCAPTCHA widget](#integrating-web-based-storefronts) on your storefront.

#### Place order key

If a reCAPTCHA validation token is necessary for a given order and this request is made without it, you should get an error response with the `recaptchaKey` in the `fields` object, like in the example below.

```json
{
    "fields": {
        "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-",
            "recaptchaKeyV3": "6LfnCR8mAAAAAGfsca_MuJ4oXTWJWOJ4TkPFOXzT"
    },
    "operationId": "749dt09-34d3-4b5b-b244-978473d0d373",
    "error": {
        "code": "CHK0082",
        "message": "ReCAPTCHA necessário. Tente novamente passando o token reCAPTCHA junto com a chave fornecida.",
        "exception": null
    }
}
```

Now you can use this key to [display the reCAPTCHA widget](#integrating-web-based-storefronts) on your storefront.

## Integrating reCAPTCHA on your storefront

See below instructions for integrating reCAPTCHA depending on whether you are implementing a [mobile](#integrating-mobile-apps) or [web-based storefront](#integrating-web-based-storefronts).

### Integrating mobile apps

See the documentation provided by Google to learn how to integrate reCAPTCHA v3 on your mobile app according to the mobile platform of your choice:

- [Android](https://cloud.google.com/recaptcha-enterprise/docs/instrument-android-apps)
- [iOS](https://cloud.google.com/recaptcha-enterprise/docs/instrument-ios-apps)

### Integrating web-based storefronts

Having obtained the reCAPTCHA key, you can apply validation on your storefront according to the version of reCAPTCHA you are using:

- reCAPTCHA v2: pass the `recaptchaKey` value you got as the `siteKey` property when displaying the validation widget as described in the [reCAPTCHA v2 documentation](https://developers.google.com/recaptcha/docs/display).
- reCAPTCHA v3: integrate the validation according to the instructions in the [reCAPTCHA v3 documentation](https://developers.google.com/recaptcha/docs/v3).

Since reCAPTCHA application may vary according to payment method, we recommend that the integration is prepared apply the validation after the payment selection step.

## Final validation

After the shopper successfully solves the validation, the integration should receive a response token. This token should be included in the API request that places the order, along with the `recaptchaKey` that was used, be it with the [orderForm transaction endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) or the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders). The example below works for both cases.

```json
{
    ...,
    "recaptchaKey": "5Lc5UOBTRDBDBLNo2iOCPG0q7JCUgHUerDIJEHR-",
    "recaptchaToken": "03AERD8Xp5arKO6-vS76sxlAFIMqCQwHOp2XTKO-DF7HcNZZVVZGJrCmHGIBCywHstiaoOpsdmAUp5pIRVD0hOwSydYvubdor45EmSH37QuBbD4qmKfjyatKTMLpsIfmXSy40kmooZ2_TZAlVH0jnKBH5avX1BdYM4qN2uihVPjlRI1RX6ze05PG3ZDn9RQmjqHLot5jDX16nSLMauiZgCqhFPPZaKXz5qNXi2irsuM6xDIfoju50wKp9fJkDmY5eyT4_1iqEVOYkGjMq8hAorY2B6KmaiqxOYWwOPwyrPYP1sFbELO2teGeFYCuxqjOSi7Zq22xEYqQhWGeFHmu4L0ydfhbk3cHnHEyYdQpr3gaG-wHK2dVI1cMD6MYYiLwDfxZ_LgdruW7O-fT12WZCtZhUrwrefaw53hQ"
}
```

>❗ The `recaptchaKey` you send must be the one used to display the challenge that was solved.

## Handling errors

The reCAPTCHA token is valid for only one attempt. So in case of error during validation, the widget has to be displayed again to the shopper, in order to get a new token. The key used to display the validation widget after the error may vary depending on the error and order placement method, as described below.

### orderForm transaction errors

In case of internal error (`status 500`), the widget has to be displayed using the `recaptchaKey` from the latest updated `orderForm`.

If validation fails (`status 403`), the API returns the same error `CHK0082` as mentioned above. Note that the `recaptchaKey` returned in the error may be different than the one used previously.

### Place order errors

In case of internal error (`status 500`), the widget has to be displayed again. The `recaptchaKey` that was used the first time may be used this time.

If validation with the [Place order endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) fails (`status 403`), the API returns the same error `CHK0082` as mentioned above. Note that the `recaptchaKey` returned in the error may be different than the one used previously. Be sure to use the latest one received.
