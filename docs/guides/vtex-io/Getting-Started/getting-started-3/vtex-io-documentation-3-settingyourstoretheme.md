---
title: "3. Creating a Store Theme project"
slug: "vtex-io-documentation-3-settingyourstoretheme"
hidden: false
createdAt: "2020-06-03T16:02:44.903Z"
updatedAt: "2022-12-13T20:17:44.902Z"
category: "Storefront Development"
excerpt: "Now that your development environment is set up, you are ready to dive in and create your very first Store Framework storefront."
seeAlso:
 - "/docs/guides/vtex-io-documentation-edition-app"
 - "/docs/guides/vtex-io-documentation-manifest"
 - "/docs/guides/vtex-io-documentation-creating-a-development-workspace"
 - "/docs/guides/vtex-io-documentation-linking-an-app"
---

This article provides a step-by-step guide on how to initiate a storefront project, also known as a Store Theme, for your online store. A Store Theme is a VTEX IO project that uses the `store` builder, and Store Framework blocks to create the storefront of a VTEX online store. The Store Theme is responsible for defining the visual and interactive elements of the store, such as the layout, colors, typography, icons, and animations.

To jumpstart our storefront project, we'll utilize a pre-defined [Store Theme boilerplate app](https://github.com/vtex-apps/store-theme) that will be further adapted to meet specific needs. This boilerplate app streamlines the process of creating a custom Store Theme by providing pre-defined templates and styles. In the upcoming sections of this getting started guide, we'll define templates, which involve configuring and combining components for each page of the store, and declare styles, including primary and secondary colors, typography scales, and spacing.

## Before you begin

Before downloading the Store Theme app, make sure your VTEX account has the [Store Edition](https://developers.vtex.com/docs/guides/vtex-io-documentation-edition-app) app installed, as recommended in this track's second step. Otherwise, you won't be able to successfully implement the VTEX Store Framework.

## Step 1 - Downloading the Store Theme app

The VTEX IO CLI simplifies the process of starting a new VTEX IO project by proving a list of pre-defined app templates. In the following steps, we will kick-start a new Store Theme project.

1. Using your terminal, navigate to an already existing local files directory where you want Store Theme to be copied to:

 ```sh
 cd {folderName}
 ```

 > ⚠️ Replace `{folderName}` with the actual folder name where you want to copy the Store Theme boilerplate app.

2. Run the `vtex init` command to start a new project from a list of pre-defined templates.

 ```sh
 vtex init
 ```

3. Select the `store` option confirm the destination folder. VTEX IO CLI will prompt you to continue creating the new folder. Type y to clone a `minimum-boilerplate-theme` to your folder.

 ![VTEX IO CLI-store-theme-selection](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-0.png)

4. Open the `minimum-boilerplate-theme` in the code editor of your preference.
5. Go to the `manifest.json` file and replace the predefined `vendor`  value with the account name of the store you're developing. This will ensure that you can publish the theme app correctly later on.

## Step 2 - Understanding the Store Theme's structure

In this section, we'll take a closer look at the files and folders that make up the Store Theme app's structure. Understanding the purpose of each file and folder will help you configure the store's templates and visual theme according to your needs.

The following files and folders comprise the Store Theme app:

```txt mark=5,9,16
📂 STORE-THEME/
│
├── 📂 .github/
├── 📂 public/
├── 📂 store/
│   ├── 📂 blocks/
│   ├── 📄 blocks.jsonc
│   └── 📄 routes.json
├── 📂 styles/
│   ├── 📂 configs/
│   └── 📂 css/
├── 📄 .editorconfig
├── 📄 .gitignore
├── 📄 .vtexignore
├── 📄 CHANGELOG.md
├── 📄 manifest.json
├── 📄 package-lock.json
└── 📄 README.md
```

- **`manifest.json`** - File containing the metadata about the app, including its vendor, name, version, [dependencies](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies/) and [builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders/).
- **`store`** - Folder containing the store's templates, including components and properties for various pages, such as the Product Listing Page and Product Details Page.
- **`styles`** - Folder containing the store's visual theme, such as colors, typography and other style-related settings.

It is important to note that the Store Theme boilerplate app you copied to your local machine already defines a basic theme for your store. You'll notice that code has already been declared in the `store` and `styles` folders, providing default components and styles to help you build your desired store frontend.

## Step 3 - Linking your local code to the VTEX IO platform

After setting up your local development environment and cloning the Store Theme boilerplate app, you'll want to sync your changes with the VTEX IO platform to preview them on your website. Since the boilerplate app already includes a default theme, you can immediately see how this theme affect your website's frontend. This is done using a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) and the `vtex link` command, which sends your code to the platform and allows you to see your changes in real-time.

1. Open the terminal and log in to your VTEX account.
```sh
 vtex login {account}
```

2. Create a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace).
3. Change to the `minimum-boilerplate-theme` directory.
4. Link the Store Theme app to the current workspace by running the following command:

 ```sh
  vtex link
 ```

 ![VTEX link example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-2.png)

By successfully running this command in your terminal, your local code is sent to the VTEX IO cloud-native infrastructure and it is reflected in the development workspace you are currently working in. Now, any changes you make to your Store Theme app files will be automatically reflected on your website in real-time.

## Step 4 - Checking out your new Store Theme

After linking your local code to the VTEX IO platform, you can check out your new Store Theme in action on your store's website. To do this, navigate to `https://{workspaceName}--{account}.myvtex.com`, replacing the values between brackets with your development workspace and VTEX account name.

Once you're logged in, you should see the following Store Theme rendered on your store's website:

![Store Theme](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-3-settingyourstoretheme-3.png)

Now that your store is using a default theme code, you can start configuring the Store Theme app to match your store's needs. This involves changing templates and customizing styles to build a unique identity for your store.
