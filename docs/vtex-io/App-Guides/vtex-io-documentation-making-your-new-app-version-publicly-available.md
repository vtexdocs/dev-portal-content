---
title: "Deploying a new app version"
slug: "vtex-io-documentation-making-your-new-app-version-publicly-available"
excerpt: "Learn how to make your new app version publicly available."
hidden: false
createdAt: "2020-06-03T16:02:44.750Z"
updatedAt: "2022-12-13T20:17:44.423Z"
---

Deploying a new version of your app in VTEX IO is a crucial step in delivering improvements and updates to your target audience. This guide will walk you through the process to make your latest app version publicly available.

![public](https://github.com/vtexdocs/dev-portal-content/blob/main/images/making-an-app-publicly-available.png)

<Steps>

## Release the app

The Releasing stage marks the beginning of the deployment process in VTEX IO. It initiates the deployment process by releasing your app using Git as a version control system. It increments the app version in the `manifest.json` file, updates the `CHANGELOG.md file` with the changes, and creates a commit and a tag on the app repository.

For more information, refer to: [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).

## Publish a candidate version

In the Publishing stage, your app version becomes a candidate version, ready for testing and validation in a production workspace.

For more information, refer to: [Publishing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).

## Test the candidate version in a production workspace

Collaborate with your development and quality assurance teams to conduct thorough testing in a production workspace. This includes A/B testing, as well as rigorous performance and security testing to identify and address any potential issues with your app.

For more information, refer to: [A/B tests](https://developers.vtex.com/docs/guides/ab-tests).

## Deploy the app as a stable version

Initiate the deployment process to update the app version across all accounts where the app is installed, ensuring stability and consistency.

For more information, refer to: [Deploying the app's stable version](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version).

## (Optional) Promote your changes to `master`

The Promotion stage is *optional* and the final step in the deployment process. It involves promoting the production workspace used for testing to the master workspace.

For more information, refer to: [Promoting a workspace to `master`](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master).

</Steps>
