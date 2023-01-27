---
title: "3. Setting your store's theme"
slug: "vtex-io-documentation-3-settingyourstoretheme"
excerpt: "vtex.io-documentation@0.88.24"
hidden: false
createdAt: "2020-06-03T16:02:44.903Z"
updatedAt: "2022-12-13T20:17:44.902Z"
seeAlso:
 - "/docs/guides/vtex-io-documentation-4-configuringtemplates"
---

A store theme is every front end related to your website, from UI components to any applied customization.

For you to start using Store Framework, you therefore need to install the **Store Theme app** - the VTEX IO application responsible for defining your store's front using our framework.

The Store Theme app will define your store's theme by:

- **Declaring templates**, namely configuring and mixing components for each of your store's page.
- **Declaring styles**, namely configuring primary and secondary colors, typography scales and spacing, etc.

## Step 1 - Installing the Store Theme app

> ⚠️ Before installing the Store Theme app, make sure your VTEX account has the Store Edition app installed, as recommended in this track's second step. Otherwise, you won't be able to successfully implement the VTEX Store Framework.

The VTEX IO CLI offers the `vtex init` command which can quickly copy the Store Theme app repository to your computer, where it may be configured and fine-tuned according to your business needs.

1. Using your terminal, navigate to an already existing local files directory where you want Store Theme to be copied to:

```sh
cd {example folder}
```

> ⚠️ Note that `{example folder}` should be replaced with the folder name where the Store Theme is going to be copied to.

2. Run the `vtex init` command:

```sh
vtex init
```

3. Select the `store` option and confirm that you want to download the theme folder to the destination you just chose:

![VTEX IO CLI-store-theme-selection](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-0.png)

> ℹ️ Once you select the `store` option, VTEX IO CLI will ask you if you want to continue to create the new folder, by typing `y` it will clone a `minimum-boilerplate-theme` to your folder.

4. On the `manifest.json` file, replace the predefined `vendor` value with the account name of the store that you are developing so that you'll be able to correctly publish its theme app later on.

## Step 2 - Understanding the Store Theme's structure

Once you select the `store` option, VTEX IO CLI will create a copy of the Store Theme app in your local files, allowing you to work on it as you please.

Open the newly created Store Theme folder in your local files using any code editor, such as Visual Studio Code. You can also use your terminal directly to achieve the same result:

```sh
cd store
```

To better understand the app's structure, let's have a closer look at its files and folders:

![Repository tree](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-1.png)

- **`manifest.json`** - App's main file. It stores important metadata, such as the app's *vendor*, name, version, [dependencies](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-dependencies/) and [builders](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-builders/).
- **`store`** - Folder responsible for defining the store's templates. It's where you configure each page's components and properties.
- **`styles`**: folder responsible for setting the store's visual theme. It's where you configure colors, typography and anything related to the store's style.

> ℹ️ Taking a closer look in the `store` and `styles` folder and their files, you'll notice code already being declared there. The reason behind this is that the Store Theme app that was copied to your local machine is already defining a basic theme for your store, declaring default components and styles to help you build your desired store front end.

## Step 3 - Linking your local code to the VTEX IO platform

Since Store Theme already declares a default theme, you can check your website's front end in real time once the app is installed.

You'll need to sync your local files, where your Store Theme app code was copied and is now stored, with the VTEX IO platform (responsible for supporting the VTEX Store Framework operation). This is achieved by running the `vtex link` command in your terminal:

```sh
 vtex link
```

> ⚠️ You can run `vtex whoami` in your terminal to make sure that you're logged into the right VTEX account and using the Development workspace you've just created. Otherwise, the link won't work.

![VTEX link example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-2.png)

By successfully running this command in your terminal, your local code is sent to the VTEX IO cloud-native infrastructure and it is reflected in the development workspace you are currently working in.

## Step 4 - Checking out your new store theme

Navigate to your store's website by accessing `https://{workspaceName}--{account}.myvtex.com`, replacing the brackets and their values with your Development workspace and VTEX account names.

After logging in, you should already see the new store theme rendered in your store:

![Store Theme](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-3.png)

Now that your store is online and using a default theme code, we can build its identity by configuring the Store Theme app according to your store's needs: it's time to change templates and customize styles!
