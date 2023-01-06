---
title: "Payments"
slug: "payments-integration-guide"
hidden: false
createdAt: "2020-10-27T00:24:27.500Z"
updatedAt: "2022-06-23T17:26:11.955Z"
---
In VTEX, stores and partners can integrate some of their services into our system by using integration protocols - a set of conditions that must be followed to properly establish communication with VTEX.

As every service has its particularities, VTEX provides an integration protocol for each of them. This applies to the Payment Provider Protocol, the protocol created to assist institutions that work with payments and financial transactions to integrate with VTEX.

Before continuing, make sure you are familiar with some terms that will frequently appear in this guide:

  * **Acquirer:** an acquirer is a company that specializes in processing payments. For more information, refer to [What is an acquirer](https://help.vtex.com/en/tutorial/what-is-an-acquirer--7N1oRTG8dGmOiIugC0cs4E).
  * **Merchant or Client:** a client that holds its ecommerce operations in the VTEX platform.
  * **Customer:** an individual or business that purchases a product or service from a VTEX client.
  * **Provider:** it can be a payment system, a gateway, or a provider. The agent that will process the merchant's payments.
  * **Partner:** the agent responsible to carry out the integration between the provider and VTEX’s SmartCheckout.
  * **VTEX Payment Gateway:** VTEX system responsible for processing payments. The gateway communicates with the provider through the payment provider protocol.
  * **Payment Service Provider (PSP):** a PSP is a financial entity that is authorized to process financial transactions between merchants, acquiring banks, and card networks. It is a fast and cost-effective way to accept payments without needing to open a company in another country or having to create a merchant account.
  * **Payload:** request body in JSON format.
  * **Connector:** the provider’s affiliation that works as a bridge between the provider and VTEX’s SmartCheckout.
  * **Oauth:** it is an authorization protocol made for APIs. It allows the provider system to access the customer data to process a transaction.

The sections of this tutorial will present the main concepts and guide you through the steps required to complete an integration using the Payment Provider Protocol.

## Structure of this guide


[block:html]
{
  "html": "<style>\n  .markdown-body .rdmd-table table:only-child thead th {\n    width: 195px;\n  }\n</style>"
}
[/block]

[block:parameters]
{
  "data": {
    "h-0": "Article",
    "h-1": "Description",
    "0-0": "[Payment Provider Protocol](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol)",
    "1-0": "[PCI - DSS Compliance](https://developers.vtex.com/docs/guides/payments-integration-pci-dss-compliance)",
    "2-0": "[Payment Methods](https://developers.vtex.com/docs/guides/payments-integration-payment-methods)",
    "4-0": "[Implementing a Payment Provider](https://developers.vtex.com/docs/guides/payments-integration-implementing-a-payment-provider)",
    "5-0": "[Payment Provider Homologation](https://developers.vtex.com/docs/guides/payments-integration-payment-provider-homologation)",
    "11-0": "[Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy)",
    "0-1": "An overview of our Payment Provider Protocol and how it works.",
    "1-1": "What the PCI-DSS Certification is and why it is required.",
    "2-1": "An explanation of what payment methods are and what types are accepted by VTEX.",
    "4-1": "Walkthrough of the API endpoints that your middleware must implement to adhere to our Payment Provider Protocol, along with activation instructions.",
    "5-1": "How to proceed with the homologation process in order to check if the integration was done correctly.",
    "11-1": "A feature that allows payment integrations that use credit, debit, or co-branded cards as a payment method to be developed in the VTEX ecosystem without the need for a PCI DSS certification.",
    "3-0": "[Purchase Flows](https://developers.vtex.com/docs/guides/payments-integration-purchase-flows)",
    "3-1": "How the payment flow works and which operations are involved in this process.",
    "6-0": "[Pix: Instant Payments in Brazil](https://developers.vtex.com/docs/guides/payments-integration-pix-instant-payments-in-brazil)",
    "6-1": "An explanation of what the PIX payment method is and how to use it in your store.",
    "7-0": "[Installing Affirm Payment App](https://developers.vtex.com/docs/guides/installing-affirm-payment-app-1)",
    "7-1": "How to install the Affirm Payment App in your store.",
    "8-0": "[Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app)",
    "8-1": "An explanation of what the Payment App is and how to use it in your store.",
    "9-0": "[Split Payouts on Payment Provider Protocol](https://developers.vtex.com/docs/guides/split-payouts-on-payment-provider-protocol)",
    "9-1": "An overview of our Split Payouts process on the Payment Provider Protocol and how it works.",
    "10-0": "[Custom Auto Capture Feature](https://developers.vtex.com/docs/guides/custom-auto-capture-feature)",
    "10-1": "An explanation of a feature that gives merchants the possibility to set a custom delay interval for automatic payment capture.",
    "12-0": "Use Cases and Additional Resources\n(Article under development)",
    "12-1": "A final (optional) step covering some use cases and some additional resources to illustrate how the payment provider protocol works in the daily routine."
  },
  "cols": 2,
  "rows": 13
}
[/block]

[block:callout]
{
  "type": "success",
  "title": "Become a VTEX Partner",
  "body": "To integrate a payment solution in VTEX you must fill out the registration form to join our [Partner Program](https://vtex.com/us-en/partner/) to get access to your own VTEX account.\n\nIf you are already a client or partner, you can [open a support ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) if you have any questions."
}
[/block]
