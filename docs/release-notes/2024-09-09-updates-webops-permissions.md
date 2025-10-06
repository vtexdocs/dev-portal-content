---
title: "FastStore WebOps: Preview your store changes before deployment"
slug: "2024-09-09-updates-webops-permissions"
type: "added"
excerpt: "FastStore WebOps users can now preview their pull request changes in a live environment before merging them into production, reducing the risk of bugs and improving store quality."
createdAt: "2024-09-05T10:00:00.000Z"
updatedAt: "2024-09-09T16:00:00.000Z"
tags:
  - WebOps
  - FastStore
---

The [FastStore WebOps app](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) now includes **Deployment Previews**, a feature that allows users to preview their pull request changes in a live environment before merging them into production. This feature helps minimize the risk of introducing bugs or unexpected behaviors to the live store, safeguarding the store user experience.

![webops-preview-example](https://vtexhelp.vtexassets.com/assets/docs/src/webops-deployment-overview___2ad1ba00eeeae1bb590d159271449936.gif)

## What has changed?

Previously, FastStore WebOps users could commit changes to their repository and preview them in the [Dashboard](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard), but this required finding the specific commit in the [Preview Deploys](https://developers.vtex.com/docs/guides/faststore/1-onboarding-dashboard#preview-deploys) list.

Now, with the new deployment preview feature, developers can see store previews directly on GitHub, staying focused on their tasks and reducing the risk of introducing issues to the live store.

## Why did we make this change?

With Deployment Previews, FastStore WebOps users can:

- **Reduce risk of bugs:** Catch and fix errors early in the development process.
- **Improve quality control:** Ensure your changes align with your store's design and functionality.
- **Faster Development:** Iterate on your changes more efficiently without worrying about unintended behaviors.

## What needs to be done?

To enable the **Deployment Previews**, update the FastStore WebOps permissions on your store repository. Follow these steps:

1. Open your GitHub repository.
2. Access the Settings page on the `⚙ Settings` tab.
3. On the Settings page, go to **Integrations > GitHub Apps**.
4. In the FastStore WebOps app section, click `Configure`.
5. You will see the message `FastStore WebOps is requesting an update to its permissions`. Click `Review request`.

   ![review-webops-permissions](https://vtexhelp.vtexassets.com/assets/docs/src/webops-pr-preview___ca4ce57e2afa1323eb0c678e98f6c73b.png)

6. Click `Accept new permissions`.
7. Make a small change to your store's code.

   > ℹ️ For example, you can go to `src/themes/custom-theme.scss` and change one of the [Global tokens](https://developers.vtex.com/docs/guides/faststore/global-tokens-overview) of the stylesheet.

8. With this change, create a commit and open a pull request to see if the new Deployment feature is available.

9. Submit the changes as a pull request.
10. Once you have opened the pull request, look for the deployment preview link in the pull request details:

      ![view-deployment](https://vtexhelp.vtexassets.com/assets/docs/src/webops-pr-deploy-preview___ac839d3368cab18043e87c9516333198.png)

11. Click `View deployment`, and a new browser tab will open with a new store preview.
