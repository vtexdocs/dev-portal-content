---
title: "Creating a Development workspace"
slug: "vtex-io-documentation-creating-a-development-workspace"
hidden: false
createdAt: "2020-06-03T16:02:44.266Z"
updatedAt: "2022-12-13T20:17:44.248Z"
---
[Workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/) in development mode allow you to [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/), [publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/), and [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) apps. These workspaces provide **greater development freedom** since **they do not handle traffic** from any user except yourself.

Because development workspaces do not have any level of user traffic, you should use them whenever you want to perform changes in your code. Note: Development workspaces cannot be [promoted to Master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/) nor used for [A/B testing](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing/). Only [Production workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace/) have these capabilities.

## Instructions

1. [Log in to](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) the desired VTEX account.
2. Run the following command:

```sh
vtex use {workspaceName}
```

> ⚠️ Remember to replace the value in the curly brackets according to your store scenario and needs.

Once created, the Developer workspace has no expiration date, which means that settings will remain stored in it unless there is a conflict with the store's Master workspace configurations. In these cases, **the Master settings will always prevail over the settings of other account workspaces**, including the Developer one in which you are working, since account workspaces work as a copy of the version available to end users.

Stick to the list of workspaces created for your account and keep a shortlist for two reasons:

- Organizational purposes.

- Spare platform infrastructure resources.

Currently, there is no automated service responsible for deleting unused workspaces from an account. This means you must manually delete workspaces that are no longer in use by running the command `vtex workspace delete {workspaceName}`.

> ⚠️ Be aware: once you **delete a workspace**, it is **not possible to restore it** and its content.

## Next steps

Once you are sure of the changes performed in the Development workspace, it is time to [create a Production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) to test your changes with some user traffic.

> ⚠️ **The Production workspace will not inherit the changes made in the Development workspace**. Any changes made in the Development workspace will need to be replicated in the new Production workspace.

Creating a Development workspace is one of the steps to make your code new version publicly available, allowing it to be accessed by your end users. For more details on the next steps and to better understand the complete flow, please refer to the documentation on [making your new app version publicly available.](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available)
