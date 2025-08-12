---
title: "FastStore: Supports refresh token session"
slug: "2025-08-15-faststore-refresh-token"
hidden: false
type: "added"
createdAt: "2025-08-15T00:00:00.219Z"
updatedAt: "2025-08-15T00:00:00.219Z"
excerpt: "FastStore now supports refresh tokens, allowing users to stay logged in longer without re-authenticating, improving the shopping experience."
---

FastStore storefronts now support the [refresh token flow](https://developers.vtex.com/docs/guides/faststore/security-implementing-refresh-token), ensuring users stay logged in to their store sessions for a longer time without needing to reauthenticate. 

## What has changed?

Previously, user sessions in stores were managed by a cookie that expired after 24 hours, requiring users to log in again if they returned after a day.

With the refresh token, users remain logged in for longer without needing to manually reauthenticate. As long as the user accesses the store within the refresh token’s configured timeframe (1, 7 or 30 days), their session is automatically renewed, keeping them logged in.

## Why did we make this change?

By extending user session duration, shoppers can remain logged in for longer, resulting in a more continuous and improved shopping experience, and fewer login prompts.

## What needs to be done?

To enable the refresh token flow in your account, see the instructions in the [Implementing refresh token](https://developers.vtex.com/docs/guides/faststore/security-implementing-refresh-token) guide.
