---
title: "Batch inventory updates (Beta)"
slug: "batch-inventory-updates"
hidden: false
createdAt: "2026-05-20T00:00:00.000Z"
updatedAt: "2026-05-20T00:00:00.000Z"
excerpt: "Learn how to update large volumes of inventory data asynchronously using the new Batch operations endpoints in the Logistics API."
seeAlso:
 - "/docs/api-reference/logistics-api"
 - "/docs/guides/logistics-api-overview"
 - "https://help.vtex.com/en/docs/tutorials/updating-the-quantity-of-items-in-inventory"
 - "https://help.vtex.com/en/docs/tutorials/managing-stock-items"
---

>ℹ️ This feature is in early access, which means that we are working to improve it. If you want to use this feature, please contact our [Support Center](https://support.vtex.com/hc/en-us/requests).

The **Batch operations** endpoints of the [Logistics API](https://developers.vtex.com/docs/api-reference/logistics-api) let you update large volumes of inventory data asynchronously by uploading a single CSV file to [Amazon S3](https://aws.amazon.com/s3/) and tracking its processing through the API. This flow is designed for scenarios such as full inventory refreshes and bulk synchronizations, where the existing per-SKU endpoints would require too many requests.

This guide walks you through the end-to-end flow: creating a batch job, uploading the CSV file, committing the batch for processing, polling the processing status, and downloading the error report if there are failed rows.

The integration involves four API endpoints and one direct upload to the pre-signed S3 URL returned by VTEX:

1. **Create batch:** Call the [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch) endpoint to register a new batch. The response includes a `batchId` and a pre-signed S3 URL for the CSV upload.
2. **Upload CSV:** Upload the CSV file directly to S3 using the pre-signed URL. This step does not go through the VTEX API.
3. **Confirm batch:** Call the [Confirm batch inventory](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch/-batchId-/commit) endpoint to confirm the upload and queue the batch for processing.
4. **Monitor processing:** Poll the [Get batch inventory status](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/status) endpoint until the batch reaches a terminal status.
5. **Download error report (optional):** If the status response indicates `errorCount > 0`, call the [Get batch inventory errors](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/errors) endpoint to retrieve a pre-signed URL for the error CSV.

## Create a batch inventory job

Use the [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch) endpoint to register a new batch. The response returns the `batchId` you will use throughout the flow and the pre-signed `upload` object you will use to send the CSV to S3.

Response example:

```json
{
  "batchId": "550e8400-e29b-41d4-a716-446655440000",
  "status": "AWAITING_UPLOAD",
  "upload": {
    "method": "PUT",
    "url": "https://availability-bulk-upload.s3.amazonaws.com/550e8400-e29b-41d4-a716-446655440000.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&...",
    "headers": {
      "Content-Type": "text/csv"
    },
    "expiresAt": "2026-01-12T20:10:00Z"
  }
}
```

The batch starts in `AWAITING_UPLOAD` status and remains in this state until the CSV is uploaded and committed.

> ⚠️ The pre-signed URL returned in `url` is valid for 30 minutes (see `expiresAt`). If the URL expires before you upload the file, create a new batch.

## Upload the CSV to S3 (data plane)

Upload the CSV file directly to S3 using the `url` returned by the [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch) endpoint. This request does not go through the VTEX API.

Keep the following requirements in mind:

- Submit every field following the order defined in the CSV file.
- The CSV file name must match the `batchId` returned in the [Create batch inventory job](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch) response (for example, `550e8400-e29b-41d4-a716-446655440000.csv`).
- Use the HTTP method (`PUT`) and headers (`Content-Type: text/csv`) returned in the `upload` object.

Example request:

```bash
curl -X PUT \
  "{presignedUrl}" \
  -H "Content-Type: text/csv" \
  --data-binary "@550e8400-e29b-41d4-a716-446655440000.csv"
```

Replace `{presignedUrl}` with the value returned in `url`. A successful upload returns an HTTP `200 OK` response from S3.

### CSV file schema

The CSV file must contain one row per SKU, warehouse and account name combination you want to update, with the following fields:

| **Field** | **Type** | **Description** |
| :--- | :--- | :--- |
| `item_id` | string | SKU identifier of the item you want to update. |
| `account_name` | string | Name of the VTEX account the warehouse belongs to. |
| `container_id` | string | ID of the warehouse where the inventory update should be applied. |
| `quantity` | integer | Number of units available for the SKU in the given warehouse. This value is ignored when `unlimited` is `true`. |
| `unlimited` | boolean | Indicates whether the SKU has [unlimited inventory](https://help.vtex.com/docs/tutorials/managing-stock-items#inventory-information) (`true`) or a finite `quantity` (`false`). |
| `lead_time` | string | Shipping [lead time](https://help.vtex.com/docs/tutorials/managing-stock-items#inventory-information) for the SKU at the warehouse, in ISO 8601 duration format (for example, `PT24H` for 24 hours). |

Keep the following in mind when filling out each field:

- **`item_id`:** Use the exact SKU ID as registered in your catalog. Rows with a nonexistent SKU return the `UNKNOWN` error code.
- **`account_name`:** Use the store's account name exactly as it appears in the VTEX URL (for example, the `{accountName}` in `https://{accountName}.myvtex.com`).
- **`container_id`:** Use the exact warehouse ID configured in Warehouse & Inventory Management. An incorrect or nonexistent ID causes the row to fail.
- **`quantity`:** Provide a non-negative integer. This field is still required even when `unlimited` is `true`, but its value is ignored during processing.
- **`unlimited`:** Use the lowercase literals `true` or `false`. Any other value is treated as an invalid format.
- **`lead_time`:** Use ISO 8601 duration format (for example, `PT24H` for 24 hours or `PT0S` for immediate availability). Omitting this field or using an invalid format causes the row to fail.

CSV example:

```csv
item_id,account_name,container_id,quantity,unlimited,lead_time
SKU-12345,WH-01,dgbransonmissouri,150,false,PT24H
```

## Confirm the batch

After uploading the CSV to S3, call the [Confirm batch inventory](https://developers.vtex.com/docs/api-reference/logistics-api#post-/availability/v1/inventory/batch/-batchId-/commit) endpoint, passing the `batchId` as a path parameter. This request confirms that the upload is complete and triggers the asynchronous processing of the batch.

>⚠️ You have 30 minutes to confirm the batch after uploading the CSV file, otherwise the upload will expire and you will have to start the process again.

A successful commit returns an HTTP `202 Accepted` response, and the batch transitions to the `QUEUED` status. From this point on, processing is handled asynchronously by VTEX, and you can use the status endpoint to track progress.

>⚠️ If you call this endpoint twice in parallel for the same `batchId`, the second request will receive a `423 Locked` response. Wait for the first commit to complete before retrying.

## Monitor the batch status

Use the [Get batch inventory status](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/status) endpoint to track the processing progress of the batch. The response returns row counts, error counts, percentage completed, processing stages, and a final summary once the batch is processed.

Response example:

```json
{
  "batchId": "550e8400-e29b-41d4-a716-446655440000",
  "status": "PROCESSING",
  "rowCount": 13800000,
  "processedCount": 8500000,
  "errorCount": 0,
  "amountCompleted": 61,
  "createdAt": "2026-01-12T20:00:00Z",
  "startedAt": "2026-01-12T20:01:00Z",
  "stages": {
    "ingestedChunks": 276,
    "classifiedChunks": 250,
    "processedChunks": 170,
    "notifiedChunks": 165,
    "totalChunks": 276
  },
  "summary": {
    "insertCount": 5200000,
    "updateCount": 3100000,
    "noopCount": 200000,
    "conflictCount": 0,
    "skippedDueApiUpdateCount": 0,
    "perItemRoutedCount": 0,
    "dlqEventsCount": 0
  }
}
```

The `status` field can return the following values:

| **Status** | **Description** |
| :--- | :--- |
| `AWAITING_UPLOAD` | Batch created, waiting for CSV upload. |
| `QUEUED` | Upload committed, waiting to begin processing. |
| `PROCESSING` | Batch is currently being processed. |
| `COMPLETED` | All rows processed successfully. |
| `COMPLETED_WITH_ERRORS` | Processing finished with some row errors. |
| `FAILED` | Processing failed due to validation or system errors. |
| `EXPIRED` | Batch metadata has expired. |

`COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`, and `EXPIRED` are terminal statuses. Once any of these is returned, no further updates will be made to the batch and you can stop polling.

## Download the error report

If the batch status response indicates `errorCount > 0`, use the [Get batch inventory errors](https://developers.vtex.com/docs/api-reference/logistics-api#get-/availability/v1/inventory/batch/-batchId-/errors) endpoint to retrieve a pre-signed URL for downloading a CSV report with all rows that failed processing.

Response example:

```json
{
  "batchId": "550e8400-e29b-41d4-a716-446655440000",
  "downloadUrl": "https://availability-bulk-upload-errors.s3.amazonaws.com/550e8400-e29b-41d4-a716-446655440000-errors.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&...",
  "errorCount": 3
}
```

The `downloadUrl` is a pre-signed S3 URL valid for 60 minutes. The error report itself remains available until the batch metadata expires, which is 7 days after batch completion.

>ℹ️ The endpoint returns a `204 No Content` response if `errorCount` is `0` or the batch is not in a status that produces an error report (`PROCESSING`, `COMPLETED`, `COMPLETED_WITH_ERRORS`, or `FAILED`).

### Error CSV schema

The error CSV contains the following fields:

| **Field** | **Type** | **Description** |
| :--- | :--- | :--- |
| `line_number` | integer | Original line number in the uploaded CSV. |
| `item_id` | string | SKU identifier from the failed row. |
| `container_id` | string | Warehouse ID from the failed row. |
| `error_code` | string | Machine-readable error code. |
| `error_message` | string | Human-readable error description. |

Example:

```csv
line_number,item_id,container_id,error_code,error_message
1523,SKU-12345,WH-01,INVALID_QUANTITY,"quantity cannot be negative: -50"
4892,SKU-67890,WH-01,MISSING_REQUIRED_FIELD,"container_id is required"
10234,SKU-11111,WH-01,INVALID_DATE_FORMAT,"supply_date is not valid"
```

### Error types

The error report distinguishes between two categories of errors:

- **Deterministic errors:** Caused by invalid or incomplete data in the submitted file, such as missing required fields or invalid values. They are detected during file ingestion from S3 and fail the affected records immediately. The system does not retry these operations automatically. To resolve them, fix the data in the CSV file and submit a new batch.
- **Non-deterministic errors:** Caused by infrastructure or system issues. The system automatically retries the operation up to three times. If it still fails, the message is sent to a Dead Letter Queue (DLQ) for further investigation. These errors appear as `UPDATE_FAILED` in the error CSV.

### Error codes

| **Error code** | **Description** |
| :--- | :--- |
| `INVALID_QUANTITY` | Quantity value is invalid (negative or non-numeric). |
| `MISSING_REQUIRED_FIELD` | A required field is empty or missing. |
| `INVALID_DATE_FORMAT` | A date or time field has an invalid format. |
| `UPDATE_FAILED` | Database update failed after retries (non-deterministic error). |
| `INSERT_CONFLICT` | Insert conflicted with a concurrent operation. |
| `INVALID_FORMAT` | Row format is invalid (for example, wrong number of columns). |
| `CONFLICT` | Compare-And-Set conflict or per-item routing conflict. |
| `UNKNOWN` | Unclassified error. |

## Best practices

- **Reuse the same `batchId`:** Always use the `batchId` returned by the Create batch inventory job endpoint when uploading the CSV, committing the batch, polling its status, and retrieving errors.
- **Respect the upload window:** The pre-signed upload URL expires 30 minutes after creation. If it expires before the upload is complete, create a new batch.
- **Avoid concurrent commits:** Do not commit the same batch in parallel. A second commit while one is in progress returns a `423 Locked` response.
- **Use a reasonable polling interval:** When monitoring large batches, poll the status endpoint at intervals proportional to the batch size to avoid unnecessary requests.
- **Fix deterministic errors at the source:** If the error report shows deterministic errors, correct them in your source data and submit a new batch instead of retrying the same file.
