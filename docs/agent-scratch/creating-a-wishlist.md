---
title: "Creating a wishlist"
slug: "creating-a-wishlist"
hidden: false
createdAt: "2026-11-13T22:30:52.939Z"
updatedAt: "2026-11-13T22:30:52.939Z"
excerpt: "Learn how to create a wishlist using the API or the Admin."
tags:
  - Wishlists
---

In this guide, you will learn how to create a wishlist, either by calling the API directly or through the Admin. Use the API when you need to automate wishlist creation from your own application, and use the Admin when you want to create a wishlist manually, without writing code.

## Before you begin

- API requests require an `Authorization: Bearer <token>` header.
- The test base URL for API requests is `https://wishlist.example.com`.

> ⚠️ **Content gap:** How to obtain the bearer token used in the `Authorization` header — expected from authentication or API reference documentation — unavailable because that source was not among the sources provided for this guide.

## Instructions

### Step 1 — Creating a wishlist via the API

1. Send a `POST` request to `/wishlists` on the base URL `https://wishlist.example.com`.
2. Include the `Authorization: Bearer <token>` header.
3. Set the request body to JSON containing the wishlist `name`, for example:

```json
{
  "name": "Winter"
}
```

1. Check the response. A successful request returns HTTP 201 with a JSON body containing `id`, `name`, and an empty `items` array, for example:

```json
{
  "id": "wl-1",
  "name": "Winter",
  "items": []
}
```

### Step 2 — Creating a wishlist via the Admin

1. In the Admin, go to **Wishlists**.
2. Click `New wishlist`.
3. In the **Name** field, type the wishlist name, for example `Winter`.
4. Click `Save`.

The new wishlist now appears listed on the **Wishlists** page.
