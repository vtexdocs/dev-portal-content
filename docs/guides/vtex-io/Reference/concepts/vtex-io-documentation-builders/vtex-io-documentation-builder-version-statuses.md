---
title: "Builder version statuses"
slug: "vtex-io-documentation-builder-version-statuses"
excerpt: Learn what are builder version statuses and the status of each builder version
hidden: false
createdAt: "2026-03-09T14:00:00.000Z"
updatedAt: "2026-03-09T14:00:00.000Z"
---

The [VTEX IO platform](https://developers.vtex.com/docs/guides/vtex-io-overview) uses a set of statuses to manage the lifecycle of its [Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) versions. A **status** defines the level of support and usability assigned to a specific version of a Builder.

The primary purpose of defining these statuses is to ensure the platform's long-term efficiency, security, and stability. By guiding developers and merchants toward the most up-to-date and recommended versions, we can systematically retire outdated or vulnerable components. The statuses provide a roadmap and a necessary transition period, allowing developers enough time to update their applications whenever a status change is announced.

This document outlines the definition of each status and presents a table detailing the current status of VTEX IO Builder versions.

## Understanding Builder statuses

The possible statuses a Builder version can have are:

- **Beta:** Pre-release version containing experimental features not yet stable for production.
- **Stable:** Fully functional and recommended for use.
- **Deprecated:** Existing apps are permitted to run, link, and publish minor or patch updates, but new apps or major versions cannot be linked or published.
- **Decommissioned:** Existing apps can run, but linking or publishing new apps or any new versions is not permitted.
- **Non-functional:** Apps are not operational on the platform.

The table below summarizes what can be done for each status.

| Status | Run on the platform | Link and publish new versions in a published major version of an existing app | Link and publish a new app or a major version of an existing app |
| - | :-: | :-: | :-: |
| Beta | ✅ | ✅ | ✅ |
| Stable | ✅ | ✅ | ✅ |
| Deprecated | ✅ | ✅ | ❌ |
| Decommissioned | ✅ | ❌ | ❌ |
| Non-functional | ❌ | ❌ | ❌ |

If you try to use a non-supported Builder, you will receive an error message in the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), such as the ones below:

![GraphQL Builder 1.x warning](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/graphql-1x-builder-warn.jpg)
*Warning after trying to link an app (major published) with the deprecated GraphQL `1.x` Builder.*

![Node Builder 4.x error](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/node-builder-4x-error.jpg)
*Error after trying to link an app (major published) with the deprecated Node `4.x` Builder.*

## Current statuses

The table below shows the current statuses of each Builder version:

| Builder | Status |
| - | - |
| `dotnet` | Stable: `2.x`. Decommissioned: `0.x`, `1.x`. |
| `graphql` | Stable: `2.x`. Deprecated: `1.x`. |
| `node` | Stable: `6.x`, `7.x`. Decommissioned: `3.x`, `4.x`. |

> ℹ️ If you want to use a Builder version that is not listed here and you are unsure of its status, open a ticket with our [support](http://help.vtex.com/en/support).
