---
title: "Creating a Development workspace"
slug: "vtex-io-documentation-creating-a-development-workspace"
excerpt: "Learn how to create and use a Development workspace." 
hidden: false
createdAt: "2020-06-03T16:02:44.266Z"
updatedAt: "2022-12-13T20:17:44.248Z"
---
Development [workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace/) allow you to [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/), [publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app/), and [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) apps. These workspaces provide greater freedom in code development without affecting user traffic and the live store.

Since Development workspaces operate in isolation from user traffic, they are ideal for making code changes. Note: Development workspaces cannot be [promoted to Master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/) or used for [A/B testing](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing/); these capabilities are reserved for [Production workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace/).

## Instructions

1. [Log in to](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) the desired VTEX account.
2. Create a development workspace by running the following command:

    ```sh
    vtex use {workspaceName}
    ```
    
    > ⚠️ Replace `{workspaceName}` according to your scenario.

## Next steps

Embark on your development journey by creating a new app using our [template apps](https://developers.vtex.com/docs/guides/code-samples) or [build from scratch](https://developers.vtex.com/docs/guides/vtex-io-getting-started). [Link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) and initiate the development process. Once satisfied with the changes in your Development workspace, change to the next phase by creating a [Production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace). This step ensures comprehensive testing of your modifications under real user traffic conditions.

## Deleting a workspace

You can manually delete workspaces that are no longer in use by running the following command:

```shell
vtex workspace delete {workspaceName}
```

>❗ Deleting a workspace is irreversible, and its content cannot be restored.

## Development workspace behavior

In Development workspaces, certain actions are permitted while others are restricted to maintain stability and reliability. Here is a summary of allowed and restricted actions:

| Action                                | Allowed |
|---------------------------------------|---------|
| [Install apps.](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) | ✅ |
| [Run A/B tests.](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) | ❌ |
| Handle traffic. | ❌ |
| [Promote to master.](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master) | ❌ |
| App development. | ✅ |
| [Link an app.](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) | ✅ |
| [Publish an app.](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) | ✅ |

## Key considerations

- **Workspace inheritance:** Production workspaces are initiated independently and do not inherit code changes from a [Development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace). Therefore, any modifications made in a Development workspace must be manually replicated to the new Production workspace. 
- **Data persistency:** Workspace settings persist unless conflicts arise with the Master workspace. In such cases, Master settings take precedence over settings in other workspaces, including the Development ones.
- **Expiration:** Once created, Production workspaces have no expiration date.
- **Deletion:** Unused workspaces are not automatically deleted. Manually deleting unused workspaces is recommended to optimize platform resources and maintain an efficient operational state.
- **Organization:** Maintain a concise list of workspaces for organizational and resource efficiency reasons.
