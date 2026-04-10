---
title: "Bulk pricing import integration"
slug: "bulk-pricing-import-integration"
hidden: false
createdAt: "2026-03-19T13:00:00.152Z"
updatedAt: "2026-03-19T13:00:00.152Z"
---

The Bulk Pricing API allows for asynchronous processing of large-scale price updates by sending a single CSV file containing the price updates and letting the platform process them in the background. 
This guide is intended for developers and integrators responsible for implementing bulk pricing update flows against the VTEX platform.

To update the price of only one SKU, use the [API](https://developers.vtex.com/docs/api-reference/pricing-api)

This API supports two types of pricing updates: **base prices** (cost price, base price, and list price per SKU) and **fixed prices** (price-table-specific prices with optional date ranges and minimum quantities). The workflow follows an async pattern where you start an import job, upload your CSV to a pre-signed URL, and then poll for status until processing completes.

The main actors involved are:

- **External pricing system** (ERP or custom integration): prepares the CSV file and orchestrates the import workflow.  
- **Bulk Pricing API**: receives the import request, provides the upload URL, and processes the pricing data.  
- **Cloud storage**: hosts the pre-signed URL where the CSV file is uploaded directly.

This guide covers the following integration flows:

- [Bulk import flow](#bulk-import-flow)  
- [Batch monitoring and error handling flow](#batch-monitoring-and-error-handling-flow)


## How it works

Every bulk pricing import follows the same three-step async pattern, regardless of whether you are importing base prices or fixed prices:

1. Your system sends a `POST` request to the [Import prices endpoint](https://developers.vtex.com/docs/api-reference/bulk-pricing-api#post-/api/price-importer/pvt/import/-importType-), specifying the import type (`base-prices` or `fixed-prices`) and the file metadata (content type and size in bytes). The API returns a unique `batchId` and a pre-signed upload URL.  
2. Your system uploads the CSV file directly to the pre-signed URL using a `PUT` request with the headers provided in the response.  
3. Your system polls the [Get batch status endpoint](https://developers.vtex.com/docs/api-reference/bulk-pricing-api#get-/api/price-importer/pvt/batches/-batchId-) using the `batchId` to monitor processing progress. If errors occur, you retrieve the error details via the [Get batch errors endpoint](https://developers.vtex.com/docs/api-reference/bulk-pricing-api#get-/api/price-importer/pvt/batches/-batchId-/errors).

⚠️ The pre-signed upload URL has an expiration timestamp (`expiresAt`). You must complete the file upload before this time. If the URL expires, you need to start a new import job.

ℹ️ The pre-signed URL points directly to cloud storage. Do not replace it with the API base URL or any other endpoint.

```
sequenceDiagram
    participant ExtSystem as External System
    participant PricingAPI as Bulk Pricing API
    participant Storage as Cloud Storage

    ExtSystem->>PricingAPI: POST /api/price-importer/pvt/import/{importType}
    PricingAPI-->>ExtSystem: 200 OK (batchId, pre-signed upload URL)
    ExtSystem->>Storage: PUT CSV file to pre-signed URL
    Storage-->>ExtSystem: 200 OK
    loop Poll until terminal status
        ExtSystem->>PricingAPI: GET /api/price-importer/pvt/batches/{batchId}
        PricingAPI-->>ExtSystem: 200 OK (status, progress)
    end
    alt COMPLETED_WITH_ERRORS
        ExtSystem->>PricingAPI: GET /api/price-importer/pvt/batches/{batchId}/errors
        PricingAPI-->>ExtSystem: 200 OK (pre-signed URL to error CSV)
    end
```

## Permissions

Each endpoint requires specific License Manager resources. Requests made without the proper permissions return a `403 Forbidden` error.

| Endpoint | Product | Category | Resource |
| :---- | :---- | :---- | :---- |
| `POST` Import prices | Pricing | Price List | **Modify prices** |
| `GET` Get batch status | Pricing | Price List | **Read prices** |
| `GET` Get batch errors | Pricing | Price List | **Read prices** |

⚠️ There are no predefined roles for these resources. You must [create a custom role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc#creating-a-role) and assign the appropriate resources to it.

ℹ️ To prevent integrations from having excessive permissions, follow the [best practices for managing API keys](https://help.vtex.com/en/tutorial/best-practices-api-keys--7b6nD1VMHa49aI5brlOvJm) when assigning License Manager roles to integrations.

## Bulk import flow

Use this unified flow to import either base prices or fixed prices. The high-level process is identical for both import types; differences are noted inline where they matter.

### When to use this flow

- Use this flow when you need to update pricing data for many SKUs at once.  
- Use base-price imports when you need to update cost, base and optional list prices for SKUs.  
- Use fixed-price imports when you need to update trade-policy-specific prices, time-bound prices (Date From / Date To), or quantity-based rules (Min Quantity).

### Main endpoints involved

- `POST /api/price-importer/pvt/import/{importType}` – Start an import job. `importType` must be `base-prices` or `fixed-prices`. The response includes `batchId` and pre-signed upload details.  
- `GET /api/price-importer/pvt/batches/{batchId}` – Poll batch status and progress.  
- `GET /api/price-importer/pvt/batches/{batchId}/errors` – Retrieve a pre-signed URL to download a CSV with row-level errors.

### Step-by-step

1. Prepare a CSV file following the schema for the import type (see CSV schemas below). Ensure UTF-8 encoding, comma delimiter and a header row.  
2. Call `POST /api/price-importer/pvt/import/{importType}` with a JSON body containing `contentType` and `contentLengthBytes`. Optionally set `output=email` for email notifications.  
   - Example `importType` values:  
     - `base-prices` — base price import.  
     - `fixed-prices` — fixed price import.  
3. Extract `batchId` and `upload.url` from the response.  
4. Upload the CSV to `upload.url` with `PUT`. Include `Content-Type: text/csv` and any headers in `upload.headers`.  
5. Poll `GET /api/price-importer/pvt/batches/{batchId}` until status is a terminal state (`COMPLETED`, `COMPLETED_WITH_ERRORS`, `FAILED`).  
6. If `COMPLETED_WITH_ERRORS`, call the errors endpoint to download a CSV with `Error Code` and `Error Message` columns, fix failing rows and re-submit them as needed.

ℹ️ The upload URL expires at `upload.expiresAt`. If it expires before you upload, start a new import job.

### Request examples

Start a base price import:

```shell
curl -X POST \
  "https://{accountName}.vtexcommercestable.com.br/api/price-importer/pvt/import/base-prices?output=email" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}" \
  -d '{
    "contentType": "text/csv",
    "contentLengthBytes": 524288000
  }'
```

Start a fixed price import:

```shell
curl -X POST \
  "https://{accountName}.vtexcommercestable.com.br/api/price-importer/pvt/import/fixed-prices?output=email" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}" \
  -d '{
    "contentType": "text/csv",
    "contentLengthBytes": 10485760
  }'
```

### Generic response example (start import)

```json
{
  "batchId": "550e8400-e29b-41d4-a716-446655440000",
  "status": "AWAITING_UPLOAD",
  "upload": {
    "method": "PUT",
    "url": "https://pricing-bucket.s3.amazonaws.com/imports/550e8400.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=600",
    "headers": {
      "Content-Type": "text/csv"
    },
    "expiresAt": "2026-01-12T20:10:00Z"
  }
}
```

Upload the CSV file:

```shell
curl -X PUT \
  "https://pricing-bucket.s3.amazonaws.com/imports/550e8400.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=600" \
  -H "Content-Type: text/csv" \
  --data-binary @your-import-file.csv
```

### CSV schemas and examples

#### Base prices CSV schema

| Field         | Type    | Required | Description                                                                                                                                                                                                 | Example            |
|--------------|---------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| SKU ID       | String  | Yes      | SKU identifier.                                                                                                                                                                                             | SKU-12345          |
| Cost Price   | Decimal | Yes      | Cost price of the item.                                                                                                                                                                                     | 10                 |
| Base Price   | Decimal | Yes      | Base price of the item.                                                                                                                                                                                     | 25.03              |
| List Price   | Decimal | No       | List price of the item.                                                                                                                                                                                     | 30                 |
| Child Account| String  | No       | Name of a child account under the account that started the import process. When this field is filled in, the price update in that row is applied to the specified [child account](https://help.vtex.com/docs/tutorials/what-is-a-franchise-account#franchise-account-configuration) instead of the account that initiated the import. If the value is invalid, that row fails processing and is listed in the error report. | ChildAccountValue  |

CSV example (base prices):

```
SKU ID,Cost Price,Base Price,List Price,Child Account
1,45.50,59.99,65,
2,47.50,62.30,70.50,ChildAccountValue
```

#### Fixed prices CSV schema

| Field          | Type    | Required | Description                                                                                                                                                                                                 | Example              |
|----------------|---------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| SKU ID         | String  | Yes      | SKU identifier.                                                                                                                                                                                             | SKU-12345            |
| Trade Policy   | String  | Yes      | The price table to modify.                                                                                                                                                                                  | gold                 |
| Price          | Decimal | Yes      | The fixed price of the item in the price table.                                                                                                                                                             | 25                   |
| List Price     | Decimal | No       | List price of the item in the price table.                                                                                                                                                                  | 30.03                |
| Min Quantity   | Integer | No       | Minimum quantity required to start applying this price.                                                                                                                                                     | 2                    |
| Date From      | String  | No       | Date from which the price starts being applied, in ISO 8601 UTC.                                                                                                                                            | 2025-07-29T18:20:37Z |
| Date To        | String  | No       | End date for the fixed price, in ISO 8601 UTC.                                                                                                                                                              | 2025-08-29T18:20:37Z |
| Child Account  | String  | No       | Name of a [child account](https://help.vtex.com/docs/tutorials/what-is-a-franchise-account#franchise-account-configuration) under the account that started the import process. When this field is filled in, the price update in that row is applied to the specified child account instead of the account that initiated the import. If the value is invalid, that row fails processing and is listed in the error report. | ChildAccountValue    |

CSV example (fixed prices):

```
SKU ID,Trade Policy,Price,List Price,Min Quantity,Date From,Date To,Child Account
25,gold,10.80,20.00,2,2025-07-29T18:20:37Z,2025-08-29T18:20:37Z,ChildAccountValue
25,silver,11.80,,2,2025-07-29T18:20:37Z,2025-08-29T18:20:37Z,
26,gold,15.00,17.00,,,,
```

### Error handling

| HTTP Status | Meaning | Action |
| :---- | :---- | :---- |
| 200 | Batch accepted for processing. | Extract `batchId` and `upload.url`, then upload the CSV. |
| 401 | Unauthorized. | Verify your API key credentials or user token. |
| 403 | Forbidden. | Ensure your credentials have the **Modify prices** permission for imports and **Read prices** for status/errors. |
| 413 | File exceeds the 500 MB size limit. | Split your CSV into smaller files and submit separate import jobs. |
| 422 | Validation error in the file or request body. | Review row-level errors returned in the error CSV. |
| 429 | Rate limit exceeded. | Wait and retry the request after a delay. |
| 503 | Service unavailable. | Retry with exponential backoff. |

> ⛔ If you receive a `413` error, check if the file is up to 500MB; if necessary, split it into several smaller files of up to 500MB each and submit them as individual import jobs.


## Batch monitoring and error handling flow

After uploading a CSV file, use this flow to track the import progress and retrieve error details when processing finishes with errors.

### When to use this flow

- Use this flow after uploading a CSV file to monitor the batch processing status.  
- Use this flow to determine when the import has completed and whether it succeeded or had errors.  
- Use this flow to download a detailed error report when the batch finishes with the `COMPLETED_WITH_ERRORS` status.

### Main endpoints involved

- [`GET /api/price-importer/pvt/batches/{batchId}`](https://developers.vtex.com/docs/api-reference/bulk-pricing-api#get-/api/price-importer/pvt/batches/-batchId-) – Retrieves the current status and progress of a batch job.  
- [`GET /api/price-importer/pvt/batches/{batchId}/errors`](https://developers.vtex.com/docs/api-reference/bulk-pricing-api#get-/api/price-importer/pvt/batches/-batchId-/errors) – Retrieves a pre-signed URL to download the error CSV.

### Status lifecycle

A batch job progresses through the following statuses:

| Status | Description |
| :---- | :---- |
| `AWAITING_UPLOAD` | Batch created, waiting for the CSV file upload. |
| `RECEIVED` | File received, waiting for processing to start. |
| `VALIDATING` | An initial file validation is being performed. |
| `PROCESSING` | The batch is actively processing rows. |
| `DOCUMENTING` | The import results are being generated. |
| `COMPLETED` | All rows processed successfully. |
| `COMPLETED_WITH_ERRORS` | Processing finished, but some rows had errors. |
| `FAILED` | Processing failed entirely. |

ℹ️ Terminal statuses are `COMPLETED`, `COMPLETED_WITH_ERRORS`, and `FAILED`. Stop polling once the batch reaches one of these statuses.

### Step-by-step

1. After uploading the CSV file, start polling the batch status endpoint using the `batchId` from the import response.  
2. Check the `status` field in each response. Continue polling until the status reaches a terminal state.  
3. Use the `bytesProcessed` and `bytesTotal` fields to calculate progress during the `PROCESSING` stage.  
4. If the final status is `COMPLETED`, all rows were imported successfully.  
5. If the final status is `COMPLETED_WITH_ERRORS`, call the Get batch errors endpoint to download the error report. The `errorCount` field tells you how many rows failed.  
6. If the final status is `FAILED`, the entire batch failed. Review the batch metadata and your CSV file for issues.

> ⚠️ Implement a polling interval with exponential backoff to avoid excessive API calls. A reasonable starting interval is 5 seconds, increasing gradually for long-running imports.

### Request example – Get batch status

```shell
curl -X GET \
  "https://{accountName}.vtexcommercestable.com.br/api/price-importer/pvt/batches/550e8400-e29b-41d4-a716-446655440000" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}"
```

### Response example – Get batch status

```json
{
  "batchId": "550e8400-e29b-41d4-a716-446655440000",
  "type": "base",
  "status": "COMPLETED_WITH_ERRORS",
  "outputs": [
    "email:user@example.com"
  ],
  "bytesProcessed": 13800000,
  "bytesTotal": 13800000,
  "errorCount": 12,
  "createdAt": "2026-01-12T20:00:00Z",
  "startedAt": "2026-01-12T20:01:00Z"
}
```

- `type`: indicates the import type (`base` for base prices, `fixed` for fixed prices).  
- `status`: current processing status. Here, `COMPLETED_WITH_ERRORS` means some rows failed.  
- `bytesProcessed` / `bytesTotal`: track upload and processing progress.  
- `errorCount`: number of rows that failed. Use this to decide whether to retrieve the error report.  
- `outputs`: configured notification channels for when the job finishes.

### Request example – Get batch errors

```shell
curl -X GET \
  "https://{accountName}.vtexcommercestable.com.br/api/price-importer/pvt/batches/550e8400-e29b-41d4-a716-446655440000/errors" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {appKey}" \
  -H "X-VTEX-API-AppToken: {appToken}"
```

### Response example – Get batch errors

```json
{
  "url": "https://pricing-bucket.s3.amazonaws.com/errors/550e8400-e29b-41d4-a716-446655440000.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=600"
}
```

The `url` field contains a pre-signed URL to download a CSV file with error details. This CSV has the same format as your original import file, with two additional columns: `Error Code` and `Error Message`. Download the file, review the errors, fix the affected rows, and re-submit them in a new import job.

### CSV format requirements

All CSV files must follow these formatting rules:

| Requirement | Value |
| :---- | :---- |
| Encoding | UTF-8 |
| Header row | Required (first row) |
| Delimiter | Comma (`,`) |
| Quote character | Double quote (`"`) |



### Output notifications

Use the `output` query parameter in the Import prices request to configure email notifications when the job finishes:

| Value | Description |
| :---- | :---- |
| `email` | Sends an email notification when processing completes. The target email address is configured separately in the platform settings. |