---
title: "LoginProfileBlock"
slug: "sicredi-login-components-loginprofileblock"
excerpt: "sicredi.login-components@0.1.0"
hidden: true
createdAt: "2022-08-08T17:41:04.699Z"
updatedAt: "2022-08-08T17:41:04.699Z"
---
## Description

This component is responsable to show points and name use when logged.

## Modus Operandi

1. User no logged
    - Show button and label to login
    - Whe clicked, Open the modal and ask use is Associated or not

2. User logged
    - Show username user logged and points where profile user can access.
    - When clicked, redirect user to my account

## Configuration

1. Add the `sicredi.login-components` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.login-components": "0.x"
}
```

2. The component can be called inside another component as `<LoginProfileBlock />` or using the the json `login-profile-block`

3. To open modal `BeAssociated`, the component needs the provider `LoginModalProvider` 
```jsx
<LoginModalProvider>
  <LoginProfileBlock />
</LoginModalProvider>
```

## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                          |
| ----------------------------         |
| `login-profile-block__container`     |
| `login-profile-block__name-content`  |
| `login-profile-block__profile-name`  |
| `login-profile-block__profile-icon`  |