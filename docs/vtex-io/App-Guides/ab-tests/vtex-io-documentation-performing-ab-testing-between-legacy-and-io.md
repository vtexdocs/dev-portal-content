---
title: "A/B testing Legacy and IO store versions"
slug: "vtex-io-documentation-performing-ab-testing-between-legacy-and-io"
hidden: false
createdAt: "2022-04-04T18:23:34.122Z"
updatedAt: "2022-12-13T20:17:44.777Z"
---
In this guide, you will learn how to perform A/B testing between store workspaces in CMS Legacy and VTEX IO to confirm which workspace has the highest conversion rate for your store.

## Before you start

1. [Install the VTEX IO Command-line Interface (CLI)](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). Through the CLI, you can log in to your VTEX account, manage workspaces and develop new apps.

2. Ensure that you already have a Development workspace for your account. Otherwise, create and set up one following [Creating a Development workspace in IO for a CMS legacy store](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-development-workspace-for-cms-legacy) guide.

3. Ensure that your Development workspace has the `vtex.edition-store@5.x` Edition app installed. Run the `vtex edition get` in your terminal to verify the Edition App version installed on the current account. Otherwise, [Open a ticket to the VTEX support team](https://help-tickets.vtex.com/smartlink/sso/login/zendesk?_ga=2.222513819.1487123273.1647865109-1001456323.1619912759) requesting the installation of the `vtex.edition-store@5.x` Edition app in the new Development workspace.

## Step by step

### Step 1 - Developing your Store Framework theme

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log into your VTEX account by running the following command. *Remember to replace `{accountName}` with your VTEX account name.*

        ```bash
        vtex login {accountName}
        ```

2. Access the development workspace that you have created by running the following command. *Remember to replace the value between the brackets with the name of the development workspace you created in the previous step.*

        ```bash
        vtex use {workspace} 
        ```

3. Perfom the desired changes in the store theme in the development workspace. Refer to [Creating a Store Theme project](https://developers.vtex.com/docs/guides/vtex-io-documentation-3-settingyourstoretheme) guide for more information.

### Step 2 - Setting up the Legacy CMS

1. Once you have created and performed changes in the development workspace, [create a production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) to test your changes with some user traffic.

2. Run the `vtex use master` command in your terminal to perform the steps below in the master workspace. The master workspace must be set to the `vtex.edition-business@0.x` [Edition app](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app).

3. Install the `vtex.colossus-legacy-proxy@@1.8.9-hkignore` app by running the following command:

        ```bash
        vtex install vtex.colossus-legacy-proxy@@1.8.9-hkignore
        ```

#### `vtex.colossus-legacy-proxy@1.8.9-hkignore`

The app’s version must be `vtex.colossus-legacy-proxy@1.8.9-hkignore`. If not, the store won’t respond to the request. **Do not uninstall this app, as it's essential for proper store rendering.**

The `vtex.colossus-legacy-proxy` app routes requests from the store website within the VTEX IO environment. For example, during an A/B test between IO and Legacy CMS Portal, the store is placed inside the IO environment, and this app is configured in a workspace to route requests for the website to render the store. The `vtex.colossus-legacy-proxy@1.8.9-hkignore` points to the master workspace that is in Legacy CMS Portal and the `vtex.colossus-legacy-proxy@2.x` points to the development workspace in VTEX IO.

### Step 3 - Requesting an A/B test

1. [Open a ticket to the VTEX support team](https://help-tickets.vtex.com/smartlink/sso/login/zendesk?_ga=2.222513819.1487123273.1647865109-1001456323.1619912759) requesting the redirection of the production workspace to be rendered in VTEX IO. Pleasse provide the following information in your ticket:

      - Account name
      - Production workspace
      - Indicate whether the store features a distinct storefront for mobile devices.

2. Once the production workspace is rendering in the VTEX IO, you can enable the A/B test between the workspaces described in the [Running native A/B tests](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) guide.

### Step 4 - Validating if the A/B test is running

1. To ensure that the A/B test is working, send a `GET` request to the following API: `http://platform.io.vtex.com/{{accountName}}/_abtest/parameters`.

        >⚠️ The Header must have `VtexIdclientAutCookie` from the account you want to get the information. For example: `VtexIdclientAutCookie: {{VtexIdclientAutCookie}}`

2. The response indicates that the `master` is with 90% of the traffic and the `wsio` production workspace is with 10%.

        ```json
        "master": {
                "A": 9000,
                "b": 1
                },
                "wsio": {
                "A": 1000,
                "b": 1
                }

        ```

The response indicates that the `master` is with 90% of the traffic and the `wsio` production workspace is with 10%.

## Next Step

After finishing the A/B test and want to migrate your store to IO, [open a ticket to the VTEX support team](https://help-tickets.vtex.com/smartlink/sso/login/zendesk?_ga=2.222513819.1487123273.1647865109-1001456323.1619912759)  requesting the migration of your `development` workspace to the IO.
