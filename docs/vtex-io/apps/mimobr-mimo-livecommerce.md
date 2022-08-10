---
title: "Mimo Live Sales"
slug: "mimobr-mimo-livecommerce"
excerpt: "mimobr.mimo-livecommerce@0.5.6"
hidden: true
createdAt: "2022-07-05T20:04:39.602Z"
updatedAt: "2022-07-28T15:38:14.449Z"
---
Mimo Live Commerce VTEX IO integration app. This solution allows you to embed [Mimo's](https://mimo.com.br/) Player at any page/uri with no needed code customization.

⚠️ **IMPORTANT: This app works only at VTEX IO Stores.**

## Configuration

### Install Using VTEX App Store

It is possible to install in your store either by using App Store or the VTEX IO Toolbelt.

1. Access the **Apps** section in your account's admin page and look for the Mimo Live Commerce box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Ignore It.

## Account Setup
1. In Store's admin, look for **Mimo Live Commerce** page below tab: Other;
2. Login with your Mimo's credentials;
3. After login, you can choose a **Live Selected** and **Player status** (active or inactive) at settings window;
4. Click on **Save**.

## Player Setup

### Create a new page

1. In Store's admin, look for **CMS > Pages** page below tab;
2. Under pages, create a **new one**;
3. Fill page details and under **Templates**, choose **#mimoplayer** option;
4. Click on **Save**;
5. After that, the page will be available at the endpoint you filled.

### Add on existing pages using pageBlocks

1. Open your Store Theme app in your code editor;
2. Add the `mimo-livecommerce` app as a peerDependency in your theme's `manifest.json` file:
```json
  "peerDependencies": {
+   "mimobr.mimo-livecommerce": "0.x"
  }
```
3. This will create a new block named `mimoplayer` available;
4. In the `store/routes.json` file, add a new children in desired template as shown below:
```json
  "store.custom#any-page": {
     "children": [
+       "mimoplayer"
     ]
  }
```
5. **Thats it!**