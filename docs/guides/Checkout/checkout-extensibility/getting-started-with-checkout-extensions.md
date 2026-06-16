---
title: "Getting started with Checkout extensions"
slug: "getting-started-with-checkout-extensions"
hidden: false
createdAt: "2026-06-10T00:00:00.000Z"
updatedAt: "2026-06-10T00:00:00.000Z"
excerpt: "Understand the structure of a Checkout extensions project and build your first extension."
---

> ⚠️ This feature is only available for stores using B2B Buyer Portal, which is currently available to selected accounts.

After you have a Checkout extensions project in your monorepo, you can create your first extension. When you create the project, a sample extension is already set up for you. To understand how it works, this guide walks through the files inside the project folder and then builds a new extension.

> ℹ️ Before starting, make sure you have [set up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout).

## Understanding the project

### Entrypoint

The `src/index.tsx` file, located at the root of your project, is the entry point for all extensions created for Checkout. Upon project creation, this file contains the following structure:

```tsx
// src/index.tsx
import { defineExtensions } from '@vtex/checkout';
import { HelloWorld } from './HelloWorld';

export default defineExtensions({
  'cart.cart-list.after': HelloWorld,
});
```

Consider the following key aspects of this file:

| Element                     | Description                                                                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `defineExtensions` function | Associates the extensions you create with their target extension points.                                                                                |
| Extension files             | Extensions may be defined in separate files and imported into `index.tsx`.                                                                              |
| `defineExtensions` function | Required for extensions to function correctly. It also provides type-checking and autocomplete, which help you identify the available extension points. |
| `@vtex/checkout` package    | Installed in your monorepo during the setup process, it provides the resources required to build extensions, including hooks, types, and functions.     |

> ℹ️ For the full list of available extension points, see [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).

### The extension

Upon project creation, a sample extension is provided in the `src/HelloWorld.tsx` file. This sample extension consists of two files: a TypeScript file for the implementation and a CSS file for styling. Implementation and style files may be organized as preferred, either as multiple files or combined into a single file.

> ℹ️ A stylesheet is not required for every extension. This structure is provided only as an example.

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

Consider the following key aspects of this example:

1. Extensions are React components and may use any React feature, such as the `useEffect` or `useState` hooks, as in any other React application.
2. Extensions may import CSS files, making the defined classes globally accessible.

## Creating your first extension

With an understanding of the essential parts of an extension and the project structure, you can create your first extension. This guide uses the example created in the [Setting up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout) step, with the sample folders and accounts. Replace the account and folder names, such as `store-a`, with your own to ensure the extension works as expected.

### 1. Running the Checkout extensions project

Before starting the implementation, set up the development environment by running the dev command from the FastStore CLI:

```yarn
yarn fsp dev store-a
```

```npx
npx fsp dev store-a
```

The store's URL is returned as output in your terminal, and Checkout becomes accessible at the `/checkout/cart` path.

### 2. Creating the component

Because extensions in FastStore are React components, one approach to creating an extension is to define its implementation in a TypeScript file. To create a custom footer for Checkout, add the following content to a new `src/CustomFooter.tsx` file:

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

Next, connect the extension to an extension point by modifying the `src/index.tsx` file:

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

After saving the file, open the browser with the storefront running. The extension is rendered at the bottom of the cart page.

### 3. Adding the logo

To add the Checkout logo to the footer component, use the [`useSettings` hook](https://developers.vtex.com/docs/guides/usesettings-hook) provided by the `@vtex/checkout` package in the `src/CustomFooter.tsx` file:

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

To style the `CustomFooter` component, create a `.css` file in the same folder as the component, `src/`:

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

Apply the CSS class to the `CustomFooter` component:

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

With the application open in the browser, the result is your first Checkout extension.

> ℹ️ For more ways to style your extensions, see [Using CSS in Checkout extensions](https://developers.vtex.com/docs/guides/css-styling-in-checkout-extensibility).
