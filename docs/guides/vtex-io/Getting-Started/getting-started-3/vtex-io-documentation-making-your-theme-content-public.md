---
title: "7. Making your theme content public"
slug: "vtex-io-documentation-making-your-theme-content-public"
hidden: false
category: "Storefront Development"
excerpt: "Learn how to make your Store Framework theme public."
createdAt: "2020-06-03T16:02:49.869Z"
updatedAt: "2025-01-22T17:41:31.648Z"
---

A Store Theme is a VTEX IO app that operates like any other app with built-in features such as versioning and deployment.

In this guide, you'll find instructions on how to make your Store Theme available to end users.

## Instructions

If you're satisfied with the configurations you've made and want your theme to be available to all users, follow the steps below:

1. [**Link**](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the theme to a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) to test your changes.
2. [**Release**](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version/) the theme.
3. [**Publish**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate version.
4. [**Install**](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) the theme in a [**production workspace**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace/) to test your changes with traffic.
5. [**Validate**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate if no more changes are needed. Otherwise, go back to step 1 and use a development workspace. **Don't perform changes in a production workspace**.
6. [**Deploy**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a stable version if you're sure about all the changes you've made.
7. [**Promote the production workspace to master**](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/) to make your theme public to your store's end users. Follow the [Deployment and workspace promotion](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspaces-best-practices#deployment-and-workspace-promotion) best practices to deploy changes and promote workspaces seamlessly.

For more details on each of these steps, see [Making your new app version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available/).

>ℹ To publish a new major version of your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) app, see [Migrating CMS settings after a major theme update](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update).
