---
title: "Updating Edition apps"
slug: "vtex-io-documentation-updating-edition-apps"
category: "App Development"
excerpt: "Learn how to publish a new version of an Edition app."
hidden: false
createdAt: "2020-06-03T16:02:44.265Z"
updatedAt: "2022-12-13T20:17:44.354Z"
---
After an [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) is [configured](https://developers.vtex.com/docs/guides/vtex-io-documentation-configuring-an-edition-app), you can launch new versions of it, either by defining new required apps for child accounts or by changing the Edition initial settings.

To do this, follow the walk-through below:

## Instructions

1. Open the Edition App folder and access the `apps.json` file using the code editor of your preference.
2. Make the desired apps and settings changes in the file.

  >⚠️ In a scenario in which an app that is already installed on the account is added to the Edition, the type of installation of that app will become `edition` and it can no longer be removed from the accounts or undergo any changes in major version since it is now enforced by the Edition. In the same way, removing apps from the `apps.json` will automatically uninstall them from all child accounts with this Edition. If an removed app is still needed in some of the child accounts, it will need to be manually and individually installed again in each desired child account.

3. Save and commit your changes;
4. [Publish and deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) the new Edition version.

After the new version is published, the Edition is automatically updated in all accounts. This automatic update is done asynchronously, periodically and individually in each child account.

> Notice that an Edition app version is updated only if its major has not been changed, meaning it is not a breaking change for the child accounts consuming that Edition.

In case bumping the major version is necessary due to the changes performed, the Edition update must be made manually and individually for each child account.
