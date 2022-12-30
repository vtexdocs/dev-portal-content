---
title: "1. Setting up your development environment"
slug: "vtex-io-documentation-2-basic-development-setup-in-vtex-io"
excerpt: "vtex.io-documentation@0.88.24"
hidden: false
createdAt: "2021-03-25T20:58:43.721Z"
updatedAt: "2022-12-13T20:17:44.103Z"
---

Any development in VTEX IO begins and ends with the [**VTEX IO CLI**](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). The VTEX IO CLI works as a communication gateway between your VTEX account and the VTEX IO development platform.

With VTEX IO's CLI, you will be able to log in to your VTEX account, manage workspaces, develop apps, and install new ones.

## Installing VTEX IO's CLI

To install VTEX IO’s CLI, you need to ensure that [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/) are properly installed on your machine.

To follow all the required steps for installing VTEX IO's CLI, access our documentation on [VTEX IO CLI Installation and Command Reference](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## Logging in to your VTEX account

Once VTEX IO’s CLI is installed, log in to your VTEX account with the following command:

```sh
vtex login {accountName}
```

This will open a browser window asking for your credentials.

> ⚠️ Replace `{accountName}` with the name of your VTEX account.

Once you are logged in, run the `vtex whoami` command to show which **VTEX account** and **workspace** are being used by the VTEX IO CLI.

![VTEX IO CLI - whoami](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-2-basic-development-setup-in-vtex-io-0.png)

## Creating your own workspace

When using VTEX IO, any development must happen in a [**workspace**](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-workspace/).

A workspace works as a GitHub branch in the sense that any development operation is done in a specific workspace that is separate from others. This means that workspaces allow you to develop and test your changes without any risk of interfering with live apps or with the work of other developers.

To start developing, you have to [create a **Developer workspace**](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-development-workspace/) in your VTEX account. When you log in, you are automatically using the Master workspace, which means you are in the version available to the end user.

Run the `vtex use` command in your terminal as shown below:

```sh
vtex use {exampleName}
```

This changes your VTEX account to a Development workspace called `exampleName`, creating it from scratch if it does not already exist.

![workspace-examplename EN](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-2-basic-development-setup-in-vtex-io-1.png)

Having logged in to your account and created your own Development workspace, you are ready to begin developing your React app and building your storefront using VTEX IO.
