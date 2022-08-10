---
title: "CUSTOM CATEGORY LINKS"
slug: "micocacola-custom-category-links"
excerpt: "micocacola.custom-category-links@0.0.9"
hidden: true
createdAt: "2022-07-26T16:50:29.704Z"
updatedAt: "2022-07-26T16:50:29.704Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Allows you to create a div that contains an action button with LINK to a URL or to trigger a modal event through pixels. It also adds a list of links that can be scrolled horizontally.

![Media Placeholder](./custom-category-links.JPG)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-category-links",
  "version": "0.0.0",
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
<your-vendor>.custom-category-links: "0.x"
```
2. Declare the main application block in a given theme template or within another theme block. For example:
```
{
    "flex-layout.row#retornables": {
        "children": [
            "custom-category-links#retornables"
        ]
    },
    "custom-category-links#retornables": {
        "props": {
            "actionButton": {
                "text": "Retornables",
                "url": ""
            },
            "linksButtons": [
                {
                    "text": "Starter, incluye envases",
                    "url": "/retornables/starter"
                },
                {
                    "text": "Refill, no incluye envases",
                    "url": "/retornables/refill"
                }
            ],
            "customPixelEventId": "modal-retornables",
            "visible": true
        }
    },
}
```

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `customPixelEventId` | `string`  |   Defines if the behavior of the actionButton will be a link or a modal using 'vtex.pixel-manager'      | `undefined`   |
| `actionButton`      | `Object { text: string; url: string }` |     Execute a redirect to a URL or trigger a modal if customPixelEventId comes with text from the props.    | `undefined`       |
| `linksButtons`      | `Array <{ text: string; url: string }>` |  An array of objects where each object contains the following properties: text, url. | `undefined`    |
| `visible` | `Boolean` | Determines if the component should be shown or hidden | `true` |

## Modus Operandi
The application will receive the customPixelEventId which will determine if the actionButton is a link or the trigger of an event for a modal.

We also have the actionButton that receives an object that contains text for the button and a URL.

As for linkButtons, it is an array of objects that, when mapped, displays a list of links horizontally. If this list exceeds the width of the <div> container, horizontal scrolling will be activated.

The app can be edited from the site editor.

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `actionContainer` |
| `actionLink` |
| `linksContainer` |
| `linkItem` |

## Styles.css
Create a new file named `<your-vendor> .custom-category-links.css` in the css folder and add the following styles.
```
.container{
  margin: 20px 0;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: auto;
  max-height: max-content;
  border-radius: 18px;
  background-color: #ebebeb;
}

.actionContainer{
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  min-height: 50px;
  height: 100%;
  width: 40%;
  min-width: 24%;
  max-width: 400px;
  border-radius: inherit;
  background-color: #e41d1e;
}

.actionLink {
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  border-radius: 18px;
  text-decoration: none;
  color: white;
  font-weight: 900;
  font-size: 22px;
  min-height: 100%;
  width: 90%;
  padding: 10px;
}

.linksContainer{
  display: flex;
  justify-content: flex-start;
  align-items: center;
  z-index: 1;
  height: 100%;
  overflow-x: scroll;
  margin-left: -20px;
  padding-left: 40px;
  width: calc(100% - 40px);
}

.linksContainer::-webkit-scrollbar {
  display: none;
}

.linkItem {
  transition: 100ms ease-in-out;
  text-decoration: none;
  white-space: nowrap;
  color: #5a5a5a;
  font-size: 17px;
  margin: 0 10px;
  font-weight: bold;
}

.linkItem:hover{
  color: #e41d1e;

}

/* tablets config */
@media (min-width: 651px) and (max-width: 1025px){
  .actionContainer{
    text-align: center;
  }

  .actionLink{
    font-size: 18px;
  }
}

/* mobile config*/
@media only screen and (max-width: 650px){
  .container {
    margin: 10px 0;
    border-radius: 8px;
  }

  .actionContainer{
    text-align: center;
    min-height: 37px;
    border-radius: 8px;
    max-width: 60%;
    min-width: 42%;
  }

  .actionLink {
    padding: 0px 5px;
    font-size: 14px;
    border-radius: 8px;
  }

  .linksContainer{
    height: 100%;
    border-radius: 8px;
    background-color: transparent;
  } 

  .linkItem {
    font-size: 12px;
    font-family: gothamlightregular;
  }
}

```

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**