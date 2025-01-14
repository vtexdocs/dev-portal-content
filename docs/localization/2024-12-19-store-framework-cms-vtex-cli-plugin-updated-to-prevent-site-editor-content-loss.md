---
title: "Store Framework CMS: VTEX CLI plugin updated to prevent Site Editor content loss"
slug: "2024-12-19-store-framework-cms-vtex-cli-plugin-updated-to-prevent-site-editor-content-loss"
type: improved
excerpt: "The VTEX IO CLI workspace plugin has been updated to address the issue of content loss in Site Editor during workspace promotions."
createdAt: ""
updatedAt: ""
hidden: false
---

Some customers may experience content loss in Site Editor when promoting a production workspace to master due to workspace conflicts.

To prevent this issue, the VTEX IO CLI workspace plugin has been updated to `v1.2.0`.

## What has changed?
In `v1.2.0` of the VTEX IO CLI workspace plugin, rebase conflicts are identified and solved before the production workspace is promoted to master.

## What needs to be done?

To update the VTEX IO CLI workspace plugin to `v1.2.0`, follow the steps below:

With VTEX IO CLI, log in to your VTEX account by running the `vtex login {accountName}` command.

>⚠ Replace `{accountName}` based on your scenario.

Update the `@vtex/cli-plugin-workspace` to `v1.2.0` by running the `vtex plugins update` command. Another option is to directly install the new version by running the `vtex plugins install @vtex/cli-plugin-workspace@1.2.0` command.
