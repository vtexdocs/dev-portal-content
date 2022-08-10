---
title: "Product Summary Attachment List"
slug: "cea-cea-product-summary-productsummaryattachmentlist"
excerpt: "cea.cea-product-summary@0.23.0"
hidden: true
createdAt: "2022-07-14T17:15:53.802Z"
updatedAt: "2022-08-09T12:32:19.339Z"
---
## Description

`ProductSummaryAttachmentList` is a VTEX Component.
This Component can be imported and used by any VTEX App.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

## Table of Contents
- [Usage](#usage)
  - [Blocks API](#blocks-api)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/product-summary/blob/master/README.md#usage).

Then, add `product-summary-attachment-list` block into your app theme, as we do in our [Product Summary app](https://github.com/vtex-apps/product-summary/blob/master/store/blocks.json).

### Blocks API

This component has an interface that describes which rules must be implemented by a block when you want to use the `ProductSummaryAttachmentList`.

```json
  "product-summary-attachment-list": {
    "component": "ProductSummaryAttachmentList"
  }
```

### Configuration

Through the Storefront, you can change the `ProductSummaryAttachmentList`'s behavior and interface. However, you also can make in your theme app.

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `vtex.product-summary.css` inside the `styles/css` folder. Add your custom styles:

```css
.attachmentListContainer {
  margin-top: 10px;
}
```

#### CSS Handles

| CSS Handles  |
| ------------ |
| `attachmentListContainer`   |
| `attachmentItemContainer`   |
| `attachmentItem`            |
| `attachmentItemProductText` |