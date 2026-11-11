---
title: "Master Data API: Bulk document deletion for v1 and v2 entities"
slug: "2026-10-08-master-data-api-bulk-document-deletion"
hidden: false
type: "added"
createdAt: "2026-10-08T00:00:00.000Z"
excerpt: "Master Data v1 and v2 data entities now support an open-beta job that deletes every document matching a filter in one operation. Existing integrations require no action."
---

The **Master Data** API now offers [bulk document deletion](https://developers.vtex.com/docs/guides/deleting-documents-in-bulk-in-master-data) for v1 and v2 data entities. The feature is in open beta. In one operation, the job removes every document in a data entity that matches a filter.

## What has changed?

Previously, deleting many documents required scrolling through the data entity and sending one `DELETE` request per document. You can now delete those **Master Data** documents with a single asynchronous job.

The API exposes two operations:

- `POST /api/dataentities/{name}/delete` creates the job and returns `202 Accepted` with a `JobId`. The request itself deletes nothing.
- `GET /api/dataentities/{name}/delete/jobs/{jobId}` returns the job status and the number of documents deleted.

Deletion is asynchronous. Poll the job until it succeeds or fails.

## What needs to be done?

No action is required. Per-document deletion is unchanged and still supported for selective cleanups and privacy erasure flows.

> ❗ Bulk deletion cannot be undone. Deleted documents are permanently lost.

## Learn more

- [Deleting documents in bulk in Master Data](https://developers.vtex.com/docs/guides/deleting-documents-in-bulk-in-master-data)
