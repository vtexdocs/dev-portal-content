---
title: "Applicable cases"
slug: "applicable-cases"
hidden: false
createdAt: "2021-08-03T21:55:45.686Z"
updatedAt: "2022-05-10T14:01:46.295Z"
---
When a shopper places an order on your store paying with a credit or debit card, they may or may not be required to perform reCAPTCHA validation according to the criteria set in the [orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration).

The recommended configuration is `vtexCriteria`, which uses an algorithm to determine which sessions are trustworthy. This reduces the application of reCAPTCHA validation, improving security with no impact conversion.

Regardless of this configuration, reCAPTCHA verification will not be required in some cases:

- Fulfillment orders, meaning orders received through a marketplace, in which your store is responsible only for the fulfillment. In this case, reCAPTCHA validation is applied in the marketplace where the order was made by the shopper according to its own configuration.

- Orders made by authenticated administrator users, including [call center users](https://help.vtex.com/en/tutorial/how-can-i-create-callcenter-user--frequentlyAskedQuestions_4227#).

- Orders made through the private (`/pvt`) placeOrder API endpoint, which is commonly used by integrations and authenticated with appKey and appToken.

- Orders where payment does not include a debit or credit card.