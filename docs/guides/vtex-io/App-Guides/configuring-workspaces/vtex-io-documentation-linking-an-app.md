---
title: "Linking an app"
slug: "vtex-io-documentation-linking-an-app"
hidden: false
createdAt: "2020-06-03T16:02:44.237Z"
updatedAt: "2022-12-13T20:17:45.061Z"
category: "App Development"
---
For development, an app can be linked to a **development workspace** so that any local code change can be automatically synced and made available in that corresponding workspace.

>⚠️ Linking an app to a [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) is not possible.

## Instructions

1. Open the terminal and log in to your VTEX account.

  ```sh
  vtex login {account}
  ```

2. Change to a **development workspace**.

  ```sh
  vtex use {workspace}
  ```

3. Change to your app's directory.

  ```sh
  cd {directory}
  ```

4. Link your app to the current workspace by running the following command:

  ```sh
  vtex link
  ```

Once your local files are uploaded and synced to your development environment, you should see the following message: `App linked successfully`. Use `https://{workspace}--{account}.myvtex.com`, where `workspace` is the development workspace in use and `account` is the name of your VTEX account, to check your local version of the app.

Notice that the synced app will only be available within the specified development workspace.

If you are comfortable with your changes and want to make your changes publicly available, please refer to [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide.
