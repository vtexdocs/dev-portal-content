---
title: "Title"
slug: "sicredi-cashback-availablepoints"
excerpt: "sicredi.cashback@0.2.0"
hidden: true
createdAt: "2022-07-11T17:57:37.441Z"
updatedAt: "2022-08-08T17:39:02.065Z"
---
AvailablePoints

## Description

This component will show the logged in user cashback points available for withdrawal.

## Configuration

1. Add the `sicredi.cashback` app to your theme's dependencies in the `manifest.json`, for example:

```diff
"dependencies": {
+  "sicredi.cashback": "0.x"
}
```

2. The component can be called inside another component as `<AvailablePoints {...props}/>`

3. This component needs to be wrapped inside the `cashback-context` to work correctly, as it uses properties of that context

```jsx
<CashbackProvider>
  <AvailablePoints />
</CashbackProvider>
```
## Props of the `CashbackProvider`

| Prop name         | Type      | Description                              | Default value |
| ----------------- | --------- | ---------------------------------------- | ------------- |
| `balance`         | `number`  | user balance available                   |      0        |
| `maxPointWithdraw`| `number`  | Min points to withdraw                   |     7000      |
| `minPointWithdraw`| `number`  | Min points withdraw per Month            |     300000    |



## `AvailablePoints` props

| Prop name         | Type      | Description                              | Default value    |
| ----------------- | --------- | ---------------------------------------- | ---------------- |
| `subtitle`        | `string`  | Title cashback points                    | `Como funciona?` |
| `description`     | `string`  |  Info text about user points             | ``           |


## Customization

Below are the classes available for customization. For more information access: [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                                |
| -----------------------------------------  |
|  `availablepoints__container`              |
|  `availablepoints__points`                 |
|  `availablepoints__label`                  |
|  `availablepoints__value`                  |
|  `availablepoints__subtitle`               |
|  `availablepoints__minmax`                 |
|  `availablepoints__minmax-label`           |
|  `availablepoints__less-balance`           |
|  `availablepoints__less-balance-icon`      |
|  `availablepoints__less-balance-label`     |