---
title: "Gallery List Items"
slug: "vtex-list-gallerylistitems"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.838Z"
updatedAt: "2022-12-01T16:44:24.276Z"
---
The `gallery.list-items` block displays the gallery with the products contained in a list.

![GalleryListItems](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-gallerylistitems-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `gallery.list-items` block to other theme block inside the list context, such as the `store.list`. For example:

```diff
  "store.list":{
    "children":{
      "flex-layout.row"
    }
  },

  "flex-layout.row": {
    "children": [
+     "gallery.list-items",
    ]
  }
```

### Props

| Prop Name               | Type    | Description                                                                                                         | Default value                                 |
| ----------------------- | ------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| emptyListIcon           | string  | Name for the button                                                                                                 | -                                             |
| emptyListText           | string  | Text for empty lists                                                                                                | " Your list is empty \n Add items right now " |
| buttonEmptyList         | boolean | If set to true adds a button for adding items at an empty list                                                      | true                                          |
| nameButtonEmptyList     | string  | Name of the button in case the prop buttonEmptyList is true                                                         | "Add Items"                                   |
| emptyTextAlignment      | string  | Align the text of the button (RIGHT / CENTER / LEFT)                                                                | CENTER                                        |
| emptyTextPosition       | string  | Align the position of the text at button (RIGHT / CENTER / LEFT)                                                    | CENTER                                        |
| linkButtonEmptyList     | string  | The redirect link for the button (department / category / collection)                                               | -                                             |
| linkIconButtonEmptyList | string  | Link for the icon of an empty list                                                                                  | -                                             |
| limit                   | number  | At a guest context if wants to add a button to create a list and set a maximum limit of lists for creation per user | -                                             |