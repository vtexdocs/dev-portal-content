---
title: "I am getting errors with my service configuration app"
slug: "i-am-getting-errors-with-my-service-configuration-app"
hidden: false
createdAt: "2024-09-09T10:00:00.000Z"
updatedAt: "2024-09-09T10:00:00.000Z"
tags:
  -apps
  -services
---

If you are [developing a configuration app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-service-configuration-apps), you may be getting some errors due to the service that your app is configuring being installed or linked to a different workspace you are working in. That happens because, when creating a new configuration app, the configuration builder first looks for the schema of that configuration in all the apps installed in your current workspace. Consequently, linking your app may fail if the configuration builder cannot find this specific configuration.

## Solution

We present the following solutions for when you are getting errors with the service configuration app:

1. Avoid errors when installing or linking your configuration app.
2. Publish your configuration app in an alternative workspace.

### Avoid errors when installing or linking your configuration app

To avoid errors, link or install the configuration app in the same workspace the service app is linked or installed, follow the instructions below:

1. In a terminal, go to the desired workspace using the following VTEX IO CLI command:

    ```
    vtex use workspace {desiredWorkspace}
    ```

    > ℹ️ Replace {desiredWorkspace} for the workspace you want to work on.

2. If your service app is not yet linked or installed, [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) or [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your service app.
3. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) or [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your configuration app.

### Publish your configuration app in an alternative workspace

To publish your configuration app without installing the service in the master workspace, follow the instructions below:

1. In a terminal, go to the desired workspace using the following VTEX IO CLI command:

    ```
    vtex use workspace {desiredWorkspace}
    ```

    Replace `{desiredWorkspace}` for the workspace you want to work on.

2. If your service app is not yet linked or installed, [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) or [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your service app.
3. Create a new version of your configuration app by following the instructions in [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).
4. [Publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) your configuration app using the following command.

    ```
    vtex publish -w {desiredWorkspace}
    ```

    The `-w` flag allows you to choose the workspace of the app you are publishing.
