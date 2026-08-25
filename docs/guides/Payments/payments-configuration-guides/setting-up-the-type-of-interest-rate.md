---
title: "Setting up the type of interest rate"
slug: "setting-up-the-type-of-interest-rate"
excerpt: "Learn how to define the interest calculation method of a payment condition with the Payments Gateway API, including the simple interest with tax option, which is unavailable in the VTEX Admin."
hidden: false
createdAt: "2022-01-27T14:33:58.199Z"
updatedAt: "2026-08-25T00:00:00.000Z"
---

When a payment condition offers installments with interest, the VTEX Payment Gateway uses the `interestRateMethod` field to calculate the amount of each installment. This field belongs to the `installmentOptions` object of the payment condition, which the Payments Gateway API refers to as a rule.

The field accepts the following values:

| Value | Interest calculation | Available in the VTEX Admin |
| ----- | -------------------- | --------------------------- |
| `null` or `0` | Compound interest, levied on the order total and on the interest accumulated between installments. This is the default value. | Yes |
| `1` | Simple interest with tax, levied on the order total and combined with the interest tax defined for each installment in `interestTax`. | No |
| `2` | Simple interest, levied only on the order total. | Yes |

Compound interest is the most common model in Brazil, while countries such as Argentina prefer simple interest. For a comparison between both models, see [How to choose the type of interest for a payment condition](https://help.vtex.com/en/docs/tutorials/how-to-choose-the-type-of-interest-for-a-payment-condition).

> ℹ️ The interest type selector in the VTEX Admin offers only compound interest (`0`) and simple interest (`2`). To set either of these values, follow [How to choose the type of interest for a payment condition](https://help.vtex.com/en/docs/tutorials/how-to-choose-the-type-of-interest-for-a-payment-condition). Use the following steps to set simple interest with tax (`1`), which is only available through the API.

## Before you begin

To complete the steps in this guide, you need the following:

- The name of your VTEX account, used in the request URL.
- An [API key](https://developers.vtex.com/docs/guides/api-authentication-using-api-keys) with the [License Manager resources](https://help.vtex.com/en/docs/tutorials/license-manager-resources) required by each endpoint:

| Endpoint | Product | Category | Resource |
| -------- | ------- | -------- | -------- |
| [Get payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/rules/-ruleId-) | PCI Gateway | Payment-Make Payments | **View Payment Data** |
| [Update payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#put-/api/pvt/rules/-ruleId-) | PCI Gateway | Payment-ManageStore | **Manage Store** |

> ❗ No [predefined role](https://help.vtex.com/en/docs/tutorials/predefined-roles) grants these resources. [Create a custom role](https://help.vtex.com/en/docs/tutorials/creating-roles) with the resources in the preceding table, and follow the [best practices for managing API keys](https://help.vtex.com/en/docs/tutorials/best-practices-api-keys) to avoid granting excessive permissions.

## Step 1: Get the payment condition ID

1. In the VTEX Admin, go to **Store Settings > Payment > Settings**, or type **Settings** in the search bar at the top of the page.
2. Click the **Payment Conditions** tab.
3. Select the payment condition you want to configure.
4. Copy the last parameter of the page URL, which is the ID of the payment condition, as shown in the following image.

![Payment condition settings page in the VTEX Admin, with the payment condition ID highlighted at the end of the browser address bar.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-the-type-of-interest-rate-0.png)

This value corresponds to the `ruleId` path parameter in the following requests.

> ⚠️ The `ruleId` identifies the payment condition, not the payment method. A payment method such as Visa can have several payment conditions, each with its own `ruleId` and interest settings. Setting the interest rate type affects only the payment condition you send in the request.

## Step 2: Retrieve the payment condition

Send a [Get payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/rules/-ruleId-) request to retrieve the current configuration of the payment condition:

```sh
curl --request GET \
  --url https://{accountName}.vtexpayments.com.br/api/pvt/rules/{ruleId} \
  --header 'Accept: application/json' \
  --header 'X-VTEX-API-AppKey: {appKey}' \
  --header 'X-VTEX-API-AppToken: {appToken}'
```

Replace `{accountName}` with your account name, `{ruleId}` with the ID from the previous step, and `{appKey}` and `{appToken}` with your API key credentials.

A successful request returns the status code `200 OK` and the complete payment condition. The `installmentOptions` object holds the interest settings:

```json
{
  "dueDateType": 0,
  "interestRateMethod": null,
  "minimumInstallmentValue": 400,
  "installments": [
    {
      "ruleId": null,
      "quantity": 12,
      "value": 0,
      "interestRate": 25,
      "isExternalInstallmentService": null,
      "interestTax": 0
    }
  ]
}
```

Save the entire response body, as you need it to build the request in the next step.

## Step 3: Set the interest rate type

Send an [Update payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#put-/api/pvt/rules/-ruleId-) request using the response from the previous step as the request body, changing only the value of `interestRateMethod`:

```sh
curl --request PUT \
  --url https://{accountName}.vtexpayments.com.br/api/pvt/rules/{ruleId} \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'X-VTEX-API-AppKey: {appKey}' \
  --header 'X-VTEX-API-AppToken: {appToken}' \
  --data '{
  "id": "c997267e-39bf-4217-a890-a503f6a7dc47",
  "name": "Visa 12 installments with interest",
  "salesChannels": [
    {
      "id": "1"
    }
  ],
  "paymentSystem": {
    "id": 8,
    "name": "Visa",
    "implementation": null
  },
  "connector": {
    "implementation": "Vtex.PaymentGateway.Connectors.CieloV3Connector",
    "affiliationId": "0a8488e6-0c30-4150-be96-b0dcaaa6a0cd"
  },
  "issuer": null,
  "antifraud": null,
  "installmentOptions": {
    "dueDateType": 0,
    "interestRateMethod": 1,
    "minimumInstallmentValue": 400,
    "installments": [
      {
        "ruleId": null,
        "quantity": 12,
        "value": 0,
        "interestRate": 25,
        "isExternalInstallmentService": null,
        "interestTax": 0
      }
    ]
  },
  "isSelfAuthorized": null,
  "requiresAuthentication": null,
  "enabled": true,
  "installmentsService": false,
  "isDefault": null,
  "condition": null,
  "multiMerchantList": [],
  "country": {
    "name": null,
    "isoCode": "br"
  },
  "externalInterest": false,
  "minimumValue": null,
  "deadlines": [],
  "excludedBinsRanges": null
}'
```

> ⚠️ This request replaces the entire payment condition. Any field omitted from the request body is overwritten with its default value, which can disable the payment condition or remove its installment settings. Always build the request body from the response you retrieved in the previous step, rather than from the preceding example.

A successful request returns the status code `200 OK` and the updated payment condition.

## Step 4: Check the configuration

1. Send a new [Get payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/rules/-ruleId-) request and confirm that `interestRateMethod` returns the expected value.
2. Place a test order in your store and confirm that the installment amounts displayed at checkout match the interest model you configured.

> ⚠️ The interest type selector in the VTEX Admin doesn't display simple interest with tax, and it hides the option to change the interest type when the payment condition uses this value. If you edit and save this payment condition in the VTEX Admin, check `interestRateMethod` again with [Get payment rule by ID](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/pvt/rules/-ruleId-) and repeat step 3 if the value changed.
