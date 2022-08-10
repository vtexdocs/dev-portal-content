---
title: "Checkout UI Settings"
slug: "gbarbosaqa-checkout-ui-settings"
excerpt: "gbarbosaqa.checkout-ui-settings@0.5.25"
hidden: true
createdAt: "2022-08-05T14:06:13.140Z"
updatedAt: "2022-08-05T14:06:13.140Z"
---
The Checkout UI Settings app is responsible for customizing your store's Checkout UI.

The main advantage of using the app instead of the [store's admin](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en) for this customization is that your checkout scripts will behave as VTEX IO apps. It allows you to manage versions, have a different checkout customization by workspaces, etc.

In practice, it means that Checkout UI Settings allows A/B testing in your store's scripts, in addition to the possibility of quick rollbacks for old scripts (i.e. scripts pertaining to older Checkout UI Settings app's versions).

## Configuration
1.  Using your terminal and the [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference), run `vtex login` to log into the desired account;
2. Run `vtex use {workspace}` to create your dev workspace;
3. Run `yarn build` to compile your customization files;
4. Run `vtex link` to link and see your changes at workspace;
5. If everthing is ok and done, run `vtex release` to [publish](https://vtex.io/docs/recipes/development/publishing-an-app) the app's new version;
6. Still logged into the desired account, and run `vtex use {workspace} --production` to [create a production workspace](https://vtex.io/docs/recipes/development/creating-a-production-workspace) and then `vtex install` to [install the app](https://vtex.io/docs/recipes/development/installing-an-app);
7. If everything is working as expected, run `vtex workspace promote` to [promote the workspace to master](https://vtex.io/docs/recipes/development/promoting-a-workspace-to-master) and then `vtex deploy`.