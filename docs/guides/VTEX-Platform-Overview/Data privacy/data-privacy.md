---
title: "Data privacy"
slug: "data-privacy"
hidden: false
createdAt: "2024-05-20T10:45:55.338Z"
updatedAt: "2024-05-21T10:10:00.000Z"
excerpt: "Learn how VTEX ensures compliance with data privacy regulations."
---

This guide presents an overview of VTEX's approach towards data privacy. Read the following sections to understand how our platform's resources can help merchants and developers protect shopper's personal data.

## Data processed by VTEX

VTEX follows the principle of data minimization, which refers to the practice of collecting, processing and storing only the information that is essential to achieve a specific purpose. This means we limit the amount of personal data we collect and keep, thus reducing the risk associated with excessive information processing.

VTEX processes shoppers’ personal data only when strictly necessary, in accordance with the requirements of each platform module to carry out ecommerce operations. Our platform may process personal data of the following types, as described in our [Data Processing Addendum (DPA)](https://vtex.com/us-en/privacy-and-agreements/data-processing-addendum/):

* Name
* Email address
* IP address
* Browsing information ([cookies](https://vtex.com/br-pt/privacy-and-agreements/vtex-platform-cookies-information/))
* Cart information
* Order information and history
* Delivery address
* ID number (when required by the country in which the store operates)
* Gift card history
* Unused cart
* [Conversation Tracker](https://help.vtex.com/pt/tutorial/conversation-tracker) information
* Session passwords (encrypted)
* Generated tokens

VTEX does not sell, monetize, enrich or transfer any personal data of shoppers to other companies. See the [Privacy & Contracts](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/) section of our website to learn more about our approach to data privacy, including certifications, internal policies and commitments.

>ℹ Learn more about the definition of personal data and our role in data protection at the [Data and privacy](https://help.vtex.com/en/tracks/data-and-privacy--4Lc0i0an0DgnEtB0AUwlcq/65ZqZlNWcmFSOqZQxr8gha) track on VTEX Help Center.

## Data lifecycle

All data on the platform has a life cycle from creation to deletion, including four phases: Creation, Storage, Processing and Disposal. This flow is illustrated below:

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX-Platform-Overview/Data-privacy/data-lifecycle.jpg)

1. **Creation:** Process for creating or collecting data.
2. **Storage:** Data that will be reused is stored.
3. **Processing:** Data is processed and used to achieve the tenant's business objectives. During this stage, data can be refined, merged or aggregated.
4. **Disposal:** When the data is no longer needed, we dispose of it permanently.

### Retention limits

Data retention limits define the duration for which data can be stored within our platform. These limits are influenced by various factors such as legal and compliance requirements, data privacy considerations, and costs. By establishing data retention limits, we aim to ensure compliance with regulations, protect user privacy, and maintain efficient resource allocation.

VTEX stores the shopper's personal data for the duration of the [Master Services Agreement (MSA)](https://vtex.com/us-en/privacy-and-agreements/agreements/). In the event of termination of the contract with VTEX, the merchant must ensure that the data is extracted from the Master Data within 30 (thirty) days prior to the date of termination of the MSA, in accordance with Clause 7 of the [DPA](https://vtex.com/us-en/privacy-and-agreements/data-processing-addendum/).

Responsibility for compliance with local laws and regulations lies with the merchants. This includes defining and respecting data retention periods, which may vary according to the specific legislation to which each store is subject.

## Data subject rights

VTEX offers tools for merchants to assist shoppers with requests related to data subject rights, including access and portability, rectification, consent, and erasure. Learn more at [Data subject rights](https://help.vtex.com/en/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM). For details on the data exclusion procedure, check the [Erasing customer data](https://help.vtex.com/en/tutorial/erasing-customer-data--1R9Fn7A06Ifj4R9YD4JTKU) guide.

>❗ VTEX is not responsible for personal data stored by systems integrated with your store, such as ERPs, third-party marketplaces, third-party sellers, third-party applications available in the [VTEX App Store](https://help.vtex.com/en/tutorial/visao-geral-apps--4xfsHXyAQTjbZNuiKl6Y0e) or customizations implemented by your development team. You must map this data and ensure the enforceability of the rights of personal data subjects in these instances, in addition to the processes described below.

## Data protection mechanisms

Data in transit is protected by the TLS 1.2 security standard. Connections that use older and less secure encryption methods are denied.

When working with storage or data at rest, VTEX can use one of the following algorithms to support applications that need to encrypt data:

- Two-way encryption:
  - RSA with keys of 2048 bits or more
  - AES-256
- One-way encryption:
  - PBKDF2 based on SHA-256

All relevant systems make automatic backups at a daily frequency by default, but this can be adjusted as necessary to ensure data integrity and availability.

In addition, we have implemented strict information security processes and access controls to ensure that only authorized persons have access to the data.

Learn more about our Security practices at the [Security](https://developers.vtex.com/docs/guides/security) guide.

## Storage location

The [hosting provider](https://vtex.com/us-en/privacy-and-agreements/subprocessors/.) used by VTEX is Amazon Web Services (AWS), which stores data in the Northern Virginia region of the United States. The AWS platform has important certifications such as ISO 27001, PCI DSS, CSA, and NIST. To see a detailed list of certifications, go to [AWS Compliance Programs](https://aws.amazon.com/en/compliance/programs/). Authorization for storing data on AWS can be found in our [DPA](https://vtex.com/us-en/privacy-and-agreements/data-processing-addendum/).

## Policies and compliance

VTEX has privacy and data protection policies, which are reviewed annually. The [External Privacy Notice](https://vtex.com/us-en/privacy-and-agreements/external-notice/) can be accessed on the VTEX website.

Merchants should add their own privacy policies to their websites, in compliance with local privacy regulations.

VTEX is committed to complying with all applicable data protection regulations, including GDPR and LGPD. The tools provided by our platform, through Admin and our APIs, allow merchants to comply with GDPR and local regulations. Learn more about our policies, contracts and commitment to data protection compliance in the [Privacy & Contracts](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/) section of our website.
