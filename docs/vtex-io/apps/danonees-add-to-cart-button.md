---
title: "Danone Add To Cart Button"
slug: "danonees-add-to-cart-button"
excerpt: "danonees.add-to-cart-button@0.28.0"
hidden: true
createdAt: "2022-08-01T06:11:09.875Z"
updatedAt: "2022-08-01T06:11:09.875Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The `danonees.add-to-cart-button` is a custom app from `add-to-cart-button` to check if the `DeliveryPostalCode` cookie exists at the time of adding a product to the cart, if it does not exist, execute a popup of the app `danonees.danonees-postal-codes`.

## Dependencies
```json
"dependencies": {
    ...
    "vtex.add-to-cart-button": "0.x",
  },
```

## Configuration

1. Import the `danone.add-to-cart-button` app to your theme's dependencies in the manifest.json, for example:

```json
"dependencies": {
  "danonees.add-to-cart-button": "0.x"
}
```

## Installation``

You will then install and link this application from the command console:

```cmd
vtex install danonees.add-to-cart-button@x.x.x
```