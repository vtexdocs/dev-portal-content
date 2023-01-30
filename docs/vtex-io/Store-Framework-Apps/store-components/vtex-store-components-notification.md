---
title: "Notification"
slug: "vtex-store-components-notification"
hidden: false
createdAt: "2020-06-03T16:04:30.371Z"
updatedAt: "2022-11-22T18:39:23.075Z"
---
The `notification` component displays text content in a bar style (`notification.bar`) or inline (`notification.inline`). This Component can be imported and used by any VTEX app.

![notification-bar](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-store-components-notification-0.png)
## Configuration

1. Import the `vtex.store-components` app to your theme's dependencies in the `manifest.json` file as in the following example:

```json
  "dependencies": {
    "vtex.store-components": "3.x"
  }
```

2. Add the `notification` block to any template of your choice. For example:

```diff
  "store.home": {
      "blocks": [
+       "notification.bar",
        "carousel#home",
        "shelf#home"
      ]
    },
```

3. Then, declare the `notification` block using the props stated in the [Props](#props) table.

### Props

| Prop name | Type | Description | Default value |
| --------- | ---- | ----------- | ------------- |
| `content` | `String` | Text to be used in the bar. | '' |
| `classes` | `CustomCSSClasses` | Overrides default CSS handles. To better understand how this prop works, check [this document](https://github.com/vtex-apps/css-handles#usecustomclasses). Note that this is only helpful if you're using this block as a React component.| `undefined` |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles                     |
| ------------------------------- |
| `notificationBarContainer` | 
| `notificationBarInner` |
| `notificationContent` |