---
title: "FastStore WebOps: Preview your store changes before deployment"
slug: "2024-09-09-faststore-core-new-version"
type: "added"
excerpt: "FastStore WebOps users can now preview their pull request changes in a live environment before merging into production, reducing the risk of bugs and improving store quality."
createdAt: "2024-09-05T10:00:00.000Z"
---

The [FastStore WebOps app](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) now includes **Deployment Previews**, a feature that allows users to preview their pull request changes in a live environment before merging them into production. This helps minimize the risk of introducing bugs or unexpected behaviors to the live store, safeguarding the store user experience.

![webops-preview-example](https://vtexhelp.vtexassets.com/assets/docs/src/webops-preview___81240fb41a9ba63f108020f4193147e8.gif)

## What has changed?

Previously, FastStore WebOps users would commit changes to their repository without seeing a preview before sending them to production. This could lead to bugs being introduced to the live store, affecting the user experience.

Now, with the new deployment preview feature, FastStore WebOps users can check a store preview of their current deployment and prevent issues from reaching the live store.

## Why did we make this change?

With Deployment Previews, FastStore WebOps users can:

- **Reduce risk of bugs:** Catch and fix errors early in the development process.
- **Improve quality control:** Ensure that your changes align with your store's design and functionality.
- **Faster Development:** Iterate on your changes more efficiently without worrying about unintended behaviors.

## What needs to be done?

To enable the **Deployment Previews**, update the FastStore WebOps permissions on your store repository. Follow these steps:

1. Open your GitHub repository.
2. Click on the `⚙ Settings` tab to access the Settings page.
3. In the Settings page, got to **Integrations > GitHub Apps**.
4. In the FastStore WebOps app section click `Configure`.
5. You will see the message `FastStore WebOps is requesting an update to its permissions`. Click `Review request`.

   ![review-webops-permissions](https://vtexhelp.vtexassets.com/assets/docs/src/webops-review-permissions___2369dff18d193c85e02c640ac2a99c89.png)

6. Click `Accept new permissions`.
7. Make a small change to your store's code. This change is to create a commit and open a pull request to see if the new Deployment feature is available.

   > An example of a change, you can go to `src/themes/custom-theme.scss` and change one of the [Global tokens](https://developers.vtex.com/docs/guides/faststore/global-tokens-overview) of the stylesheet.

8. Submit the changes as a pull request.
9. Once you have open the pull request, look for the deployment preview link in the pull request details.:

   ![view-deployment](https://vtexhelp.vtexassets.com/assets/docs/src/pr-preview___7a3e866da3e934077b5a1f595dc00d69.png)

10. Click `View deployment` and a new browser tab will open with a new store preview.
