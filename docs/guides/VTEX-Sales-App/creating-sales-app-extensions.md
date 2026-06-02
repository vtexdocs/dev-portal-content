---
title: "Creating Sales App extensions"
slug: "creating-sales-app-extensions"
hidden: false
excerpt: "Learn how to create a Sales App extension and render it in a predefined extension point."
createdAt: "2026-05-28T00:00:00.000Z"
updatedAt: "2026-06-02T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

After setting up a Sales App extension project in your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview), you're ready to create custom experiences by rendering React components in predefined extension points.

> ℹ️ To create a Sales App extension, it's not mandatory to configure the `discovery` module. In this setup, FastStore provides the monorepo structure, tooling, and build process, while the `sales-app` module contains the extension code.

In this guide, you'll learn how to create a basic extension and connect it to an extension point.

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

![VTEX cart page with empty cart and Extension example area displayed without custom styling](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/creating-extensions-example-without-css.webp)

Once you have created an extension and connected it to an extension point, you can customize your component's styling. For detailed instructions, see the guide [CSS styling in VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/css-styling-in-vtex-sales-app-extensibility).
