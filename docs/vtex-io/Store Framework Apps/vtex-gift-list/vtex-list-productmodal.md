---
title: "Product Modal"
slug: "vtex-list-productmodal"
excerpt: "vtex.list@3.6.2"
hidden: false
createdAt: "2022-09-16T00:32:17.915Z"
updatedAt: "2022-12-01T16:44:24.347Z"
---
The `modal-select-product` block displays a modal with detailed information (such as size and color) about the product the costumer wants to add to the lists they own.

![chrome-capture-2022-8-15 (2)](https://user-images.githubusercontent.com/76453090/190513307-0d92633f-e0ad-4a92-a794-5defb1beb7c0.gif)

## Configuration

1. Import the `vtex.list` app to your theme's peer dependencies in the `manifest.json` file as in the following example:

```json
  "peerDependencies": {
    "vtex.list": "3.x"
  }
```

2. Add the `modal-select-product` block to other theme block, such as the `responsive-layout.desktop`. For example:

```diff
  "responsive-layout.desktop": {
    "children": [
+     "modal-select-product",
    ]
  }
```

## Customization

| Prop Name  | Type   | Description                                         | Default Value |
| ---------- | ------ | --------------------------------------------------- | ------------- |
| nameButton | string | Changes the name of the button that opens the modal | "Button name" |