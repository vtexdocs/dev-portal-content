---
title: "Creating an inventory item"
slug: "creating-an-inventory-item"
hidden: false
createdAt: "2026-11-12T23:54:22.151Z"
updatedAt: "2026-11-12T23:54:22.151Z"
excerpt: "Learn how to create a new inventory item using the Sample Inventory API."
tags:
  - Sample Inventory API
---

In this guide, you will learn how to create a new inventory item by sending a request to the Sample Inventory API. Creating an item returns an identifier you need later, for example to update that item's quantity.

## Before you begin

- A bearer token for authenticating requests, sent in the `Authorization: Bearer <token>` header.
- The test base URL for the API: `https://inventory.example.com`.

## Instructions

Creating an item takes a single request, so the steps are listed directly below.

1. Send a `POST` request to `/items` on the base URL, with the header `Authorization: Bearer <token>` and a JSON content type.
2. Include a JSON body with the `sku` and `quantity` fields. For example:

```json
{
  "sku": "shirt-blue",
  "quantity": 10
}
```

1. Check the response. A successful request returns HTTP 201 with a JSON body containing `id`, `sku`, and `quantity`. For example:

```json
{
  "id": "item-123",
  "sku": "shirt-blue",
  "quantity": 10
}
```

Save the returned `id` value. It identifies the item for future operations, such as [updating the quantity of an inventory item](/docs/guides/updating-the-quantity-of-an-inventory-item).
