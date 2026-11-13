---
title: "Updating the quantity of an inventory item"
slug: "updating-the-quantity-of-an-inventory-item"
hidden: false
createdAt: "2026-11-12T23:54:22.151Z"
updatedAt: "2026-11-12T23:54:22.151Z"
excerpt: "Learn how to update the quantity of an existing inventory item using the Sample Inventory API."
tags:
  - Sample Inventory API
---

In this guide, you will learn how to update the quantity of an existing inventory item by sending a request to the Sample Inventory API, and how to confirm that the change took effect.

## Before you begin

- Create an inventory item first and obtain its `id`. Follow [Creating an inventory item](/docs/guides/creating-an-inventory-item) to complete this prerequisite.
- Have a valid bearer token to send with the `Authorization: Bearer <token>` header.
- Know the base URL for requests: `https://inventory.example.com`.

## Instructions

### Step 1 — Send the update request

1. Note the `id` of the item you want to update. You obtain this `id` from the response of the creation guide, for example `item-123`.

2. Send a `PATCH` request to `/items/{id}`, replacing `{id}` with the item's `id`, and include the `Authorization: Bearer <token>` header.

```http
PATCH /items/item-123
Authorization: Bearer <token>
Content-Type: application/json
```

1. Include a JSON body with the new `quantity` value.

```json
{
  "quantity": 7
}
```

### Step 2 — Confirm the update

1. Check that the response status is `200`.

2. Confirm the response body reflects the updated `quantity`.

```json
{
  "id": "item-123",
  "sku": "shirt-blue",
  "quantity": 7
}
```

The item now shows the new `quantity` value in the response body. Compare this value against the one you sent in your request to confirm the update succeeded.
