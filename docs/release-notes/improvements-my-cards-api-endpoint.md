---
slug: "improvements-my-cards-api-endpoint"
title: "Improvements to the My Cards API endpoint"
createdAt: 2021-11-12T14:53:48.759Z
hidden: false
type: "improved"
---

![Commerce APIs](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/improvements-my-cards-api-endpoint-0.png)

Starting November 18, 2021, there will be critical improvements to the My Cards API endpoint:

```
POST
https://{accountName}.{environment}.com.br/api/checkout/pub/current-user/payment-tokens
```

This request is used when a customer registers a new credit card through the [My Cards page](https://help.vtex.com/en/tutorial/como-funciona-a-minha-conta--2BQ3GiqhqGJTXsWVuio3Xh#cartoes).

The most significant change is the requirement of [reCAPTCHA](https://developers.google.com/recaptcha/docs/display) validation, which dramatically reduces the likelihood of card attacks to this particular API path.

## What needs to be done

If your store uses our native UI in the [My Cards page](https://help.vtex.com/en/tutorial/como-funciona-a-minha-conta--2BQ3GiqhqGJTXsWVuio3Xh#cartoes), the change should happen automatically. In this case, we expect no action will be needed, but recommend you revise the page’s layout, to ensure it works properly.

Note that, in order to test this validation on your store, you must access it through the public address (without the `myvtex` environment), using a common user, without store administrator or developer privileges.

If your store uses any UI implementation that communicates directly with this API endpoint, such as proprietary sites or apps, get in touch with our [support](https://help.vtex.com/pt/support) so as to update your implementation accordingly.
