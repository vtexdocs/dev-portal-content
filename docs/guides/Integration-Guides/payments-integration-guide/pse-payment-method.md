---
title: "PSE Payment Method"
slug: "pse-payment-method"
hidden: true
createdAt: "2022-05-18T19:17:21.588Z"
updatedAt: "2022-09-01T19:53:36.514Z"
---
This is a guide intended for payment providers that want to offer [PSE payment method](https://help.vtex.com/en/tutorial/setting-up-payments-with-pse--7dRChubn7TqdEyWrHQEQp6) in a VTEX store. As part of the order transaction flow, it is necessary to inform the connector that will process the payment which bank was selected by the customer.

To provide this information in a way that is frictionless to the shopper experience, follow the steps
below:

1. Send banks and authentication information to VTEX.
2. Update the [List Payment Provider Manifest](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest) API.
3. [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) configuration.
4. Request through the [VTEX Support Portal](https://help.vtex.com/support) for the payment connector update.

>⚠️ To carry out the integration of the PSE, it is necessary to have a partnership contract with VTEX. If you do not have the contract, access [VTEX Support Portal](https://help.vtex.com/support).


## Send bank and authentication information

To start the PSE integration process, VTEX needs to receive information that will allow performing the necessary setting in API requests.

The following information should be sent to [VTEX](https://help.vtex.com/en/support):
- **GET Banks endpoint** used by you to list the banks available to the customer. It should include the response body and any additional information required. 
- **Authentication key information** required to perform the GET request call.

See below an example of the GET Banks endpoint that VTEX will make:

```json
curl --request GET \
--url https://{{providerPSEEndpoint}}/ \
--header 'Application: application/json' \
--header 'Content-type: application/json' \
--header 'auth-token: token'
```

>⚠️ If there are additional steps to build the auth-token, it should also be described.

After that, VTEX expects a response body following the structure described below:

```json
{
 "banks":  [
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
      "code":  "5555"
    },
  ]
}
```

## List Payment Provider Manifest API Update

After forwarding the banking and authentication information to VTEX, it will be necessary for the payment provider to update information in the API, so that the PSE is recognized as a payment method.

The following PSE information should be added on [List Payment Provider Manifest API](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).

```json
{
...
"paymentMethods":[
...
{
    "name": "PSE",
    "allowsSplit": "disabled"
},
...
]
...
}
```

## POST Creating Payment request configuration

The bank selected by the shopper will be sent to the connector on the authorization request in the following format:

```json
...
    "metadata": {
        "bankCode": "1051"
    },
    "transactionId": "xyz",
    "paymentId": "xpt0"
...
```

>⚠️ Use the `bankCode` attribute inside the metadata object to create the payment in the PSE and return the `paymentUrl` in order to redirect the buyer to the bank's authentication. Keep in mind that the metadata field can also be <i>null</i>, so the connector should also handle this case by throwing an error with the following error code: `PSE_CUSTOM_APP_NOT_FOUND`.

The PSE payment method requires a pre-condition to be processed (bank selection by shopper) and it occurs in an external payment environment. Then, in addition to the fields present in a standard response body, you should use the following fields in the create payment response body:

- `status`: undefined
- `paymentUrl`: bank’s authentication page

For more information, check [POST Create Payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) documentation.

> ℹ️ By selecting the PSE payment method at checkout, your customers will be redirected to the bank environment (page). There, they will complete the necessary authentication (specified according to the chosen bank). After that, there are two possible scenarios: **Payment approved** (a page containing the order details is shown) or **Payment denied** (a page containing the specific error is shown).
