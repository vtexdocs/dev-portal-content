---
title: "PSE Payment Method"
slug: "pse-payment-method"
hidden: false
createdAt: "2022-05-18T19:17:21.588Z"
updatedAt: "2022-09-01T19:53:36.514Z"
excerpt: "Learn how payment providers can offer the PSE payment method in VTEX stores."
---
This guide is for payment  that want to offer [PSE (Pagos Seguros en Línea)](https://help.vtex.com/en/tutorial/setting-up-payments-with-pse--7dRChprovidersubn7TqdEyWrHQEQp6) as a payment method on VTEX stores. PSE is a Colombian online bank transfer method that uses the [redirect purchase flow](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#redirect).

During the order transaction, the connector must know which bank the customer selected. The integration requires the following steps:

1. Send bank list endpoint and authentication information to VTEX.
2. Update the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) to include PSE.
3. Handle the `bankCode` metadata in the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request.
4. Request the payment connector update through the [VTEX Support Portal](https://help.vtex.com/support).

> ⚠️ To integrate PSE, you must have a [partnership agreement for financial services](https://vtex.com/us-en/partners) with VTEX. If you do not have one, contact the [VTEX Support Portal](https://help.vtex.com/support).

## Step 1: Send bank and authentication information

VTEX needs access to your bank list endpoint to display available banks to the shopper at checkout. Submit the following information through [VTEX Support](https://help.vtex.com/en/support):

- **GET Banks endpoint:** the URL that returns the list of available banks. Include the expected response body format and any required parameters.
- **Authentication credentials:** any keys or tokens required to call the endpoint.

Example request that VTEX makes to your endpoint:

```bash
curl --request GET \
  --url https://{{providerPSEEndpoint}}/ \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --header 'auth-token: {{token}}'
```

> ⚠️ If the `auth-token` requires additional steps to generate (for example, an OAuth flow), describe the process when submitting your information.

Expected response body:

```json
{
  "banks": [
    {
      "name": "XXXX BANK",
      "code": "1111"
    },
    {
      "name": "YYYY BANK",
      "code": "2000"
    },
    {
      "name": "ZZZZ BANK",
      "code": "5555"
    }
  ]
}
```

## Step 2: Update the Payment Provider Manifest

Add PSE to the `paymentMethods` array in your [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) response:

```json
{
  "paymentMethods": [
    {
      "name": "PSE",
      "allowsSplit": "disabled"
    }
  ]
}
```

## Step 3: Handle the Create Payment request

When a shopper selects PSE and chooses a bank at checkout, VTEX sends the selected bank code in the `metadata` field of the [Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request:

```json
{
  "metadata": {
    "bankCode": "1051"
  },
  "transactionId": "D3AA1FC8372E430E8236649DB5EBD08E",
  "paymentId": "F5C1A4E20D3B4E07B7E871F5B5BC9F91"
}
```

Your connector must:

1. Read the `bankCode` from the `metadata` object.
2. Create the payment in PSE using the selected bank.
3. Return a response with:
   - `status`: `"undefined"` (since the payment requires redirect).
   - `paymentUrl`: the bank's authentication page URL where the shopper completes the payment.

> ⚠️ The `metadata` field can be `null` if the bank selection app is not properly configured. In this case, the connector must return an error with code `PSE_CUSTOM_APP_NOT_FOUND`.

## Step 4: Post-authentication flow

After the shopper is redirected to the bank's authentication page:

1. The shopper completes authentication at the selected bank.
2. The bank processes the transfer and returns the result to the provider.
3. The provider calls the `callbackUrl` (included in the original Create Payment request) to notify VTEX of the final status: `approved` or `denied`.
4. VTEX redirects the shopper back to the store using the `returnUrl`:
   - **Payment approved:** the order confirmation page is displayed.
   - **Payment denied:** an error page with the specific failure reason is displayed.

For more details on the redirect flow and callback mechanism, see [Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows#redirect).

## Next steps

After implementing the PSE integration, submit the connector for [homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation) to make it available to VTEX merchants.