---
slug: "secure-proxy-a-new-option-for-card-payment-integrations"
title: "Secure Proxy: An alternative option for card payment integrations"
createdAt: 2022-03-04T23:58:10.324Z
hidden: false
type: "added"
---

Secure Proxy is a feature that allows payment integrations that use credit, debit, or cobranded cards as a payment method to be developed in the VTEX ecosystem without the need of a [PCI DSS certification](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-pci-dss-compliance).

PCI DSS certification is needed to guarantee that sensitive information in the payment process is handled securely. Since not every integration is PCI compliant, Secure Proxy comes as an alternative to ease this process for developer partners. When using Secure Proxy, the payment provider does not receive any sensitive information, which is completely handled by VTEX until making the request to the acquirer.

The main differences between the standard flow and making use of Secure Proxy are:

1. The Authorization request works as usual.
2. The provider receives tokens from VTEX’s Gateway that refers to the sensitive data, instead of the actual data.
3. The provider sends the API endpoint of the acquirer and the merchant credentials to the Gateway, instead of making the call directly to the acquirer.
4. The Gateway makes the API call to the acquirer, acting as a proxy between the provider and the acquirer. In this call, the tokens are replaced by sensitive data.
![Secure Proxy flow](https://files.readme.io/6a44052-Secure_Proxy_simplified_flow_diagram.png)

To learn more about the feature, check our [Secure Proxy article](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy).