---
title: "Data privacy"
slug: "data-privacy"
hidden: true
createdAt: "2022-02-22T22:27:02.330Z"
updatedAt: "2023-05-16T09:38:36.446Z"
---
The VTEX platform allows stores to process shoppers’ Personal Identifiable Information (PII) in compliance with data privacy regulations such as [GDPR and LGPD](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/).

>❗ This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.

In the PII data architecture, all PII is stored in the Profile System. Other VTEX modules, such as order management and checkout, store only pseudoanonymised data associated to a Profile System token. These modules may also, at times, access PII from the Profile System according to the specifications linked below.

>ℹ️ See the [Trust Hub](https://vtex.com/us-en/trust/) to learn more about VTEX's vision regarding data privacy, including certifications, internal policies and commitments.

## Solutions and implementation

VTEX has established a comprehensive [PII data architecture](https://developers.vtex.com/docs/guides/pii-data-architecture) that incorporates a range of solutions and processes for PII. See the documentation below to learn more about how it works and how to implement it.

- [PII data architecture](https://developers.vtex.com/docs/guides/pii-data-architecture-specifications) - Technical specifications of the PII data architecture, including the Profile System, data encryption and auditability, among other key features.
- [Data residency](https://developers.vtex.com/docs/guides/data-residency) - How PII data residency works for VTEX stores.
- [Data subject rights](https://help.vtex.com/tutorial/data-subject-rights--6imchxTx09icupKMbzHVIM) - Detailed instructions on how VTEX stores can apply each right of data subjects.
- [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system) - How to integrate with the Profile System API.
- [Changes and limitations of the PII data architecture](https://developers.vtex.com/docs/guides/changes-and-limitations-pii-data-architecture) - Differences in the implementation of the PII data architecture.

## Parties' responsibilities

VTEX will isolate all fields that are mapped as sensitive and protect them. There are scenarios, however, in which VTEX has no control, and therefore it is up to your store to ensure that your integration is not using data improperly. The main scenarios are:

- Sending PII in custom or text fields.
- Adhere to IO apps that depend on or consume PII data.
- Integrations with other systems that consume PII data, such as ERPs.
