---
title: "Responsive Layout"
slug: "vtex-responsive-layout"
excerpt: "vtex.responsive-layout@0.1.3"
hidden: false
createdAt: "2020-06-03T15:19:31.983Z"
updatedAt: "2020-06-23T20:25:09.531Z"
---
# VTEX Responsive Layout

Responsive-layout allows you to declare layout structures that will only be rendered in a specific screen-size breakpoint.

![responsive-layout-gif](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-responsive-layout-0.gif)

There are four blocks defined and exported by this app:

- `responsive-layout.desktop`
- `responsive-layout.mobile`
- `responsive-layout.tablet`
- `responsive-layout.phone`

Each of them have `composition: children`, which means that they expect to receive an array of `children` blocks to be rendered by them, if the current screen-size is right for their breakpoint.

## Configuration

1. Import the Responsive Layout app to your theme's dependencies on the `manifest.json`, for example:

```json
  "dependencies: {
    "vtex.responsive-layout": "0.x"
  }
```

2. Add the `responsive-layout` block into your theme. Here's an example:

```json
  "store.custom#about-us": {
    "blocks": [
      "responsive-layout.desktop",
      "responsive-layout.tablet",
      "responsive-layout.phone"
    ]
  },
  
  "responsive-layout.desktop": {
    "children": ["rich-text#desktop"]
  },
  "responsive-layout.tablet": {
    "children": ["rich-text#tablet"]
  },
  "responsive-layout.phone": {
    "children": ["rich-text#phone"]
  },

  "rich-text#desktop": {
    "props": {
      "text": "# This will only show up on desktop.",
      "blockClass": "title"
    }
  },
  "rich-text#tablet": {
    "props": {
      "text": "# This will only show up on tablet.",
      "blockClass": "title"
    }
  },
  "rich-text#phone": {
    "props": {
      "text": "# This will only show up on phone.",
      "blockClass": "title"
    }
  },
```

Notice that you could use _any_ array of blocks as `children`, given that they are allowed by the `block` that is directly above your `responsive-layout`.