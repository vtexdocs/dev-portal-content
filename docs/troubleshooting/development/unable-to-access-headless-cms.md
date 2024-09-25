---
title: "I can’t access the Headless CMS"
slug: "unable-to-access-headless-cms"
excerpt: "Permission denied error in faststore cms-sync or vtex cms sync indicates user access issues."
tags:
    - headless-cms
    - license-manager
---

**Keywords:** Headless CMS | FastStore| CLI

If you encounter the error `Error: Permission denied` or `Error: User indicated by VtexIdclientAutCookie is not authorized to access the indicated resource` when using `faststore cms-sync` or `vtex cms sync`, this issue is related to the user permissions needed to execute the command and save resources.

## Solution

To solve this problem, ask the user who granted your user Admin access to follow the steps below:

### Granting user Admin access

1. Open the VTEX Admin and go to **Account Settings > User Roles.**

   ![license-manager-cms](https://vtexhelp.vtexassets.com/assets/docs/src/cms-license-manager___57f69d96f44f3d29413f2651df7d98c8.png)

2. Under **Roles**, select the role associated with the user requesting CMS permissions. For example, **Owner (Admin Super)**.

3. In **Products and Resources**, find and click **CMS**.

   ![role-permission](https://vtexhelp.vtexassets.com/assets/docs/src/cms-license-manager-role___f67a8717b5411664dd29cfa9de1764bc.gif)

4. Make sure both **See CMS menu on the top-bar** and **Settings** are checked.

5. Navigate to the **Users** section and add the email of the user who needs access to the CMS.

6. Click `Save`. Ask the user who requested access to run the `faststore cms-sync` or `vtex cms sync` command again. They should now be able to sync their changes.
