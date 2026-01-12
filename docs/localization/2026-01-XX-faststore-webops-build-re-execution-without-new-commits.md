---
title: "FastStore WebOps: Rerun failed builds without new commits"
slug: "2026-01-XX-faststore-webops-build-re-execution-without-new-commits"
type: "added"
createdAt: "2026-10-XXT10:00:00.000Z"
hidden: false
excerpt: "FastStore WebOps now lets you redeploy failed builds from the dashboard without creating new commits, helping you fix operational issues faster while keeping your repository history clean."
tags:
  - FastStore
---

FastStore WebOps now includes a rerun feature for failed builds. This allows you to directly execute a failed build from the dashboard.

With this feature, you can quickly resolve issues that are not related to code, such as misconfigurations of environment variables or network interruptions, without having to create a new commit in your repository.


> ℹ️ If the build failed due to problems in your code (for example, syntax errors or failing tests), update the code in your local environment and push a new commit. WebOps will automatically trigger a new deploy for that commit.

## What has changed?

Previously, if a build failed due to non-code issues, you had to make a new commit to the repository to trigger a rebuild.

Now, you can rerun the build job from the WebOps interface itself, enabling you to resolve operational problems more quickly without modifying your codebase or affecting your commit history.

## What needs to be done?

This feature is available for all WebOps users, and no additional configuration is required. To use it, follow the instructions below:

1. In the **Deploys** tab of [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#deploys), click the entry you want to redeploy.
2. In the top-right corner of the page, click `⋮`, then click **Rerun this deployment**.

  ![rerun-webops](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/rerun-webops.png)

