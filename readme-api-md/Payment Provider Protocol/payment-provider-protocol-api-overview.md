---
title: "Payment Provider Protocol - Overview"
slug: "payment-provider-protocol-api-overview"
hidden: false
createdAt: "2020-01-02T04:28:35.950Z"
updatedAt: "2022-06-15T19:37:26.692Z"
---
[block:callout]
{
  "type": "info",
  "body": "Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer's journey.",
  "title": "Onboarding guide"
}
[/block]
The Payment Provider Protocol is a set of definitions to help you integrate your payment processing API into VTEX platform, including sub-acquirers, acquirers, gateways and custom payment services. 

To achieve this, you need to implement a web API (REST) following the specifications described in this documentation.

To learn more about the Payment Provider Protocol, check our [Help Center article](https://help.vtex.com/en/tutorial/payment-provider-protocol).


## Endpoint requirements

  * Must use a standard subdomain/domain name, and not a IP address.
  * Must be served over HTTPS on port 443 with TLS 1.2 support.
  * Must respond in less than 5 seconds when running the tests.
  * Must respond in less than 20 seconds when in production.
  * Must be [PCI-DSS compliant](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance) or use [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy) to accept branded cards like Visa, Mastercard, Amex, etc.

## Testing

*VTEX - Payment Provider Test Suite*: https://apps.vtex.com/vtex-payment-provider-test-suite/p

*An extra header* `X-VTEX-API-Is-TestSuite` = `true` *will be sent for every test suite request, to help you easily identify it and mock any required scenarios.*


## Common parameters in the documentation

<table>
  <tr>
    <td><code>{{providerApiEndpoint}}</code></td>
    <td>Provider's endpoint for the implementation</td>
  </tr>
  <tr>
    <td><code>{{X-VTEX-API-AppKey}}</code></td>
    <td>The AppKey configured by the merchant</td>
  </tr>
  <tr>
    <td><code>{{X-VTEX-API-AppToken}}</code></td>
    <td>The AppToken configured by the merchant</td>
  </tr>
</table>