---
title: "Styles builder"
slug: "vtex-io-documentation-styles-builder"
excerpt: "Learn how to use the VTEX IO Styles builder."
hidden: false
createdAt: "2024-04-19T14:07:00.000Z"
updatedAt: "2024-04-19T14:07:00.000Z"
category: "App Development"
---

The `styles` builder helps you set a cohesive style for all components within your Store Theme app. During the app-building process, the `styles` builder interprets the `styles/style.json` file using [Tachyons](https://tachyons.io/) to generate your storefront’s CSS.

Using this builder, you avoid having to customize each component on different pages, as you set a standard style.

## Folder structure

An app that uses the `styles` builder has a folder named `\styles` in its root directory. The directory structure may vary depending on the specific project settings. 

Below is the folder structure of this builder:

```txt
styles
 ┣ 📄 style.json
```

The `style.json` file contains information relevant to styling, such as type scales, spacing, colors, typography, and other style-related settings. 

## Usage

If you are developing a Store Theme with VTEX IO and Store Framework from the [Store Theme boilerplate](https://github.com/vtex-apps/store-theme), the `styles` builder is installed automatically, and the `/styles` folder is created in the directory root.

>ℹ️ To learn more about app development using this builder, see the [Defining styles](https://developers.vtex.com/docs/guides/vtex-io-documentation-5-definingstyles) guide.

## Use case examples

An app using the `styles` builder has a folder named `/styles` in its root directory and the `style.json` file in it. The directory structure may vary depending on specific project settings. 

The basic structure of a `/styles` folder is composed of the following files, as you can see in the [Store Theme app](https://github.com/vtex-apps/store-theme) repository:

```txt
styles
 ┣ 📂 configs
      ┗ 📄 style.json
 ┣ 📂 css
```
      
- Within the `style.json` file, there is a set of values and configurations to be used to guide styling decisions.
- The `css` folder contains the CSS files, which, in turn, can be organized into different folders.
