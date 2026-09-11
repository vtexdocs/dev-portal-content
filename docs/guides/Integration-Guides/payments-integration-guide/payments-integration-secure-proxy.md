---
title: "Secure Proxy"
slug: "payments-integration-secure-proxy"
excerpt: "Learn how Secure Proxy allows payment connectors hosted in non-PCI environments to transfer sensitive card data securely."
hidden: false
createdAt: "2022-02-15T20:28:58.081Z"
updatedAt: "2026-09-10T00:00:00.000Z"
---

Secure Proxy is a solution that allows payment integrations to transfer sensitive data (such as credit card numbers) in a secure environment. An integration must use Secure Proxy if it meets the following conditions:

- It uses credit, debit, or cobranded cards as payment methods.
- The environment where the connector is hosted doesn't have an [Attestation of Compliance (AOC) for PCI DSS (Payment Card Industry Data Security Standard)](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance).

When an integration is PCI compliant, it doesn't need to use Secure Proxy, being allowed to receive sensitive data and communicate directly with the acquirer. When using Secure Proxy, the following changes occur in the flow of the integration:

1. The Authorization request works as usual.
2. The provider receives tokens from VTEX’s Payments Gateway that refer to the sensitive data, instead of the actual data.
3. The provider sends the API endpoint of the acquirer and the merchant credentials to the Gateway.
4. The Gateway makes the API call to the acquirer, acting as a proxy between the provider and the acquirer. In this call, the tokens are replaced by sensitive data.

   ![Diagram of the simplified Secure Proxy flow between the Gateway, the payment provider, and the acquirer](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-secure-proxy-0.png)

## PCI DSS at VTEX

PCI DSS is an international standard for how companies must process card information. Among the many rules of this standard is an important one that states that card information must be transferred in a secure infrastructure that has been audited by a [Qualified Security Assessor (QSA) company](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors), which is qualified by the PCI Security Standards Council.

VTEX’s Payments Gateway service is certified by this entity to process sensitive card information, and this information can only be transferred in a secure environment in which services and partners have an AOC signed by a QSA company. Security measures needed to meet the PCI DSS requirements include, but aren't limited to, using a firewall, encrypting the transmission of cardholder data, keeping antivirus software updated, restricting access to cardholder data with authentication, and monitoring all access to network resources. For more information about PCI DSS requirements, including the current version of the Quick Reference Guide, see the [PCI DSS standard page](https://www.pcisecuritystandards.org/standards/pci-dss/).

## Reasons to use Secure Proxy

Not all of VTEX’s payment ecosystem (partners and clients) have PCI DSS certification, which is required for our Payments Gateway to send card information. Besides, the VTEX IO platform is a development environment designed to accelerate the creation of new solutions for our ecosystem and we want to enable it to create payment solutions as well.

Considering that the integration environment is fundamental for a transaction to take place based on business rules about how a payment should be processed, a solution is necessary to address the scenarios in which the integration environment isn't certified by PCI requirements. Therefore, Secure Proxy comes as a solution to enable new integration scenarios with VTEX’s payment partner ecosystem.

Through this solution, the Payments Gateway acts as a communication service between a payment provider in a non-PCI environment and an acquirer. The Payments Gateway sends tokenized card information to the payment provider without the risk of compromising data security. The tokens are used to replace sensitive information in the provider and to act as a reference to the information in the Gateway.

When a system doesn't meet all the security requirements, it might be vulnerable to attacks and data theft. This can lead to serious consequences, including fraud losses, loss of customer confidence, reduced sales, legal costs, and fines. For more information about these security issues, see the [PCI Security Standards Council resources for merchants](https://www.pcisecuritystandards.org/merchants/). By meeting the requirements of PCI DSS, those issues and their consequences can be avoided.

> ℹ️ Secure Proxy is mandatory for connectors built with the VTEX IO infrastructure since it isn't compliant with PCI DSS. This also includes connectors made through our [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework).

## How it works

This section details how the solution works in a payment authorization flow. The following image shows an overview of the flow containing the Secure Proxy, as well as the four steps required for the payment to be authorized by the acquirer.

![Diagram of the four steps of the Secure Proxy authorization flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/payments-integration-secure-proxy-1.png)

### 1. Checkout submits a payment authorization request to the Gateway

There is no change to the current flow. The Checkout makes an [Authorize new transaction](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/authorization-request) request to the Gateway.

### 2. Gateway requests the provider to create a new payment using tokens

The Gateway makes a [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request to the provider. The provider is responsible for receiving all the payment requests from the Gateway (creation, authorization, capture, and cancellation), whether or not it uses the Secure Proxy, and uses the settings defined in the integration, such as the maximum time to cancel a transaction and the supported payment methods.

The following example shows a payment creation request using a non-PCI payment provider. In this solution, there is a `secureProxyUrl` field containing the API that the payment provider must call when communicating with the acquirer. In addition, all sensitive card information has been tokenized by the Gateway.

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

For the response body of this request, see the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) endpoint reference.

### 3. Provider calls the Gateway to use the Secure Proxy

The provider makes a POST `https://account.vtexpayments.com.br/.../proxy` call to the Gateway. This is the endpoint provided in the `secureProxyUrl` field. This step occurs as follows:

1. The payment provider creates the object to be sent to the acquirer, using the tokenized data submitted by the Gateway in the corresponding fields. To have the request transferred to the acquirer, the provider submits the target URL in the `X-PROVIDER-Forward-To` header. The Gateway then does the following:
   1. Verifies if the URL is in the list of PCI-certified URLs.
   2. Replaces the tokens placed in the card fields.
   3. Submits the request to the acquirer.
2. To submit custom headers to the acquirer, the provider adds the `X-PROVIDER-Forward-` prefix to each one, for instance `X-PROVIDER-Forward-MerchantId`. The Gateway removes the prefix and submits the headers.
3. The response body is forwarded from the external gateway or acquirer to the payment provider.

#### Possible response errors

The possible known errors are:

- **Error 400:** The submission URL isn't specified in the header.
- **Error 400:** The integration transfers data not recognized by the Payments Gateway in the tokenized fields (`holderToken`, `numberToken`, `cscToken`).
- **Error 403:** The submission URL of the request isn't allowed.
- **Error 500:** The Gateway can't respond due to an internal failure.

The external gateway or acquirer can also respond with their own 4XX or 5XX errors.

> ⚠️ You must [open a ticket](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support) requesting that the acquirer’s endpoint (the one used in the `X-PROVIDER-Forward-To` header) be added to VTEX’s allowed list of endpoints, along with the [AOC](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance#attestation-of-compliance-for-onsite-assessments-aoc) of the acquirer. If a request is made to the acquirer’s endpoint and it isn't on the allowed list, the request results in an error.

**Request header**

```text
Accept: application/json
Content-Type: application/json
User-Agent: HttpClient-1.0
X-PROVIDER-Forward-To: https://apisandbox.acquirer.com/v2/sales/
X-PROVIDER-Forward-MerchantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
X-PROVIDER-Forward-MerchantKey: 012345678901234567890123456789012345678
```

> ⚠️ Requests to the Secure Proxy only accept two options for `Content-Type`: `application/json` or `application/x-www-form-urlencoded`. Other `Content-Type` options aren't supported. If your integration needs a different one, share your use case with the product team by [opening a ticket to the VTEX support team](https://help.vtex.com/en/docs/tutorials/opening-tickets-to-vtex-support).

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
}
```

> ⚠️ Secure Proxy only supports HTTP-API (REST) integrations, which means it doesn't support Webservice (SOAP) or any other type of communication protocol.

### 4. Requests for external gateways or acquirers in a PCI environment

An example request that the Gateway submits to the acquirer: POST `https://apisandbox.acquirer.com/v2/sales/`.

**Request header**

```text
Accept: application/json
Content-Type: application/json
User-Agent: HttpClient-1.0
MerchantId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MerchantKey: 012345678901234567890123456789012345678
```

The request includes the following default headers:

- `Accept`
- `Content-Type`
- `User-Agent`

It also includes the custom headers sent by the provider, with the `X-PROVIDER-Forward-` prefix removed:

- `MerchantId`
- `MerchantKey`

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
}
```

> ℹ️ This request has a timeout of 15 seconds. This means the Gateway waits 15 seconds for the acquirer’s response before responding to the payment provider.

## Custom tokens

As shown in the preceding examples, card fields are the most often used tokens. However, the Secure Proxy also supports the creation and usage of custom tokens. This is done via the `secureProxyTokensURL` field, which is included by the Gateway in the request body of the [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments) request to the payment provider. The field contains the path to the endpoint that allows dealing with custom tokens.

In the following examples, the `secureProxyTokensURL` field has the value `https://{accountName}.vtexpayments.com.br/payment-provider/transactions/{transactionId}/payments/{paymentId}/tokens?hash={longSecureHash}`.

### Accessing tokens

To fetch the list of all tokens created for a payment, send a GET request to the `secureProxyTokensURL`. By default, the list only includes the immutable credit card information tokens (`number`, `holder`, and `csc`) created by the Gateway.

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

The `secureHash` is a short string used to authenticate access to a specific payment within the Secure Proxy, such as `d799bae`, as shown in [Gateway requests the provider to create a new payment using tokens](#2-gateway-requests-the-provider-to-create-a-new-payment-using-tokens).

### Creating custom tokens

To create tokens, send a POST request to the `secureProxyTokensURL`. After you create them, you can reference these tokens inside requests to the Secure Proxy, and they are replaced with their values before the requests are forwarded to the acquirer.

> ℹ️ Custom tokens allow, for example, the creation of tokens whose values are derived from credit card information.

The creation request must include a list of tokens to be created, where each one consists of a `name` and a `value`. The `name` is included in the placeholder used to reference the token, and the `value` is a [JsonLogic](https://jsonlogic.com/) expression that describes it. In the `value` field for each token in the request body, every string must be encoded in the UTF-8 format.

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

The preceding request creates two new tokens:

- The first token is created from a simple expression, and its value evaluates to `true`.
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

> ℹ️ A `placeholder` can be referenced in the body or as a header in a request to the Secure Proxy.

#### Custom supported operators

Aside from the [default JsonLogic operators](https://jsonlogic.com/operations.html), the Secure Proxy also supports the following operators:

- `replaceTokens`: Given a string, replaces the tokens in it with their respective values.
- `base64`: Given a string, encodes it in Base64.
- `hmac-sha256`: Given two UTF-8 encoded string arguments, computes the [HMAC-SHA256](https://datatracker.ietf.org/doc/html/rfc4868) hash, considering the first string argument as the *key* and the second as the *data* to be hashed. The result is [Base64-encoded](https://developer.mozilla.org/en-US/docs/Glossary/Base64) by default.
  - Optionally, a third parameter may be specified to choose the desired format of the output. The available options are `"base64"` (default) and `"hex"`.
  - Also optionally, a fourth parameter can be specified to choose the format of the key. The available options are `"plainText"` (default), `"hex"`, and `"base64"`.
- Other hashing operators: `md5`, `sha1`, `sha256`, `sha384`, `sha512`.
  - Given a string, these operators compute the hash and return the hex digest.
  - These operators also have a second optional parameter that lets you choose between a hex digest output and a Base64 output. The parameter is case-insensitive and, if used, must be the string `"hex"` or the string `"base64"`. If the optional parameter isn't used, the default output is the hex digest.

The following example creates a token named `example-signature` with an `hmac-sha256` hash as its value:

```json
{
  "tokens": [
    {
      "name": "example-signature",
      "value": {
        "hmac-sha256": [
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

The following example creates a token named `example-signature-2` with an MD5 hash as its value:

```json
{
  "tokens": [
    {
      "name": "example-signature-2",
      "value": {
        "md5": [
          "this-is-the-data-value",
          "this-is-the-optional-parameter-base64-or-hex-output"
        ]
      }
    }
  ]
}
```

The following example creates a token named `example-base64` with a Base64-encoded string as its value:

```json
{
  "tokens": [
    {
      "name": "example-base64",
      "value": {
        "base64": [
          "string-to-be-encoded"
        ]
      }
    }
  ]
}
```

### Known issues

The `cat` operator from the [JsonLogic library](https://jsonlogic.com/operations.html) may misbehave when concatenating dates, changing the date format.

## Learn more

- [PCI DSS compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance)
- [Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol)
- [Payment Provider Framework](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-framework)
- [Payments Gateway API](https://developers.vtex.com/docs/api-reference/payments-gateway-api)
