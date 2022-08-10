---
title: "Checkout UI Settings"
slug: "vtex-checkout-ui-settings"
excerpt: "vtex.checkout-ui-settings@0.1.0"
hidden: false
createdAt: "2020-06-03T15:19:09.589Z"
updatedAt: "2022-05-20T00:24:43.708Z"
---
# Checkout UI Settings

The Checkout UI Settings app allows you to customize your store's through the terminal and the [VTEX IO Toolbelt](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install).

The main advantage of using the app instead of the [store's admin](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en) for this customization is that your Checkout scripts will behave as configurations for platform apps.

In practice, it means that Checkout UI Settings allows A/B testing in your store's scripts, in addition to the possibility of quick rollbacks for old scripts (i.e. scripts pertaining to older Checkout UI Settings app's versions).

## Configuration

1.  Using your terminal and the [VTEX IO Toolbelt](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-install), log into the desired account;
2.  Run `vtex list` to access the list of apps that are already installed on the account you're working on. If the Checkout UI Settings option already exists, you can skip to step 7 of this step-by-step;
3.  If the Checkout UI Settings app was not found in the list of installed apps, run the `vtex init` command;
4. Select the `checkout-ui-settings` option;
5.  Open the `checkout-ui-settings`  app in whichever code editor you prefer;
6.  In the  `manifest.json`  file, change the predefined default value  `vendor`  to the name of the account in which you want to install the app;
7.  In the  `checkout-ui-custom`  folder, create the files in which the scripts will be included, just as you would do in the [admin's interface](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configure-code). Notice that a few defaults files already exist in the `checkout-ui-custom` folder, files which you can use to insert the scripts;
8.  According to the Checkout customization you are looking for, open the most suitable file and insert the desired scripts;
9.  Save your changes. Then, [publish](https://vtex.io/docs/recipes/development/publishing-an-app) the app's new version;
10. Still logged into the desired account, [create a production workspace](https://vtex.io/docs/recipes/development/creating-a-production-workspace) and [install the app](https://vtex.io/docs/recipes/development/installing-an-app);
10. If everything is working as expected, [promote the workspace to master](https://vtex.io/docs/recipes/development/promoting-a-workspace-to-master).

## Modus Operandi 

Once the app is deployed and installed in the account, every scripts contained in it will be automatically linked to your store and used to [build the templates](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configuring-templates-from-the-code-menu) to customize your Checkout.
[block:callout]
{
  "type": "warning",
  "title": "Scripts used by Checkout are linked to the Checkout UI Settings version that's installed in your store",
  "body": "If a prior app version was already installed and your want to change the scripts linked to it, you'll need to repeat the already existing code and thereafter launch the app's new version containing the changes you just did. Housekeeper is responsible for updating app versions in the accounts it's installed."
}
[/block]

[block:callout]
{
  "type": "warning",
  "title": "If you are using the classic CMS (Legacy):",
  "body": "You can create a workspace and install the app there. While using the app, you will need to apply your changes and copy/paste the content of the files to your portal."
}
[/block]