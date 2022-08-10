---
title: "Cashback calculator"
slug: "sicredi-cashback-calculator"
excerpt: "sicredi.cashback@0.2.0"
hidden: true
createdAt: "2022-07-11T17:57:37.406Z"
updatedAt: "2022-08-08T17:39:02.045Z"
---
Cashback calculator is a component to simulate the return in currency money, based on total points the user wants do exchange for cashback.

![Media Placeholder](https://gitlab.com/acct.global/program-04/sicredi/sicredi.cashback/uploads/e3df03db57947f8bddae202224d888a0/image.png)


## Modus operandi

to correctly use the `Cashback calculator` first you need to provide the parameters to calculate the amounts and set all business rules used in this module.
See [Parameters Example](../parameters/PARAMETERS.md).

## Configuration

1. Add the `Cashback calculator` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.cashback": "0.x"
}
```

or, add the component inside your custom page, for example: `<Calculator />`

2. You are now able to use the `Cashback calculator` block.

```json
{
  "cashback-calculator"
}
```

### `Cashback calculator` props

| Prop name | Type | Description | Default value |
| --------- | ---- | ----------- | ------------- |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                              |
| ---------------------------------------- |
| `calculator__container`                  |
| `calculator__wrapper`                    |
| `calculator__input-wrapper`              |
| `calculator__redemption-value-container` |
| `calculator__redemption-value`           |
| `calculator__redemption-value`           |
| `calculator__redemption-text`            |
| `calculator__redemption-container`       |
| `calculator__title-container`            |
| `calculator__step`                       |
| `calculator__step-text`                  |
| `calculator__slider`                     |
| `calculator__slider-container`           |
| `calculator__slider-ranges`              |
| `calculator__slider-values`              |
| `calculator__input`                      |
| `calculator__input-icon-container`       |
| `calculator__input-container`            |