---
title: "Headless CMS Plugin v1.0.10: Bug fix for sync error"
slug: "2023-09-06-fixed-headless-cms-plugin"
type: "fixed"
createdAt: "2023-09-06T10:28:00.000Z"
excerpt: "The SyntaxError issue has been resolved in the latest release,`v1.0.10`"
---

In version [`v1.0.8` of the Headless CMS Plugin](https://developers.vtex.com/updates/release-notes/2023-07-31-improved-headless-cms-plugin), running the `vtex cms sync` command would lead to the following error message: `SyntaxError: Cannot use import statement outside a module.` This issue has been resolved in the latest release,`v1.0.10`.

> ⚠️ Headless CMS is currently only available for FastStore projects.

## What needs to be done?

To update the Headless CMS plugin to `v1.0.10`, follow the steps below:

1. Access the VTEX IO CLI and log in to your VTEX account:

    > ⚠️  Remember to replace the values between curly brackets according to your account name.

        ```bash
        vtex login {account}
        ```

2. Update the `@vtex/cli-plugin-cms` to `v1.0.10` by running the following command:

        ```bash
        vtex plugins update
        ```

3. Open your FastStore project.
4. Change to the `cms` folder and run `vtex cms sync`. Once your changes are synced, you should see the following message:

        ```bash
        CMS synced successfully…
        ```
