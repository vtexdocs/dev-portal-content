---
title: "Creating a Production workspace"
slug: "vtex-io-documentation-creating-a-production-workspace"
excerpt: "Learn how to create and use a production workspace." 
hidden: false
createdAt: "2020-06-03T16:02:44.959Z"
updatedAt: "2022-12-13T20:17:44.589Z"
---
Production [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/) are ready to handle live traffic. This guide provides step-by-step instructions on creating and managing a Production workspace.

Production workspaces serve multiple purposes, including quality assurance, testing, running A/B tests, and validating VTEX IO apps. It's important to note that for making changes or developing a new VTEX IO app, you must use a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).

## Creating a production workspace

1. [Log in to](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) your VTEX account.
2. Create a production workspace by running the following command:

```sh
vtex use {workspaceName} --production
```

> ⚠️ Replace `{workspaceName}` according to your scenario.

### Next steps

After testing your app and configurations, you can [promote a Production workspace to Master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master) to make your code changes available to the end-user.

Creating a Production workspace is one of the steps to making your code's new version public. Refer to the [Making your new app version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide for detailed information on subsequent steps.

## Deleting a workspace

You can manually delete workspaces that are no longer in use by running the following command:

```shell
vtex workspace delete {workspaceName}
```

>❗ Deleting a workspace is irreversible, and its content cannot be restored.

## Production workspace behavior

In Production workspaces, certain actions are permitted while others are restricted to maintain stability and reliability. Here is a summary of allowed and restricted actions:

| Action                                | Allowed |
|---------------------------------------|---------|
| [Install apps.](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) | ✅ |
| [Run A/B tests.](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) | ✅ |
| Handle traffic. | ✅ |
| [Promote to master.](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master) | ✅ |
| App development. | ❌ |
| [Link an app.](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) | ❌ |
| [Publish an app.](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) | ❌ |

## Key considerations

- **Code modifications:** Production workspaces strictly prohibit code changes in VTEX IO apps. To implement code modifications, it is necessary to switch to a dedicated [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).
- **Workspace inheritance:** Production workspaces are initiated independently and do not inherit code changes from a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace). Therefore, any modifications made in a Development workspace must be manually replicated to the new Production workspace. 
- **Data persistency:** Workspace settings persist unless conflicts arise with the Master workspace. In such cases, Master settings take precedence over settings in other workspaces, including the Development ones.
- **Expiration:** Once created, Production workspaces have no expiration date.
- **Deletion:** Unused workspaces are not automatically deleted. It is recommended to perform manual deletion to optimize platform resources and maintain an efficient operational state.
- **Organization:** Maintain a concise list of workspaces for organizational and resource efficiency reasons.
