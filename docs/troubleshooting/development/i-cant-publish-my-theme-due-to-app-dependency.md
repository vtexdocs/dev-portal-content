---
title: "I can't publish my theme due to app dependency"
slug: "i-cant-publish-my-theme-due-to-app-dependency"
hidden: false
createdAt: "2026-03-20T00:00:00.000Z"
updatedAt: "2026-03-20T00:00:00.000Z"
excerpt: "Learn how to fix app dependency validation errors when publishing a theme or app in VTEX IO."
tags:
    - VTEX IO
    - Store Framework
    - Apps
---

**Keywords:** Dependency | App | Theme | Publish | VTEX IO CLI

When attempting to [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) a new [store theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) or [publish an app in VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app), you may encounter a [dependency](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies) validation error.

This issue occurs when an app dependency is [deprecated](https://developers.vtex.com/docs/guides/vtex-io-documentation-deprecating-an-app), a release candidate, or a pre-release [version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version). In this scenario, VTEX IO blocks theme installation or app publishing and displays an error similar to the following:

`Error validating app dependencies: Error with dependency {appvendor}.{appname}@{appversion}: App cannot be deprecated, a release candidate version or a prerelease version: {appvendor}.{appname}@{appversion}`

## Solution

To solve this issue, follow the steps below:

1. In the error message, identify the specific app causing the issue with the format `{appvendor}.{appname}@{appversion}`. For example: `template.mygiftcard@0.x`.
2. If the dependent app version is deprecated, a release candidate, or a pre-release, deprecate it so the system can use a stable version. Run:

   ```sh
   vtex deprecate {appvendor}.{appname}@{appversion}
   ```

3. To install the latest stable version of the app in an account, run:

   ```sh
   vtex update {appvendor}.{appname}
   ```

4. If deprecation is not needed and you want to republish that specific version, run:

   ```sh
   vtex undeprecate {appvendor}.{appname}@{appversion}
   ```

5. After adjusting dependencies, try installing the theme or publishing the app again.

> ⚠️ If the issue persists, open a ticket with [VTEX Support](https://support.vtex.com/hc/en-us).
