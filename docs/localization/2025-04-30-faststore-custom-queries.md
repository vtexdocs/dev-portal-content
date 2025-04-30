---
title: "FastStore: Use `GET` requests for custom queries to improve store caching"
slug: "2025-04-30-faststore-custom-queries"
type: improved
excerpt: "Ensure proper caching by using GET requests for custom queries in FastStore."
createdAt: "2025-04-30T00:00:00.007Z"
updatedAt: "2025-04-30T10:30:00.007Z"
hidden: false
---

To ensure proper caching behavior when navigating store pages (such as Home, PDP, and PLP), use `GET` instead of `POST` for API requests in custom queries. `GET` requests are cacheable by default, while `POST` requests bypass caching.

## What has changed?

Previously, some custom queries used `POST` methods, which prevented caching. Now, queries with the `Query` suffix in their names automatically use `GET`. For example, rename `getOrderForm` to `getOrderFormQuery`.

## What needs to be done?

To enable proper caching related to custom queries do the following:

1. Review your project's custom queries using `POST` method.
2. Rename these queries by adding the `Query` suffix to default to `GET`. For example:

- Uncached (`POST`): `getOrderForm`
- Cached (`GET`): `getOrderFormQuery` (ensures proper store caching)
