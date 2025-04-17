---
slug: "vtex-io-ttl-parameter-standardizeded-for-all-io-apps"
title: "VTEX IO: TTL parameter standardized for all IO apps"
createdAt: 2025-04-25T12:00:00.000Z
hidden: false
type: "info"
excerpt: "The TTL parameter was removed from services configuration and is now defined as 24 hours for all IO apps."
---

The [TTL (time-to-live) parameter](https://developers.vtex.com/docs/guides/vtex-io-documentation-service#ttl-management), which defines how long an IO app instance remains active without receiving new requests before shutting down, is now fixed at **24 hours** for all IO apps.

When an app is shut down due to an expired TTL, accessing it creates a new app instance. This process is called a cold start, and it can cause delays, longer response times, and potential timeout errors.

## What has changed?

Previously, the TTL parameter could be defined for [services](https://developers.vtex.com/docs/guides/vtex-io-documentation-service) by app developers between 10 and 60 minutes. This parameter is now defined as 24 hours for all IO apps. App developers can no longer determine this parameter, which will be ignored if declared in the `service.json` file.

## Why did we make this change?

This change aims to improve platform stability and performance.

Previously, developers could set the TTL manually, but without the proper tools for optimization. By managing this parameter internally, we aim to reduce cold starts — ensuring apps remain available with faster response times and fewer timeouts. This change also simplifies services configuration for developers, since it is one less parameter to worry about.

## What needs to be done?

No action is required by app developers and users. The change is applied automatically to all IO apps.
