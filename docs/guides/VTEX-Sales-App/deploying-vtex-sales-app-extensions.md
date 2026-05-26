---
title: "Deploying VTEX Sales App extension"
slug: "deploying-vtex-sales-app-extensions"
hidden: false
excerpt: "Learn how to deploy VTEX Sales App extensions for public availability."
createdAt: "2026-05-26T00:00:00.000Z"
---

After creating extensions for your VTEX Sales App, you can deploy them and make them publicly available.

A deployment starts when you push a commit to the configured production branch, typically `main`. If FastStore WebOps detects changes in the `sales-app` module, it automatically builds and deploys the extension to VTEX. No separate manual build step is required. In about 10 minutes, the changes are usually applied to your Sales App.

> ⚠️ VTEX Sales App extensions support only production deployments. Once a commit is pushed to the configured production branch, your changes are applied to production. To revert a change, create a new commit that reverses the previous changes, then push it to the same branch.

## Requirements

Make sure you have installed the FastStore WebOps. For detailed instructions, see the guide [Installing FastStore WebOps](https://developers.vtex.com/docs/guides/installing-webops-for-sales-app-extensions).

> ℹ️ Deploying VTEX Sales App extensions with WebOps doesn't require the `discovery` module. The storefront can use another technology, as long as the account is configured to use the `sales-app` module.

## Handling build failures

If the build fails, the issue is usually in your extension code or configuration. Common causes include type-checking errors and typos.

FastStore WebOps shows when a build fails, but Sales App build logs aren't available there. To inspect the logs, check the GitHub Checks for the failed commit:

![GitHub checks notification showing failed check for commit 'Added missing totalizer validations' in a VTEX app repository](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-18419-creating-extension-point/images/deploying-extensions-github-checks.webp)

You can also run the following command. Remember to replace `{account-name}` with the name of your account.

```yarn
yarn fsp build {account-name} sales-app
```

```npm
npx fsp build {account-name} sales-app
```

This command builds the VTEX Sales App extension for the specified account and displays any local build errors. If the command succeeds locally, check your GitHub repository for issues in the build workflow.
