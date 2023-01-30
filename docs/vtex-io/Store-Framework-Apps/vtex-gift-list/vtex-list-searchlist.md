---
title: "Search List"
slug: "vtex-list-searchlist"
hidden: false
createdAt: "2022-09-16T00:32:17.836Z"
updatedAt: "2022-12-01T16:44:24.216Z"
---
The `search-list` block displays a search box for public lists according to the name of the owner of the list or the name of the list.

![SearchList](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-searchlist-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

1. Add the `search-list` block to other theme block, such as the `flex-layout.col`. For example:

```diff
  "flex-layout.col": {
    "children": [
+     "search-list",
    ]
  }
```

### Props

| Prop Name   | Type    | Description                                                  | Default value                                                  |
| ----------- | ------- | ------------------------------------------------------------ | -------------------------------------------------------------- |
| title       | string  | Title for the search bar                                     | " Find a list "                                                |
| subtitle    | string  | Subtitle for the search bar                                  | " Find public lists by typing the name of the list or owners " |
| placeholder | string  | Placeholder inside the search bar                            | " Name of list or owners "                                     |
| button      | boolean | Add buttons to create list and my lists above the search bar | false                                                          |

## Customization

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles             |
| ----------------------- |
| `shareListContainer`    |
| `shareListIcon`         |
| `shareListNotification` |