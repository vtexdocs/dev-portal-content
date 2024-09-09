---
title: "1. Setting up your development environment"
slug: "vtex-io-documentation-1-basicsetup"
hidden: false
createdAt: "2020-08-11T07:03:17.968Z"
updatedAt: "2022-12-13T20:17:44.100Z"
category: "Storefront Development"
excerpt: "Learn how to configure your development environment to build a Store Theme app with VTEX IO."
seeAlso:
  - "/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference"
  - "/docs/guides/vtex-io-documentation-workspace"
---

This guide will teach you the essential steps to configure your development environment. By the end of this part, you'll be well-prepared to build a Store Theme app for your online store. This app defines the visual and interactive aspects of your ecommerce website, shaping how it appears and functions for your customers.

When working with [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), you are essentially developing within [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io/). This means you have access to a comprehensive suite of frontend and backend [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps) to help you build and customize your storefront.

## Instructions

### Step 1 - Installing VTEX IO CLI

To kickstart your journey, you will need to install the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) (Command Line Interface), which serves as the gateway between your VTEX account and the VTEX IO development platform. Follow the VTEX IO CLI [installation guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) for detailed a step-by-step. The VTEX IO CLI is an essential tool for managing, developing, and deploying your Store Theme app.

### Step 2 - Logging in to your VTEX account

With the VTEX IO CLI installed, log in to your VTEX account using the following command (replace `{accountName}` with your VTEX account name):

```sh
vtex login {accountName}
```

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-3.png)

After running this command, a new browser tab will open, prompting you to log in to your VTEX account using your email credentials.

Once logged in, you'll see a message in your web browser: "You may now close this window." At this point, you will have access to a development environment for your VTEX account.

### Step 3 - Creating a development workspace

On VTEX IO, all your interactions with your account occur within a specific [workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/), which acts as a separate version of your account where you can experiment with changes without affecting the live version of your store.

By default, when you log in to a VTEX store using VTEX IO, you are in the `master` workspace, representing the version accessible to your shoppers.

Let's create a dedicated development workspace to keep your work isolated. Use the following command to create a development workspace (replace `{exampleName}` with your desired workspace name):

```sh
vtex use {exampleName}
```

Note that if the workspace already exists, the command will switch to it. If not, VTEX IO CLI will create it for you.

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-1.png)

> ℹ️ The `vtex use` command ensures that all your operations run in the specified workspace. To switch back to the main workspace (`master`), run `vtex use master` in the VTEX IO CLI.

To confirm the `account` and `workspace` you are using, run the `vtex whoami` command in your terminal.

![VTEX IO CLI-whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-0.png)

### Step 4 - Accessing your store using a workspace

Now that you've created your development workspace on VTEX IO, you can access your store by visiting `https://{workspace}--{accountName}.myvtex.com`, replacing `{workspace}` with the name of your workspace and `{accountName}` with your VTEX account name. Alternatively, use the `vtex browse` command in your terminal to open your browser with the correct workspace and account settings.

![VTEX IO CLI-whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-1-basicsetup-4.png)

Your account is now connected to the VTEX IO platform, and you are ready to dive into implementing a Store Theme with Store Framework.
