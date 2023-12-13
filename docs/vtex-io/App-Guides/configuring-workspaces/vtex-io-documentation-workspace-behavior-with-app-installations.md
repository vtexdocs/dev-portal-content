---
title: "Workspace behavior with app installations"
slug: "vtex-io-documentation-workspace-behavior-with-app-installations"
hidden: false
createdAt: "2023-12-14T10:00:00.000Z"
updatedAt: "2023-12-14T10:00:00.000Z"
---

On VTEX IO, [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) work like [git](https://git-scm.com/) [branches](https://www.atlassian.com/git/tutorials/using-branches) with automatic [rebase](https://www.w3docs.com/learn-git/git-rebase.html). You always have your work on top of what is in production (master).

Below is an example to illustrate the behavior of apps when performing operations on workspaces.

Imagine there is a VTEX account with four identical workspaces:

- `master`: `appA@1.x`
- `prod1`: `appA@1.x`
- `prod2`: `appA@1.x`
- `dev1`: `appA@1.x`

## Install an app on development or production

[Installing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) on a development or production workspace does not affect other workspaces.

The following actions:

- Install `appA@2.x` on `prod1`
- Install `appC@2.x` on `prod2`
- Install `appC@3.x` on `dev1`

Results in:

- `master`: `appA@1.x`
- `prod1`: `appA@2.x`
- `prod2`:`appA@1.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appC@3.x`

## Install an app on master

When installing an app on the master workspace, it is installed on every workspace that does not have this app installed. If a workspace has the same app installed with another major version, the app version on this workspace is unchanged.

The following action:

- Install `appB@0.x` on `master`

Results in:

- `master`: `appA@1.x`, `appB@0.x`
- `prod1`: `appA@2.x`, `appB@0.x`
- `prod2`:`appA@1.x`, `appB@0.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appB@0.x`, `appC@3.x`

## Promote workspace

When a production workspace is [promoted to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master), all the other workspaces are updated to reflect the changes seen in the promoted workspace.

After promoting `prod2` to `master`, we have the following result:

- `master`: `appA@1.x`, `appB@0.x`, `appC@2.x`
- `prod1`: `appA@2.x`, `appB@0.x`, `appC@2.x`
- `dev1`: `appA@1.x`, `appB@0.x`, `appC@3.x`

> ⚠ After promoting a workspace, the name of the promoted workspace will not appear in the [list of workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#workspace-list), since it became the new master workspace.
