---
title: "Creating Sales App extensions"
slug: "creating-sales-app-extensions"
hidden: false
excerpt: "Learn how to create a Sales App extension and render it in a predefined extension point."
createdAt: "2026-05-28T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

After setting up a Sales App extension project in your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview), you're ready to create custom experiences by rendering React components in predefined extension points.

> ℹ️ To create a Sales App extension, it's not mandatory to configure the `discovery` module. In this setup, FastStore provides the monorepo structure, tooling, and build process, while the `sales-app` module contains the extension code.

In this guide, you'll learn how to create a basic extension, connect it to an extension point, and style it with CSS.

## Before you begin

* Complete the [Setting up Sales App extensions](https://developers.vtex.com/docs/guides/setting-up-sales-app-extensions) guide.

## Instructions

Suppose you want to create a custom message for your Sales App. Based on the sample folder generated in your monorepo when creating the project, follow the steps below.

### Step 1 - Creating the component

To create a new component, add the following content to your TypeScript JSX file (for example, `src/components/CustomMessage.tsx`):

```tsx src/components/CustomMessage.tsx
export const CustomMessage = () => {
  return (
      <p>
        Extension example
      </p>
  )
}
```

This component renders a simple custom message in the VTEX Sales App interface.

### Step 2 - Registering the extension

Import the new component into `src/index.tsx`. Then, connect it to an extension point.

```tsx src/index.tsx
import { defineExtensions } from '@vtex/sales-app';
import { Example } from './components/Example';
import { CustomMessage } from './components/CustomMessage';

export default defineExtensions({
  'cart.cart-list.after': CustomMessage,
});
```

In this example, the component is rendered in the `cart.cart-list.after` extension point. Learn more about the available extension points in the [Exploring Sales App extensions](https://developers.vtex.com/docs/guides/exploring-sales-app-extensions) guide.

After saving the file, open the cart page again. The custom message should appear below the cart item list.

![VTEX cart page with empty cart and Extension example area displayed without custom styling](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-18419-creating-extension-point/images/creating-extensions-example-without-css.webp)

### Step 3 - (Optional) Styling the extension

To style your component, create a CSS file in the same folder as the component. For example:

```css
.custom-message {
  background: #000;
  color: #fafafa;
  padding: 16px;
}
```

Then update `CustomMessage.tsx` to import the stylesheet and apply the class.

```tsx src/components/CustomMessage.tsx
import { useSettings } from "@vtex/sales-app"
import './custom-message.css'

export const CustomMessage = () => {
  const { branding } = useSettings()
  return (
    <p className='custom-message'>
      Extension example
    </p>
  )
}
```

After saving the file, return to the browser to preview the styled extension.

![VTEX cart page with empty cart and Extension example area styled as a black bar at the bottom](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-18419-creating-extension-point/images/creating-extensions-example-with-css.webp)
