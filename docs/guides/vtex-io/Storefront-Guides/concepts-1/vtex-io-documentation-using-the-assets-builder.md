---
title: "Using the Assets Builder"
slug: "vtex-io-documentation-using-the-assets-builder"
excerpt: "Learn how to use the Assets Builder to manage and reference images and other assets within your VTEX IO Store Theme."
hidden: false
createdAt: "2020-06-03T16:02:44.305Z"
updatedAt: "2022-12-13T20:17:44.494Z"
---

This guide explains how to use the [Assets Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-assets-builder) to handle assets, such as images, within your Store Theme. By following these steps, you can simplify asset management by letting the builder automatically handle file paths and uploads to the VTEX File Manager, making your theme's code lighter and more efficient.

Before you begin, keep the following points in mind:

- **Caching:** The Assets Builder is not responsible for URL caching; the File Manager handles this.
- **Scope:** You can only reference assets from your theme's `blocks` and CSS. It is not possible to reference them from React components or other apps.
- **File optimization:** Avoid long file names or unnecessarily large assets, as this can negatively affect request payload size and builder performance.
- **Supported formats:** You can use any image extension, such as `.jpeg`, `.png`, and `.gif`. Video files are not supported.

## Instructions

### Step 1 - Add the Assets Builder

1. Open your theme's `manifest.json` file.
2. Add the `assets` builder to the `builders` list:
   ```json
   "builders": {
     "assets": "0.x"
   },
   ```

### Step 2 - Create the assets folder

In the `store` root directory of your theme, create a new folder named `assets`. This folder will store all your theme's assets.

### Step 3 - Add asset files

Add your asset files to the `assets` folder. You can create subfolders within `assets` to better organize your files.

 ![assets-folder](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-the-assets-builder-0.png)

 > ⚠️ If you use subfolders, remember to include the full path when referencing the asset, such as `assets/events/vtex-day.jpg`.

### Step 4 - Reference the assets

Use the asset path (e.g., `assets/{fileName}.{extension}`) as the value for a block's prop, such as `src`, or a CSS class to render your media.

   ```json
   "image": {
     "props": {
       "src": "assets/myimage.png"
     }
   }
   ```

Once you save the changes, the Assets Builder automatically uploads the file to the VTEX File Manager and generates an immutable URL, which the platform will use when rendering the theme.
