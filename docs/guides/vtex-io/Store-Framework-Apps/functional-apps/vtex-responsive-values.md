---
title: "Responsive Values"
slug: "vtex-responsive-values"
hidden: false
createdAt: "2020-06-03T15:19:17.689Z"
updatedAt: "2021-05-24T19:48:59.780Z"
---

Utility for using props that accept different values for different devices or media queries.

For example, a given prop could accept both just a number...

```json
props: {
  quantity: 1,
}
```

...or different values depending on the device or a media query:

```js
props: {
  quantity: {
    mobile: 1,
    desktop: 2,
    '(min-width: 1500px)': 4,
  }
}
```

...and the component, in turn, would use it like this:

```js
import { useResponsiveValue } from 'vtex.responsive-values'

const MyComponent = ({ quantity }) => {
  const quantity = useResponsiveValue(quantity)

  return <span>{quantity}</span>
}

<MyComponent quantity={1} /> {/* always returns 1 */}

<MyComponent quantity={{
  '(min-width: 1500px)': 4,
  desktop: 2,
  mobile: 1,
}} /> {/* returns 1 on mobile devices, 2 on desktop */}
```

Alternately, if you want to apply it to multiple values at once, or even the entire `props` object, you can use the hook `useResponsiveValues` (notice the plural) hook.

```tsx
import { useResponsiveValues } from 'vtex.responsive-values'

const MyComponent = props => {
  const { margin, padding } = useResponsiveValues(
    {
      margin: props.margin,
      padding: props.padding
    }
  )

  return (
    <section style={{ margin, padding }}>
      <span>{props.children}</span>
    </section>
  )
}

<MyComponent margin={4} padding={4} /> {/* always returns margin 4 / padding 4 */}

<MyComponent
  margin={{
    desktop: 4,
    mobile: 2,
  }}
  padding={{
    desktop: 4,
    mobile: 2,
  }}
/> {/* returns 1 on mobile devices, 2 on desktop */}
```

There are some things to keep in mind when using media queries:

- Media queries take precedence over devices. If one matches, any device-specific value is ignored.
- Media queries are written following the [standard media query syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries#Syntax).
- The definiton order matters. If more than one media query is matched, the first matched one is used.

## API

Props that use this hook accept either a value by itself, or an object with the following options: `phone` and `tablet` separately (or just `mobile` for both), `desktop` and generic media queries.

If there is any missing device, it will fallback to the next largest one. For example, if only the values of `phone` and `desktop` are passed, `tablet` devices will receive the value from `desktop`. Media queries have no fallback behavior.
