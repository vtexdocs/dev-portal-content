---
title: "Add New Item"
slug: "vtex-list-addnewitem"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.826Z"
updatedAt: "2022-12-01T16:44:24.226Z"
---
The `add-new-item` block displays a button to direct the list owner to the search page for adding new items to their list.

![addNewItem](https://user-images.githubusercontent.com/67066494/190399924-dda34a9d-dc23-4e90-b3d8-e1a1105696f1.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `add-new-item` block to other theme block, such as the `responsive-layout.desktop`. For example:

```diff
  "responsive-layout.desktop": {
    "children": [
+     "add-new-item",
    ]
  }
```

### Props

| Prop Name       | Type   | Description                                                                          | Default value                                                                                                                      |
| --------------- | ------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| linkIcon        | string | Icon for the button                                                                  | https://vtex.vtexassets.com/assets/vtex/assets-builder/vtex.list-theme/0.11.0/ico_plus_blue___c42684ec58c4f1545ce21a4e355211c8.svg |
| linkRedirection | string | Path where the user will be redirected on click.(department / category / collection) | -                                                                                                                                  |
| nameButton      | string | Text at the button                                                                   | Add items                                                                                                                          |
| textAlignment   | string | Text alignment on the button (LEFT / CENTER / RIGHT)                                 | CENTER                                                                                                                             |
| textPosition    | string | Text position on the button (LEFT / CENTER / RIGHT)                                  | CENTER                                                                                                                             |
| classes         | string | Add new classes                                                                      | -                                                                                                                                  |