---
title: "Master Data API v2: schema saves are blocked while a reindex is in progress"
slug: "2026-09-30-master-data-api-v2-schema-saves-blocked-during-reindex"
hidden: false
type: "improved"
createdAt: "2026-09-30T00:00:00.000Z"
excerpt: "A schema save that triggers a full reindex of a data entity now blocks further schema saves on that for 12 hours, which return 423 Locked."
---

Saving a schema in **Master Data** with [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) now can apply a temporary reindex lock if the save triggers a full reindex of a data entity.

## What has changed?

If a [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-) triggers a full reindex, further schema changes via the same endpoint are blocked for 12 hours.

While the lock holds, `PUT /api/dataentities/{dataEntityName}/schemas/{schemaName}` returns `423 Locked`. The response body carries a `Message` field stating that a reindex is in progress and, when available, the time after which the save can be retried.

> ℹ️ The reindex lock does not block document saves.

## What needs to be done?

If your integration updates schemas programmatically, handle `423 Locked` as an expected response rather than a failure. Retry the save after the time reported in the `Message` field, or try again later if `Message` does not report a time.

If you only change schemas manually, no action is required.

## Learn more

- [Master Data API v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) reference
- [Save schema by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-)
