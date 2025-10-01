---
title: "FastStore: Support for refresh token sessions"
slug: "2025-09-19-faststore-refresh-token"
hidden: false
type: "added"
createdAt: "2025-09-19T00:00:00.219Z"
updatedAt: "2025-09-19T00:00:00.219Z"
excerpt: "FastStore now supports refresh tokens, allowing users to stay logged in longer without reauthenticating, improving the shopping experience."
---

FastStore storefronts now support the [refresh token flow](https://developers.vtex.com/docs/guides/faststore/security-enabling-refresh-token), ensuring users stay logged in longer without reauthenticating.

## What has changed?

Previously, user sessions in stores were managed by a cookie that expired after 24 hours, requiring users to log in again if they returned after a day.

With the refresh token, users remain logged in for longer without manually reauthenticating. As long as the user accesses the store within the refresh token’s configured timeframe (1, 7, or 30 days), their session is automatically renewed, keeping them logged in.

## Why did we make this change?

By extending session duration, shoppers can remain logged in longer, resulting in a more seamless shopping experience and fewer login prompts.

## What needs to be done?

To enable the refresh token flow in your account, see the instructions in the [Enabling refresh token on FastStore](https://developers.vtex.com/docs/guides/faststore/security-enabling-refresh-token) guide.
