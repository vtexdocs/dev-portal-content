---
title: "PII platform version"
slug: "pii-platform-version"
hidden: true
createdAt: "2022-02-22T22:27:02.330Z"
updatedAt: "2022-11-18T18:34:36.446Z"
---
>❗ This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.

The VTEX platform allows stores to manage shoppers’ Personal Identifiable Information (PII) in compliance with data privacy regulations such as [GDPR and LGPD](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/). This means that:
- PII is hidden by default.
- Each PII retrieval is an auditable event.
- Data at rest is stored in the region or country selected by the store.

## Parties' responsibilities

VTEX will isolate all fields that are mapped as sensitive and protect them. There are scenarios, however, in which VTEX cannot control, and therefore it is up to each store to ensure that its integration is not using PII data improperly. The main scenarios are:
- Sending personal data in custom or text fields.
- Adhere to IO apps that depend on or consume PII data.

[block:callout]
{
  "type": "warning",
  "body": "For European accounts, it is also important to have in mind that only [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) data will be stored in Europe. PII information added to any other service that allows parameters creation or open text information will be stored in the USA."
}
[/block]
## Integration

In order to implement these features in your store, you must make some commerce features adaptations, according to the guide [Changes and limitations of the PII platform version](https://developers.vtex.com/vtex-rest-api/docs/adaptations-and-limitations).

And to learn how to manage shopper data, see our [Profile System guide](https://developers.vtex.com/vtex-rest-api/docs/profile-system).