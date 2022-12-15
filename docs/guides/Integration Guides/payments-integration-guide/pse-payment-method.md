---
title: "PSE Payment Method"
slug: "pse-payment-method"
hidden: true
createdAt: "2022-05-18T19:17:21.588Z"
updatedAt: "2022-09-01T19:53:36.514Z"
---
This is a guide intended for those responsible for ​​integrating the [PSE payment method](xxxxx) in a VTEX store. As part of the order transaction flow, it is necessary to inform the connector that will process the payment which bank was selected by the customer.

To provide this information in a way that is frictionless to the shopper experience, follow the steps below:
1. Send banks and authentication information to VTEX.
2. Update the [List Payment Provider Manifest](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) or [List Payment Methods](https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods) API.
3. [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) configuration.
4. Update the payment connector.

## Send bank and authentication information

To start the PSE integration process, VTEX needs to receive information that will allow performing the necessary setting in API requests.

The following information should be sent to [VTEX](https://help.vtex.com/en/support):
- **GET Banks endpoint** used by you to list the banks available to the customer. It should include the response body and any additional information required. 
- **Authentication key information** required to perform the GET request call.

See below an example of the GET Banks endpoint that VTEX will make:
[block:code]
{
  "codes": [
    {
      "code": "curl --request GET \\\n--url https://{{providerPSEEndpoint}}/ \\\n--header 'Application: application/json' \\\n--header 'Content-type: application/json' \\\n--header 'auth-token: token'",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "If there are additional steps to build the auth-token, it should also be described."
}
[/block]
After that, VTEX expects a response body following the structure described below:
[block:code]
{
  "codes": [
    {
      "code": "'{\n “banks”:  [\n    {\n      “name”: “XXXX BANK”,\n      “code”:  “1111”\n    },\n   {\n      “name”: “YYYY BANK”,\n      “code”:  “2000”\n    },\n  {\n      “name”: “ZZZZ BANK”,\n      “code”:  “5555”\n    },\n  ]\n}'",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "The **GET Banks endpoint** is used whenever the PSE payment app is loaded at Checkout. In this way, when there is any modification in the endpoint (removal or addition of banks to the list), the information is automatically updated at Checkout, requiring no action from VTEX."
}
[/block]
## List Payment Provider Manifest / List Payment Methods API Update

After forwarding the banking and authentication information to VTEX, it will be necessary for the payment provider to update information in the API, so that the PSE is recognized as a payment method.

The below PSE information should be added in one of the two APIs bellow (according to your choice): 

- [List Payment Provider Manifest API](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) 

[block:code]
{
  "codes": [
    {
      "code": "{\n...\n\"paymentMethods\":[\n...\n{\n    \"name\": \"PSE\",\n    \"allowsSplit\": \"disabled\"\n},\n...\n]\n...\n}",
      "language": "json"
    }
  ]
}
[/block]
- [List Payment Methods API](https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods)

[block:code]
{
  "codes": [
    {
      "code": "{\n...\n\"paymentMethods\":[\n       \"PSE\",\n]\n...\n}",
      "language": "json"
    }
  ]
}
[/block]
## POST Creating Payment request configuration

The bank selected by the shopper will be sent to the connector on the authorization request in the following format:

[block:code]
{
  "codes": [
    {
      "code": "```\n…\n    \"metadata\": {\n        \"bankCode\": \"1051\"\n    },\n   \"transactionId\": \"xyz\",\n   \"paymentId\": \"xpt0\"\n…\n```\n",
      "language": "json"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "Use the `bankCode` attribute inside the metadata object to create the payment in the PSE and return the `paymentUrl` in order to redirect the buyer to the bank's authentication. Keep in mind that the metadata field can also be null, so the connector should also handle this case by throwing an error with the following error code: `PSE_CUSTOM_APP_NOT_FOUND`."
}
[/block]

The PSE payment method requires a pre-condition to be processed (bank selection by shopper) and it occurs in an external payment environment. Then, in addition to the fields present in a standard response body, you should use the following fields in the create payment response body:

- `status`: undefined
- `paymentUrl`: bank’s authentication page

For more information, check [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) documentation.
[block:callout]
{
  "type": "info",
  "body": "By selecting the PSE payment method at checkout, your customers will be redirected to the bank environment (page). There, they will complete the necessary authentication (specified according to the chosen bank). After that, there are two possible scenarios:\n- **Payment approved**: a page containing the order details is shown.\n- **Payment denied**: a page containing the specific error is shown."
}
[/block]
## Payment Connector Update

Request the payment connector update through the [VTEX Support Portal](https://help.vtex.com/support).

[block:callout]
{
  "type": "info",
  "body": "The [Get Bank endpoint](#send-bank-and-authentication-information) containing the list of banks must be sent when opening the ticket through the [VTEX Support Portal](https://help.vtex.com/support)."
}
[/block]