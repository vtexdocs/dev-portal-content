---
title: "FastStore WebOps: Support for GitHub Enterprise accounts with a custom domain"
slug: "2026-04-02-faststore-webops-support-for-github-enterprise-accounts-with-a-custom-domain"
createdAt: "2026-04-02T13:48:24.227Z"
---

[FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard) onboarding now includes support for GitHub Enterprise, so you can connect your storefront to enterprise GitHub instances with custom domains.

> ℹ️ **GitHub Enterprise support is currently in open beta.** If you want to use a GitHub Enterprise instance for your FastStore project, please contact [VTEX Support](https://help.vtex.com/support).

## What has changed?

The FastStore WebOps onboarding guide previously supported only GitHub personal and organization accounts. Now, you have the option to connect to [GitHub Enterprise Cloud](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-enterprise-cloud) instances with custom domains (for example, `mycompany.ghe.com`), in addition to the default GitHub.com options.

## Why did we make this change?

Many enterprise customers use GitHub Enterprise with custom domains for enhanced security, compliance, and governance. By supporting this setup, we enable enterprise teams to seamlessly integrate their FastStore projects with their existing GitHub infrastructure. This reduces setup friction and ensures that all organizations can leverage FastStore WebOps regardless of their GitHub deployment model.

## What needs to be done?

If you want to use a GitHub Enterprise instance for your FastStore project, please contact [VTEX Support](https://help.vtex.com/support).

Once enabled, follow these steps to set up FastStore WebOps with GitHub Enterprise:

1. In the **Git Provider** section of the onboarding process, select **Custom Domain** to connect to a GitHub Enterprise instance.

2. Enter your GitHub Enterprise domain. For example, `{enterpriseName}.ghe.com`, where `{enterpriseName}` is the name of your GitHub Enterprise account.

3. Click **Connect with GitHub** and complete the GitHub app installation for your custom domain.

4. In the **Repository access** section, choose whether to grant access to all repositories or only select repositories.

5. Click **Install** to complete the integration, then proceed with repository selection (create new or select existing).

For detailed instructions, see the [Starting the Project](https://developers.vtex.com/docs/guides/faststore/getting-started-2-setting-up-the-project) guide.
