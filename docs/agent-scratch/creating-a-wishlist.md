---
title: "Creating a wishlist"
slug: "creating-a-wishlist"
hidden: false
createdAt: "2026-11-16T23:03:01.600Z"
updatedAt: "2026-11-16T23:03:01.600Z"
excerpt: "Learn how to create a wishlist through the API or in the Admin."
tags:
  - Wishlists
---

In this guide, you will learn how to create a wishlist, either by calling the API directly or through the Admin. Creating a wishlist lets you group products a shopper wants to save for later.

## Before you begin

- Have an `Authorization: Bearer <token>` value to authenticate requests.
- Know the test base URL for requests: `https://wishlist.example.com`.

## Instructions

### Step 1 — Create a wishlist via the API

1. Send a `POST` request to `/wishlists` on the base URL, with an `Authorization: Bearer <token>` header and a JSON body containing a `name` field.

```json
{
  "name": "Winter"
}
```

1. Check the response. A successful request returns HTTP `201` with a JSON body containing the new wishlist's `id`, `name`, and an empty `items` array.

```json
{
  "id": "wl-1",
  "name": "Winter",
  "items": []
}
```

The returned `id` identifies the created wishlist for later use.

### Step 2 — Create a wishlist in the Admin

1. Open the **Wishlists** page in the Admin.
2. Select `New wishlist`.
3. Type a name, for example `Winter`, in the **Name** field.
4. Select `Save`.

The new wishlist now appears listed on the **Wishlists** page.
