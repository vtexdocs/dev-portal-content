---
title: "I can't install VTEX IO CLI"
slug: "i-cant-install-vtex-io-cli"
hidden: false
createdAt: "2024-06-04T11:15:35.508Z"
updatedAt: "2024-08-26T13:34:19.841Z"
excerpt: 'When installing VTEX IO CLI, it returns "Error: Cannot find module vtex".'
tags:
    - Store Framework
    - VTEX IO
    - VTEX IO CLI

---

**Keywords:** VTEX IO CLI | Plugins

When [installing VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install), I get the following error message: `Error: Cannot find module ‘vtex’`.

This error is related to [plugins](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) detached from the VTEX IO CLI base code.

Even though plugins are decoupled from VTEX IO CLI, they rely on the CLI features. Therefore, this error indicates that these plugins fail to access VTEX IO CLI features.

## Solution

To solve this problem, follow these steps:

1. Run `vtex --version` to ensure you are using the [latest CLI version](https://github.com/vtex/toolbelt/blob/3.x/CHANGELOG.md) available.
2. If not, consider [updating](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-update) it.
3. If the problem persists, follow the steps below based on your operating system:

- MacOS:

  1. Create a [symlink](https://en.wikipedia.org/wiki/Symbolic_link) from {vtex-folder}/node_modules/vtex to {vtex-folder}/.

  2. Run the following command in the terminal:

  ```sh
  ln -s /usr/local/Cellar/vtex/2.119.2/libexec /usr/local/Cellar/vtex/2.119.2/libexec/node_modules/vtex
  ```

- Linux:

  1. Create a [symlink](https://en.wikipedia.org/wiki/Symbolic_link) from {vtex-folder}/node_modules/vtex to {vtex-folder}/.

  2. Run the following command in the terminal:

  ```sh
  ln -s /usr/local/lib/vtex /usr/local/lib/vtex/node_modules/vtex
  ```

- Windows:

  1. Run the `yarn global bin` command in your terminal.

     The expected output is a path that indicates where globally installed Yarn packages are stored on your computer. It might follow the pattern: `{UserProfileDirectory}\AppData\Local\Yarn\bin`, where `{UserProfileDirectory}` refers to your user profile directory, typically found at `C:\Users\{YourUserName}` on Windows systems.

     In the example below, the output is `C:\Users\Barbara Celi\AppData\Local\Yarn\bin`
     ![windows-yarn-global-bin](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/windows-yarn-global-bin.png)

  2. Copy the path that the terminal returned after running the `yarn global bin` command.

  3. In the Windows search bar, type **Edit the system environment variables**.

  4. Click **Open**.
     ![edit-variables](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/windows-search-en.png)

  5. In the **System Properties** settings, go to the **Advanced** section and click **Environment Variables**.
     ![system-properties](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/environment-variables-en.png)

  6. In the **Environment Variables** settings, double-click **Path**.

     > ⚠️ If you want to configure the variables only for your user, click Path within **User variables for {your.user}**. If the configuration is for all system users, click Path within **System variables**.

     ![system-variables-user](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/system-variables-en.png)

  7. In the **Edit environment variable** settings, click **New**.

     ![edit-environment-variable](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/new-variable-en.png)

  8. Paste the path copied in step 2.

  9. Click **OK**.

     ![new-variable](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/new-variable-2-en.png)

  If the error persists, [open a ticket with VTEX Support](https://help-tickets.vtex.com/smartlink/sso/login/zendesk).
