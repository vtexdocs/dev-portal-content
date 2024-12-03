---
title: "7. Making your theme content public"
slug: "vtex-io-documentation-making-your-theme-content-public"
hidden: false
category: "Storefront Development"
excerpt: "Learn how to make your Store Framework theme public."
createdAt: "2020-06-03T16:02:49.869Z"
updatedAt: "2024-11-29T15:09:48.674Z"
---

A Store Theme is a VTEX IO app, meaning it operates like any other app, with built-in features such as versioning and deployment capabilities.

In this guide, you will find instructions to make your Store Theme available to end users.

## Instructions

If you are satisfied with the configurations you’ve made and want your theme to be available to all users, follow the steps below:

1. [**Link**](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the theme to a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) to test your changes.
2. [**Release**](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version/) the theme.
3. [**Publish**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate version.
4. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) the theme in a [**Production workspace**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace/) to test your changes with traffic.
5. [**Validate**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate if no more changes are needed. If changes to the theme are required, you should go back to step 1 and use a Development workspace. **Do not perform changes using a production workspace**.  
6. [**Deploy**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a stable version if you are sure about all the changes you performed.
7. [**Promote the Production workspace to Master**](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/), finally making your theme public to your store's end users.

For more details on each of these steps, see [Making your new app version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available/).
