---
title: "Publishing an app"
slug: "vtex-io-documentation-publishing-an-app"
hidden: false
createdAt: "2020-06-03T16:02:44.284Z"
updatedAt: "2022-12-13T20:17:44.112Z"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-deploying-the-app-stable-version"
---
After [releasing](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version) an app version, you must publish your app so that you can install it in certain accounts to perform A/B tests and validate your changes. In other words, you must turn your app into a **candidate version**.

A candidate version of an app is a build distributed internally for **testing purposes only**. It's intended to check, before deployment, whether any critical problems have gone undetected earlier during development. Ideally, there shouldn't be many differences between your app's last candidate version and its final build.

## Before you begin

Before proceeding any further, make sure the app you are about to publish has already been [released](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).

Notice that publishing an app is one of the steps to **making your new app version publicly available**. Please refer to [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide for more information.

## Instructions

### Step 1 - Publishing a candidate version

Until now, your app version exists only in a local environment. To make it possible to install it in specific accounts and run tests, you must first turn it into a candidate version.

1. Open the terminal and log in to the account responsible for the app development, i.e., the account specified as the app's `vendor` in the [Manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file.
2. Change to your app's root folder.
3. Publish your app by running the following command:

```
vtex publish
```

### Step 2 - Validating the candidate version

Before deploying your candidate version, you must install it in a new Production workspace and perform tests to check your app's behavior. Notice that production workspaces are ready to receive traffic and be accessed by other users.

1. Change to a new [Production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace):

- _Remember to replace the values between the curly brackets according to your scenario._

```sh
vtex use {workspaceName} --production
```

2. Install the candidate version by indicating the new app's exact version:

- _Remember to replace the values between the curly brackets according to your scenario._

```sh
vtex install {appvendor}.{appname}@{appversion}
```

3. Start an A/B test to test your candidate version. Please refer to [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) guide for more information.

From this point onwards, you won't be able to link apps or make any code changes in your app's current version. Hence, if you need to make any modifications to your app, you will need to retreat and work on it in a development workspace.

> ⚠️ If you are developing a new Store Theme major, follow the steps in the [Migrating CMS settings after a theme major update](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-cms-settings-after-major-update) guide before proceeding any further. Otherwise, you may lose page templates set up via the Admin.
