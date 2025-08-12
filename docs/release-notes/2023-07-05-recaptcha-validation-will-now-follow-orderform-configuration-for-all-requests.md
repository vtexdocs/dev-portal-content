---
title: "reCAPTCHA validation will now follow orderForm configuration for all requests"
slug: "2023-07-05-recaptcha-validation-will-now-follow-orderform-configuration-for-all-requests"
type: "improved"
excerpt: "Merchants that use the Checkout API to place orders from mobile apps and headless storefronts must review their integrations."
hidden: false
createdAt: "2023-07-05T15:54:00.000Z"
updatedAt: "2023-08-10T10:21:36.446Z"
---

To further protect our customers, VTEX will now enforce the reCAPTCHA orderForm configuration set in each account for all Checkout API requests, regardless of the roles associated with the user or API key.

Merchants that use the Checkout API to place orders from mobile apps, headless storefronts and similar applications must [review](#review-your-integrations) and [adjust](#adjust-your-integrations) their integrations before **September 1, 2023**.

## Review your integrations

First you should review your integrations that use the Checkout API to place orders to your VTEX store, using the following endpoints:

- [Place order from an existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction)
- [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders)

The diagram below can help you assess whether an integration needs to be adjusted, according to your store's [reCAPTCHA orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pvt/configuration/orderForm) and how requests made to these endpoints are [authenticated](https://developers.vtex.com/docs/guides/authentication-overview):

![reCAPTCHA diagram](https://images.ctfassets.net/alneenqid6w5/46F1byxPKdYgWcf1lSkPMn/077e3f3122263a78aaa5a4cf47bd9eb2/recaptcha-config-EN.png)

- **Case 1**: *No changes are required in the integration, but your store might be at risk.*

  Your store does not use reCAPTCHA at Checkout and is therefore vulnerable to automated attacks, unless other protective measures are implemented in your integration.

- **Case 2**: *You need to adjust your integration, otherwise it might stop working.*

  Your store uses reCAPTCHA at Checkout, but is not ready to display it correctly in the user interface. Your development team should [adjust your integrations](#adjust-your-integrations).

- **Case 3**: *No changes are required in the integration.*

  Your store uses reCAPTCHA at Checkout and is ready to display it correctly in the user interface. Congratulations for following best practices in security!

You must make sure that the [API key](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) used to make the requests to the [Place order from an existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) ("Transaction") / [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) ("PlaceOrder") endpoints of the Checkout API has one of these [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) in their [roles](https://help.vtex.com/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc):

- Checkout > CheckoutResources > Shopping Cart Full Access
- Catalog > Telesales > Assisted Sales

This includes [predefined roles](https://help.vtex.com/en/tutorial/predefined-roles--jGDurZKJHvHJS13LnO7Dy) like **Owner (Super Admin), Call center operator,** and **Checkout Admin,** as well as custom roles including either of those specific resources.

## Adjust your integrations

If your team identified that your integration requires attention, you must follow the instructions provided in the developer guide [Implementing reCAPTCHA in integrations](https://developers.vtex.com/docs/guides/implementing-recaptcha-in-integrations).

>⚠️ If you are implementing reCAPTCHA on a native mobile app, use reCAPTCHA v3. Otherwise, reCAPTCHA use v2.

Using the reCAPTCHA key returned by the Checkout, the reCAPTCHA widget should be rendered in the user interface of your mobile app/headless storefront (or similar) as described in the [reCAPTCHA v2](https://developers.google.com/recaptcha/docs/display) or [reCAPTCHA v3](https://developers.google.com/recaptcha/docs/v3) documentation provided by Google.

After the shopper has completed the reCAPTCHA challenge, their response (`recaptchaToken`) should be sent to the Checkout API to complete the purchase, as described in the *Final validation* section of [Implementing reCAPTCHA in integrations](https://developers.vtex.com/docs/guides/implementing-recaptcha-in-integrations#final-validation). Checkout API will then [verify the user's response](https://developers.google.com/recaptcha/docs/verify) using the provided token.

>❗ All integrations using Checkout API to place orders must be reviewed and adjusted before September 1, 2023. Applications that fail to render the reCAPTCHA widget and verify the user's response will not be able to place orders after this date.
