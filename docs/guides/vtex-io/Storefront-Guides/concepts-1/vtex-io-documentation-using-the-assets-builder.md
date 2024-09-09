---
title: "Using the Assets Builder"
slug: "vtex-io-documentation-using-the-assets-builder"
hidden: false
createdAt: "2020-06-03T16:02:44.305Z"
updatedAt: "2022-12-13T20:17:44.494Z"
---

The VTEX Assets Builder is responsible for  **handling assets**  within Store Theme  `blocks` and CSS classes by getting all asset paths used and uploading them in the  **File Manager**  service.

As its name implies, the File Manager manages all of your store files and their respective URLs. It is able to translate the asset paths and then export the asset immutable URLs so that all block assets can be properly rendered.

The Assets Builder has two main advantages:

- You won't need to declare URLs for assets in each blocks, making your code lighter;
- You can use it whenever you want, having no prerequisites.

Check out the instructions to use it below:

## Instructions

1. Add the  `assets-builder`  to your theme's builder list in the  `manifest.json`  file. For example:

```JSON
"builders": {
  "assets": "0.x"
},
```

2. In the `store`  root directory of your app, create an  `assets` folder to manage your store's assets, such as images.
3. Then, add the desired asset files in the  `assets` folder. Notice that you can create subfolders within the  `assets`  folder to better organize the assets used by the theme blocks, as shown below:

![assets-folder](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-using-the-assets-builder-0.png)

> ⚠️ If you created subfolders inside the Assets folder, remember to include the folder hierarchy in the asset path, such as:  `assets/events/vtex-day.jpg`.

4. Use the asset path (`assets/{imageFileName}.{jpg/png/gif}`) as the value of a given block's prop, such as `src`, or CSS class for media rendering:

```JSON
"image": {  
    "props": {  
      "src": "assets/myimage.png"  
    }  
}
```

Once the asset path was added and you save the changes performed, Assets Builder will automatically work to save it in the VTEX IO File Manager and then generate a URL for it, which will be considered by the platform during the theme rendering.

A few things to consider:

- The Assets Builder is not responsible for URL caching, File Manager is;
- It is not possible to reference assets through React or other apps;
- Avoid long file names or unnecessarily heavy assets. This will negatively affect the request payload size and Builder optimization;
- Any *image* extension is allowed, such as **JPEG**, **PNG** and **GIF**. Videos are not allowed yet.
