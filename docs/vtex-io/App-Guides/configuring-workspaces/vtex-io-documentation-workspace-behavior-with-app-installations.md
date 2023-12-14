---
title: "Workspace behavior with app installations"
slug: "vtex-io-documentation-workspace-behavior-with-app-installations"
hidden: false
createdAt: "2023-12-14T10:00:00.000Z"
updatedAt: "2023-12-14T10:00:00.000Z"
---

On VTEX IO, [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) function similarly to [Git branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) with automatic [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing). Your work in development and production workspaces is always based on what's in the master workspace.

Below is an example to illustrate the behavior of apps when performing operations on workspaces.

Imagine there is a VTEX account with four identical workspaces:

- `master`: `appA@1.x`
- `prod1`: `appA@1.x`
- `prod2`: `appA@1.x`
- `dev1`: `appA@1.x`

The following sections present scenarios based on this example. Check what happens when you:

- [Install an app on development or production](#install-an-app-on-development-or-production)
- [Install an app on master](#install-an-app-on-master)
- [Promote a workspace](#promote-a-workspace)

## Install an app on development or production

[Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) on a development or production workspace does not affect other workspaces.

Considering the given example, imagine the following actions:

- Installing `appA@2.x` on `prod1`
- Installing `appC@2.x` on `prod2`
- Installing `appC@3.x` on `dev1`

This would be the result:

- `master`: `appA@1.x`
- `prod1`: `appA@2.x`
- `prod2`:`appA@1.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appC@3.x`

## Install an app on master

When you install an app on the master workspace, it is installed on every workspace that does not have this app installed. If a workspace has the same app installed with another major version, the app version on this workspace is unchanged.

Considering the given example, imagine the following action:

- Installing `appB@0.x` on `master`

This would be the result:

- `master`: `appA@1.x`, `appB@0.x`
- `prod1`: `appA@2.x`, `appB@0.x`
- `prod2`:`appA@1.x`, `appB@0.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appB@0.x`, `appC@3.x`

## Promote a workspace

When a production workspace is [promoted to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master), all the other workspaces are updated to reflect the changes seen in the promoted workspace.

After promoting `prod2` to `master`, we have the following result:

- `master`: `appA@1.x`, `appB@0.x`, `appC@2.x`
- `prod1`: `appA@2.x`, `appB@0.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appB@0.x`, `appC@3.x`

> ⚠ After promoting a workspace, the name of the promoted workspace will not appear in the [list of workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#workspace-list), since it became the new master workspace.
