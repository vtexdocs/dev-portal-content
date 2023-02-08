---
slug: "improvements-in-checkout-api-documentation"
title: "Improvements in Checkout API documentation"
createdAt: 2021-08-09T20:00:50.206Z
hidden: false
type: ""
---

![Commerce APIs](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/improvements-in-checkout-api-documentation-0.png)

We have made new Checkout endpoints available in our API documentation:

- [Create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm)
- [Get cart information by ID](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-)
- [Ignore profile data](https://developers.vtex.com/docs/api-reference/checkout-api#patch-/api/checkout/pub/orderForm/-orderFormId-/profile)
- [Add client profile](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientProfileData)
- [Add shipping address](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData)
- [Add client preferences](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientPreferencesData)
- [Add marketing data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/marketingData)
- [Add payment data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/paymentData)
- [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders)
- [Place order from existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/gatewayCallback/-orderGroup-)

Also, we have reorganized some of the existing endpoints. The new categories include:

- **Shopping cart**
  - Cart simulation
  - Create a new cart
  - Get cart information by ID
  - Remove all items
  - Remove all personal data
  - Update cart items
  - Change price
  - Ignore profile data

- **Cart attachments**
  - Add client profile
  - Add shipping address and select delivery option
  - Add client preferences
  - Add marketing data
  - Add payment data

- **Order placement**
  - Place order from existing cart
  - Place order
