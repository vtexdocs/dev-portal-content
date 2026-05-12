---
title: "Master Data v2: Personal data fields with encryption and masking"
slug: "2026-05-15-master-data-v2-personal-data-fields-with-encryption-and-masking"
hidden: false
type: "added"
createdAt: "2026-05-15T00:00:00.000Z"
excerpt: "Master Data v2 now lets you declare personal data fields per entity. Configured fields are encrypted, returned masked by default, and automatically participate in data subject request flows."
---

[Master Data v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) now supports declaring which fields in a data entity contain personal data. Configured fields are encrypted, returned masked by default on read, and automatically participate in data subject request flows, such as the right to be forgotten.

## What has changed?

You can now configure personal data at the data entity level using the new [Configure personal data fields](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/personalData) endpoint. Once configured, the standard document and search endpoints automatically apply encryption, masking, and data subject linking to the declared fields.

>ℹ️ This feature is only available for Master Data v2 entities. Master Data v1 entities are not supported.

## What needs to be done?

This change is opt-in. Existing Master Data v2 entities continue to behave as before until you configure personal data fields.

To start using personal data in a Master Data v2 entity, follow the [Managing personal data in Master Data v2](https://developers.vtex.com/docs/guides/managing-personal-data-in-master-data-v2) guide.
