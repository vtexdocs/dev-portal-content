---
title: "User Lists"
slug: "vtex-list-userlists"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.844Z"
updatedAt: "2022-12-01T16:44:24.291Z"
---
The `user-lists` block displays the lists the user has with their names and privacy information. It has as title and a subtitle and a link button to generate new lists.

<img width="1392" alt="image" src="https://user-images.githubusercontent.com/76453090/190492242-fdddc8d1-ca4e-405c-a46d-b9315a9f392f.png">

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `user-lists` block to other theme block inside the list context, such as the `store.list`. For example:

```diff
  "store.list":{
    "children":{
      "flex-layout.row"
    }
  },
  "flex-layout.row": {
    "children": [
+     "user-lists",
    ]
  }
```

### Props

| Prop Name            | Type    | Description                                            | Default Value            |
| -------------------- | ------- | ------------------------------------------------------ | ------------------------ |
| title                | string  | defines the title of the section                       | "My lists"               |
| subTitleWithLists    | string  | Subtitle that will appear when there are lists         | "Subtitle with lists"    |
| subtitleWithoutLists | string  | Subtitle that will appear when there are no lists      | "Subtitle without lists" |
| useButton            | boolean | Optional button to create new lists                    | true                     |
| nameButton           | string  | Button name to create new lists if used                | "Button name"            |
| limit                | number  | Limit of lists a user can create, if useButton is true | -                        |

## Customization - "user-lists"

To apply CSS customizations in this and other blocks, follow the [Using CSS handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization) guide.

| CSS Handles         |
| ------------------- |
| `userListContainer` |
| `userListText`      |
| `listActive`        |