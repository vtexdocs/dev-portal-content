---
title: "Managing Secrets"
---

In this guide, you'll learn how to manage secrets in your FastStore project using [WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview).

Secrets are sensitive information, such as API keys, passwords, and tokens, that must be securely managed during the FastStore project deployment.

[WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) centralizes and standardizes secret management, providing a consistent and secure process across all deployment providers. This ensures that sensitive information is kept outside your project codebase and is retrieved securely by WebOps.

>ℹ️ The secrets of stores that don't use WebOps are handled through the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-plugins) secrets plugin. To enable secret management, you need to have an empty `vtex.env` file in the project root. The key-value pairs are stored in the `secrets.revealed.json` file, which is then encrypted into `secrets.hidden.json` before being committed to the main branch. For stores using WebOps, this workflow has been deprecated, and secrets are managed directly through the WebOps interface.

## Local development

For local development, you must use the `vtex.env` file to define the secrets needed to run your FastStore project locally.

The `vtex.env` file is only used in local environments and should always be added to `.gitignore` to avoid leaking secrets through version control. By adding it to `.gitignore`, secrets defined in the `vtex.env` file won't be available in deployed environments via WebOps.

## Instructions

To manage your secrets, go to your [FastStore WebOps dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard) and navigate to the **Settings** tab.

![secrets-settings-webops](https://vtexhelp.vtexassets.com/assets/docs/src/secrets-settings-webops___c4cc35670f1faf9ecabd30447d1ee9b6.gif)

In the [Secrets](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#secrets) section, you can [create](#creating-secrets), [update](#updating-secrets), or [delete](#deleting-secrets) secrets following the steps below.

### Creating secrets

1. In the `Key` field, enter the name of the secret, which serves as its unique identifier (example: VTEX_API_TOKEN, NEXT_SECRET_KEY). In the `Value` field, enter the corresponding sensitive information you want to store (example: the actual token, key, or password).

   >ℹ Secrets accessible in the browser (client-side) must start with the prefix `NEXT_PUBLIC_`. Use names without this prefix for all other secrets.

2. Click `Add`. A pop-up with `New secret added successfully` will open, and you'll see the message `Secrets have changed. Changes will take effect in the next successful deployment.` alongside a `Redeploy` button.

   >⚠ When creating multiple secrets, make sure you include all of them before proceeding to the next step. This prevents sync errors.

3. Click `Redeploy` to redeploy your website with the updated secret configuration. You’ll see the message `Redeploying with secret changes`, and a pop-up with `Deployment created successfully` will open.
4. Track the deployment status in the [Deploys](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#deploys) tab of the WebOps dashboard.

During the build process, any secrets added through WebOps will be transformed into environment variables within the code, which automatically loads them into the `process.env` object. You can access these values in your code using `process.env.VARIABLE_NAME`. *Remember to replace `VARIABLE_NAME` with the name you assigned to your secret in the `Key` field*.

   The secret created will be available in the **Current Keys** section.

![creating-secrets](https://vtexhelp.vtexassets.com/assets/docs/src/creating-secrets___14633df5e1e1385934d7f0854f00d340.gif)

### Updating secrets

1. Go to the `Current Keys` section.
2. Next to the secret you need to update, click `⋮` and then click `Edit`.
3. Click `Update`.  A pop-up with `Secret updated successfully` will open, and you'll see the message `Secrets have changed. Changes will take effect in the next successful deployment.` alongside a `Redeploy` button.
4. Click `Redeploy` to redeploy your website with the updated secret configuration. You’ll see the message `Redeploying with secret changes`, and a pop-up with `Deployment created successfully` will open.
5. Track the deployment status in the [Deploys](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#deploys) tab of the WebOps dashboard.

![updating-secrets](https://vtexhelp.vtexassets.com/assets/docs/src/updating-secrets___41a012c6f441bf927d67a59448c19894.gif)

### Deleting secrets

1. Go to the `Current Keys` section.
2. Next to the secret you need to update, click `⋮` and then click `Delete`.
3. Confirm the secret you want to remove.

   >⚠ This action can’t be undone.

4. Click `Delete secret`. A pop-up with `Secret deleted successfully` will open, and you'll see the message `Secrets have changed. Changes will take effect in the next successful deployment.` alongside a `Redeploy` button.
5. Click `Redeploy` to redeploy your website with the updated secret configuration. You’ll see the message `Redeploying with secret changes`, and a pop-up with `Deployment created successfully` will open.
6. Track the deployment status in the [Deploys](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#deploys) tab of the WebOps dashboard.

![deleting-secrets](https://vtexhelp.vtexassets.com/assets/docs/src/deleting-secrets___c5b464f532114c9895ce49af2fd8c76b.gif)

>ℹ If you tried to create, update, or delete a secret and got the error `Failed to create/update/delete secret. Please, try again.`, repeat the process. If the problem persists, open a ticket with [VTEX support](https://help.vtex.com/en/support).
