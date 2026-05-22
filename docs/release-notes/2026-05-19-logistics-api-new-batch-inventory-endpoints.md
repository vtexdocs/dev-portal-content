---
title: "New batch inventory endpoints (Beta) in the Logistics API "
slug: "2026-05-19-logistics-api-new-batch-inventory-endpoints"
hidden: false
type: "added"
createdAt: "2026-05-19T20:00:00.000Z"
excerpt: "Update large volumes of inventory data asynchronously through CSV file uploads with the new Batch operations endpoints."
---

The **Logistics API** now includes a new batch inventory operations endpoints designed for high-throughput [inventory updates](https://help.vtex.com/en/docs/tutorials/updating-the-quantity-of-items-in-inventory). These endpoints let you submit large volumes of inventory data through a CSV file and track the processing asynchronously, making them ideal for full inventory refreshes and bulk synchronizations.

>ℹ️ This feature is in early access, which means that we are working to improve it. If you want to use this feature, please contact our [Support Center](https://support.vtex.com/hc/en-us/requests).

## What has been added?

Four new endpoints are now available in the Logistics API, under the **Batch operations** section:

- `POST` [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch): Creates a new batch inventory job and returns, in the response, both the `batchId` and a pre-signed URL for uploading the CSV file,that are required for the following step (CSV upload). The batch remains in `AWAITING_UPLOAD` status until the CSV is uploaded and committed.
- `POST` [Commit batch inventory](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch/-batchId-/commit): Confirms that the CSV upload is complete and triggers the asynchronous processing of the batch. The batch status transitions to `QUEUED`.
- `GET` [Get batch inventory status](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/status): Retrieves the current processing status and progress information for a batch job, including row counts, error counts, and processing stages.
- `GET` [Get batch inventory errors](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/errors): Returns a pre-signed URL to download a CSV report with all rows that failed processing, along with error codes and messages.

## Why did we make this change?

The existing inventory endpoints remain optimized for low-latency, per-SKU updates, ideal for real-time or incremental inventory changes. However, for scenarios that involve millions of SKUs or require full inventory synchronizations, the new batch endpoints offer a scalable, asynchronous alternative. You do not need to choose between them: both methods can be used together within the same account, depending on the context and business needs.

With this new capability, you can:

- Update large volumes of inventory data in a single operation using CSV files with the batch endpoints, while continuing to use the per-SKU endpoints for more granular or real-time updates.
- Reduce the number of API calls and avoid rate limits when synchronizing inventory at scale.
- Track processing progress and inspect errors through dedicated status and error report endpoints.

## What needs to be done?

No changes are required for existing integrations. The previous [inventory endpoints](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) remain fully supported and operational.

If you would like to start using the new batch operations endpoints, please see our comprehensive [Batch inventory updates guide](https://developers.vtex.com/docs/guides/batch-inventory-updates) for step-by-step instructions. You can also refer to the [Logistics API reference](https://developers.vtex.com/docs/api-reference/logistics-api) for detailed endpoint information. Early access is available — contact our [Support Center](https://support.vtex.com/hc/en-us/requests) to get started.
