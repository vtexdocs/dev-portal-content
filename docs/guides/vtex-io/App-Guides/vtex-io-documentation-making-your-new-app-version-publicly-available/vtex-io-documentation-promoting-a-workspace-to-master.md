---
title: "Promoting a workspace to Master"
slug: "vtex-io-documentation-promoting-a-workspace-to-master"
hidden: false
createdAt: "2020-06-03T16:02:44.191Z"
updatedAt: "2022-12-13T20:17:44.636Z"
category: "App Development"
---

Promoting a production workspace to Master is the final step in [making an app publicly available to end users](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available). After launching your app as a stable version and thoroughly testing it in a production workspace, you can promote your workspace to Master to make your new app version publicly available to end users.

Note that once promoted to Master, you can't make new code changes in your app version. Alternatively, you would need to develop your code in a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) and reproduce it in a new production workspace, so you could test your changes with user traffic before making your new changes publicly available.

![Promoting a production workspace to Master](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-promoting-a-workspace-to-master-0.gif)

## Before you begin

Before proceeding any further, make sure your app has been [published](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) in the workspace you are about to promote.

Remember that, when you promote a workspace to master, your changes are applied to all workspaces of the current account. Hence, if you are promoting a new version of the [Store Theme app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme) to master, make sure to complete all the necessary adjustments to store content in Site Editor and to your code beforehand. Furthermore, the apps installed in the promoted workspace will be installed in all the other workspaces, which is described on [Workspace behavior with app installations](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace-behavior-with-app-installations).

Promoting a workspace to Master is a step in **making your new app version publicly available**. Please check [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide for more information.

## Instructions

Follow these steps to promote a production workspace to Master. Remember to replace the values between curly brackets according to your scenario.

1. Open the terminal and log in to your VTEX account.

    ```shell
    vtex login {accountName}
    ```

2. Change to the production workspace to be promoted.

    ```shell
    vtex use {workspaceName}
    ```

3. Promote the workspace being used.

    ```shell
    vtex workspace promote
    ```
