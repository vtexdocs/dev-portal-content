---
title: "Installing apps on live stores"
slug: "vtex-io-documentation-installing-apps-in-live-stores-best-practices"
hidden: false
createdAt: "2020-06-03T16:02:44.252Z"
updatedAt: "2022-12-13T20:17:44.589Z"
---

Managing a live store comes with its own set of challenges, particularly concerning security, stability, and performance. Making changes, such as installing new apps, can feel risky if their potential impact isn't well understood. However, by following established best practices, you can minimize risks and maintain smooth operations, protecting your store's stability and conversion rates.

Combining manual testing in [development workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) with [A/B testing](https://developers.vtex.com/docs/guides/ab-tests) is a highly effective strategy. These steps allow you to identify and address potential issues before implementing changes for all users.

## Instructions

### Step 1 - Performing manual tests in a Development Workspace

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the app in a development workspace.
2. [Link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) your local files to the development workspace with VTEX IO.
3. Access the store via the development workspace URL: `{developmentWorkspaceName}--{accountName}.myvtex.com`.
4. Navigate the store and perform manual tests to ensure the app behaves as expected. Look for any functionality issues or unintended side effects.
5. Visit the master workspace (`{accountName}.myvtex.com`) to identify any unexpected changes introduced by the app.
6. If all tests pass, install the app in a [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace);

### Step 2 - Running A/B tests

Set up an [A/B test](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) between the master workspace and the production workspace. During configuration, manually set traffic distribution for each workspace, directing a small percentage of users to the Production workspace.

>⚠️ Avoid relying on automatic traffic segmentation, which splits traffic 50/50, as it exposes a larger audience to potential issues.

### Step 3 - Promoting your changes

1. If your changes involve a new major version of the Store Theme, refer to the [Migrating CMS settings after a major theme update
](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update) guide to avoid losing Admin page template settings.
2. Once validated, [promote the production workspace to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master), making the new configurations public for all your users.
