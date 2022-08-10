---
title: "Shipping Estimate Translator"
slug: "vtex-shipping-estimate-translator"
excerpt: "vtex.shipping-estimate-translator@2.2.3"
hidden: true
createdAt: "2022-07-06T18:59:59.643Z"
updatedAt: "2022-07-06T18:59:59.643Z"
---
> A React component that renders shippingEstimate property from Checkout's OrderForm

## Setup

Through **vtex.io**:

Add the following dependency to your `manifest.json` dependencies:

```
"vtex.shipping-estimate-translator": "1.x"
```

## Usage

```js
import TranslateEstimate from 'vtex.shipping-estimate-translator/TranslateEstimate'

<TranslateEstimate shippingEstimate="0bd" />
// Same day

<TranslateEstimate shippingEstimate="1m" />
// In 1 minute

<TranslateEstimate shippingEstimate="0m" isPickup />
// Ready for pickup

<TranslateEstimate shippingEstimate="3m" lowerCase />
// in 3 minutes
```

### Params

- **shippingEstimate** | Type `string` | String to be translated
- **isPickup** | Type `boolean` | Condition to translate estimate for pickup point
- **lowerCase** | Type `boolean` | Condition to convert translated content to lowerCase

### Returns

- **Translated value** | Type `string`

## Testing

```sh
yarn test
```