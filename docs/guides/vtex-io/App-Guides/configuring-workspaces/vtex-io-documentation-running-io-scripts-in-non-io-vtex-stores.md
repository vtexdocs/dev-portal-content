---
title: "Running IO scripts in non-IO VTEX stores"
slug: "vtex-io-documentation-running-io-scripts-in-non-io-vtex-stores"
excerpt: "Execute VTEX IO scripts in non-IO VTEX stores using a custom Scripts app."
hidden: false
createdAt: "2020-10-26T21:04:47.465Z"
updatedAt: "2022-12-13T20:17:44.117Z"
---

To make it possible to run VTEX IO scripts in non-IO VTEX stores, you must develop and release your own _Scripts app_.

A _Scripts app_ is an application that allows the usage of pre-defined VTEX IO scripts in pages external to the VTEX IO. That means that any VTEX store that installs your new _Scripts app_, even the ones that don't use the VTEX IO, can take advantage of running the VTEX IO scripts defined within your application in its website pages.

Notice that nothing keeps an account from having multiple _Scripts apps_ installed. Hence, we recommend that, when building a _Scripts app_, you define a clear goal and offer a suite of coherent functionalities.

In the following sections, we'll teach you how to develop and implement your own _Scripts app_.

## Before you begin

Before proceeding with the steps outlined in this document, ensure that you have the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install) installed on your machine.

## Instructions

### Step 1 - Clone the boilerplate repository

1. Using your terminal, clone the _Scripts app_ boilerplate repository to your local files by running:

   ```sh
   git clone https://github.com/vtex-apps/app-scripts-example
   ```

2. Then, using any code editor of your choice, open the boilerplate repository's directory.

### Step 2 - Update the manifest metadata

1. Open the `manifest.json` file and update its metadata, according to your scenario. It's essential that you update the following fields:
   - `vendor` - The app owner. That is, the VTEX account responsible for the app development, maintenance, and distribution.
   - `name` - The app name. It should concisely express the app's purpose. They must be comprised of lowercase letters separated by hyphens. Special characters, such as `*` and `@`, and numbers at the beginning of the name are not recommended.
   - `title` - The app distribution name. This name is the one used in the Apps section from the Administrative Panel and in the VTEX App Store.
   - `description` - A brief description explaining the app's purpose. This description will be publicly available in the App Store, providing context for whoever wants to install your app.

### Step 3 - Customize your script

1. In the `/scripts` folder, replace the example files with your own `.ts` script files.
2. In the `/scripts` folder, open the `loader.json` file and declare which scripts should be executed on which page. Each entry in the `loader` `JSON` object must have a `RegExp` key indicating the page path, and a corresponding array of strings. Each string in the array points to the script files that need to be loaded on a page when the `RegExp` key matches the URL path of that page .

Take the following example:

```json
{
  ".*": ["script1"],
  ".*/b$": ["script2"],
  ".*/p$": ["script2", "script3"]
}
```

In this example, the `script1` will be loaded and executed in all pages (`.*`) of the application.

For brand pages, expressed by URLs ending in `/b`, besides the `script1`, the `script2` will also be loaded.

Finally, for product pages, expressed by URLs ending in `/p`, besides the `script1`, the `script2` and the `script3` will also be loaded.

> ⚠️ Note that, by default, the scripts are located in the `scripts` folder. Hence, the complete path can be omitted. Also, as the scripts builder only looks for `.ts` files, it's not necessary to indicate file extensions.

Although a single `RegExp` can have multiple corresponding scripts and multiple `RegExp` can match a single URL path, each script is loaded and executed only one time per page, independently of how many occurrences it has in matched `RegExps`.

### Step 4 - Link your app

1. Open the Admin of the account you are using to develop your app, and follow the instructions provided in the [Importing scripts](#importing-scripts) section, considering a development workspace.
2. Once your app is set up, use the terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference/) to log in to the VTEX account that you are using to develop your VTEX IO _Scripts App_.
   > ⚠️ Remember to replace the values between the curly brackets according to your scenario.

   ```sh
   vtex login {accountName}
   ```

3. Change to development workspace.

   ```sh
   vtex use {workspace}
   ```

4. Go to the local app directory and [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) the app to your development workspace.

   ```sh
   cd app-scripts-example
   vtex link
   ```

### Step 5 - Test and deploy

1. Check the pages for which you implemented your scripts.
2. Make your new app version publicly available by following [this guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available/).

### Step 6 - Implement your app

Now that you finished developing your _Scripts_ app, you follow these steps to implement it in your desired VTEX account:

1. Using the VTEX IO CLI or the App Store, install the app you just developed in the desired account.
2. Follow the instructions provided in the [Importing scripts](#importing-scripts) section, considering a production workspace.

## Importing scripts

1. Considering the workspace in which you're currently working, open the Admin of the desired account and workspace.
2. Go to **Storefront > Layout**.
3. Open the desired page template.
4. Before the `body` closure, place a single HTML `script` tag to import the `load.js` file, as in the following examples:

### Development

```html
<script
  src="https://{devWorkspace}--{account}.myvtex.com/_v/public/vtex.scripts-server/v1/load.js"
  type="text/javascript"
></script>
```

where:

- `devWorkspace`- the development workspace of the account used to develop your _Scripts app._
- `account`- the name of the account used to develop your _Scripts app._

### Production

```html
<script
  src="/api/io/_v/public/vtex.scripts-server/v1/load.js?workspace={productionWorkspace}"
  type="text/javascript"
></script>
```

where:

- `productionWorkspace` - the production workspace of the account you are implementing the _Scripts app._

The `src` value from the `script` tag is the same for all pages in which you want to load your app's scripts.

According to the definitions from the `loader.json` file, the script server will load and execute only the appropriate scripts for that page: the ones whose the URL matches the `RegExps` from the `loader.json` file against the page path.

## App behavior

All scripts available in a _Scripts app_ are saved in its `/scripts` folder along with a `loader.json` file, which indicates in which page each script must be executed.

The scrips builder, set in the `manifest.json` file, is responsible for parsing each script declared in the `loader.json` file and for making them available to the `/load.js` route of the VTEX IO script server.

Hence, once you install a _Scripts app_ in a VTEX account, you can import the script server's route (`/load.js`) to your pages by using the `script` HTML tag.

Finally, according to the definitions from the `loader.json` file, the appropriate scripts for each page will be loaded and executed instantly.
