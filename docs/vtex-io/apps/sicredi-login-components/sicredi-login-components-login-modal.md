---
title: "Title"
slug: "sicredi-login-components-login-modal"
excerpt: "sicredi.login-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:41:04.566Z"
updatedAt: "2022-08-08T17:41:04.566Z"
---
Modal login

## Description

The objective of this component is to render a vtex native login inside a modal

## Configuration

1. Add the `sicredi.login-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.login-components": "0.x"
}
```

2. now you can call your component inside the blocks, as this example.
Obs. the ```json "blocks": ["login-content"] ``` is mandatory to this works, u need to setup the modal for this component call.

```json 
"modal-login": {
    "blocks":["login-content"]
}
```

3. To use with React this component needs to be used with and `Extension Point` , and be setup inside another component with Blocks.
```jsx
<ExtensionPoint id="modal-login" />
```

```json 
"conditional-button#meus-pedidos": {    
    "blocks": ["modal-login"],    
  }
```
## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                                |
| -----------------------------------------  |
|  `login-modal__container`                  |
|  `login-modal__content`                    |
|  `login-modal__overlay`                    |