---
title: "Creating an inventory item"
slug: "creating-an-inventory-item"
hidden: false
createdAt: "2026-11-23T20:27:52.775Z"
updatedAt: "2026-11-23T20:27:52.775Z"
excerpt: "Learn how to create an inventory item using the Sample Inventory API."
tags:
  - Sample Inventory API
---

In this guide, you will learn how to create an inventory item by sending a request to the Sample Inventory API. The item's `id` returned by this request is required to update its quantity later, so keep it on hand once you finish this guide.

## Before you begin

- An `Authorization: Bearer <token>` value to authenticate your requests.
- The test base URL, `https://inventory.example.com`.

## Instructions

1. Send a `POST` request to `/items` on the base URL, with the `Authorization: Bearer <token>` header and a JSON body containing the `sku` and `quantity` of the item you want to create.

```json
{
  "sku": "shirt-blue",
  "quantity": 10
}
```

1. Check the response. A successful creation returns HTTP 201 with a JSON body containing the generated `id` for the new item, along with the `sku` and `quantity` you sent.

```json
{
  "id": "item-123",
  "sku": "shirt-blue",
  "quantity": 10
}
```

Note the `id` returned in the response. You need it to update this item's quantity in a follow-up guide.
