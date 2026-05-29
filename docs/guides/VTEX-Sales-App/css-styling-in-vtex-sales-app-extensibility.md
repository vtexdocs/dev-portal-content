---
title: "CSS styling in VTEX Sales App Extensibility"
slug: "css-styling-in-vtex-sales-app-extensibility"
hidden: false
excerpt: "Learn how to style extensions using CSS in VTEX Sales App Extensibility."
createdAt: "2026-05-25T00:00:00.000Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

Once you have [created a Sales App extension](https://developers.vtex.com/docs/guides/creating-sales-app-extensions), you can style your component by importing plain `.css` files to apply classes globally (for example, `className='btn'`). This configuration is optional.

## Scope and limitations

CSS files have access to the global scope where they're loaded, meaning they can technically target and style other elements of the Sales App core. We recommend using CSS exclusively to style your extensions.

> ❗ Any styling applied to core elements is subject to breaking changes due to bug fixes, new features, and other updates.

Avoid using global CSS to target elements outside your extension, such as with `tag`, `class`, or `id` selectors, for the following reasons:

- Future releases may include sandboxing mechanisms that isolate CSS and/or extensions from the core application's global scope (for example, DOM).
- Using selectors like classes or IDs on core Sales App elements (for example, the "Continue" button, the cart list, header, logo) is not supported, as Sales App generates unique IDs for classes applied to its elements.
- Relying on the markup to create selectors with the goal of customizing the core Sales App is risky, as the markup may change with core updates (for example, adding or removing elements in the DOM).

> ℹ️ Visual changes, such as the primary brand color, are currently done through configuration.

## Styling extensions with plain CSS

You'll include `.css` files in the relevant `.tsx` file. You can either create a single file and import it once in `src/index.tsx`, or create component-specific files and import them in the component's file.

Example with a single CSS file:

```tsx
  // src/index.tsx
  import { defineExtensions } from '@vtex/sales-app'
  import './styles.css'
```

Examples with multiple CSS files:

```tsx
  // CustomMessage.tsx
  import './custom-message.css'
  const CustomMessage = () => {...}
```

```tsx
  // CustomTotalizer.tsx
  import './custom-totalizer.css'
  const CustomTotalizer = () => {...}
```

> ⚠️ Sales App generates classes with unique IDs, so there's no conflict with the core, but globally scoped CSS class names might conflict with other extensions you're styling.
