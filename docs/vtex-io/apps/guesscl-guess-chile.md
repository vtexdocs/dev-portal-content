---
title: "ECOMSUR Vtex IO Starter Theme"
slug: "guesscl-guess-chile"
excerpt: "guesscl.guess-chile@2.0.8"
hidden: true
createdAt: "2022-07-04T21:06:15.445Z"
updatedAt: "2022-08-08T02:00:20.871Z"
---
The minimum Boilerplate Theme is basic store front model based on the VTEX IO Store Framework.

## Configuration

### Step 1 - Basic setup

Access the VTEX IO [basic setup guide](https://vtex.io/docs/getting-started/build-stores-with-store-framework/2) and follow all the given steps.

By the end of the setup, you should have the VTEX command line interface (Toolbelt) installed along with a developer workspace you can work in.

### Step 2 - Editing the `Manifest.json`

Once in the repository directory, it is time to edit the Minimum Boilerplate `manifest.json` file.

Once in are in the file, you must replace the `vendor` and `account` values. `vendor` is the account name you are working on and `account` is anything you want to name your theme. For example:

```json
{
  "vendor": "storecomponents",
  "name": "my-test-theme"
}
```

### Step 3 - Installing required apps

In order to use Store Framework and work on your store theme, it is needed to have both `vtex.store-sitemap` , `vtex.store`, `vtex.admin-search` and `vtex.search-resolver@1.x` installed.

In order to visualize products in shelf and product list page in necessary to indexe the product with grapql, so in the admin go to setup store > search > Integration settings and click in the indexe button

Run `vtex list` and check whether those apps are already installed.

If they aren't, run the following command to install them: `vtex install vtex.store-sitemap vtex.store vtex.admin-search vtex.search-resolver@1.x -f`

### Step 4 - Uninstalling any existing theme

By running `vtex list`, you can verify if any theme is installed.

It is common to already have a `vtex.store-theme` installed when you start the store's front development process.

Therefore, if you find it in the app's list, copy its name and use it together with the command `vtex uninstall`. For example:

```json
vtex uninstall vtex.store-theme
```

### Step 5- Run and preview your store

Then time has come to upload all the changes you made in your local files to the  platform. For that, use the `vtex link` command.

If the process runs without any errors, the following message will be displayed: `App linked successfully`. Then, run the `vtex browse` command to open a browser window having your linked store in it.

This will enable   you to see the applied changes in real time, through the account and workspace in which you are working