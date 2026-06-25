---
title: "FastStore WebOps: Self-service Git provider management"
slug: "2026-06-25-faststore-webops-self-service-git-provider-management"
type: added
excerpt: "FastStore WebOps now allows you to change the GitHub organization and repository connected to your project."
createdAt: "2026-06-25T00:00:00.000Z"
tags:
  - FastStore
  - WebOps
---

FastStore WebOps now provides a self-service interface for changing the GitHub organization and repository connected to your project. This feature streamlines the process of moving FastStore projects between organizations or repositories, eliminating the need to open support tickets for repository migrations.

## What has changed?

The **Integrations** tab in the FastStore WebOps dashboard now includes a **Git Provider** section where you can configure the GitHub organization and repository associated with your FastStore project.

Before, moving a FastStore project to a different GitHub organization or repository required opening a ticket with VTEX Support and providing detailed information including repository IDs, installation IDs, and account details. The process involved multiple manual steps and coordination with the Support team.

Now, you can change your project's connected repository directly from the WebOps dashboard. The **Git Provider** card allows you to:

- **Change the GitHub organization:** Switch your project to a different GitHub organization by clicking `Change account` and selecting the target organization.
- **Change the repository:** Move your project to a different repository within the same organization by selecting the target repository from the dropdown.

## Why did we make this change?

This change was made to simplify the repository migration process and give developers more control over their FastStore project configuration.

The feature is available to all FastStore projects using WebOps that meet the required permissions (Owner role in VTEX Admin and Admin role in GitHub repositories).

> ⚠️ The repository change feature is not available for private GitHub instances. If your project is connected to a private GitHub instance, the option will not be displayed.

## What needs to be done?

To change your Git Provider configuration:

1. In your VTEX Admin, go to **Storefront > FastStore WebOps** and navigate to the **Integrations** tab.
2. In the **Git Provider** card:
   - To change organizations: Click `Change account` under **Account/Organization**, select the target organization on GitHub, grant repository access, and select the target repository in WebOps.
   - To change repositories in the same organization: Select the target repository from the **Repository** dropdown.
3. Click `Save` to apply your changes.

Learn more in the guide [Moving your FastStore project to a new GitHub repository](https://developers.vtex.com/docs/guides/faststore/webops-moving-your-faststore-project-to-a-new-github-repository).
