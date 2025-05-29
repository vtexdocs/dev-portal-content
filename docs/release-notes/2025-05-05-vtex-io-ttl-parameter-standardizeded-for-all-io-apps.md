---
slug: "vtex-io-ttl-parameter-standardizeded-for-all-io-apps"
title: "VTEX IO: TTL parameter standardized for all IO apps"
createdAt: 2025-05-05T12:00:00.000Z
hidden: false
type: "info"
excerpt: "The TTL parameter was removed from services configuration and is now defined as 24 hours for all IO apps."
---

The [TTL (time-to-live) parameter](https://developers.vtex.com/docs/guides/vtex-io-documentation-service#ttl-management), which defines how long an IO app instance remains active before shutting down if no new requests are received, is now fixed at **24 hours** for all IO apps.

When an app is shut down due to an expired TTL, accessing it creates a new app instance. This process is called a cold start, and it can cause delays, longer response times, and potential timeout errors.

## What has changed?

Previously, app developers could define the TTL parameter for [services](https://developers.vtex.com/docs/guides/vtex-io-documentation-service) with values between 10 and 60 minutes. This parameter is now fixed at 24 hours for all IO apps. App developers can no longer determine this parameter, which will be ignored if declared in the `service.json` file.

## Why did we make this change?

This change aims to improve platform stability and performance.

Previously, developers could set the TTL manually, but lacked the proper tools to optimize it. By managing this parameter internally, we aim to reduce cold starts — keeping apps available with faster response times and fewer timeouts. This change also simplifies service configuration, removing one more parameter developers need to manage.

## What needs to be done?

No action is required from app developers or users. The change is applied automatically to all IO apps.
