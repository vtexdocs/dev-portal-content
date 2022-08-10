---
title: "Modal localstorage"
slug: "vinasantaemacl-modal-localstorage"
excerpt: "vinasantaemacl.modal-localstorage@0.0.2"
hidden: true
createdAt: "2022-07-20T15:54:38.359Z"
updatedAt: "2022-07-22T17:09:47.166Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Modal that saves response in localstorage to never show it again

![Media Placeholder](./modal-localStorage.JPG)

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
      "modal-localstorage#mayor-de-edad"
    ]
  },
  "modal-localstorage#mayor-de-edad": {
    "title": "Modal Mayor de edad",
    "children": [
        "flex-layout.row#mayor-de-edad"
    ],
    "props": {
        "whiteListUrl": [
            "/Terminos-Condiciones"
        ],
        "cancel": {
            "label": "NO",
            "redirect": "/Terminos-Condiciones"
        },
        "accept": {
            "label": "SI"
        }
    }
  },
}
```

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `whiteListUrl` | `Array of strings` |  White list of URLs where the modal will not be displayed.   | `undefined`   |
| `accept` | `object` | Properties for button 'accept'. | `undefined`   |
| `cancel` | `object` | Properties for button 'cancel'. | `undefined`   |

### `accept` and `cancel` object
| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `label` | `String` |  Represents the button text  | `undefined`  |
| `redirect` | `String` |  Represents the URL to redirect| `undefined`  |

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

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**