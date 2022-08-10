---
title: "Editable Top Bar"
slug: "heringhomolog-heringhomolog-components-editabletopbar"
excerpt: "heringhomolog.heringhomolog-components@0.45.63"
hidden: true
createdAt: "2022-08-05T19:16:19.556Z"
updatedAt: "2022-08-05T19:16:19.556Z"
---
## Description

- Top bar for customized notices integrated with browser cookie

![desktop](https://res.cloudinary.com/acct/image/upload/v1600199434/acct/topbar_bkeg1g.png)

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS Namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](/README.md#usage).

To import it into your code:

```JSON
{
    "editable-bar#default": {
    "title": "Top bar de informações",
    "props": {
      "active": true,
      "modalLabel": "Informações sobre as entregas devido a Covid.",
      "html": "<p>Conteudo</p>",
      "showLink": true
    }
  }
```

### Configuration

| Prop name    | Type       | Description                                    |
| ------------ | ---------- | ---------------------------------------------- |
| `isActive`   | `Boolean!` | Should show or not the benefits bar animation  |
| `modalLabel` | `String!`  | Label showing information from the warning bar |
| `html`       | `String!`  | HTML of modal content                          |

### Styles API

You should follow the Styles API instruction in the main [README](/README.md#styles-api).

### Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles           |
| --------------------- |
| topBarContainer       |
| topBarLabelContainer  |
| modalLabel            |
| modalOpenButton       |
| modalLabelContainer   |
| modalDateContainer    |
| modalBoldLabel        |
| modaltitleContainer   |
| modalContainer        |
| modalContainerOverlay |
| modalOverlay          |
| reOpenLabel           |
| iconCloseBar          |