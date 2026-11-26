---
title: "Updating the quantity of an inventory item"
slug: "updating-inventory-item-quantity"
hidden: false
createdAt: "2026-11-23T20:27:52.775Z"
updatedAt: "2026-11-23T20:27:52.775Z"
excerpt: "Learn how to update the quantity of an existing item in the Sample Inventory API."
tags:
  - Sample Inventory API
---

In this guide, you will learn how to update the quantity of an existing item in the Sample Inventory API. This task requires an item that already exists in the system, as described in [Creating an inventory item](/docs/guides/creating-an-inventory-item).

## Before you begin

Before you begin, make sure you have the following:

- An existing item ID, such as `item-123`. You get this ID by completing the steps in [Creating an inventory item](/docs/guides/creating-an-inventory-item).
- A valid `Authorization: Bearer <token>` credential for the Sample Inventory API.

> ℹ️ The examples in this guide use the base URL `https://inventory.example.com`.

## Instructions

### Step 1 — Sending the update request

1. Send a `PATCH` request to `/items/{id}` on the base URL `https://inventory.example.com`. For example, to update the item with ID `item-123`, send the request to `/items/item-123`.
2. Set the `Authorization: Bearer <token>` header.
3. Set the request body as JSON containing the new `quantity` value.

The following example updates the quantity of `item-123` to seven units.

```http
PATCH /items/item-123 HTTP/1.1
Host: inventory.example.com
Authorization: Bearer <token>
Content-Type: application/json

{
  "quantity": 7
}
```

### Step 2 — Confirming the result

1. Check that the response status is `200`.
2. Inspect the response body. It echoes the item's `id` and `sku`, along with the updated `quantity`.

```json
{
  "id": "item-123",
  "sku": "shirt-blue",
  "quantity": 7
}
```

After you complete these steps, the item now shows the new quantity. Compare the `quantity` field in the response body against the value you sent to confirm the update.
