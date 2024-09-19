---
title: "2. Creating the new app"
slug: "vtex-io-documentation-3-creating-the-new-app"
hidden: false
createdAt: "2021-03-25T20:58:43.434Z"
category: "App Development"
excerpt: "Now that your development environment is set up, it is time to start developing your new React app."
seeAlso:
 - "/docs/guides/vtex-io-documentation-manifest"
 - "/docs/guides/vtex-io-documentation-builders"
---

To begin developing your app, you need to follow these steps:

- Clone the React [boilerplate app](https://github.com/vtex-apps/react-app-template) to your local files.
- Modify the `manifest.json` file in the React example app to include your app's information, such as its name, version, vendor, and dependencies.
- [Link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace.

Once copied, the repository will automatically import the basic settings that you will need to kickstart your app development.

## Instructions

### Step 1 - Cloning the boilerplate repository to your local files

Clone the boilerplate repository to your local files by running the following command:

 ```sh
 git clone https://github.com/vtex-apps/react-app-template
 ```

### Step 2 - Editing the `manifest.json` file

Now, let's examine the manifest.json file, which contains essential information about the app such as:

- `vendor` - Name of the VTEX account responsible for developing, maintaining, and distributing the app.
- `name` - App name of your choice. Avoid special characters.
- `version` - Current version of the app following [Semantic Versioning 2.0.0](https://semver.org/) standards.
- `title` - The distribution name of the app that is displayed on the `Apps` section in the admin and, also, on the VTEX App Store.
- `description` - Brief description of the app's features.
- `builders` - List of [builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders/) that facilitate the app's development by abstracting service configurations.
- `dependencies` - List of apps that the app you are developing depends on for proper functioning.

Incorporating the new app's basic information into the `manifest.json` file is a crucial step at the beginning of the development process. This step is essential to make the app unique and distinct from the example version provided by VTEX.

To add this information, open the app's code in your code editor, and update the `manifest.json` file as in the following:

1. Replace the `vendor` field value with the name of the VTEX account you are using for development.
2. Replace the `name` field value with the name of your app. Avoid using special characters, except hyphens (-).
3. Replace the values in the `title` and `description` fields with appropriate ones that describe the app you are developing.
4. Add the `store@0.x` builder to the builder list to allow the creation of new blocks:

  ```diff
  "builders": {
  +  "store": "0.x"
  }
  ```

5. If you want to import any React components previously developed for your new app, update the `dependencies` list with the name and version of the app that runs the desired component. For example:

  ```diff
  "dependencies": {
  +  "vtex.styleguide": "9.x"
  }
  ```

This will allow you to later import the app component added in `dependencies` into your code via the `import {componentName} from '{dependency}'` structure.

### Step 3 - Linking your app

To upload all the changes you made in your local files, you must link your app to the current development workspace by running the following command:

  ```sh
  vtex link
  ```

If the process runs without any errors, the following message will be displayed: `App linked successfully`.

To check and review your local app code, run the `vtex browse` command to open a browser window for your current workspace. Alternatively, access `https://{workspace}--{account}.myvtex.com`, replacing `workspace` with the development workspace in use and `account` with the name of your VTEX account.

>ℹ️ When linking an app to a development workspace, the `yarn install` command is automatically executed in the builder directories (e.g., `node` and `react` directories). Nevertheless, for an enhanced development experience, consider manually running `yarn install` in the root folder of your project to activate additional features, such as linter and prettier checks.
