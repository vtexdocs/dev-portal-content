---
title: "Totalizer Translator"
slug: "vtex-totalizer-translator"
excerpt: "vtex.totalizer-translator@2.4.0"
hidden: true
createdAt: "2022-07-12T18:45:29.345Z"
updatedAt: "2022-07-12T18:45:29.345Z"
---
> A React component that renders translated totalizer property from Checkout's OrderForm

## Setup

Through **vtex.io**:

Add the following dependency to your `manifest.json` dependencies:

```
"vtex.totalizer-translator": "1.x"
```

## Usage

```js
import TranslateTotalizer from 'vtex.totalizer-translator/TranslateTotalizer'

<TranslateTotalizer id="Discounts" />
// Discount

<TranslateTotalizer id="Items" />
// Subtotal

<TranslateTotalizer id="Foo Custom" />
// Foo Custom
```

### Params

- **id** | Type `string` | Id of the totalizer to be translated

### Returns

- **Translated value** | Type `string`

## Testing

```sh
yarn test
```