---
title: "Title"
slug: "sicredi-login-components-beassociatedmodal"
excerpt: "sicredi.login-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:41:04.619Z"
updatedAt: "2022-08-08T17:41:04.619Z"
---
BeAssociatedModal

## Description

The objective of this component is to verify whether the user is already a Sicredi customer or not. It refers to a modal with two click options: Sicredi Customer or Sicredi Non-Customer.
To use this component you need to be inside another component inside this same repository

## Configuration

1. Add the `sicredi.login-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.login-components": "0.x"
}
```

2. The component can be called inside another component as `<BeAssociatedModal/>`


3. This component needs to be wrapped inside the `cashback-context` to work correctly, as it uses properties of that context

```jsx
<LoginModalProvider>
  <BeAssociatedModal />
</LoginModalProvider>
```
## Props of the `LoginModalProvider`

| Prop name                 | Type      | escription          | Default value |
| -----------------------   | --------- | ------------------- | -----------   |
|`isOenBeAssociatedModal`   | `boolean` | open modal          | false         |
|`setIsOpenBeAssociatedModal` | `function`| open and close modal| ''            |



## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                                |
| -----------------------------------------  |
|  `beassociated-modal`                      |
|  `beassociated-modal__container`           |
|  `beassociated-modal__overlay`             |
|  `beassociated-modal__button-associated`   |
|  `beassociated-modal__button-noassociated` |
|  `beassociated-modal__close-icon`          |