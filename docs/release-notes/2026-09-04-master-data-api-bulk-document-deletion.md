---
title: "Master Data API: Bulk document deletion for v1 and v2 entities"
slug: "2026-09-04-master-data-api-bulk-document-deletion"
hidden: false
type: "added"
createdAt: "2026-09-04T12:00:00.000Z"
excerpt: "Master Data v1 and v2 entities now support an asynchronous job that deletes every document matching a filter in a single operation. Existing integrations require no action."
---

The [Master Data](https://developers.vtex.com/docs/guides/master-data-introduction) API now offers a bulk deletion job for v1 and v2 entities. In a single operation, the job removes every document of a data entity matching a filter.

## What has changed?

Previously, deleting many documents required [scrolling through the data entity](https://developers.vtex.com/docs/guides/extracting-data-from-master-data-with-search-and-scroll) and sending one `DELETE` request per document. Now you can delete Master Data documents in bulk with just a single deletion job.

The API now exposes two operations:

- `POST /api/dataentities/{name}/delete` creates the job and returns `202 Accepted` with a `JobId`. The request itself deletes nothing.
- `GET /api/dataentities/{name}/delete/jobs/{jobId}` returns the job status and the number of documents deleted.

Deletion is asynchronous, so you can poll the job until it succeeds or fails.

## What needs to be done?

No action is required. Per-document deletion is unchanged and still supported for selective cleanups and privacy erasure flows.

> ❗ Bulk deletion cannot be undone, deleted documents are permanently lost.

To adopt the new job, follow [Bulk deleting documents in Master Data](https://developers.vtex.com/docs/guides/bulk-deleting-documents-in-master-data), which covers filter rules, polling, and error handling.
