---
title: "FastStore: Debug logging for third-party scripts"
slug: "2026-02-20-faststore-enable-scripts-logs"
type: improved
createdAt: "2026-02-20T11:00:00.000Z"
updatedAt: "2026-02-20T11:00:00.000Z"
hidden: false
excerpt: "FastStore now supports the experimental enableScriptsLogs flag, improving troubleshooting for third-party scripts and analytics."
tags:
    - FastStore
---

FastStore now supports the experimental `enableScriptsLogs` flag to help developers troubleshoot third-party scripts and analytics behavior by enabling additional debug logs.

## What has changed?

You can now enable `experimental.enableScriptsLogs` in your `discovery.config.js` file.

When this flag is set to `true`, FastStore enables additional debugging capabilities, such as:

- **Partytown debug logs:** Enables Partytown `debug` and `logCalls`.
- **Google Tag Manager observability:** Adds debug logs for `dataLayer.push` calls.
- **VTEX scripts observability:** Adds debug logs for VTEX scripts (for example, RC `sendrc` and Activity Flow calls).
- **VTEX Search Events observability:** Logs payloads sent to VTEX Search Events.

## Why did we make this change?

Third-party scripts and analytics integrations can be difficult to debug, especially when they run in different contexts (for example, offloaded to Partytown). This flag makes it easier to validate events and script execution without requiring custom instrumentation or code changes.

## What needs to be done?

1. Update the FastStore packages to the latest version by running `yarn upgrade -L --scope @faststore`.
2. Enable the flag in `discovery.config.js`:

```js
module.exports = {
  // ...
  experimental: {
    enableScriptsLogs: true,
  },
}
```

> ℹ️ This flag increases browser console output. We recommend enabling it only while debugging (for example, in development or staging environments).

For more information about configuration options, see [Configuration options for `discovery.config.js`](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options).
