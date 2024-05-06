---
title: "Assets builder"
slug: "vtex-io-documentation-assets-builder"
excerpt: "Learn how to use the VTEX IO Assets builder."
hidden: false
createdAt: "2024-05-06T10:53:00.000Z"
updatedAt: "2024-05-06T10:53:00.000Z"
category: "App Development"
---

The `assets` builder manages assets within VTEX IO apps. It does this by collecting all asset paths used and uploading them to the File Manager service.

The File Manager service manages store files and their respective URLs, translating asset paths and exporting immutable URLs for proper rendering of block assets.

>ℹ️ For more information about using this builder in a Store Theme app, see [Using the `assets` builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-assets-builder).

## Folder structure

An app that uses the `assets` builder has a folder named `\assets` in its root directory. The directory structure may vary depending on specific project settings.

You can add any image extension, such as `.jpeg`, `.png`, and `.gif`, as well as store font files (`.ttf`or `.woff`) to later [customize store typography](https://developers.vtex.com/docs/guides/vtex-io-documentation-customizing-your-stores-typography).

Assets can be added directly to the `/assets` folder, or for better organization, subfolders can be created within it, as illustrated below:

```txt
assets
 ┣ 📂 fonts
      ┗ 📄 {FileName}.woff
 ┣ 📄 {FileName}.jpeg
 ┣ 📄 {FileName}.png
```

## Usage

To use the `assets` builder in your app, follow these steps:

1. Add the `assets` builder to your app’s builder list in the `manifest.json` file, as shown below:

   ```json
   "builders": {
  	   "assets": "0.x"
   }
   ```

2. In the root directory of your app, create an `/assets` folder to manage store assets.
3. Add the asset files to the `/assets` folder. Add subfolders to organize the files as needed.
4. To use the stored assets within your app, use the asset path as the value of a given parameter. Note that if you have structured subfolders within the `assets` folder, you need to include the folder hierarchy in the asset path. For example: `assets/fonts/{FileName}.woff`.

## Use case examples

As an example, check the folder structure of this builder in the [B2B Theme app](https://github.com/vtex-apps/b2b-theme):

```txt
assets
 ┣ 📂 fonts
      ┗ 📄 {FileName}.woff
 ┣ 📂 icons
      ┗ 📄 {FileName}.svg
      ┗ 📄 {FileName}.svg
┗ 📄 {FileName}.jpg
```

- The `fonts` folder contains `.woff` files, which are web fonts.
- The `icons` folder holds `.svg` files, which may be icons, logos, graphics, and other vector images.
