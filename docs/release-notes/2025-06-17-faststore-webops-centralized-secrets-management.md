---
title: "FastStore WebOps: Centralized secrets management"
slug: "2025-06-17-faststore-webops-centralized-secrets-management"
type: added
excerpt: "FastStore secrets are now managed in WebOps, improving security by deploying them as environment variables through AWS Secrets Manager."
createdAt: "2025-06-17T00:00:00.909Z"
updatedAt: ""
hidden: false
---

Secrets are now managed via the WebOps interface to improve the security of sensitive data and streamline deployment processes. This change centralizes the handling of sensitive information, such as API keys, tokens, and passwords, directly within WebOps.

![secrets-settings-webops](https://vtexhelp.vtexassets.com/assets/docs/src/secrets-settings-webops___c4cc35670f1faf9ecabd30447d1ee9b6.gif)

## What has changed?

Previously, secrets were handled through the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) secrets plugin. To enable secrets management, an empty `vtex.env` file needed to be present in the project root. The key-value pairs were stored in the `secrets.revealed.json` file, then encrypted into `secrets.hidden.json` before being committed to the main branch.

Now, this workflow has been deprecated, and secrets are managed directly through the WebOps interface, where you can create, update, and delete them. Secrets are loaded as environment variables during deployment and are no longer committed to your project’s codebase.

## Why did we make this change?

Secrets management via WebOps addresses the following concerns:

- To improve the security of sensitive data by eliminating secrets from source code and version control.
- To reduce operational overhead and potential sync errors that might arise from CLI-managed secrets files.
- To ensure that secrets are managed in a uniform way across all FastStore deployment providers.

## What needs to be done?

### For stores using the deprecated workflow

If your store currently uses the deprecated [secrets plugin](https://v1.faststore.dev/how-to-guides/webops/security/setting-up-secrets) via the VTEX IO CLI, follow these steps to migrate to WebOps secrets management:

1. Push a new commit to your repository to trigger migration.
2. After pushing the new commit, access the VTEX Admin and got to **Storefront** > **WebOps**.
3. In the WebOps, go to the [Secrets](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#secrets) tab and verify if the secrets were correctly migrated.
4. Once the secrets were correctly migrated, delete the `secrets.revealed.json` and `secrets. hidden.json` files from your store repository.

    > ⚠️ Do not delete the `vtex.env` file, it's still necessary for local development.

5. After finishing this process, you can [manage secrets](#for-all-stores-managing-secrets) through WebOps in the VTEX Admin.

### For all stores managing secrets

All FastStore deployments now use WebOps for secrets management by default. To manage your secrets, follow these steps:

1. Access your [FastStore WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard) and navigate to the Settings tab.
2. In the [Secrets](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#secrets) tab, you can create, update, or delete secrets according to your needs.

For detailed instructions, see the [Managing Secrets](https://developers.vtex.com/docs/guides/faststore/security-managing-secrets) guide.
