---
title: "Batch inventory updates are now available in open beta"
slug: "2026-09-30-batch-inventory-updates-now-available-in-open-beta"
hidden: false
type: "added"
createdAt: "2026-09-30T12:00:00.000Z"
updatedAt: "2026-09-30T12:00:00.000Z"
excerpt: "All customers can now use the Batch operations endpoints in the Logistics API to update large volumes of inventory data asynchronously, without opening a support ticket."
---

[Batch inventory updates](https://developers.vtex.com/docs/guides/batch-inventory-updates) are now available in open beta. You can use the **Batch operations** endpoints in the [Logistics API](https://developers.vtex.com/docs/api-reference/logistics-api) to update large volumes of inventory data asynchronously by uploading a CSV file, monitoring the processing status, and downloading an error report if any rows fail.

## What has changed?

Batch inventory updates are now available to all customers through the public API documentation.

As part of this open beta release, we've also made performance and observability improvements, giving merchants and integrators more reliability and visibility into batch processing status, progress, and errors.

The following endpoints are part of the **Batch operations** section of the Logistics API:

- `POST` [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch)
- `POST` [Commit batch inventory](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch/-batchId-/commit)
- `GET` [Get batch inventory status](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/status)
- `GET` [Get batch inventory errors](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/errors)

## Why did we make this change?

Merchants with large catalogs, multiple sellers, or many warehouses often need to synchronize high volumes of inventory data. Batch inventory updates offer a more scalable way to process these updates asynchronously, reducing the need for many individual API requests to per-SKU inventory endpoints and making large inventory refreshes easier to monitor.

## What needs to be done?

No action is required for existing integrations. The per-SKU [inventory endpoints](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) remain fully supported, and you can use both methods in the same account.

To start using batch inventory updates, see the [Batch inventory updates](https://developers.vtex.com/docs/guides/batch-inventory-updates) guide for step-by-step instructions.
