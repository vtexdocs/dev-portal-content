---
title: "PCI DSS Compliance"
slug: "payments-integration-pci-dss-compliance"
excerpt: "Learn when PCI DSS certification is required for VTEX payment integrations and how to submit the Attestation of Compliance."
hidden: false
createdAt: "2020-11-11T13:07:47.492Z"
updatedAt: "2028-05-12T00:00:00.000Z"
---
Partners that process credit, debit, or co-branded card transactions must hold a valid [Payment Card Industry Data Security Standard](https://www.pcisecuritystandards.org/document_library?document=PCI_DSS_v4) (PCI DSS) certification before integrating with the VTEX Payment Gateway. The PCI DSS is an international standard that ensures services can process transactions securely and protect cardholder data.

> ℹ️ **Who needs PCI DSS certification?**
>
> PCI DSS certification is **only** required for partners that process **credit**, **debit**, or **co-branded** card payments and do not use the [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy) in their integrations.
>
> The certification requirement applies to the entity that receives and processes transactions. If a tech service develops the connector infrastructure but a separate partner processes the transactions, only the partner processing the transactions must be PCI DSS certified.

## Requirements

On VTEX, only partners with **PCI DSS Level 1** certification (processing more than six million card transactions per year) can integrate their payment connectors.

Partners that use [Secure Proxy](https://developers.vtex.com/docs/guides/payments-integration-secure-proxy) in the development environment of the connector do not need PCI DSS certification.

If your provider only processes [boleto](http://help.vtex.com/docs/tutorials/registered-ticket-flow), notes payable, or other redirect-based payment methods, PCI DSS certification is not required. Contact the VTEX Sales Team directly to start the integration.

## Self-Assessment Questionnaire (SAQ)

The [Self-Assessment Questionnaire](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) (SAQ) is a list of yes-or-no questions designed to help service providers or merchants report the results of their PCI DSS self-assessment.

> ❗ The SAQ is not accepted in the VTEX integration process.

## Attestation of Compliance for Onsite Assessments (AOC)

The Attestation of Compliance for Onsite Assessments ([AOC](https://www.pcisecuritystandards.org/document_library)) is a document that declares the compliance status of the service provider or merchant with PCI DSS. It must be signed by a company representative and a Qualified Security Assessor ([QSA](\[https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors])).

The provider must forward the AOC (Service Provider version) fully completed to VTEX, noting the following points:

Submit the AOC (**Service Provider** version) fully completed to VTEX. Make sure the following requirements are met:

- **Company Name**: The URL field (Part 1a.) must match the company requesting the integration. If the field contains a different name (for example, a company acquired by another), you must send additional documentation proving the relationship between the companies and confirming that the PCI DSS assessment covered the service URL of the provider.
- **Signature**: The document must be signed by the company representative and the QSA.
- **Expiration Date**: The AOC is valid for one year after the signing date. Do not submit an AOC issued more than 11 months ago (less than 30 days before expiration).

> ❗ The AOC (Merchant version) is not accepted in the VTEX integration process.
