---
title: "Container"
slug: "vtex-store-components-container"
excerpt: "vtex.store-components@3.132.1"
hidden: false
createdAt: "2020-06-03T16:04:30.345Z"
updatedAt: "2021-10-25T14:42:59.544Z"
---
![https://img.shields.io/badge/-Deprecated-red](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-store-components-container-0.png)

>⚠️ **Warning**
>
> **The Container block has been deprecated**. Despite this, support for it is still granted.

`Container` is a VTEX component that is used to wrap code, applying custom styles in the process. Is used throughout the apps in the store to apply similar behavior.
This component can be imported and used by any VTEX app.

## Usage

You should follow the usage instruction in the main [README](https://github.com/vtex-apps/store-components/blob/master/README.md#usage).

To import it into your code: 
```js
import { Container } from 'vtex.store-components'
```

You can use it in your code like a React component with the jsx tag: `<Container>`. 
```jsx
<Container className="my-section">
  My content
</Container>
```

### Configuration

| Prop name | Type | Description |
| --------- | ---- | ----------- |
| `className` | `String` | The tachyons classes to be applied in the container |
| `children` | `Node` | The content to be wrapped |

### Styles API
You should follow the Styles API instruction in the main [README](/README.md#styles-api).

#### CSS Namespaces

For now this component does not have any css namespaces.