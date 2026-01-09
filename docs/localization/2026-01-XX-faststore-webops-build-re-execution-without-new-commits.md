---
title: "FastStore WebOps: Build re-execution without new commits"
slug: "2026-01-XX-faststore-webops-build-re-execution-without-new-commits"
type: "added"
createdAt: "2026-10-XXT10:00:00.000Z"
hidden: false
excerpt: "FastStore WebOps now lets you redeploy failed builds from the dashboard without creating new commits, helping you fix operational issues faster while keeping your repository history clean."
tags:
  - FastStore
---

We introduced the ability to re-execute a build directly from the WebOps interface. This enhancement allows you to quickly address issues unrelated to code, such as environment variable misconfigurations or network interruptions, without needing to create a new commit in your repository.

As a result, you can resolve operational problems more quickly and maintain a clean commit history.

> ℹ️ If the build failed due to problems in your code (for example, syntax errors or failing tests), update the code in your local environment and push a new commit. WebOps will automatically trigger a new deploy for that commit.

## What has changed?

Previously, if a build failed due to non-code issues, you had to make a new commit to the repository to trigger a rebuild.

Now, you can re-execute the build job from the WebOps interface itself, enabling you to retry builds and fix issues without modifying your codebase or affecting your commit history.

## What needs to be done?

To use this feature, follow the instructions below:

1. In the **Deploys** tab of [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard#deploys), click the entry you want to redeploy.
2. In the top-right corner of the page, click `⋮`, then click **Rerun this deployment**.

  ![rerun-webops](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-16950/images/rerun-webops.png)

This update is available for all WebOps users, and no additional configuration is required.
