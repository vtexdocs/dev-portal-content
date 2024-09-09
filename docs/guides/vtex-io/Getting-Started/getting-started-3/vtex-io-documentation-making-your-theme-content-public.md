---
title: "7. Making your theme content public"
slug: "vtex-io-documentation-making-your-theme-content-public"
hidden: false
category: "Storefront Development"
excerpt: "Learn how to make your Store Framework theme public."
createdAt: "2020-06-03T16:02:49.869Z"
updatedAt: "2022-12-13T20:17:44.111Z"
---
Once you're using VTEX IO Store Framework, making a new version of your theme public (or even the first version) can be a big challenge if any of the necessary steps are unclear.

Note that your Store Theme works exactly as any other VTEX IO app. This means it takes on an app's default behavior, with its own versioning and deploys.

## Instructions

If you’re comfortable with the configurations you’ve performed and want your new theme to be made available to any user, you’ll need to:

1. [**Link**](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the theme to a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/) in order to test your changes;
2. [**Release**](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version/) the theme;
3. [**Publish**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate version;
4. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) the theme in a [**Production workspace**](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace/) in order to test your changes with traffic;
5. [**Validate**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a release candidate if no more changes are needed. If changes to the theme are required, you should go back to step 1 and use a Development workspace. You must not perform changes using a production workspace.  
6. [**Deploy**](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/) it as a stable version if you are sure about all the changes you performed;
7. [Promote the Production workspace to **Master**](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/), finally making your theme public to your store's end users.

For more details on each of these steps, you can check out the recipe on [**Making your new app version publicly available**](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available/), considering that your Store Theme works exactly as an app, as previously mentioned.
