---
title: "FastStore: Supports refresh token session"
slug: "2025-08-15-faststore-refresh-token"
hidden: false
type: "added"
createdAt: "2025-08-15T00:00:00.219Z"
updatedAt: "2025-08-15T00:00:00.219Z"
excerpt: "FastStore now supports refresh tokens, allowing users to stay logged in longer without re-authenticating, improving the shopping experience."
---

FastStore storefronts now support the [refresh token](https://developers.vtex.com/docs/guides/refresh-token-flow-for-headless-implementations) feature, ensuring users stay logged in to their store sessions for a longer time without needing to reauthenticate. 

## What has changed?

Previously, user sessions in stores were managed by a cookie that expired after 24 hours. This limited duration disrupted the user experience, especially when users returned after a day and found their session had ended.

With the refresh token, the cookie's duration is extended, ensuring sessions last as long as the cookie remains.

## Why did we make this change?

By extending user session duration, shoppers can remain logged in for longer periods, resulting in a more continuous and improved shopping experience, with fewer login prompts.

## What needs to be done?

To enable the refresh token flow in your account, see the instructions on [Implementing refresh token](/tbd) guide.
