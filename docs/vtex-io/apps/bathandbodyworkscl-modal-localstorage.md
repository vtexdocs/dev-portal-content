---
title: "Modal localstorage"
slug: "bathandbodyworkscl-modal-localstorage"
excerpt: "bathandbodyworkscl.modal-localstorage@0.0.8"
hidden: true
createdAt: "2022-07-06T19:39:26.323Z"
updatedAt: "2022-07-12T16:19:14.854Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Modal that saves response in localstorage to never show it again

![Media Placeholder](./newsletter-coupon.PNG)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "modal-localstorage",
  .
  .
  .
}
```
2. Login to your vtex account:
```
> vtex login <development-environment>
```
3. Select your workspace and use `vtex link`:
```
> vtex use <workspace>
> vtex link
```

## Block ⚙
1. Adding the app as a theme dependency in the `manifest.json` file:
```
<your-vendor>.modal-localstorage: "0.x"
```
2. Declare the application in a block that corresponds to the lading where the modal should be displayed. For example:
```
{
  "header-layout.desktop": {
    "title": "Header desktop",
    "children": [
      "sticky-layout#desktop",
      "modal-localstorage#newsletter-coupon"
    ]
  },
  "modal-localstorage#newsletter-coupon": {
    "title": "Nesletter coupon",
    "children": [
        "flex-layout.row#newsletter-coupon"
    ],
    "props": {
        "image" : "URL"
    }
  },
}
```

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `image` | `string` | Image URL. | `undefined`   |

## Modus Operandi

The modal receives the content to display from a 'children', and displays two buttons (Accept, cancel). 

'Accept' creates a variable in local storage that determines whether or not the modal should be redisplayed. 

'Cancel' will redirect to a specific URL.

Important: The buttons can be edited from the site-editor.

## Customization

| CSS Handles |
| ----------- |
| `backdrop` |
| `container_modal` |
| `container_buttons` |
| `link_button` |
| `link_button_cancel` |
| `link_button_accept` |

| CSS Handles Form |
| ----------- |
| `container` |
| `textContainer` |
| `textContent` |
| `title` |
| `formContainer` |
| `form` |
| `inputContainer` |
| `inputForm` |
| `inputLabel` |
| `buttonContainer` |
| `btnEnviar` |
## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro** 
- **Gabriela Montes**