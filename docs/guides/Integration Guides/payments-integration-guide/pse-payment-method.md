---
title: "PSE Payment Method"
slug: "pse-payment-method"
hidden: true
createdAt: "2022-05-18T19:17:21.588Z"
updatedAt: "2022-05-19T12:53:08.865Z"
---
This is a guide intended for those responsible for ​​integrating the [PSE payment method](xxxxx) in a VTEX store. As part of the order transaction flow, it is necessary to inform the connector that will process the payment which bank was selected by the customer.

To provide this information in a way that is frictionless to the shopper experience, follow the steps below:
1. Send bank and authentication information to VTEX.
2. Update the [List Payment Provider Manifest](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) or [List Payment Methods](https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods) API.
3. [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) configuration.
4. Additional [GET orderForm](#get-orderform-request) request.
5. Request through the [VTEX Support Portal](https://help.vtex.com/support) for the payment connector update.

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
      "language": "text"
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
      "language": "text"
    }
  ]
}
[/block]
## List Payment Provider Manifest / List Payment Methods API Update

After forwarding the banking and authentication information to VTEX, it will be necessary to update information in the API, so that the PSE is recognized as a payment method.

The PSE information should be added in one of the two APIs below (according to your choice): 

- [List Payment Provider Manifest API](https://developers.vtex.com/vtex-developer-docs/reference/manifest-1) 

[block:code]
{
  "codes": [
    {
      "code": "{\n...\n\"paymentMethods\":[\n...\n{\n    \"name\": \"pse\",\n    \"allowsSplit\": \"disabled\"\n},\n...\n]\n...\n}",
      "language": "text"
    }
  ]
}
[/block]
- [List Payment Methods API](https://developers.vtex.com/vtex-developer-docs/reference/paymentmethods)

[block:code]
{
  "codes": [
    {
      "code": "{\n...\n\"paymentMethods\":[\n       \"pse\",\n]\n...\n}",
      "language": "text"
    }
  ]
}
[/block]
## POST Creating Payment request configuration

The PSE payment method requires a pre-condition to be processed (bank selection by shopper) and it occurs in an external payment environment. Then, in addition to the fields present in a standard response body, you should use the following fields in the create payment response body:

- `status`: undefined
- `paymentUrl`: bank’s authentication page

For more information, check [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) documentation.

## GET orderForm request 

During the order transaction flow, right after the [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) request, you need to make a new GET orderForm request (`https://{{merchant}}.vtexcommercestable.com.br/api/checkout/pub/orderForm/{{orderFormId}}`). The fields `merchant` and `orderFormId` used in this request are received from the [POST Create Payment](https://developers.vtex.com/vtex-rest-api/reference/createpayment) request body.

The GET orderForm request will return an object in the following format:

[block:code]
{
  "codes": [
    {
      "code": "```\n…\n    \"customData\": {\n        \"customApps\": [\n    …\n            {\n                \"fields\": {\n                    \"bankCode\": \"1051\"\n                },\n                \"id\": \"pse\",\n                \"major\": 1\n            }\n    …\n        ]\n    },\n…\n```",
      "language": "text"
    }
  ]
}
[/block]
For more information, check [orderForm Fields (customData)](https://developers.vtex.com/vtex-developer-docs/reference/orderform-fields#customdata).
[block:callout]
{
  "type": "warning",
  "body": "Use the `bankCode` attribute inside the customData object to create the payment in the PSE and return the `paymentUrl` in order to redirect the buyer to the bank's authentication. Keep in mind that the customData field can also be null, so the connector should also handle this case by throwing an error with the following error code: `PSE_CUSTOM_APP_NOT_FOUND`."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "By selecting the PSE payment method at checkout, your customers will be redirected to the bank environment (page). There, they will complete the necessary authentication (specified according to the chosen bank). After that, there are two possible scenarios:\n- <b>Payment approved</b>: a page containing the order details is shown.\n- <b>Payment denied</b>: a page containing the specific error is shown."
}
[/block]