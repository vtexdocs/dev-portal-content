---
title: "Slots"
slug: "vtex-io-documentation-slots"
excerpt: "Slots provide an alternative way for defining component structures within Store Framework themes."
hidden: false
createdAt: "2020-10-21T17:35:29.193Z"
updatedAt: "2022-12-13T20:17:44.635Z"
---

Slots composition is an alternative paradigm for defining component structures within the Store Framework themes. Unlike the conventional block composition method, slots enable developers to pass React props directly to components, providing enhanced flexibility in storefront design.

When using slots, consider the following:

- The requirement for the `blocks` attribute is eliminated when implementing components that utilize slots in the Store Theme. Instead, developers can pass the desired blocks as regular `props`.
- Slots grant the ability to include any block from any app as a regular prop. Hence, unlike the blocks composition method, declaring the `allowed` interface attribute is not necessary.

## Blocks vs. Slots

To better understand the distinctions between blocks and slots, let's delve into the specifics of each method using a hypothetical `hello-world` component.

### Blocks

When using the blocks composition, the focus revolves around defining `allowed` blocks and structuring their arrangement. In this approach, the `blocks` attribute specifies which blocks can be used within the `hello-world` component. Consider the following example:

<table>
<tr>
<th>`HelloWorld.tsx`</th>
<th>`interfaces.json`</th>
<th>`blocks.json`</th>
</tr>
<tr>
<td>

```tsx
// HelloWorld.tsx
import React from 'react'
import { ExtensionPoint } from 'vtex.render-runtime'  

const HelloWorld = () => (
  <div className="tc pv5">
    <ExtensionPoint id="icon-caret" size={32} />
    <h1 className="t-heading-1 c-on-base">Hello, world!<h1>
  </div>
)

export default HelloWorld
```

</td>
<td>
```json
// interfaces.json
{
  "hello-world": {
    "component": "HelloWorld",
    "allowed": ["icon-caret"]
  }
}
```
</td>

<td>
```json
// blocks.json
{
  "hello-world": {
    "blocks": ["icon-caret#point-up"]
  },
  "icon-caret#point-up": {
    "props": {
      "orientation": "up"
    }
  }
}
```
</td>
</tr>
</table>

Note that, in this example, the `icon-caret` block is the only child block allowed for `hello-world`. Other limitations of this method include:

- The `hello-world` block only accepts the `icon-caret` block as a child. Any other `icon-*` block or any block beyond that scope is incompatible, necessitating the explicit allowance of each distinct block in the `interfaces.json` file.
- Implementing the block-based approach within `HelloWorld.tsx` involves conditional logic to identify the block passed by the developer and subsequently convey its ID to the `ExtensionPoint` component.
- Passing multiple instances of the same block within the `HelloWorld` component may lead to rendering problems. For example, passing and rendering both `icon-caret#point-up` and `icon-caret#point-down` in the `blocks.json` file would lead to an ambiguous scenario. 

### Slots

Now, let's reimagine the same scenario using slots composition:

<table>
<tr>
<th>`HelloWorld.tsx`</th>
<th>`interfaces.json`</th>
<th>`blocks.json`</th>
</tr>
<tr>
<td>

```tsx
import React, { ReactElement } from 'react';
const HelloWorld = ({ Icon }) => (
  <div className="tc pv5">
    <Icon size={32} />
    <h1 className="t-heading-1 c-on-base">Hello, world!</h1>
  </div>
);

export default HelloWorld;
```

</td>
<td>
```json
// interfaces.json
{
  "hello-world": {
    "component": "HelloWorld"
  }
}
```
</td>


<td>
```json
//blocks.json
{
  "hello-world": {
    "props": {
      "Icon": "icon-caret#point-up"
    }
  },
  "icon-caret#point-up": {
    "props": {
      "orientation": "up"
    }
  }
}
```
</td>
</tr>
</table>

Note that, by directly passing required components as `props`, the slots approach eliminates the need for the `allowed` attribute. This method introduces flexibility into the component integration process, allowing any component to be included as a prop without prior restrictions.

This example demonstrates how slots composition simplifies the component declaration process and enhances flexibility. You can adjust the composition by passing different components as props, making the structure more adaptable to your needs.

To ensure consistent and effective usage of slots, it is important to adhere to the following guidelines:

- Slots are always exposed via `PascalCased` props.

<table>
<tr>
<th>✅ Do</th>
<th>❌ Don't</th>
</tr>
<tr>
<td>

```json
{
  "props": {
    // Works!
    "Icon": "icon-caret"
  }
}
```

</td>
<td>
  
```json
{
  "props": {
    // Does NOT work. This will be interpreted as a string by store builder
    "icon": "icon-caret"
  }
}
```
</td>

</tr>
</table>

- Nested slots are not supported. This means that you can't have a slot prop inside of an object, such as shown below:

```json
{
  "props": {
    "somePropThatsAnObject": {
      "p1": "this",
      "p2": "will",
      "p3": "not",
      "p4": "work",
      // This will NOT be picked up by the store builder
      "Slot": "some-block"
    }
  }
}
```
