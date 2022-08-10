---
title: "Product Specification Display"
slug: "lecercleio-product-specification-display"
excerpt: "lecercleio.product-specification-display@0.1.0"
hidden: true
createdAt: "2022-07-28T13:26:24.815Z"
updatedAt: "2022-07-28T13:26:24.815Z"
---
## Description

This app allows the rendering of simple specification values outside of the specification table, free from any predefined styling or customization. It is capable of rendering either single fields or whole groups, depending you set.

## 🚨 Disclaimer - Template Application
>:warning: **This project is not maintained by VTEX, and this app is provided as a working example on how this feature can be implemented. Improvements and fixes will be on the implementation team side.**
>
>All template applications provided are developed by the VTEX community, you can use them freely.

## Table of Contents

- [Usage](#usage)
- [CSS Handles](#css-handles)


## Usage

Clone the app and make it yours, by editing `manifest.json`. Replace the vendor name with the name of your account. To use this app, you need to import in your dependencies on manifest.json.

```json
  "dependencies": {
    "vendor.product-specification-display": "0.x"
  }
```

Then, you can add a component block into your app theme on your product detail page. Via the "mode" prop you can choose to render a single field or a whole group of fields. By default, it renders a single field. 

```json
"product-specification-display":{
    "props":{
      "specification": "headline_1",
      "group": "marketing_texts",
      "displayFieldName": false
    }
  }
```


## Props:
| Prop | Purpose | expected values| Default |
| ---- | ---- | ---- |---- |
| specification | the specification field name to load the value from. | string | undefined |
| group | The specification group name to look for the specification | string | undefined |
| displayFieldName | Render name field or no | boolean | true |

No props are mandatory :heart:

## CSS handles
The following CSS handles can be used for styling:

```js
'containerEmpty',
'specificationTextContainer',
'specificationTextValue',
'specificationTextField'
```