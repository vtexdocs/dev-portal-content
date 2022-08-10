---
title: "Mini Cart Free Shipping Bar"
slug: "unileverytu-minicart-freeshipping-bar"
excerpt: "unileverytu.minicart-freeshipping-bar@1.2.2"
hidden: true
createdAt: "2022-07-19T06:18:44.045Z"
updatedAt: "2022-07-19T06:18:44.045Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The **Mini Cart Free Shipping Bar** is a MiniCart.v2 component that adds a progress bar to the minicart in order to display how much progress a customer has for to **win** free shipping. 

This block is **only a visual guide**, meaning it will not make any calculation or deduct the shipping amount from your store. You should pair this app with a **Free Shipping Promotion** of the same **amount**
The **amount** value, which by default is 200, can be edited inside your store's **Site Editor**. 
It consist of 4 different texts, which have messages developed for: English, Spanish, Italian and Portuguese. 

## Configuration
You should first install the app on the desired **Account**. To install run: `vtex install vtex.minicart-freeshipping-bar@0.x` inside the Toolbelt. 
Once installed, you should declare the app as a **Dependency** inside your store's **Store Theme**:
```
"dependencies": { 
    "vtex.minicart-freeshipping-bar": "0.x"
}
```

After this is completed, you should add the block **minicart-bar** inside your **Store-Theme's Header** under the **MiniCart** section:
```
{
  "minicart.v2": {
    "props": {
      "MinicartIcon": "icon-cart#minicart-icon"
    },
    "children": ["minicart-base-content"]
  },
  "icon-cart#minicart-icon": {
    "props": {
      "size": 24
    }
  },
  "minicart-base-content": {
    "blocks": ["minicart-empty-state"],
    "children": ["minicart-product-list", "flex-layout.row#minicart-footer"]
  },
  "flex-layout.row#minicart-footer": {
    "props": {
      "blockClass": "minicart-footer"
    },
    "children": ["flex-layout.col#minicart-footer"]
  },
  "flex-layout.col#minicart-footer": {
    "children": ["minicart-bar","minicart-summary", "minicart-checkout-button"]
  },
  "minicart-product-list": {
    "blocks": ["product-list#minicart"]
  },
  "product-list#minicart": {
    "blocks": ["product-list-content-mobile"]
  },
  "minicart-summary": {
    "blocks": ["checkout-summary.compact#minicart"]
  },

  "checkout-summary.compact#minicart": {
    "children": ["summary-totalizers#minicart"],
    "props": {
      "totalizersToShow": ["Items", "Discounts"]
    }
  },
  "summary-totalizers#minicart": {
    "props": {
      "showTotal": true,
      "showDeliveryTotal": false
    }
  },
  "minicart-empty-state": {
    "children": ["flex-layout.row#empty-state"]
  },
  "flex-layout.row#empty-state": {
    "children": ["flex-layout.col#empty-state"]
  },
  "flex-layout.col#empty-state": {
    "children": [
      "icon-cart#minicart-empty-state",
      "rich-text#minicart-default-empty-state"
    ],
    "props": {
      "horizontalAlign": "center",
      "verticalAlign": "middle",
      "rowGap": 5
    }
  },
  "icon-cart#minicart-empty-state": {
    "props": {
      "size": 64,
      "blockClass": "minicart-empty-state"
    }
  },
  "rich-text#minicart-default-empty-state": {
    "props": {
      "text": "Your cart is empty."
    }
  }
}
```
## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in blocks:

Thereafter, you should add a single column table with the available CSS handles for that block:

| CSS Handles |
| ----------- | 
| `freigthScaleContainer` | 
| `.sliderContainer` | 
| `.barContainer` | 
| `.sliderText` | 
| `.text1` |
| `.text2` |
| `.text3` |
| `.text4` |
| `.currencyText` |

## Contributors (

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!


**Upcoming documentation:**

 - [Fix bug reported regarding totalizers with tax](https://github.com/vtex-apps/minicart-freeshipping-bar/pull/3)