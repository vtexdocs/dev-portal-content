---
title: "Developing an Edition App"
slug: "vtex-io-documentation-configuring-an-edition-app"
hidden: false
category: "App Development"
excerpt: "Learn now how to develop your own Edition Apps."
createdAt: "2020-06-03T16:02:44.714Z"
updatedAt: "2022-12-13T20:17:44.546Z"
---

If you belong to a complex VTEX account family under the same brand or holding, creating an [Edition App](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app/) can streamline the setup process of your accounts. This guide will walk you through the entire process of developing your Edition App and installing it on your child accounts.

## Before you begin

Before you dive into the development process, ensure that you have already [enabled the Sponsor Account behavior](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-sponsor-account) on one of your accounts.

## Instructions

To create a new Edition App, you'll initiate the development of a VTEX IO app. In this app, you will specify an Edition App dependency and define the apps to be included within the new Edition App.

### Step 1 - Creating an Edition app

1. Open the terminal and use [VTEX IO's CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) to log in to your Sponsor Account.
2. Run the `vtex init` command to start a new VTEX IO app project.
3. Select the `edition app` option when prompted. This will create a boilerplate repository in your local files.
4. Change to the `edition-app` folder and open the `manifest.json` file. It should look something like this:

    ```json
    {
      "vendor": "vtex",
      "name": "edition-hello",
      "version": "0.1.1",
      "title": "Getting Started with VTEX Edition Apps",
      "description": "A sample edition app with a blank apps.json",
      "builders": {
        "edition": "0.x"
      },
      "dependencies": {
        "vtex.edition-business": "0.x"
      },
      "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
    }
    ```

5. Customize the `manifest.json` file as follows:
   - Replace the `vendor` value with the name of your Sponsor Account.
   - Replace the `name` value with one of your choosing, using the `edition-` prefix for easier identification.
   - Set your app's `version`, `title`, and `description`.

### Step 2 - Setting the Edition dependencies

An Edition App inherits its dependencies, encompassing all associated apps and configurations. It's crucial to understand that every Edition app must define a dependency, which must either be a native Edition App (`vtex.edition-business` or `vtex.edition-store`) or a previously developed Edition App from the same `vendor`.

1. In the `manifest.json` file, go to the `dependecies` section.
2. Change the `dependencies` declaration according to your needs:
    - If you use [Legacy CMS Portal](https://help.vtex.com/tutorial/o-que-e-o-cms--EmO8u2WBj2W4MUQCS8262) and this is your first Edition App, set the `"vtex.edition-business": "0.x"` as a dependency.
    - If you use [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework) and this is your first Edition App, set the `"vtex.edition-store": "5.x"` as a dependency.
    - If you have more complex inheritance needs, change it to a previously developed Edition App from your `vendor`.
3. Save your changes.

### Step 3 - Declaring apps

After setting up the initial configurations for your Edition App, you can declare the bundle of apps and configurations it will include. Note that a Edition App can only contain apps exclusively developed by the same `vendor` responsible for its release.

1. Open the `edition/apps.json` file.
2. In the `apps` section, add all the apps and settings you want to install in the child accounts as in the following:

    ```diff
    {
        "apps": {
    +      "vtex.vtex-graphql-service": {
    +        "defaultMajor": 1,
    +        "allowedMajors": [0, 2],
    +        "allowsUninstall": false,
    +        "settings": {}
    +       }
        }
    }
    ```

    - `defaultMajor` or `major` - determines the major of the app.
    - (Optional) `allowedMajors` - specifies alternative majors that can be used by child accounts using the Edition App. If omitted, only the default major is allowed and cannot be changed.
    - (Optional) `allowsUninstall` - allows users to uninstall the app from the Edition manually using VTEX IO CLI (`vtex uninstall`). If omitted, it defaults to `false`, preventing app uninstallation by the child account.
    - (Optional) `settings` - defines the initial app settings when the app is installed in a child account. If omitted, which is recommended for most cases, no setting changes are made when installing the app.

    Note that the parent Edition always takes priority if any conflicts arise from declaring divergent app versions. This means you cannot change any inherited apps or configurations; you can only extend them.

3. Save your changes.

### Step 4 - Deploying the Edition App

Once you are sure of all the changes made, [publish and deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) your Edition App.

### Step 5 - Installing the Edition App on a child account

[Open a ticket](https://help-tickets.vtex.com/smartlink/sso/login/zendesk) with the VTEX Support team, requesting the installation of your new Edition App on the desired child accounts.

From the child accounts' perspective, the apps specified in an Edition App are immutable. That means they cannot modify or uninstall apps installed by a Sponsor Account.

If you need to modify any app or configuration of your Edition App, you must launch a new version with these changes. For more information, see the [Updating Edition apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-updating-edition-apps) guide.
