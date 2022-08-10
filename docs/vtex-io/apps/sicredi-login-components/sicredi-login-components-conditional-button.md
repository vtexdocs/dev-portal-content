---
title: "Title"
slug: "sicredi-login-components-conditional-button"
excerpt: "sicredi.login-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:41:04.573Z"
updatedAt: "2022-08-08T17:41:04.573Z"
---
Conditional button

## Description

The objective of this component is to verify whether the user is authenticated or not, if the user is not authenticated it will open one modal, if the user is already authenticated it will redirect the user for a url.

## Configuration

1. Add the `sicredi.login-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.login-components": "0.x"
}
```

2. now you can call your component inside the blocks, as this example.
Obs. the ```json "blocks": ["modal-login"] ``` is mandatory to this works, u need to setup the modal for this component call.

```json 
"conditional-button#meus-pedidos": {
    "title": "Meus pedidos",
    "children": ["icon#package"],
    "blocks": ["modal-login"],
    "props": {
      "blockClass":"",
      "href": "/account#/orders",
      "label": "Meus pedidos"
    }
  }
```

3. To use with React this component needs to be wrapped inside the `login-context` to work correctly, as it uses properties of that context

```jsx
<LoginModalProvider>
    <ConditionalButton href={''} label={''}>
        {children}
    </ConditionalButton>
 </LoginModalProvider>
```
## Props of the `ConditionalButton`

| Prop name               | Type             | Description                    | Default value |
| ------------------------| ---------------- | -----------------------------  | -----------   |
|`href`        | `string` | Url to redirect if the user is authenticated      | 'false'       |
|`label`       | `string` | Text to be showed with the button                 | ''            |
|`blockClass`  | `string` | Class modifier                                    | ''            |



## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                                |
| -----------------------------------------  |
|  `conditional-button__container`           |
|  `conditional-button__button`              |
|  `conditional-button__label`               |
|  `conditional-button__children-container`  |