---
title: "I can't access the Headless CMS"
slug: "unable-to-access-headless-cms"
excerpt: "Permission denied error in faststore cms-sync or vtex cms sync indicates user access issues."
tags:
    - Headless CMS
    - License Manager
---

**Keywords:** Headless CMS, FastStore, CLI

FastStore users may encounter the following errors after using the commands `faststore cms-sync` or `vtex cms sync`.

| Error message | Possible cause | Solution |
| --- | --- | --- |
| `Error: Permission denied` | The user role does not have the required CMS permissions. | [Grant user Admin access](#grant-user-admin-access) |
| `Error: User indicated by VtexIdclientAutCookie is not authorized to access the indicated resource` | The user does not have access to the required CMS resources in License Manager. | [Grant user Admin access](#grant-user-admin-access) |
| `Error: SyntaxError: Unexpected token` | The VTEX IO CLI environment is not configured correctly. | [Check VTEX IO CLI environment](#check-vtex-io-cli-environment) |

## Solutions

To solve your issue, follow one of the paths below based on the error message displayed in your CLI.

### Grant user Admin access

Use this path when the error is related to authorization or permissions in License Manager.

1. Open the VTEX Admin and go to **Account Settings > User Roles.**

   ![license-manager-cms](https://vtexhelp.vtexassets.com/assets/docs/src/cms-license-manager___57f69d96f44f3d29413f2651df7d98c8.png)

2. Under **Roles**, select the role associated with the user requesting CMS permissions. For example, **Owner (Admin Super)**.
3. In **Products and Resources**, find and click **CMS**.

   ![role-permission](https://vtexhelp.vtexassets.com/assets/docs/src/cms-license-manager-role___f67a8717b5411664dd29cfa9de1764bc.gif)

4. Make sure both **See CMS menu on the top-bar** and **Settings** are checked.
5. Go to the **Users** section and add the email of the user who needs CMS access.
6. Click `Save`.
7. Ask the user who requested access to run `faststore cms-sync` or `vtex cms sync` again.
8. Confirm the command runs without `Error: Permission denied` or any authorization errors.

### Check VTEX IO CLI environment

Use this path when the error points to CLI execution or environment configuration.

#### Verify authentication
1. Open the terminal and run `vtex whoami`.
2. Confirm that the displayed account and workspace are the ones expected for CMS sync.
3. If you are not logged in, or if the account or workspace is incorrect, run `vtex login` and authenticate with the correct account and workspace.

#### Update VTEX IO CLI
1. Run `vtex autoupdate` in Windows Terminal.
2. Run `vtex -v` to verify that the VTEX IO CLI and Node versions are updated.

#### Verify the workspace
1. Run `vtex workspace list` to see the available workspaces.
2. If required, switch to the correct workspace with `vtex use <workspace-name>`.

#### Retry the sync in verbose mode
1. After adjusting the environment, run `vtex cms sync`.
2. If the error persists, run `vtex cms sync --verbose` to get more details about the sync error.
