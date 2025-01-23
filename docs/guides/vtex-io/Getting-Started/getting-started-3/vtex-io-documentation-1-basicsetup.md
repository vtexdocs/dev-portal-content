---
title: "1. Setting up your development environment"
slug: "vtex-io-documentation-1-basicsetup"
hidden: false
createdAt: "2020-08-11T07:03:17.968Z"
updatedAt: "2025-01-07T14:11:11.707Z"
category: "Storefront Development"
excerpt: "Learn how to configure your development environment to build a Store Theme app with VTEX IO."
---

In this guide, you'll learn how to set up a development environment to build a [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) app for your store.

When working with [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), you're essentially developing within [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io/), which means you have access to a comprehensive suite of [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps) to help you build and customize your storefront.

## Instructions

### Step 1 - Installing Git

Download [Git](https://git-scm.com/downloads) on your computer directly from its website and install it by following the instructions of your operating system (Windows, Mac, or Linux). Git is a version control system that tracks file changes, facilitates collaboration, and allows developers to efficiently manage and recover project versions.

### Step 2 - Installing VTEX IO CLI

Install the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) (Command Line Interface), which serves as the gateway between your VTEX account and the VTEX IO development platform. The VTEX IO CLI is an essential tool for managing, developing, and deploying your Store Theme app.

For detailed instructions, follow the VTEX IO CLI [installation guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).

### Step 2 - Logging in to your VTEX account

With the VTEX IO CLI installed, log in to your VTEX account using the command below, and replace `{accountName}` with your VTEX account name:

```sh
vtex login {accountName}
```

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-3.png)

After running this command, a new browser tab will open, prompting you to log in to your VTEX account using your email credentials.

Once logged in, your web browser will display the following message: 'You may now close this window.' At this point, you will have access to your VTEX account.

### Step 3 - Creating a development workspace

On VTEX IO, all the interactions with your account occur within a specific [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/), which acts as a separate version of your account where you can run the changes without affecting the live version of your store.

By default, when you log in to a VTEX store using VTEX IO, you're in the `master` workspace, which reflects the version accessible to your shoppers.

To keep your work isolated from `master`, create a [development workspace](
https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) by using the command below, and replace `{exampleName}` with your desired workspace name:

```sh
vtex use {exampleName}
```

If the workspace already exists, the command will switch to it. If not, VTEX IO CLI will create it for you.

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-1.png)

> ℹ️ The `vtex use` command ensures that all your operations run in the specified workspace. To switch back to the main workspace (`master`), run `vtex use master` in the VTEX IO CLI.

To confirm the `account` and `workspace` you're using, run the `vtex whoami` command in your terminal. Learn more in [Command reference](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference).

![VTEX IO CLI-whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-0.png)

### Step 4 - Accessing your store using a workspace

Once you've created your development workspace, access your store by visiting `https://{workspace}--{accountName}.myvtex.com`, replacing `{workspace}` with the name of your workspace and `{accountName}` with your VTEX account name. Alternatively, run the `vtex browse` command in your terminal to open your browser with the correct workspace and account settings.

![VTEX IO CLI-whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-4.png)

Your account is now connected to the VTEX IO platform, and you're ready to start building a Store Theme with Store Framework.
