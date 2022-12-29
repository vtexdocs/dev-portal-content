---
title: "Setting up the type of interest rate"
slug: "setting-up-the-type-of-interest-rate"
hidden: false
createdAt: "2022-01-27T14:33:58.199Z"
updatedAt: "2022-02-03T16:47:43.820Z"
---

## Identifying the payment method's ID

The payment method's ID can be configured to have Simple Interest Rates and is obtained by following these steps:

1. Access the **Admin VTEX**.
2. Click on **Payments**.
3. Then, click on **Settings**.
4. In **Payment Conditions** tab, select the payment condition that should be configured to use Simple Interest Rates.
5. Copy the last URL parameter, which shows the ID of this Payment Method (see image).

![ENjuros](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/setting-up-the-type-of-interest-rate-0.png)

## Setting up the interest rate type using API

The `interestRateMethod` field is where the setup should be implemented, if we were to use the Simple Interest Rate or Compound Interest Rate calculation algorithm:

- **Simple Interest Rate** will equal `interestRateMethod`: 1.
- **Compound Interest Rate** will equal `interestRateMethod`: null.

A `GET Rule by ID` call will initially be sent in order to receive the updated Payment Method setting through the following API:

[https://developers.vtex.com/vtex-rest-api/reference/rulebyid](https://developers.vtex.com/vtex-rest-api/reference/rulebyid)

The reply that the `GET Rule by ID` call returns will be the request of the thereafter `POST Rule by ID` call. To save the new configuration, only the value `interestRateMethod`:1 should be modified:

[https://developers.vtex.com/vtex-rest-api/reference/putrulebyid](https://developers.vtex.com/vtex-rest-api/reference/putrulebyid)
>❗ At present, the only way to change a payment method is through API. Should it be necessary to change the payment method by using the user interface, the setup process through API would have to be repeated, since when saving the changes, the value will be considered empty by default.
