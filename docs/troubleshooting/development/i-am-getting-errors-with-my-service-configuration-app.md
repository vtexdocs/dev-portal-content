---
title: "I am getting errors with my service configuration app"
slug: "i-am-getting-errors-with-my-service-configuration-app"
hidden: false
createdAt: "2024-09-09T10:00:00.000Z"
updatedAt: "2024-09-09T10:00:00.000Z"
excerpt: "Errors with the service configuration app occur depending on your workspace configuration"
tags:
    - apps
    - vtex-io
    - services
---

If you are [developing a configuration app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-service-configuration-apps), you may be getting errors because the service your app is configuring is installed or linked to a different workspace. This happens because, when creating a new configuration app, the configuration builder first looks for that configuration schema in all the apps installed in your current workspace. Consequently, linking your app may fail if the configuration builder cannot find this specific configuration.

## Solution

Below, we outline solutions for addressing errors with your service configuration app:

1. [Avoid errors when installing or linking your configuration app](#avoiding-errors-when-installing-or-linking-your-configuration-app).
2. [Publish your configuration app in an alternative workspace](#publishing-your-configuration-app-in-an-alternative-workspace).

### Avoiding errors when installing or linking your configuration app

To avoid errors, link or install the configuration app in the same workspace the service app is linked or installed. Follow the instructions below:

1. In a terminal, go to the desired workspace using the following VTEX IO CLI command:

    ```
    vtex use workspace {desiredWorkspace}
    ```

    > ℹ️ Replace {desiredWorkspace} with the workspace you want to work in.

2. If your service app is not yet linked or installed, [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) or [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) your service app.
3. [Link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) or [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) your configuration app.

### Publishing your configuration app in an alternative workspace

To publish your configuration app without installing the service in the master workspace, follow the instructions below:

1. In a terminal, go to the desired workspace using the following VTEX IO CLI command:

    ```
    vtex use workspace {desiredWorkspace}
    ```

    Replace `{desiredWorkspace}` with the workspace you want to work in.

2. If your service app is not yet linked or installed, [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) or [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) your service app.
3. Create a new version of your configuration app by following the instructions in [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).
4. [Publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) your configuration app using the following command:

    ```
    vtex publish -w {desiredWorkspace}
    ```

    The `-w` flag allows you to choose the workspace of the app you are publishing.
