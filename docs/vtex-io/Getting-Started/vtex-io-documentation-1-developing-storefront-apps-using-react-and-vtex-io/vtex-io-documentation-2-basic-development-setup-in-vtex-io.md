---
title: "1. Setting up your development environment"
slug: "vtex-io-documentation-2-basic-development-setup-on-vtex-io"
hidden: false
createdAt: "2021-03-25T20:58:43.721Z"
updatedAt: "2022-12-13T20:17:44.103Z"
category: "App Development"
seeAlso:
  - "/docs/guides/vtex-io-documentation-3-creating-the-new-app"
---

Any development on VTEX IO begins and ends with [**VTEX IO CLI**](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). VTEX IO CLI works as a communication gateway between your VTEX account and the VTEX IO development platform.

With VTEX IO CLI, you can log in to your VTEX account, manage workspaces, develop apps, and install new ones.

## Installing VTEX IO CLI

To install VTEX IO CLI, you need to ensure that [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/) are correctly installed on your computer.

To follow all the required steps for installing VTEX IO CLI, read our documentation on [VTEX IO CLI Installation and Command Reference](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## Logging in to your VTEX account

Once VTEX IO CLI is installed, log in to your VTEX account with the following command:

```sh
vtex login {accountName}
```

This will open a browser window asking for your credentials.

> ⚠️ Replace `{accountName}` with the name of your VTEX account.

Once you are logged in, run the `vtex whoami` command to show which **VTEX account** and **workspace** are being used by VTEX IO CLI.

![VTEX IO CLI - whoami](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-2-basic-development-setup-in-vtex-io-0.png)

## Creating your own workspace

When using VTEX IO, any development must happen within a [**workspace**](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/).

A workspace works as a separate environment or branch, similar to how branches work in GitHub. This means that workspaces allow you to develop and test your changes without the risk of impacting live apps or conflicting with the work of other developers.

To start developing, you need to [create a **Developer workspace**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) in your VTEX account. When you log in, you are automatically using the Master workspace, which means you are in the version displayed to end users.

Run the `vtex use` command in your terminal as shown below:

```sh
vtex use {exampleName}
```

This changes your VTEX account to a Development workspace called `exampleName`, creating it from scratch if it does not already exist.

![workspace-examplename EN](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-2-basic-development-setup-in-vtex-io-1.png)

Once you have logged into your account and created your own Development workspace, you are ready to start developing your React app and building your storefront using VTEX IO.
