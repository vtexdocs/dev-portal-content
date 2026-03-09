---
title: "VTEX IO Builder statuses and decommissioning"
slug: "2026-03-09-vtex-io-builder-statuses-and-decommissioning"
hidden: false
type: "info"
createdAt: "2026-03-09T14:00:00.000Z"
excerpt: "VTEX IO introduces Builder version statuses and decommissions older versions."
---

VTEX IO is introducing a new lifecycle management system for its [Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) versions, alongside the immediate decommissioning of several outdated versions. This change is crucial for maintaining platform stability, security, and efficiency.

## What has changed?

We are implementing two main updates:

1. **Defined Builder version statuses:** Every VTEX IO Builder version now has a defined status that communicates its lifecycle stage and level of support. The statuses are: **Beta, Stable, Deprecated, Decommissioned, and Non-functional**.
2. **Builder decommissioning:** The following outdated Builder versions have been moved to the **Decommissioned** status and are no longer supported for new development or updates:
    - **Node**:  versions `3.x` and `4.x`.
    - **Dotnet**: versions `0.x` and `1.x`.

For a detailed explanation of each status and the current status of each Builder version, please refer to the [Builder version statuses](https://developers.vtex.com/docs/guides/vtex-io-documentation-builder-version-statuses) documentation.

If you try to use a non-supported Builder, you will receive an error message in the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), such as the one below:

![Node Builder 4.x error](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/node-builder-4x-error.jpg)
*Error after trying to link an app with the deprecated Node `4.x` Builder.*

## Why did we make this change?

Defining clear statuses for Builder versions allows VTEX IO to systematically manage the platform's long-term efficiency, security, and stability. By retiring outdated or vulnerable components, we can ensure a better, safer, and more predictable development environment for all merchants and developers. The status system provides a necessary transition roadmap for developers, giving adequate notice to update their applications. The immediate decommissioning of the listed versions addresses critical stability and security concerns associated with older technology stacks.

## What needs to be done?

App Developers should adhere to the following guidelines:

- **Prefer Stable Versions:** When developing new apps or major versions, always use **Stable** Builder versions.
- **Update Apps:** Developers must prioritize updating existing applications that rely on **Deprecated, Decommissioned, or Non-functional** Builder versions to a currently **Stable** version.
    - Apps running on **Decommissioned** versions will continue to run, but you cannot link new workspaces or publish any new versions (minor, patch, or major).
    - Apps on **Non-functional** versions will cease to operate on the platform.

Review the [Builder version statuses](https://developers.vtex.com/docs/guides/vtex-io-documentation-builder-version-statuses) documentation to verify the status of the Builders used in your applications.
