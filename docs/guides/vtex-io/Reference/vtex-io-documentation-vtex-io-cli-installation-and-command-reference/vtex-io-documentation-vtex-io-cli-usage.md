---
title: "Using VTEX IO CLI"
slug: "vtex-io-documentation-vtex-io-cli-usage"
hidden: false
createdAt: "2021-04-04t22:02:14.084Z"
updatedAt: "2022-12-13T20:17:44.738Z"
---

## Accessing the list of commands

Start using VTEX IO CLI by running the following command to access a summary of the CLI default commands.

```shell
vtex help
```

![VTEX command](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-0.png)

> ℹ️ See the [Command Reference](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference) for more details.

## Logging in to your VTEX account

Log in to your VTEX account by running the following command:

```shell
vtex login {accountName}
```

> ⚠️ Remember to replace the value in curly brackets with the values that apply to your scenario.

After running this command, a new tab will open in your browser, asking you to log in to the desired VTEX account with your email.

Once logged in, the web page will display the following message: *“You may now close this window.”*

When you return to the computer terminal, you will have access to a development environment for this VTEX account. You will see some basic information about your account displayed as follows:

![Login Screen](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-1.png)

> ℹ️ If you decide to work on another account later, run the command `vtex switch {accountName}`, specifying the account name to which you want to switch.

## Creating a new workspace

After logging in to a VTEX account, you will be automatically directed to the `master` workspace, the version publicly available to end users.

To start customizing your storefront or developing a VTEX IO app, you must switch from the master workspace to a development one.

To switch to an existing development workspace or create a new one, run the following command:

```shell
vtex use {workspaceName}
```

Notice that if a workspace with the chosen name already exists, you will be directed to it.

![Change Workspace](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-2.png)

Otherwise, you will be prompted to confirm whether you want to create a new workspace.

![New Workspace](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-3.png)

From now on, all operations will be performed within the specified workspace.

## Verifying your environment

To verify the account you are currently logged in to and the workspace you are using, run the following command:

```shell
vtex whoami
```

## Installing an app

To install an app on your current account and workspace, use the following command:

```shell
vtex install {appVendor}.{appName}@{appVersion}
```

> ⚠️ Remember to replace the values in curly brackets with the values that apply to your scenario.

If you try to install an app that has [Billing Options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options), you must first access the [VTEX App Store](https://apps.vtex.com/) and agree to the app terms and conditions.

![Billing Options](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-4.png)

1. If you type `Y`, the app page you wish to install from the VTEX App Store will open in your browser.
2. To proceed with the installation, click `GET APP` > `CONFIRM` to log in to your VTEX store.
3. Read and agree to the app's Terms and Conditions.

> ℹ️ Note that some apps are free, and others may have specific charging methods.

## Starting a new project

To start a new project from pre-defined templates, you can run the following command:

```shell
vtex init
```

![Init command](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-5.png)

For example, choose the `store` option to start developing a Store Theme app. This will clone the [Store Theme](https://github.com/vtex-apps/store) boilerplate app to your local files.

## Developing locally

To develop locally, navigate to the directory of the app you are working on and run the following command to synchronize your local files with the VTEX platform.

```shell
vtex link
```

![Link Command](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-6.png)

VTEX IO CLI will monitor your files and provide a URL related to that workspace. You will be able to access it through `https://{workspace}--{account}.myvtex.com` by replacing the value between curly braces with the name of the workspace previously created and your VTEX account. For example, `https://marianacaetano--appliancetheme.myvtex.com`.

By accessing this URL, you can observe any local changes made to the linked files.

## Checking the installed apps

To check apps installed on your account, you can run the following command:

```shell
vtex list
```

The installed apps are classified as follows:

1. Apps automatically installed by your account [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app).
2. Apps manually installed on the current workspace.
3. Apps linked to the current workspace.

## Authenticating API requests

You can use the VTEX IO CLI to generate a unique and temporary [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token), which can be helpful when running tests with VTEX APIs.

To generate a user token, run the following command:

```shell
vtex local token
```

The token will be automatically copied to the clipboard and can be used to authenticate requests for 24 hours. Learn more about [user tokens](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).

> ⚠️ The authentication of VTEX IO apps does not require this token. If you are developing VTEX IO apps, please refer to the [App authentication](https://developers.vtex.com/docs/guides/getting-started-authentication#app-authentication) guide.

## Learning more about a command

Use the `--help` flag as shown below to learn more about a specific command.

```shell
vtex [COMMAND] --help
```

![Help Command](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-vtex-io-cli-usage-7.png)
