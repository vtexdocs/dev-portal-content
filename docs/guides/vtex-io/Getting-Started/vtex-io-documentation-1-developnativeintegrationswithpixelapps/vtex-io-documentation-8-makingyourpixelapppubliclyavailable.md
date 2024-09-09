---
title: "7. Deploying your Pixel app"
slug: "vtex-io-documentation-8-makingyourpixelapppubliclyavailable"
excerpt: "Learn how to deploy your Pixel app for wider use on the VTEX IO platform."
hidden: false
category: "App Development"
createdAt: "2020-11-03T18:19:23.096Z"
updatedAt: "2022-12-13T20:17:44.384Z"
---

Until this point, your Pixel app has been restricted to your local development environment, functioning exclusively within the context of your [development](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) workspace.

Once you are happy with your app development, the next step is to transition it into a publicly accessible state, allowing other users to install and utilize your Pixel app. It's worth emphasizing that [linking](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) the app you are working on in a development workspace is not enough. To make it available in the VTEX IO platform, you will need to release, publish, test, and, finally, deploy it. 

## Instructions

### Step 1 - Defining your app distribution

The first step involves establishing the distribution aspects of your app. This decision involves determining who will have access to install your app and whether you intend to charge users.

Your choice regarding distribution type falls into one of two categories within the VTEX IO platform:

- **Private** - This option restricts installation to the `vendor` account, which is the VTEX account responsible for the app development and maintenance.
- **Public** - This option makes your app accessible to all account ecosystems within the VTEX platform.

To set up your preferences, you will need to update the app's `manifest.json` file and configure specific fields based on the chosen distribution model. Detailed guidance on configuring these settings is available in the [Billing Options](https://developers.vtex.com/docs/guides/vtex-io-documentation-billing-options/) article.

### Step 2 - Releasing a new version

Assuming you are confident in the changes made in your development workspace, it is time to launch a new version of your app. 

1. Open the terminal and log in to the VTEX account corresponding to the app's `vendor`.
  - _Replace `{vendorAccount}` with the name of the `vendor` account._ 
  ```sh
  vtex login {vendorAccount}
  ```
2. Navigate to the app directory and execute the following command:
  ```sh
  vtex release major
  ```

This command will:

- Update the app's version in `CHANGELOG.md` and `manifest.json` files following [SemVer](https://semver.org/) guidelines.
- Create a release commit.
- Set up a new GitHub repository for your app.

> For a **beta** release, use `vtex release major beta` instead. This will perform the same actions as the previous command, with the difference that you will release a beta version of your application instead of *stable* one.

Notice that, until this step, the app has not been published to the platform yet. The `vtex release major` command only ran actions for the app versioning.

### Step 3 - Publishing the app in the VTEX IO platform

Once you've released your app, the next step is publishing it on the VTEX IO platform. This step is essential to allow your app to be installed in [production](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace) workspaces. This, in turn, will allow you to test your app's functionality in real-world scenarios.

In the terminal, change to the app directory and run the following command:

```sh
vtex publish
```

> ℹ️ You must always be logged into the desired VTEX account for publishing the app. Ensure the app's `vendor` is the same as the account you're working on.

The publish command will make your app a ***release candidate version***, enabling it to be installed via the VTEX IO CLI for testing purposes in production workspaces.

>⚠️ If your app does not have the `billingOptions` field configured, users with access to the VTEX account responsible for the publication will also be able to install the app via the Admin in the **Apps** section.

### Step 4 - Installing it in a production workspace

Now, to test your app's settings and behaviors, create a production workspace. 

1. In the terminal, run the following command:
  - _Replace `{workspaceName}` with the desired name for your new workspace._
  ```sh
  vtex use {workspaceName} --production
  ```
2. Run the command below to install the app in the new workspace, replacing the values between curly braces according to your scenario:

  ```sh
  vtex install {vendorAccount}.{appName}@{appVersion}
  ```

From this point, changes in your app code are no longer permitted since production workspaces are not intended for development. If you need to make changes to your app, switch to a development workspace and follow this guide again.

### Step 5 - Validating your app

Now, it's time to validate your release candidate version. We recommend running a [native A/B test](https://developers.vtex.com/docs/guides/vtex-io-documentation-running-native-ab-testing) between the new production workspace and your store's Master workspace to check the app stability.

> If you're working with a beta version and everything is tested correctly, return to [Step 2](#step-2-releasing-a-new-version) to release the stable version.

If you are happy with the results, change to the app directory in the terminal and run the following command to deploy the *release candidate* version as a *stable* version:

```sh
vtex deploy
```

This command will automatically install your app's new *stable* version in all accounts that had previously installed the release candidate version.

## Extra steps

### Promoting your production workspace to Master

Promote the production workspace where the app was installed to Master to use your Pixel app on your store website. In the terminal, ensure you're logged into your VTEX account and using the production workspace from the previous steps. Then, run the following command:

```sh
vtex workspace promote
```

> ℹ️ The status of a Master workspace is `production true`. Once you receive this response from your terminal, your new Pixel app is already available on your store website.

By the end of these steps, your Pixel app will have been released, published, tested, validated to be deployed, and finally made available on your store website.

### Submitting your app to the VTEX App Store

You can also add your Pixel app to the [VTEX App Store](https://apps.vtex.com/), a marketplace for plug-and-play solutions. Check the [VTEX App Store](https://developers.vtex.com/docs/guides/vtex-app-store) documentation section for more information.
