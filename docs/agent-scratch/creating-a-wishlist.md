---
title: "Creating a wishlist"
slug: "creating-a-wishlist"
hidden: false
createdAt: "2026-11-13T17:32:31.147Z"
updatedAt: "2026-11-13T17:32:31.147Z"
excerpt: "Learn how to create a wishlist through the Wishlist API."
tags:
  - Wishlist
---

In this guide, you will learn how to create a wishlist by sending a request to the Wishlist API. It covers the request format and the response you should expect once the wishlist is created.

## Before you begin

- An `Authorization: Bearer <token>` header value to authenticate your requests.

  > ⚠️ **Content gap:** How a developer obtains this bearer token — expected from authentication or API reference documentation — unavailable because that source was not among the sources provided for this draft.

- The test base URL, `https://wishlist.example.com`, to send requests to.

## Instructions

1. Send a `POST` request to `/wishlists` on the test base URL, with the `Authorization: Bearer <token>` header and a JSON body containing a `name` field. For example:

   ```json
   {
     "name": "Winter"
   }
   ```

2. Check the response. A successful request returns an HTTP `201` status with a JSON body containing the new wishlist's `id`, its `name`, and an empty `items` array. For example:

   ```json
   {
     "id": "wl-1",
     "name": "Winter",
     "items": []
   }
   ```

You should now have a new wishlist identified by the returned `id`, with the `name` you submitted and an empty `items` list, confirming that the wishlist was created successfully.
