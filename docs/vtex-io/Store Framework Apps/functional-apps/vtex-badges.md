---
title: "Badges"
slug: "vtex-badges"
excerpt: "vtex.badges@3.5.0"
hidden: false
createdAt: "2022-07-04T19:51:14.430Z"
updatedAt: "2022-07-14T17:57:50.472Z"
---
This app allows you to add content badges to an ecommerce. In the Admin panel, you can create, edit and remove badges. There is also a storefront component that allows these badges to be added to your store theme.

## Setup

In order to setup **Badges** in your store, follow these steps:

1. Install the app. You can do this by going to the [Badges app page](https://apps.vtex.com/vtex-badges/p) in the VTEX app store or by running this command in your terminal:
```bash
  vtex install vtex.badges@3.x
```
2. Add **Badges** to the `peerDependencies` in your `manifest.json` file:
```json
"dependencies": {
  "vtex.badges": "3.x"
}
```

With this, you should be able to start using the app.

## Managing badges

After installing the app you will be able to access it by going to the `OTHER` section of the Admin panel and clicking `Badge Management`.

![badges home screen](https://user-images.githubusercontent.com/47991446/176534387-6ce7a70c-3c75-4e19-acf6-3211cfa69555.PNG)

### Creating badges

The `Add badges` tab allows you to create new badges by following these steps:
1. Fill in the name of the badge.
2. Select the badge type, which can be `IMAGE`, `TEXT` or `HTML`.
3. Insert the badge content, according to the selected type.
4. Select the badge priority level, where `1` is the maximum priority and `5` is the minimum.
5. Setup the activation rule, which is composed of one or more conditions.
6. Click `SAVE`.

See below a badge creation example.

![form fill](https://user-images.githubusercontent.com/47991446/176534433-be56d30d-bdf3-4c30-a933-235aba6b1115.PNG)

> ⚠️ Note that each badge must contain at least one activation rule condition with the verb `is`. The app will not work properly if all activation rules conditions use `is not`.

### Editing badges

To edit an existing badge, go to the `Edit badges` tab and follow these steps:
1. Click the menu icon in the row corresponding with the badge you wish to edit.
2. Click `Edit`.
3. Edit the badge attributes.
4. Click `EDIT`.

![edit badges](https://user-images.githubusercontent.com/47991446/176534410-67fac67e-3ae5-40ef-96a0-e8fabb09f2bb.PNG)

### Deleting badges

If you wish to delete an existing badge from your store, go to the `Edit badges` tab and follow these steps:
1. Click the menu icon in the row corresponding with the badge you wish to edit.
2. Click `Delete`.
3. In the prompt that will be displayed, click `DELETE`.

## Displaying badges in your store

In order to display the created badges in your store, you must add the `store-badges` component to a product page (`store.product`) or a `product-summary`. See an example of how to add badges to a product page below.

```diff
  "store.product": {
    "children": [
+     "store-badges",
      "stack-layout",
      "breadcrumb",
      "flex-layout.row#main",
      "condition-layout.product"
    ]
  },

+  "store-badges":{
+    "props": {
+      "numberOfBadges": 1,
+      "text":{
+        "font": "t-heading-5",
+        "textColor": "blue",
+        "textAlignment": "CENTER",
+        "textPosition": "CENTER",
+        "htmlId": "teste1"
+      },
+      "image":{
+        "blockClass": "container",
+        "height": 500,
+        "width": 500,
+         "minWidth": 25,
+         "minHeight": 25,
+         "alt": "teste",
+         "title": "title",
+         "preload": true
+      }
+    }
+  }

```

### Component props

These are the props available for customization of the badge component.

| Prop name     | Type     | Description                                                                                                                                                       |
| ---------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `numberOfBadges` | `number` | Number of badges that will be rendered.                                                                                                                        |
| `text`           | `array`  | Defines values that will be used when rendering a badge. To learn more about this prop see [Rich text](https://github.com/vtex-apps/rich-text).    |
| `image`          | `array`  | Defines values that will be used when rendering image badges. To learn more about these prop see [Store image](https://github.com/vtex-apps/store-image) |

## Final result

After finishing all steps, you can check the result in your store. The order of the badges is set according to the priority defined when creating them. See the image below, that corresponds to the badge setup in this tutorial's examples.

![result](https://user-images.githubusercontent.com/47991446/176911546-14dd3e5b-2af7-4f66-bd9e-2cd2c154cd09.PNG)