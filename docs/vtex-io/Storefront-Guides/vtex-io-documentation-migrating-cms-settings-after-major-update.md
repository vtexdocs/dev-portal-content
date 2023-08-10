---
title: "Migrating CMS settings after a major theme update"
slug: "vtex-io-documentation-migrating-cms-settings-after-major-update"
hidden: false
createdAt: "2020-09-22T20:44:01.218Z"
updatedAt: "2022-12-13T20:17:44.742Z"
---

You may need to perform a major update of your store theme app due to changes in its peer dependencies. However, transitioning to a new major version of the store theme could potentially result in undesired consequences, such as losing the configured Admin page template settings.

To handle this situation and ensure a smooth migration, follow the steps below to migrate template settings.

## Before you start

1. Install [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).
2. Install GraphQL IDE by running the following command: `vtex install vtex.admin-graphql-ide@3.x`.

## Instructions

1. Open the terminal and log in to your account.
2. Change to the **production workspace** containing your latest changes and [publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available#step-2---publishing-the-new-app-version) a new major version of your store theme app.
3. Create a new production workspace by running the following command:

 >ℹ️ Replace the values in curly brackets with the values that apply to your scenario.

  ```sh
  vtex use {workspaceName} --production
  ```

4. Install the store theme app published in the previous steps:

   ```sh
   vtex install {appVendor}.{appName}@{appVersion}
   ```

5. Open the VTEX Admin using the workspace created in Step 3 and go to the **GraphQL Admin IDE**:

  ```sh
  vtex browse admin/graphql-ide
  ```

6. From the **Choose an app** dropdown list, select `vtex.pages-graphql@2.x`.
7. Copy the code below and paste it into the GraphQL IDE.

  ```gql
  mutation{
    updateThemeIds(from:"{appvendor}.{appname}@{oldmajor}.x", to:"{appvendor}.{appname}@{newmajor}.x")
  }
  ```

8. Replace the values in curly brackets with the values that apply to your scenario, and press **Play**.
9. Open the VTEX Admin using the workspace created in the previous steps and validate the CMS content, routes, pages, and redirects.
10. Once you have validated your data, [promote your workspace to master](https://developers.vtex.com/docs/guides/vtex-io-documentation-promoting-a-workspace-to-master/).
