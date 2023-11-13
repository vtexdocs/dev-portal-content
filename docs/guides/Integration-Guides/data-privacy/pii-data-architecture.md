---
title: "PII data architecture"
slug: "pii-data-architecture"
hidden: true
createdAt: "2022-02-22T22:27:02.330Z"
updatedAt: "2023-06-14T43:38:36.446Z"
seeAlso:
 - "/docs/guides/pii-data-architecture-specifications"
 - "/docs/guides/data-residency"
 - "/docs/guides/profile-system"
 - "/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data"
 - "/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta"
---

>❗ This feature is in closed beta phase, meaning we are evolving it to support all scenarios. Do not share this documentation with people outside of your company.

The VTEX platform allows stores to process shoppers’ Personal Identifiable Information (PII) in compliance with data privacy regulations such as [GDPR and LGPD](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/).

In the PII data architecture, all PII is stored in the **Profile System**. Other VTEX modules, such as **Order Management** and **Checkout**, store only pseudonymized data associated with a **Profile System** token. These modules may also access PII from the **Profile System**, as described in the [PII data architecture specifications](https://developers.vtex.com/docs/guides/pii-data-architecture-specifications).

>ℹ️ See the [Trust Hub](https://vtex.com/us-en/trust/) to learn more about VTEX's vision regarding data privacy, including certifications, internal policies and commitments.

## Solutions and implementation

VTEX has established a comprehensive PII data architecture that incorporates a range of solutions and processes for PII. See the documentation below to learn more about how it works and how to implement it.

- [PII Data Architecture specifications](https://developers.vtex.com/docs/guides/pii-data-architecture-specifications): Technical specifications of the PII data architecture, including the Profile System, data encryption and auditability, among other key features.
- [Data residency](https://developers.vtex.com/docs/guides/data-residency): How PII data residency works for VTEX stores using the PII data architecture.
- [Data subject rights](https://help.vtex.com/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM): Detailed instructions on how VTEX stores can apply data subject rights.
- [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system): How to integrate with the Profile System API.
- [Working with schemas in the Profile System](https://developers.vtex.com/docs/guides/working-with-schemas-in-the-profile-system): How to interact with the structure of data stored in the Profile System.
- [Changes in VTEX features behavior to handle PII data](https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data): Adaptations in the default behavior of certain VTEX features to handle the PII data architecture.
- [Limitations of the PII data architecture during closed beta](https://developers.vtex.com/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta): Current limitations that apply to stores using PII data architecture, in relation to certain VTEX features.

## Parties' responsibilities

VTEX isolates and protects all fields classified as sensitive. However, it is important to acknowledge that there are scenarios beyond VTEX's control. In such cases, as a VTEX client, it is the store's responsibility to ensure the integrity of your integrations and prevent any data misuse. The main scenarios to consider include:

- Sending PII in custom or text fields.
- Adhering to IO apps that depend on or consume PII data.
- Integrating with third-party systems that consume PII data, such as ERPs.
