---
title: "List Modal"
slug: "vtex-list-listmodal"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.842Z"
updatedAt: "2022-12-01T16:44:24.325Z"
---
The `create-or-edit-list-modal` block displays a modal for editing or creating lists.

![ListModal](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-list-listmodal-0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `create-or-edit-list-modal` block to other theme block, such as the `responsive-layout.desktop`. For example:

```diff
  "responsive-layout.desktop": {
    "children": [
+     "create-or-edit-list-modal",
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