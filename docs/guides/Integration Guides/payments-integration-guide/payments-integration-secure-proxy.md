---
title: "Secure Proxy"
slug: "payments-integration-secure-proxy"
hidden: false
createdAt: "2022-02-15T20:28:58.081Z"
updatedAt: "2022-11-03T18:14:40.007Z"
---

Secure Proxy is a solution that allows payment integrations to transfer sensitive data (i.e.: credit card numbers) in a secure environment. An integration must use Secure Proxy if it meets the following conditions:

- It uses credit, debit, or cobranded cards as payment methods
- The environment where the connector is hosted does not have an [Attestation of Compliance (AOC) of PCI - DSS (Payment Card Industry - Data Security Standard)](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance)

When an integration is PCI compliant, it does not need to use Secure Proxy, being allowed to receive sensitive data and communicate directly with the acquirer. When using Secure Proxy, the following changes occur in the flow of the integration:

1. The Authorization request works as usual.
2. The provider receives tokens from VTEX’s Payments Gateway that refers to the sensitive data, instead of the actual data.
3. The provider sends the API endpoint of the acquirer and the merchant credentials to the Gateway.
4. The Gateway makes the API call to the acquirer, acting as a proxy between the provider and the acquirer. In this call, the tokens are replaced by sensitive data.
   ![Secure Proxy simplified flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/payments-integration-guide/a68e6b6-Secure_Proxy_simplified_flow_diagram_19.png)

## What is PCI DSS and how is it used in VTEX?

PCI DSS is an international standard for how companies must process card information. Among the many rules of this standard is an important one that states that card information must be transferred in a secure infrastructure that has been audited by a [QSA (Qualified Security Assessors) Company](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors), which are qualified by the PCI Security Standards Council.

VTEX’s Payments Gateway service is certified by this entity to process sensitive card information, and this information can only be transferred in a secure environment in which services and partners have an AOC signed by a QSA Company. Security measures needed to meet the PCI DSS requirements include, but are not limited to the use of a firewall, encrypt the transmission of cardholder data, use of updated anti-virus, restrict access to cardholder data with authentication and monitor all access to network resources. More information about PCI DSS requirements can be found in the [PCI DSS Quick Reference Guide](https://www.pcisecuritystandards.org/documents/PCI_DSS-QRG-v3_2_1.pdf).

## Why use Secure Proxy?

Not all of VTEX’s payment ecosystem (partners and clients) have PCI DSS certification, which is required for our Payments Gateway to send card information. Besides, the VTEX IO platform is a development environment designed to accelerate the creation of new solutions for our ecosystem and we want to enable it to create payment solutions as well.

Considering that the integration environment is fundamental for a transaction to take place based on business rules about how a payment should be processed, a solution is necessary to address the scenarios in which the integration environment is not certified by PCI requirements. Therefore, Secure Proxy comes as a solution to enable new integration scenarios with VTEX’s payment partner ecosystem.

Through this solution, the Payments Gateway acts as a communication service between a payment provider in a non-PCI environment and an acquirer. The Payments Gateway sends tokenized card information to the payment provider without the risk of compromising data security. The tokens are used to replace sensitive information in the provider and to act as a reference to the information in the Gateway.

When a system does not meet all the security requirements, it might be vulnerable to attacks and data theft. This can lead to serious consequences including fraud losses, loss of confidence from customers, reduction in sales, legal costs, fines, etc. More information about these security issues can be found in the PCI article [Why Security Matters](https://www.pcisecuritystandards.org/pci_security/why_security_matters). By meeting the requirements of PCI DSS, those issues and their consequences can be avoided.

[block:callout]
{
  "type": "info",
  "body": "Secure Proxy is mandatory for connectors built with the VTEX IO infrastructure since it is not compliant with PCI DSS. This also includes connectors made through our [Payment Provider Framework](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-payment-provider-framework)."
}
[/block]

## How it works

In this section, we detail how the solution works in a payment authorization flow. The image below shows an overview of the flow containing the Secure Proxy, as well as the four steps required for the payment to be authorized by the acquirer.
![Secure Proxy detailed flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/payments-integration-guide/3e0fbfa-Secure_Proxy_detailed_flow_44.png)

### 1. Checkout submits a payment authorization request to the Gateway

There is no change to the current flow. The Checkout makes an [Authorization request](https://developers.vtex.com/vtex-rest-api/reference/4doauthorization) to the Gateway.

### 2. Gateway requests the provider to create a new payment using tokens

The Gateway makes a [Create Payment request](https://developers.vtex.com/vtex-rest-api/reference/createpayment) to the provider. The provider is responsible for receiving all the payment requests from the Gateway (creation, authorization, capture and cancel), regardless of using the Secure Proxy or not, and will use the defined settings in the integration including maximum time to cancel a transaction, supported payment methods, etc.

Below is an example of a payment creation request using a non-PCI payment provider. In this solution, there is a `secureProxyUrl` field containing the API that the payment provider must call when communicating with the acquirer. In addition, all sensitive card information has been tokenized by the Gateway.

**Request body**

```json
{
  ...,
  "secureProxyUrl": "https://account.vtexpayments.com.br/.../proxy",
  "card": {
    "holderToken": "#vtex#token#d799bae#holder#",
    "bin": "555544",
    "numberToken": "#vtex#token#d799bae#number#",
    "numberLength": 16,
    "cscToken": "#vtex#token#d799bae#csc#",
    "cscLength": 3,
    "expiration": {
      "month": "02",
      "year": "2028"
    }
  }
}
```

The response body for this request can be seen in our [API Reference](https://developers.vtex.com/vtex-rest-api/reference/createpayment#response-body).

### 3. Provider calls the Gateway to use the Secure Proxy

The provider makes a POST `https://account.vtexpayments.com.br/.../proxy` call to the Gateway. This is the endpoint provided in the `secureProxyUrl` field. This step occurs as follows:

1. The payment provider creates the object that will be sent to the acquirer using the tokenized data submitted by the Gateway in the corresponding fields. For this request to be transferred to the acquirer, you must submit the URL you would like to use in the `X-PROVIDER-Forward-To` header. Once this is done, the Gateway will:
   1. Verify if the URL is in the list of PCI-certified URLs.
   2. Replace the tokens placed in the card fields.
   3. Submit the request to the acquirer.
2. In case custom headers must be submitted to the acquirer, add `X-PROVIDER-Forward-` as a prefix, for instance `X-PROVIDER-Forward-MerchantId`. The Gateway will remove the prefix and submit the headers.
3. The response body will be forwarded from the external gateway or acquirer to the payment provider.

#### Possible response errors

The possible known errors are:

- **Error 400:** the submission URL is not specified in the header.
- **Error 400:** the integration transfers data not recognized by the Payments Gateway in the tokenized fields (`holderToken`, `numberToken`, `cscToken`).
- **Error 403:** the submission URL of the request is not allowed.
- **Error 500:** the Gateway cannot respond due to an internal failure.

The external gateway or acquirer also can respond with their own 4XX or 5XX errors.
[block:callout]
{
  "type": "warning",
  "body": "You must open a ticket asking to add the acquirer’s endpoint (the one used in the `X-PROVIDER-Forward-To` header) in the VTEX’s allowed list of endpoints along with the [AOC](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance#attestation-of-compliance-for-onsite-assessments-aoc) of the acquirer. If a request is made to the acquirer’s endpoint and it is not on the allowed list, it will result in an error."
}
[/block]
**Request header**

```
Accept: application/json
Content-Type: application/json
User-Agent: HttpClient-1.0
X-PROVIDER-Forward-To: https://apisandbox.acquirer.com/v2/sales/
X-PROVIDER-Forward-MerchantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
X-PROVIDER-Forward-MerchantKey: 012345678901234567890123456789012345678
```

[block:callout]
{
  "type": "warning",
  "body": "Requests to the PCI Proxy only accept two options for Content-Types: `application/json` or `application/x-www-form-urlencoded`. Other Content-Type options are not supported, but if you need any other for an integration you can share your use case with the product team by [opening a ticket to the VTEX support team](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM)."
}
[/block]
**Request body**

```json
{
   "MerchantOrderId": "123456789",
   "Customer": { ... },
   "Payment": {
      ...,
      "CreditCard": {
         "Holder": "#vtex#token#d799bae#holder#",
         "CardNumber": "#vtex#token#d799bae#number#",
         "ExpirationDate": "02/2028",
         "SecurityCode": "#vtex#token#d799bae#csc#",
         ...
      },
      "Credentials": { ... }
}
```

[block:callout]
{
  "type": "warning",
  "body": "Secure Proxy only supports HTTP-API (REST) integrations, which means it does not support Webservice (SOAP) or any other type of communication protocol."
}
[/block]

### 4. Requests for external gateways or acquirers in a PCI environment

An example request that the Gateway will submit to the acquirer: POST <https://apisandbox.acquirer.com/v2/sales/>\*

**Request header**

```
Accept: application/json
Content-Type: application/json
User-Agent: HttpClient-1.0
MerchantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MerchantKey: 012345678901234567890123456789012345678

```

Default headers:

- Accept
- Content-Type
- User-Agent

Custom headers:

- MerchantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- MerchantKey: 012345678901234567890123456789012345678

**Request body**

```json
{
   "MerchantOrderId": "123456789",
   "Customer": { ... },
   "Payment": {
      ...,
      "CreditCard": {
         "Holder": "JOHN DOE",
         "CardNumber": "5555444433331111",
         "ExpirationDate": "02/2028",
         "SecurityCode": "123",
         ...
      },
      "Credentials": { ... }
}
```

[block:callout]
{
  "type": "info",
  "body": "This request has a timeout of 15 seconds. It means that the Gateway will wait 15 seconds for the response of the acquirer and respond back to the payment provider."
}
[/block]

## Custom Tokens

As illustrated in the example above, card fields are the most often used tokens. However, the Secure Proxy also supports the creation and usage of custom tokens. This is done via the `secureProxyTokensURL` field, which is included by the Gateway in the request body of [Create Payment request](https://developers.vtex.com/vtex-rest-api/reference/createpayment) to the payment provider. The field contains the path to the endpoint that allows dealing with custom tokens.

In the following examples, the `secureProxyTokensURL` field will have the value  `https://{{account}}.vtexpayments.com.br/payment-provider/transactions/{{transactionId}}/payments/{{paymentId}}/tokens?hash={{longSecureHash}}`.

### Access Tokens

The list of all tokens created for a payment can be fetched via a GET request to the `secureProxyTokensURL`. By default, the list will only include the immutable credit card information tokens (`number`, `holder` and `csc`) created by the Gateway.

**Response body**

```json
{
  "tokens": [
    {
      "name": "number",
      "placeholder": "#vtex#number#{secureHash}#"
    },
    {
      "name": "holder",
      "placeholder": "#vtex#holder#{secureHash}#"
    },
    {
      "name": "csc",
      "placeholder": "#vtex#csc#{secureHash}#"
    }
  ]
}
```

The `secureHash` is a short string used for authentication during the access to a specific payment within the Secure Proxy, such as `d799bae`, as previously illustrated in [this example](#2-gateway-requests-the-provider-to-create-a-new-payment-using-tokens).

### Create custom tokens

New tokens can be created via a POST request to the `secureProxyTokensURL`. After being created, these can be referenced inside requests to the Secure Proxy and will be replaced by their values before the requests are forwarded to the acquirer.
[block:callout]
{
  "type": "info",
  "body": "Custom tokens allow, for example, the creation of tokens whose values are derived from credit card information."
}
[/block]
The creation request should include a list of tokens to be created, where each one consists of a `name` and a `value`. The first will be included in the placeholder used to reference the token (as mentioned above) and the second will be a [JsonLogic](https://jsonlogic.com/) expression that describes its value. In the `value` field for each token in the request body, every string must be encoded in the UTF-8 format.

**Request body**

```json
{
  "tokens": [
    {
      "name": "newToken",
      "value": { "==": [1, 1] }
    },
    {
      "name": "hashedCardNumber",
      "value": {
        "md5": {
          "replaceTokens": ["#vtex#number#{secureHash}#"]
        }
      }
    }
  ]
}
```

In the example request above, two new tokens are created.

- The first token is created from a simple expression and its value is evaluated to be true.
- The second token has an expression that uses [custom Secure Proxy operators](#custom-supported-operators) to compute the MD5 hash of the card number. This is done by detokenizing the card number token with the `replaceTokens` operator and then applying the MD5 operator to the result.

**Response body**

```json
{
  "tokens": [
    {
      "name": "newToken",
      "placeholder": "#vtex#newToken#{secureHash}#"
    },
    {
      "name": "hashedCardNumber",
      "placeholder": "#vtex#hashedCardNumber#{secureHash}#"
    }
  ]
}
```

The response consists of a list of the tokens that were created. The `placeholder` can then be used inside requests to the Secure Proxy to reference the values specified by the expression of the token.
[block:callout]
{
  "type": "info",
  "body": "A `placeholder` can be referenced in the body or as a header in a request to the Secure Proxy."
}
[/block]

#### Custom supported operators

Aside from the [default JsonLogic operators](https://jsonlogic.com/operations.html), the Secure Proxy also provides support to the following operators:

- `replaceTokens`: given a string, replaces the tokens in it by their respective values.
- `hmac-sha256`: given two UTF-8 encoded string arguments, computes the [HMAC-SHA256](https://datatracker.ietf.org/doc/html/rfc4868) hash considering the first string argument as the *key* and the second as the *data* to be hashed. The default result is [Base64-encoded](https://developer.mozilla.org/en-US/docs/Glossary/Base64) by default.
  - Optionally, a third parameter may be specified to choose the desired format of the output. The available options are `"base64"` (default) and `"hex"`.
  - Also optionally, a fourth parameter can be specified to choose the format of the key. The available options are `“plainText”` (default), `"hex”` and `"base64”`.
- Other hashing operators: `md5`, `sha1`, `sha256`, `sha384`, `sha512`.
  - Given a string, it computes the hash and returns the hex digest.
  - For these hashing operators, the result is the hex digest.
  - These hashing operators also have a second optional parameter to enable the user to choose the desired output to be a Hex digest output or a Base64 output. The parameter is case-insensitive and, if it is used, then it must be the string `"hex"` or the string `"base64"`. If the optional parameter is not used, the default output is the hex digest.

Example of the creation of a token named `"example-signature"` with a `hmac-sha256` hash as its value:

```json
{
  "tokens":[
    {
      "name":"example-signature",
      "value":{
        "hmac-sha256":[
          "this-is-the-key-value",
          "this-is-the-data-value",
          "this-is-the-optional-parameter-output-format",
          "this-is-the-optional-parameter-key-format"
        ]
      }
    }
  ]
}
```

Example of the creation of a token named `"example-signature-2"` with a MD5 hash as its value:

```json
{
  "tokens":[
    {
      "name":"example-signature-2",
      "value":{
        "md5":[
          "this-is-the-data-value",
          "this-is-the-optional-parameter-base64-or-hex-output"
        ]
      }
    }
  ]
}
```

### Known issues

The operator `cat` from the JSONLogic lib may misbehave when concatenating dates. It may change the date format.
