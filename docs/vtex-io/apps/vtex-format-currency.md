---
title: "Format Currency"
slug: "vtex-format-currency"
excerpt: "vtex.format-currency@0.4.0"
hidden: true
createdAt: "2022-07-11T15:46:58.120Z"
updatedAt: "2022-07-11T15:46:58.120Z"
---
> Format currency based on sales policy config.

## Usage

Add `"vtex.format-currency": "0.x"` to your dependencies.

### API

#### `FormattedCurrency`

```jsx
import React from 'react'
import { FormattedCurrency } from 'vtex.format-currency'

function Foo() {
  return <FormattedCurrency value={10} />
}
// <span class="vtex-format-currency-0-x-currencyContainer">
//   <span class="vtex-format-currency-0-x-currencyCode">$</span>
//   <span class="vtex-format-currency-0-x-currencyInteger">10<span>
//   <span class="vtex-format-currency-0-x-currencyDecimal">.</span>
//   <span class="vtex-format-currency-0-x-currencyFraction">00</span>
// </span>

export default Foo
```

:info: Do not change the symbol or hide the decimals and fraction using CSS! You can configure the currency, currency symbol and currency decimal places in the Trade Policy settings.

![image](https://user-images.githubusercontent.com/284515/94180906-1c70ba80-fe75-11ea-9cf6-e84f059d924a.png)

:warning: Since IE11 does not support the browser API `formatToParts`, in this browser it will fallback to render:

```html
<span class="vtex-format-currency-0-x-currencyContainer">$ 10.00</span>
```

#### `formatCurrency`

```jsx
import React from 'react'
import { useIntl } from 'react-intl'
import { formatCurrency } from 'vtex.format-currency'
import { useRuntime } from 'vtex.render-runtime'

function Foo({ intl }) {
  const { culture } = useRuntime()
  const intl = useIntl()

  const value = formatCurrency({ intl, culture, value: 10 })

  return <span>{value}</span>
}
// <span>
//   $ 10.00
// </span>

export default Foo
```