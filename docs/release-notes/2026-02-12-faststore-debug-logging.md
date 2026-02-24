---
title: "FastStore: Debug logging for third-party scripts"
slug: "2026-02-12-faststore-debug-logging"
type: improved
createdAt: "2026-02-12T11:00:00.000Z"
updatedAt: "2026-02-12T11:00:00.000Z"
hidden: false
excerpt: "FastStore now supports the experimental `enableScriptsLogs` flag, improving troubleshooting for third-party scripts and analytics."
tags:
    - FastStore
---

FastStore now supports the experimental `enableScriptsLogs` flag to help developers troubleshoot third-party scripts and analytics behavior through additional debug logs.

## What has changed?

You can now enable `enableScriptsLogs` in your [`discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/developer-tools-config-options) file.

When this flag is set to `true`, FastStore adds browser console logs for:

- Partytown debug calls and forwarded calls.
- Google Tag Manager (GTM) `dataLayer.push` events, especially when validating tags with the `gtm_debug` flow.
- VTEX scripts such as RC (`sendrc`) and Activity Flow calls.
- VTEX Search Events payloads sent by the storefront.

## Why did we make this change?

Third-party scripts and analytics integrations can be difficult to debug, especially when they run in different execution contexts (for example, offloaded to Partytown). This flag makes it easier to validate event flows and script execution without custom instrumentation, reducing time to identify issues that can impact measurement accuracy and user experience.

## What needs to be done?

To receive this improvement on your store, follow the instructions on [Debug logging for third-party scripts](https://developers.vtex.com/docs/guides/faststore/developer-tools-enable-scripts-logs).
