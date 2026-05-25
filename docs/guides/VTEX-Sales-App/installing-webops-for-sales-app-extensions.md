---
title: "Installing WebOps for Sales App extensions"
slug: "installing-webops-for-sales-app-extensions"
hidden: false
excerpt: "Learn how to install FastStore WebOps and connect your repository to deploy VTEX Sales App extensions."
createdAt: "2026-05-25T16:10:21.214Z"
---

In this guide, you'll learn how to install and configure **FastStore WebOps** so you can deploy [VTEX Sales App extensions](#LINK).

Use this guide if your project uses the FastStore monorepo and the `sales-app` module for VTEX Sales App extensions, but doesn't use the `discovery` module in production. In this setup, FastStore provides the monorepo structure, tooling, and build process, while the storefront uses another technology stack.

> ℹ️ If you already have a FastStore project that uses the `discovery` module and only need to connect it to WebOps, you don't need to follow these instructions. Instead, run `npx @vtex/fsp-cli init --from-discovery` in your project directory. Learn more in the **Setting up your monorepo** section of the [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview) guide.

## Before you begin

Before starting, have the following information:

* **VTEX account:** The name of your VTEX account (for example, `store-a`).
* **GitHub organization:** The GitHub organization where your repository lives (or where you'll create it).
* **GitHub repository:** An existing GitHub repository with your extension code, or you can create a new one during the onboarding.

## Instructions

### Step 1 - Checking existing WebOps installation

1. In your VTEX Admin, go to **Storefront > FastStore WebOps**.
2. If the WebOps page loads and shows your project and repository, it means WebOps is already installed and configured. In this case, you don't need to follow these instructions.
3. If you don't see WebOps or the page indicates no project is linked, go to [step 2](#step-2--installing-faststore-webops-in-your-account).

### Step 2 - Installing FastStore WebOps in your account

1. In your terminal, log in to the VTEX account where you want to deploy extensions by running the following command. Replace the {account-name} with your VTEX account name.

   ```bash
   vtex login {account-name}
   ```

2. Install the WebOps app by running:

   ```bash
   vtex install vtex.webops@1.0.0
   ```

3. After installing, go to **Storefront > FastStore WebOps** in the VTEX Admin. You should see the [WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/webops-dashboard).

### Step 3 - Configuring the repository in WebOps

The repository is linked to WebOps through the WebOps onboarding in the dashboard. This process installs the FastStore WebOps GitHub App, lets you create a new repository or select an existing one, and automatically stores the organization, repository, and installation IDs.

To start the onboarding process on WebOps, follow these steps:

1. Open the VTEX Admin and access **Storefront > FastStore WebOps**.
2. Click `Start Project` to start the onboarding flow.
3. Authenticate with GitHub and install the FastStore WebOps GitHub App for your organization (or account).
4. When prompted during onboarding, create a new repository or select an existing one. WebOps automatically stores the organization, repository, and installation IDs.
5. After onboarding, run `npx @vtex/fsp-cli init --from-discovery` in your repository to sync the configuration.

>❗ The full store onboarding in WebOps can **overwrite or remove existing content** in Headless CMS (hCMS). If your storefront already has relevant content in hCMS, keep this in mind before running the onboarding. If that is not a concern (for example, if you're setting up a new project or only a `sales-app` module with no FastStore project in hCMS), proceed with the onboarding as usual, then run the `npx @vtex/fsp-cli init --from-discovery` command. If you cannot run the WebOps onboarding because you already have a FastStore project or existing Headless CMS content that must not be overwritten, follow the next steps. If you have any questions, open a ticket with our [Support](https://help.vtex.com/en/support).

### Step 4 - Installing FastStore WebOps in your GitHub organization

If you cannot complete the WebOps onboarding after installing it in your account, you still need to install it in your GitHub organization. To do so, follow these steps:

1. Access the [FastStore WebOps installation page](https://github.com/apps/faststore-webops) on GitHub.
2. Click `Configure` (or `Install`, if you haven't installed it before).
3. Click the organization where your repository lives.
4. Specify whether WebOps should be enabled for **all repositories** or **only selected repositories**.
5. Click `Installing & Authorizing` to install FastStore WebOps in your new GitHub organization.

> ⚠️ Make sure the app has access to the correct organization and repository. Without the necessary permissions, WebOps will not receive push events, and builds will not run.

### Step 5 - Identifying the FastStore WebOps installation ID

To identify the installation ID of the app you set up in the previous step, follow these steps:

1. Go to the **Settings** of your GitHub organization.
2. Click `GitHub Apps` under `Third-party Access`.
3. Search for **FastStore WebOps**, then click `Configure` next to the app name.
4. Check the URL to get the app installation ID. The URL follows this pattern: `https://github.com/organizations/{organizationName}/settings/installations/{installationId}`, where `{organizationName}` is the name of your organization and `{installationId}` is the app installation ID.

    ![app-installation-id](https://vtexhelp.vtexassets.com/assets/docs/src/app-installation-id___4088942cf7166f278e856d656f29e4ea.gif)

### Step 6 - Identifying the repository ID

To identify the ID of the repository you want to link to WebOps, paste the following in your browser: `https://api.github.com/repos/{organizationName}/{repositoryName}`, replacing the values in curly brackets according to your scenario.

The `id` field in the JSON response is your repository ID.

### Step 7 - Opening a ticket with VTEX Support

Open a ticket with [VTEX Support](https://help.vtex.com/en/support) and share the following information:

* **Account:** Name of your account.
* **Link to the repository:** URL of the repository where you want to install WebOps.
* **App installation ID (`installationId`):** The unique identifier of the FastStore WebOps installation on GitHub. See how to get this ID in [Identifying the app installation ID](#step-5--identifying-the-app-installation-id).
* **Repository ID:** The unique identifier of the repository you want to migrate. See how to get this ID in the [Identifying the repository ID](#step-6--identifying-the-repository-id) section.

The Support team will work on your request and notify you when the process is complete.
