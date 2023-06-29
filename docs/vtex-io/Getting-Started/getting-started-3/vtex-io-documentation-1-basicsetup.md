---
title: "1. Setting up your development environment"
slug: "vtex-io-documentation-1-basicsetup"
hidden: false
createdAt: "2020-08-11T07:03:17.968Z"
updatedAt: "2022-12-13T20:17:44.100Z"
category: "Storefront Development"
excerpt: "Learn how to set up your development environment to build storefront components with VTEX IO."
seeAlso:
  - "/docs/guides/vtex-io-documentation-2-prerequesites"
---

You may not realize it, but once you have implemented the [**VTEX Store Framework**](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) in your store, you will be developing in [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io/) on a certain scale.

This is because **our ecommerce components are native apps on the VTEX IO development platform**. To make them work correctly on your storefront, you need to install and configure these apps. Here are the steps to get started:

## Step 1 - Installing VTEX IO CLI

All development in the VTEX IO platform revolves around the **VTEX IO CLI** (Command Line Interface).

It is the communication gateway between your VTEX store and the VTEX IO development platform, allowing you to log in, install new apps on the account, and manage those already installed.

Follow the instructions to install the VTEX IO CLI on your computer and get familiar with it by reading the [reference documentation](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference/).

## Step 2 - Logging in to your VTEX account

Once VTEX IO CLI is installed, you can log in to your VTEX account using the following command in your terminal to connect to the platform (replacing `{account}` with the name of your VTEX account):

```sh
vtex login {account}
```

By running this command, a browser window will appear for you to enter your credentials.

## Step 3 - Creating your own workspace

In VTEX IO, all interactions with an account happen within a [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/).

The workspace in VTEX IO functions as a separate version of your logged-in account, so any development operation using such a workspace will be isolated, separate from other workspaces and the public version of the account (Master).

> ℹ️ If you're familiar with GitHub, you can think of workspaces as **branches**.

When you log in to a VTEX store using VTEX IO, you are automatically in the master workspace, which represents the version accessible to end users.

To verify the **account** and **workspace** being used by the VTEX IO CLI for your login, you can run the `vtex whoami` command in your terminal.

![VTEX IO CLI-whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-0.png)

To start performing the desired changes in your storefront, you need to create a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).

Use the `vtex use` command to start configuring Store Framework in your store. For example:

```sh
vtex use examplename
```

*Replace* `examplename`  *with the desired name for your workspace.*

If the workspace already exists, the command will switch the login to that workspace. If it does not, VTEX IO CLI will create it:

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-1.png)

> ℹ️ The `vtex use` command makes all your operations run in the workspace specified in the command. This means you can shift your operations to Master simply by running `vtex use master` in the VTEX IO CLI.

## Step 4 - Accessing your store using a workspace

Having created your development workspace in VTEX IO, you can now go to your store by accessing `https://{workspace}--{account}.myvtex.com`, where `{workspace}` should be replaced with the name of your workspace and `{account}` with the name of your VTEX account.

> ℹ️ **Tip:** You can simply run `vtex browse` in your terminal to automatically open your browser with the correct workspace and account.

Done! Your store is now connected to the VTEX IO platform, and you are technically ready to implement VTEX Store Framework!
