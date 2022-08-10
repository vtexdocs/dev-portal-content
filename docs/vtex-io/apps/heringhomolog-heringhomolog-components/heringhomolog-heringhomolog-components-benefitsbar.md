---
title: "Benefits Bar"
slug: "heringhomolog-heringhomolog-components-benefitsbar"
excerpt: "heringhomolog.heringhomolog-components@0.45.63"
hidden: true
createdAt: "2022-08-05T19:16:19.530Z"
updatedAt: "2022-08-05T19:16:19.530Z"
---
## Description

- The customized benefit bar has two different behaviors for desktop and mobile

### Desktop

- Items are available laterally on the screen

![desktop](https://res.cloudinary.com/acct/image/upload/v1600183243/acct/bar-desktop_tfsu5s.png)

### Mobile

- The items become a carousel with 3 items per page

![mobile](https://res.cloudinary.com/acct/image/upload/v1600183404/acct/Captura_de_tela_de_2020-09-15_12-22-59_tcga9v.png)

### Table of Contents

- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS Namespaces](#css-namespaces)

## Usage

You should follow the usage instruction in the main [README](/README.md#usage).

To import it into your code:

```JSON
{
    "benefits-bar#default": {
        "props": {
            "isActive": true,
            "benefits": [
                {
                    "icon": "assets/free-shipping.svg",
                    "title": "Frete grátis"
                },
                {
                    "icon": "assets/credit-card.svg",
                    "title": "Todo site <br /> com 5x sem juros"
                },
                {
                    "icon": "assets/arrow-cross.svg",
                    "title": "Devolução <br /> estendida"
                },
                {
                    "icon": "assets/bag-benefits.svg",
                    "title": "Checkout único"
                }
            ]
        }
    }
```

### Configuration

| Prop name  | Type          | Description                                   |
| ---------- | ------------- | --------------------------------------------- |
| `isActive` | `Boolean!`    | Should show or not the benefits bar animation |
| `benefits` | `benefits[]!` | List of benefits                              |

- Possible values of `benefits`:

| Prop name | Type       | Description                                           |
| --------- | ---------- | ----------------------------------------------------- |
| `icon`    | `String!`  | Svg icon that will be shown above the label animation |
| `label`   | `sString!` | benefit title or description                          |

### Styles API

You should follow the Styles API instruction in the main [README](/README.md#styles-api).

### Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles         |
| ------------------- |
| `containerBenefits` |
| `benefitItem`       |
| `benefitItemImage`  |
| `iconRight`         |
| `iconLeft`          |
| `benefitItemTitle`  |
| `containerBenefits` |