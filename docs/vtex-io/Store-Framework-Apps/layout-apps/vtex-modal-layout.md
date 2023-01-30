---
title: "Modal Layout"
slug: "vtex-modal-layout"
hidden: false
createdAt: "2020-06-03T15:19:30.918Z"
updatedAt: "2022-04-11T08:02:58.274Z"
---

The Modal Layout app provides blocks that can help you create modals in your store.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-modal-layout-0.png)

## Configuration

1. Add the modal layout's app to your theme's dependencies in the `manifest.json`:

```diff
  "dependencies": {
+   "vtex.modal-layout": "0.x"
  }
```

Now, you are able to use all blocks exported by the `modal-layout` app. Check out the full list below:

| Block name | Description | 
| --------  | ------------ | 
| `modal-trigger` | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-modal-layout-1.png) Defines how the Modal content will be triggered through its children blocks. | 
| `modal-layout` | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-modal-layout-2.png) Defines how the Modal content will be rendered through its children blocks. You can declare as its children the blocks `modal-header` and `modal-content`, described below, in order to create a modal with header and footer. |
| `modal-header` | Renders a close button and the blocks listed as its children, building a modal header. Notice: it does not automatically render a header for your modal. Instead, you should create the modal header as you desire using this block's children list. | 
| `modal-content`| Defines how the Modal content will be rendered through its children blocks. Preferably, this block should be used along with the `modal-header` in order to create a modal with header and footer. | 
| `modal-actions` | Logical block only responsible for rendering its child blocks that, in turn, are responsible for rendering call-to-action buttons inside the modal, such as a confirmation button. | 
| `modal-actions.close`  | Button that closes the modal when clicked on. It is extremely useful in scenarios where your modal only has a form or a disclaimer box providing information for users. |

2. Add the `modal-trigger` block in any store template of your choosing. In the example below, it will be added to the Home page: 

```jsonc
{
  "store.home": {
    "children": [
      "modal-trigger#example"
    ]
  },
```

3. Declare the `modal-trigger` block using its prop and configuring children blocks for it. The `modal-trigger`'s first children must be a block of your choosing to trigger the Modal content. Then, a sibling block called `modal-layout` will be needed to effectively define the Modal content through its child block list. For example:

```jsonc
{
  "store.home": {
    "children": [
      "modal-trigger#example"
    ]
  },
   "modal-trigger#example": {
    "children": [
      "rich-text#example",
      "modal-layout#example"
    ]
  },
  "rich-text#example": {
    "props": {
      "text": "Click me"
    }
  },
  "modal-layout#example": {
    "children": [
      "rich-text#modal-content"
    ]
  },
  "rich-text#modal-content": {
    "props": {
      "text": "Hello"
    }
  }
}
```

*In the example above, the [Rich Text](https://vtex.io/docs/components/all/vtex.rich-text/) block renders the `Click me` text that will trigger the Modal content when clicked on. The modal content, in turn, is defined by the `modal-layout` block. According to the example above, the Modal content triggered by the `Click me` Rich Text would be a `Hello` text.*

### `modal-trigger` props

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `trigger` | `enum` | Whether the Modal content should be triggered by user click ( `click`), when the page is fully loaded (`load`) or when the page is fully loaded but the modal will appears just once per session (`load-session`). | `click` |
| `customPixelEventId` | `string`  | Store event ID responsible for triggering the `modal-trigger` block (hence triggering the opening of `modal-layout` blocks on the interface as well). | `undefined`    |
| `customPixelEventName` | `string`                                                                   | Store event name responsible for triggering the `modal-trigger` block (hence triggering the opening of `modal-layout` blocks on the interface as well). Some examples are: `'addToCart'` and `'removeFromCart'` events. Notice that using this prop will make the associated `modal-layout` open in **every** event with the specified name if no `customPixelEventId` is specified. | `undefined`    |

### `modal-layout` props

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `scroll` | `enum` | Defines how the modal should be scrolled by users. Possible values are: `body` (users can scroll the whole modal by normally scrolling the page) and `content` (users can scroll the modal *content* when hovering it). | `content` |
| `blockClass` | `string` | Unique block ID to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). | `undefined` | 
| `disableEscapeKeyDown` | `boolean` | Whether the modal should be closed when pressing the `Esc` key (`true`) or not (`false`). | `false` | 
| `fullScreen` | `boolean` | Whether the modal should fill the whole screen (`true`) or not (`false`). This prop is responsive i.e. it adapts itself to the device's breakpoints.  | `false` | 
| `backdrop` | `enum` | Whether the modal will have a clickable backdrop (`clickable`) or no backdrop at all (`none`). This prop is responsive i.e. it adapts itself to the device's breakpoints. | `clickable` | 
| `customPixelEventId` | `string`  | Store event ID responsible for triggering the `modal-layout` block (hence triggering the closing of `modal-layout` blocks on the interface as well). | `undefined`    |
| `customPixelEventName` | `string`                                                                   | Store event name responsible for triggering the `modal-layout` block (hence triggering the closing of `modal-layout` blocks on the interface as well). Some examples are: `'addToCart'` and `'removeFromCart'` events. Notice that using this prop will make the associated `modal-layout` close in **every** event with the specified name if no `customPixelEventId` is specified. | `undefined`    |
### `modal-header` props 

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `showCloseButton` | `boolean` | Whether the close icon button should be rendered in the modal header (`true`) or not (`false`). | `true` | 
| `iconCloseSize` | `number` | Size (in pixels) of the close icon button in the modal header.  | `32` |

### `modal-actions.close` props

| Prop name | Type | Description | Default value |
| --- | --- | --- | --- |
| `label` | `string` | Defines the text to be rendered in the close button. This prop default value depends on the store's default language which is set according to the website's [binding](https://help.vtex.com/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W?locale=en). | `Cancel`, `Cancelar`, or `Cancelar` for stores whose default language is, respectively, English, Spanish or Portuguese.  |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| --- |
| `modal` |
| `backdropContainer` |
| `backdrop` |
| `closeButtonContainer` |
| `closeButton` |
| `container` |
| `contentContainer` |
| `headerContainer` |
| `headerContent` |
| `paper` | 
| `topRow`| 
| `triggerContainer` |
