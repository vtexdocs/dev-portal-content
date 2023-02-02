---
title: "Promoting a workspace to Master"
slug: "vtex-io-documentation-promoting-a-workspace-to-master"
hidden: false
createdAt: "2020-06-03T16:02:44.191Z"
updatedAt: "2022-12-13T20:17:44.636Z"
category: "App Development"
---
Promoting a production workspace to Master marks the final step to [making an app publicly available to end-users](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available). After launching your app as a stable version and thoroughly testing it in a production workspace, you can promote your workspace to Master to finally make your new app version publicly available to end-users.

Notice that, once promoted to Master, it's not possible to perform new code changes in your app version. Alternatively, you would need to develop your code in a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) and reproduce it in a new production workspace, so you could test your changes with user traffic before making your new changes publicly available.

![Promoting a Production workspace to Master](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-promoting-a-workspace-to-master-0.gif)

## Before you start

Before proceeding any further, make sure the app you are about to publish has already been [deployed](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version).

Also, keep in mind that when you promote a workspace to Master, your modifications are applied to all workspaces of the logged account. Hence, if you are promoting a new version of the [Store Theme app](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme) to Master, make sure to perform all necessary store content adjustments in the Site Editor and your code beforehand.

Promoting a workspace to master is one of the steps to **making your new app version publicly available**. Please refer to [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide for more information.

## Step by step

Take the following steps to promote a Production workspace to Master. Remember to replace the values between curly braces according to your scenario.

1. Open the terminal and log in to your VTEX account.

    ```shell
    vtex login {accountName}
    ```

2. Change to the Production workspace to be promoted.

    ```shell
    vtex use {workspaceName}
    ```

3. Promote the workspace in use.

    ```shell
    vtex workspace promote
    ```
