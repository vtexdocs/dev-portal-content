---
title: "PCI - DSS Compliance"
slug: "payments-integration-pci-dss-compliance"
hidden: false
createdAt: "2020-11-11T13:07:47.492Z"
updatedAt: "2022-03-08T14:43:18.123Z"
---
Although the Payment Provider Protocol is public, not everyone can simply use it. 

To do so, clients or partners that process payments with credit, debit, and co-branded cards must have the [Payment Card Industry - Data Security Standard certification](https://www.pcisecuritystandards.org/documents/PCI_DSS-QRG-v3_2_1.pdf) (PCI - DSS). It is an international certification that guarantees that a service can process transactions safely, protecting customers' information.
[block:callout]
{
  "type": "info",
  "body": "An alternative solution for partners that want to process card transactions and do not have a PCI-DSS certification in the developing environment of the connector is to implement Secure Proxy in their integrations. For more information, check the [Secure Proxy article](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy)."
}
[/block]
In VTEX, we only allow clients or partners that configure level 1 in the PCI - DSS certification to integrate into our system. In other words, the partner must process more than six million transactions per year.

If your provider just processes payments with “boleto bancário”, promissory or any other payment that involves redirect, PCI - DSS certification is not necessary. In this case, the provider can contact the VTEX Sales Team directly to start the integration.

[block:callout]
{
  "type": "info",
  "body": "The PCI-DSS certification is **only** necessary for clients or partners that process payments with **credit**, **debit**, and **co-branded** cards and do not use [Secure Proxy](https://developers.vtex.com/vtex-rest-api/docs/payments-integration-secure-proxy) in their integrations.\n\nBy “clients or partners”, we mean the agent that will indeed receive and process the transactions. In some cases, there are clients associated with tech services that develop and offer an affiliation infrastructure, but it does not operate anything. In this case, the one that must be certificated by the PCI - DSS is **the partner that will process the transactions**, not the tech service.",
  "title": "Who needs the PCI - DSS certification?"
}
[/block]
## Self-Assessment Questionnaire (SAQ)

The [Self-Assessment Questionnaire](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) (SAQ) is a list of “yes or no” questions designed to help service providers or merchants report the results of their PCI DSS self-assessment. 
[block:callout]
{
  "type": "danger",
  "body": "The SAQ (Self-Assessment Questionnaire) is not accepted in the VTEX integration process."
}
[/block]

## Attestation of Compliance for Onsite Assessments (AOC)

The Attestation of Compliance for Onsite Assessments ([AOC](https://www.pcisecuritystandards.org/document_library)) is a document that serves as a declaration of the service provider or merchant’s compliance status with the PCI DSS. It is signed by the responsible for the company and a [QSA](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors) (Qualified Security Assessor).

The provider must forward the AOC (Service Provider version) fully completed to VTEX, observing the following points:

- <strong>Company Name</strong>: the “URL” field (Part 1a.) must be the same as that of the company requesting the integration procedure. If it is filled in with another name (example: a company acquired by another), it will be necessary to send extra documentation that proves the relationship between the companies, and that the PCI DSS evaluated the provider's service URL.
- <strong>Signature</strong>: document signed by the company representative and the QSA.
- <strong>Expiration Date</strong>: the validity of the AOC is 1 year after the signing date. The AOC issued more than 11 months ago must not be sent to VTEX, that is, less than 30 days before its expiration date.
[block:callout]
{
  "type": "danger",
  "body": "The AOC (Merchant version) is not accepted in the VTEX integration process."
}
[/block]