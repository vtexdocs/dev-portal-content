---
title: "Customizing the B2B Store Theme"
slug: "customizing-the-b2b-store-theme"
hidden: false
createdAt: "2021-08-02T20:48:26.061Z"
updatedAt: "2022-07-13T14:50:53.504Z"
---
Once you have installed either the [B2B Store Theme](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme) or the [B2B New Store Theme](https://github.com/vtex-apps/b2b-newstore-theme) (when using the [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution), you can customize the theme according to your store’s business needs. To do so, follow the steps described below. 
[block:callout]
{
  "type": "warning",
  "body": "Do not proceed with these instructions if you haven't installed the [B2B Store Theme](https://developers.vtex.com/vtex-developer-docs/docs/installing-the-b2b-store-theme) or the [B2B New Store Theme](https://github.com/vtex-apps/b2b-newstore-theme) (if using the [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite) solution), or the customization will not work."
}
[/block]
## Step 1. Clone the boilerplate repository
 
First of all, you must clone the theme's boilerplate repository to your local files by running one of the following commands:

### B2B Store Theme

```
git clone https://github.com/vtex-apps/b2b-store-theme
```

### B2B New Store Theme (compatible with the [B2B Suite](https://developers.vtex.com/docs/guides/vtex-b2b-suite))

```
git clone https://github.com/vtex-apps/b2b-newstore-theme
```

## Step 2. Customize your storefront

Now you are ready to start working on storefront customizations using the code editor of your preference:

1. Open the repository folder in your local files.
2. In the `manifest.json` file, change:
    * The `vendor` field to the name of the account you are using.
    * The `name` field to one of your choosing.
3. Customize the files in your local repository by editing the theme’s blocks to create a storefront that matches your business needs and visual identity. Refer to our [Configuring templates](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-4-configuringtemplates) and [Block templates](https://developers.vtex.com/vtex-developer-docs/docs/concepts-1) guides for more information on how Store Framework blocks work.
4. Save all changed files locally.


## Step 3. Link the theme to your workspace

Once you have finished customizing your local files, you need to link them with your development workspace so that it reflects your local changes. Check out our [guide](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-linking-an-app) if you want to learn more about linking an app.
[block:callout]
{
  "type": "warning",
  "body": "Before you link your local files with your current workspace, you should run the `vtex whoami` command to check if you are using the account and development workspace where you want to apply your customizations."
}
[/block]

Follow the steps below to link your customized theme with your development workspace.

1. Using your terminal, access the customized theme repository folder in your local files.
2. Run the `vtex link` command to link your local files with the workspace you are logged into.
3. Run the `vtex browse` command to check out your customized storefront.


## Step 4. Publish your new theme

If you are comfortable with your new storefront and you want to make your changes public in your store’s production workspace, follow the steps described in our guide on [Making your new app version publicly available](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-making-your-new-app-version-publicly-available).