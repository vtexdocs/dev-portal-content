---
title: "CUSTOM NEWSLETTER"
slug: "bathandbodyworkscl-newsletter"
excerpt: "bathandbodyworkscl.newsletter@0.0.11"
hidden: true
createdAt: "2022-07-12T15:54:07.694Z"
updatedAt: "2022-07-12T15:54:07.694Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Personalized newsletter that sends customer data to Master Data using Axios. 

![Media Placeholder](./newsletter.PNG)

## Installation 
### Step 1 - Adding the CustomDeliveryTable app to your theme's dependencies
In your theme's manifest.json, add the CustomDeliveryTable app as a dependency:
```
  "dependencies": {
        "cocacola.newsletter": "0.x"
    }
```

### Step 2 - Adding the newsletter to page templates 
First, declare your main call as children.. For example:
```
{
  "flex-layout.row#newsletter": {
        "children": [
            "custom-newsletter"
        ],
        "props": {
            "preventHorizontalStretch": true,
            "horizontalAlign": "center",
            "blockClass": "custom-newsletter"
        }
    }
}
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles |
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

- Gabriela Montes 
- Fabian Toro