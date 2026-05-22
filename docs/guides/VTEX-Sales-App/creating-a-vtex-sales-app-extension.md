---
title: "Creating a VTEX Sales App extension"
slug: "creating-a-vtex-sales-app-extension"
hidden: false
excerpt: "Learn how to create a VTEX Sales App extension in your FastStore project and render it in a predefined extension point."
createdAt: "2026-05-22T16:10:21.214Z"
---

After setting up a VTEX Sales App extensions project in your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview), you're ready to create custom experiences by rendering React components in predefined extension points.

To create a VTEX Sales App extension, you don't need to configure the `discovery` module. In this setup, FastStore provides the monorepo structure, tooling, and build process, while the `sales-app` module contains the extension code.

As a result, you can deploy a Sales App extension with WebOps without using FastStore Discovery in production. The production storefront can use another technology, as long as the account is configured to use the Sales App module.

In this guide, you'll learn how to create a basic extension, connect it to an extension point, style it with CSS, and understand how the deployment flow works.

## Before you begin

* Complete the [Setting up extensions for VTEX Sales App](https://developers.vtex.com/docs/guides/setting-up-extensions-for-vtex-sales-app) guide.
* Make sure you have installed the FastStore WebOps. For detailed instructions, see the guide [Installing FastStore WebOps](https://developers.vtex.com/docs/guides/installing-faststore-webops).

## Instructions

Suppose you want to create a custom message for your VTEX Sales App. Based on the sample folder generated in your monorepo when creating the project, follow the steps.

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

### Step 2 - Registering the extension

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

### Step 4 - Deploying your changes

A deployment starts whenever you push a commit to the `main` branch. When pushing to `main`, [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/webops-dashboard) starts the production deployment flow. In about 10 minutes, the changes will be applied to your Sales App.

> ⚠️ VTEX Sales App extensions support only production deployments. Once a commit and push are made to the `main` branch, your changes will be applied to production. To revert this change, create a new commit that reverses the previous changes, then push it to `main`.

#### Handling build failures

If the build fails, the issue is usually in your extension code or configuration. Common causes include type-checking errors and typos.

FastStore WebOps shows when a build fails, but Sales App build logs aren't available there. To inspect the logs, check the GitHub Checks for the failed commit:

![GitHub checks notification showing failed check for commit 'Added missing totalizer validations' in a VTEX app repository](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-18419-creating-extension-point/images/deploying-extensions-github-checks.webp)

You can also run the following command. Remember to replace `{account-name}` with the name of your account.

```yarn
yarn fsp build {account-name} sales-app
```

```npm
npx fsp build {account-name} sales-app
```

This command builds the VTEX Sales App extension for the specified account and displays any local build errors. If the command succeeds locally, check your GitHub repository for issues in the build workflow.
