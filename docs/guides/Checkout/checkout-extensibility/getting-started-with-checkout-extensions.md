---
title: "Getting started with Checkout extensions"
slug: "getting-started-with-checkout-extensions"
hidden: true
createdAt: "2026-06-10T00:00:00.000Z"
updatedAt: "2026-06-10T00:00:00.000Z"
excerpt: "Understand the structure of a Checkout extensions project and build your first extension."
---

> ⚠️ This feature is only available for stores using B2B Buyer Portal, which is currently available to selected accounts.

After you have a Checkout extensions project in your monorepo, you can create your first extension. When you create the project, a sample extension is already set up for you. To understand how it works, this guide walks through the files inside the project folder and then builds a new extension.

> ℹ️ Before starting, make sure you have [set up FastCheckout](https://developers.vtex.com/docs/guides/fastcheckout-setting-up).

## Understanding the project

### Entrypoint

The first file to look at is the `src/index.tsx` file located at the root of your project. This is the entry point for all the extensions you create for Checkout. When you create your project, it looks like this:

```tsx
// src/index.tsx
import { defineExtensions } from '@vtex/checkout';
import { HelloWorld } from './HelloWorld';

export default defineExtensions({
  'cart.cart-list.after': HelloWorld,
});
```

The key points to focus on are:

1. The `defineExtensions` function links the extensions you create to the target extension point.
2. You can create extensions in other files and import them into `index.tsx`.
3. Using `defineExtensions` helps you understand which extension points are available through type-checking and autocomplete, and it's also required for your extensions to work properly.
4. The `@vtex/checkout` package, installed in your monorepo during the setup process, provides everything you need to build your extension, including hooks, types, and functions.

> ℹ️ For the full list of available extension points, see [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).

### The extension itself

When you create the project, you'll find a sample extension in the `src/HelloWorld.tsx` file. This sample extension consists of two files: a TypeScript file for the implementation and a CSS file for styling. However, not every extension requires a stylesheet—this is just an example of what's possible. You can organize your style and implementation files however you prefer, creating multiple files or combining them into one.

```tsx
// src/HelloWorld.tsx
import { useState } from 'react';
import './hello-world.css';

export const HelloWorld = () => {
  const [count, setCount] = useState(0);

  return (
    <button className="hello-world-btn" onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
};
```

The main takeaways from this example are:

1. Extensions are React components, and they can use any React feature just like any other React application, such as hooks like `useEffect` or `useState`.
2. Extensions can import CSS files, allowing you to include the created classes and make them globally accessible.

## Creating your first extension

Now that you're familiar with the essential parts of an extension and how the project structure works, you can create your first extension. This guide uses the example created in the [Setting up FastCheckout](https://developers.vtex.com/docs/guides/fastcheckout-setting-up) step, with the sample folders and accounts. Remember to replace the account and folder names with your own, such as `store-a`, to ensure everything works as expected.

### 1. Running the Checkout extensions project

Before starting the implementation, set up the development environment by running the dev command from the FastStore CLI:

```yarn
yarn fsp dev store-a
```

```npx
npx fsp dev store-a
```

You should receive the store's URL as output in your terminal, and Checkout will be accessible at the `/checkout/cart` path.

### 2. Creating the component

Because extensions in FastStore are React components, one way to create your first extension is by creating a TypeScript file with the implementation. Create a custom footer for Checkout by adding the following content to a new `src/CustomFooter.tsx` file:

```tsx
// src/CustomFooter.tsx
export const CustomFooter = () => {
  return (
    <footer>
      <p>© 2024 Store A Inc. All Rights Reserved.</p>
    </footer>
  );
};
```

Now, connect this extension to an extension point by modifying your `src/index.tsx` file:

```tsx
// src/index.tsx
import { defineExtensions } from '@vtex/checkout';
import { HelloWorld } from './HelloWorld';
import { CustomFooter } from './CustomFooter';

export default defineExtensions({
  'cart.cart-list.after': HelloWorld,
  'layout.footer': CustomFooter,
});
```

After that, save the file and open your browser with the storefront running. You should see the extension rendered at the bottom of the cart page.

### 3. Adding the logo

Add the logo used in Checkout to your footer component. To do this, use the [`useSettings` hook](https://developers.vtex.com/docs/guides/usesettings-hook) provided by the `@vtex/checkout` package in your `src/CustomFooter.tsx` file:

```tsx
// src/CustomFooter.tsx
import { useSettings } from '@vtex/checkout';

export const CustomFooter = () => {
  const { branding } = useSettings();

  return (
    <footer>
      <img width={72} src={branding.logo} />
      <p>© 2024 Store A Inc. All Rights Reserved.</p>
    </footer>
  );
};
```

> ℹ️ The [`useSettings` hook](https://developers.vtex.com/docs/guides/usesettings-hook) provides other Checkout configurations as well.

### 4. Styling with CSS

To style your `CustomFooter`, create a `.css` file in the same folder where you placed your component, `src/`:

```css
/* src/footer.css */
.custom-footer {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #000;
  padding: 16px;
  color: #fafafa;
}
```

Apply your CSS class to the `CustomFooter`:

```tsx
// src/CustomFooter.tsx
import { useSettings } from '@vtex/checkout';
import './footer.css';

export const CustomFooter = () => {
  const { branding } = useSettings();

  return (
    <footer className="custom-footer">
      <img width={200} src={branding.logo} />
      <p>© 2024 Store A Inc. All Rights Reserved.</p>
    </footer>
  );
};
```

Switch to your browser with the application open, and you've created your first extension for Checkout.

> ℹ️ For more ways to style your extensions, see [Using CSS in Checkout extensions](https://developers.vtex.com/docs/guides/css-styling-in-checkout-extensibility).
