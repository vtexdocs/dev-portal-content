---
title: "Creating a VTEX Sales App extension"
slug: "creating-a-vtex-sales-app-extension"
hidden: false
excerpt: "Learn how to create a VTEX Sales App extension in your FastStore project and render it in a predefined extension point."
createdAt: "2026-05-22T16:10:21.214Z"
---

After setting up a VTEX Sales App extensions project in your FastStore monorepo, you're ready to create custom experiences by rendering React components in predefined extension points.

In this guide, you'll learn how to review the generated project structure, create a basic extension, connect it to an extension point, and style it with CSS.

## Before you begin

Complete the [Setting up extensions for VTEX Sales App in FastStore web stores](https://developers.vtex.com/docs/guides/setting-up-extensions-for-vtex-sales-app-in-faststore-web-stores) guide.

## Instructions

Consider you want to create a custom counter for your VTEX Sales App. Based on the sample folder generated in your monorepo when creating the project, follow the steps below.

### Step 1 - Creating the component

To create a new component, add the following content to your TypeScript file (for example, `src/components/CustomMessage.tsx`):

```tsx
export const CustomMessage = () => {
  return (
      <p>
        Extension example
      </p>
  )
}
```

This component renders a simple custom message in the VTEX Sales App interface.

### Step 2 - Register the extension

Import the new component into `src/index.tsx`. Then, connect it to an extension point.

```tsx
import { defineExtensions } from '@vtex/sales-app';
import { Example } from './components/Example';
import { CustomMessage } from './components/CustomMessage';

export default defineExtensions({
  'cart.cart-list.after': CustomMessage,
});
```

In this example, the component is rendered in the `cart.cart-list.after` extension point. Learn more about the available extension points in the [VTEX Sales App extension points](#LINK) guide.

After saving the file, open the cart page again. The custom message should appear below the cart item list.

![VTEX cart page with empty cart and Extension example area displayed without custom styling](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-18419-creating-extension-point/images/creating-extensions-example-without-css.webp)

### Step 3 - (Optional) Style the extension

To style your component, create a CSS file in the same folder as the component. For example:

```css
.custom-message {
  background: #000;
  color: #fafafa;
  padding: 16px;
}
```

Then update `CustomMessage.tsx` to import the stylesheet and apply the class.

```tsx
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

## Next steps
