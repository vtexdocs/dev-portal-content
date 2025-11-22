---
title: "Improving store accessibility with semantic HTML migration"
slug: "vtex-io-documentation-semantic-html-migration"
excerpt: "Learn how to implement semantic HTML updates across your Store Framework components to improve accessibility."
createdAt: ""
---

In this guide, you'll learn how to enable the `a11ySemanticHtmlMigration` flag, which allows you to implement semantic HTML updates across Store Framework components progressively. This feature allows your store to adhere to accessibility best practices, benefiting shoppers who use assistive technologies while maintaining your existing customizations.

## Before you begin

### Set up a workspace for testing

Create a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) where you can enable and implement the flag without impacting the production environment.

## Instructions

### Step 1: Enabling the flag in VTEX Admin

1. In the VTEX Admin, go to **Apps > My Apps**.
2. Search for the **VTEX Store** app and click on it.
3. Check the **Enable accessibility semantic HTML migration** checkbox. By default, this option is disabled.

  ![semantic-html](https://vtexhelp.vtexassets.com/assets/docs/src/semantic-html___3f810f66cd47bd76760fe3f56783a779.gif)

When this flag is enabled, the following native components automatically render using proper semantic HTML elements, such as <label>, <main>, and <nav>:

- [`product-quantity`](https://developers.vtex.com/docs/apps/vtex.product-quantity)
- [`product-summary`](https://developers.vtex.com/docs/apps/vtex.product-summary)

To implement semantic HTML in other components, follow the next steps.

>⚠️ If the CSS in the components is configured improperly, such as tying styles to the tag path (for example, `div > span > p`) instead of using fixed selectors like `id` or `class`, changing tags may break the layout. That's why the flag comes disabled by default, requiring you to enable it and ensure compatibility with semantic HTML.

### Step 2: Implementing semantic HTML in your components

In your component, read the flag value using `useRuntime → getSettings('vtex.store')` and check `advancedSettings.a11ySemanticHtmlMigration`. See below a use case example of implementation in the `ProductQuantity` component:

```tsx BaseProductQuantity.tsx
import React from 'react'
import { useRuntime } from 'vtex.render-runtime'

function ProductQuantity() {
  const { getSettings } = useRuntime()
  const settings = getSettings('vtex.store')
  const useSemanticHtml = settings?.advancedSettings?.a11ySemanticHtmlMigration

  return (
    <>
      {useSemanticHtml ? (
        <label htmlFor="quantity-input">Quantity:</label>
      ) : (
        <div>Quantity:</div>
      )}
      <input id={useSemanticHtml ? 'quantity-input' : 'qty-123'} type="number" />
    </>
  )
}
```

In this example, when the flag is enabled, the component renders a semantic `<label>` with `htmlFor="quantity-input"`, establishing a programmatic relation required by accessibility guidelines. When off, it falls back to a `<div>Quantity:</div>` and uses a non-specific input id (`qty-123`).

### Step 3: Validating the semantic HTML output

After enabling the flag and updating your components, validate the updated markup.

#### Inspect rendered components

- Use browser DevTools to inspect components known to have semantic updates (for example, quantity selectors, form inputs, buttons).
- Confirm if semantic elements (such as `label`, `main`, and `nav`) are now present.

#### Test accessibility workflows

- Navigate using only the keyboard to ensure focus order and visibility remain correct.
- Use a screen reader to validate that new semantic elements improve announcements.

#### Monitor console warnings

Check the browser console for JavaScript errors that may relate to DOM queries or event listeners targeting outdated selectors.

### Step 4: Making your changes publicly available

After testing the settings in your development workspace, make your changes publicly available for all users by following the guide [Making your theme content public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public).
