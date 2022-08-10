---
title: "Container"
slug: "coolboxpe-custom-store-components-container"
excerpt: "coolboxpe.custom-store-components@0.2.360"
hidden: true
createdAt: "2022-07-05T09:42:34.311Z"
updatedAt: "2022-08-09T20:06:07.694Z"
---
## Description

`Container` is a VTEX component that is used to wrap code, applying custom styles in the process. Is used throughout the apps in the store to apply similar behavior.
This component can be imported and used by any VTEX app.

:loudspeaker: **Disclaimer:** Don't fork this project, use, contribute, or open issue with your feature request.

## Table of Contents
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS Namespaces](#css-namespaces)

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