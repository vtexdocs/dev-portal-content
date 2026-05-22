---
title: "Installing FastStore WebOps"
slug: "installing-faststore-webops."
hidden: false
excerpt: ""
createdAt: "2026-05-22T16:10:21.214Z"
---

In this guide, you'll learn how to install and configure **FastStore WebOps** so you can deploy [VTEX Sales App extensions](#LINK).

> ℹ️If you already have a FastStore project and only need to connect it to WebOps, you don't need to follow these instructions. You should only run the following command in your project directory: `npx @vtex/fsp-cli init --from-discovery`. Learn more in the **Setting up your monorepo** section of the [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview) guide.
>
> For a brand-new setup, continue with the steps below.

## Before you begin

Before starting, have the following information:

* **VTEX account:** The name of your VTEX account (for example, `store-a`).
* **GitHub organization:** The GitHub organization where your repository lives (or where you will create it).
* **GitHub repository:** An existing GitHub repository with your extension code, or you can create a new one during the onboarding.

## Instructions

### Step 1 - Checking existing WebOps installation

1. In your VTEX Admin, go to **Storefront > FastStore WebOps**.
2. If the WebOps page loads and shows your project and repository, it means WebOps is already installed and configured. In this case, skip to [step 4](##step-4--verifying-COMPLETE) to confirm extensions build and run.
3. If you don't see WebOps or the page indicates no project is linked, go to [step 2](#step-2--installing-faststore-webops-in-your-account).

### Step 2 - Installing FastStore Webops in your account

1. In your terminal, log in to the VTEX account where you want to deploy extensions by running the following command. Replace the {account-name} with your VTEX account name.

   ```bash
   vtex login {account-name}
   ```

2. Install the WebOps app by running:

   ```bash
   vtex install vtex.webops@1.0.0
   ```

3. After installing, go to **Storefront > FastStore WebOps** in the VTEX Admin. You should see the [WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/webops-dashboard).

### Step 3 - Installing FastStore WebOps in your GitHub organization

You already have FastStore WebOps installed in your account, but the app has not been installed in your new GitHub organization yet.

To install the FastStore WebOps in the new GitHub organization, follow the steps below:

1. Access the [FastStore WebOps installation page](https://github.com/apps/faststore-webops) on GitHub.
2. Click `Configure`.
3. Click the organization where your repository lives.
4. Specify whether WebOps should be enabled for **all repositories** or **only selected repositories**.
5. Click `Installing & Authorizing` to install the FastStore WebOps in your new GitHub organization.

> ⚠️ Grant the app access to the correct organization and repository. Without the required permissions, WebOps will not receive push events, and builds will not run.

### Step 4 - Configuring the repository in WebOps

The repository is linked to WebOps through the WebOps onboarding in the dashboard. After you authenticate with GitHub, the onboarding process installs the FastStore WebOps GitHub App, lets you create a new repository or select an existing one, and automatically stores the organization, repository, and installation ID.

    
### Step 4 - Identifying the FastStore WebOps installation ID

> ⚠️ This step is performed in the GitHub organization where you want to move your project. For example, if you're moving your FastStore project from `current-org` to `new-org`, you must follow this step in the `new-org` organization on GitHub.

To identify the installation ID of the app you set up in the previous step, follow the steps below:

1. Go to the settings of the GitHub organization.
2. Click `GitHub Apps` under `Third-party Access`.
3. Search for **FastStore WebOps**, then click `Configure` next to the app name.
4. Check the URL to get the app installation ID. The URL follows this pattern: `https://github.com/organizations/{organizationName}/settings/installations/{installationId}`, where `{organizationName}` is the name of your organization and `{installationId}` is the app installation ID.

    ![app-installation-id](https://vtexhelp.vtexassets.com/assets/docs/src/app-installation-id___4088942cf7166f278e856d656f29e4ea.gif)

### Step 5 - Identifying the repository ID

> ⚠️ This step is performed in the repository hosted in the **new** GitHub organization.

To identify the ID of the repository where you want to move your project, follow these instructions:

1. Access the GitHub repository page where you want to host your FastStore project. The URL follows this pattern: `https://github.com/{newOrganizationName}/{newRepositoryName}`. Replace the curly brackets according to your scenario.
2. Open the console in your browser.
3. Run the following command in the console. The response is the repository ID.

    ```javascript
    $("meta[name=octolytics-dimension-repository_id]").getAttribute('content')
    ```

### Step 5 - Opening a ticket with VTEX Support

Open a ticket with [VTEX Support](https://help.vtex.com/en/support) and share the following information:

* **Account:** Name of your account.
* **Link to the old repository:** URL of the repository where your project is currently hosted.
* **Link to the new repository:** URL of the repository where you want to move your project.
* **Repository ID:** The unique identifier of the repository you want to migrate. See how to get this ID in [Identifying the repository ID](#step-4-identifying-the-repository-id) section.
* **App installation ID (`installationId`):** The unique identifier of the FastStore WebOps installation on GitHub. See how to get this ID in [Identifying the app installation ID](#step-3-identifying-the-app-installation-id).

The Support team will work on your request and notify you when the process is complete.
