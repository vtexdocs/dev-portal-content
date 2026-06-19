---
title: "Transferring credit"
slug: "transferring-credit"
excerpt: "Learn how to implement credit transfer flow between marketplaces and sellers in VTEX Ads."
hidden: false
createdAt: "2026-06-19T00:00:00.000Z"
updatedAt: "2026-06-19T00:00:00.000Z"
---
Credit transfer is the flow that allows marketplaces to transfer advertising credits to their sellers. This guide details the endpoints that marketplaces must implement and the webhook they must consume to integrate with VTEX Ads.

> ℹ️ The Authentication model follows [Basic Auth](https://developers.vtex.com/docs/guides/integrating-vtex-ads-with-external-marketplaces#vtex-ads-to-marketplace).

![transferring-credit](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/VTEX%20Ads/integrating-vtex-ads-with-external-marketplaces/transferring-credit.png)

## Endpoints to be implemented by the marketplace

Authentication: Basic Auth

### 1. Balance inquiry (`GET /checking_account`)

- **Purpose:** Check the seller's available balance.
- **Query parameters:** `seller_id`, `publisher_id` (optional, used only when an entity manages multiple publishers).
- **Success response (200 OK):**

  ```json
  { "total": "1111.00" }
  ```

### 2. Transfer request (`POST /checking_account/transfer`)

- **Purpose:** Request the transfer of an amount.
- **Request body:**

  ```json
  {
    "amount": "10.00",
    "seller_id": "SELLER_ID",
    "publisher_id": "PUBLISHER_ID",
    "transfer_identity_id": "uuid"
  }
  ```

- **Responses:**
  - **Synchronous (Success):** `201 Created`

    ```json
    {
      "transaction_id": "TRANSACTION_ID",
      "status": "success"
    }
    ```

  - **Synchronous (Failure):** `400 Bad Request`

    ```json
    {
      "transaction_id": "TRANSACTION_ID",
      "status": "failure",
      "message": "Reason for rejection"
    }
    ```

  - **Asynchronous:** `202 Accepted`

    ```json
    {
      "transaction_id": "TRANSACTION_ID",
      "status": "processing"
    }
    ```

## Webhook to be consumed by the marketplace

The marketplace must call the VTEX Ads webhook to notify the final status of each transfer. For the endpoint path, authentication headers, and the full request and response specification, see [Notify credit transfer status](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/webhook/marketplace/transfers/-publisher%5Fid-) in the VTEX Ads API reference.

- **Payload:**

  ```json
  {
    "transaction_id": "TRANSACTION_ID",
    "status": "success"
  }
  ```

  or

  ```json
  {
    "transaction_id": "TRANSACTION_ID",
    "status": "failure",
    "message": "Problem description"
  }
  ```

- **Retry logic:** In case of webhook call failure, the marketplace must retry.
- **Expected response:** `204 No Content`
