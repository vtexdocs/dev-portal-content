---
title: "Setting up extensions for VTEX Sales App"
slug: "setting-up-extensions-for-vtex-sales-app"
excerpt: "Learn how to set up extensions for VTEX Sales App in your store."
hidden: false
createdAt: "2026-05-26T15:59:53.407Z"
seeAlso:
  - "/docs/guides/creating-a-vtex-sales-app-extension"
  - "/docs/guides/vtex-sales-app-extension-points"
  - "/docs/guides/defineextensions-function"
---

> ℹ️ This feature is currently in beta, which means we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/pt/support).

[VTEX Sales App Extensibility](https://help.vtex.com/docs/tutorials/extensibility-in-vtex-sales-app) lets you customize the default assisted-sales journey with features that support your business requirements.

By using predefined extension points, you can integrate external APIs, use VTEX data, and add custom experiences to areas such as cart and checkout, the side menu, and the product details page.

In this guide, you'll learn how to set up extension points for VTEX Sales App in your FastStore project.

## Before you begin

* Set up your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview). The monorepo uses a `faststore.json` file at the repository root to define module settings such as `paths` and `ports` for local development and production.

* Install the VTEX Sales App on your account, complete the onboarding in VTEX Admin, and add a sales associate linked to a store. For detailed instructions, see the guide [VTEX Sales App - Basic settings](https://help.vtex.com/docs/tracks/vtex-sales-app-basic-settings).

## Instructions

### Step 1 - Installing the Sales App package

Add the Sales App modules to your monorepo:

```yarn
yarn add @vtex/sales-app -D -W
```

```npm
npm add @vtex/sales-app -D
```

### Step 2 - Creating a Sales App project

To create a Sales App project in your monorepo, you need the following information:

* The store account name for which you're creating extensions.
* The module you want to initialize a project. In this case, it's `sales-app`.
* The path where you want to initialize the project.

Run the following commands in your terminal:

```yarn
yarn fsp create
```

```npx
npx fsp create
```

As an example, consider the account `store-a` and the path `./store-a/sales-app`. Remember to fill in the prompts according to your project requirements:

```text
> ? What's the account name? store-a
> ? Which module do you want to initialize? sales-app
> ? What should be the path to initialize sales-app? ./store-a/sales-app
```

After running the command, the folder is created at the root of your monorepo based on the path you provided. Your monorepo structure should look similar to this:

```txt
📂 account-monorepo
│
├──📂 store-a
│   └──📂 sales-app
│      └──📂 src
│         └── 📂 components
│         │  └──📄 Example.tsx
│         ├──📄 Example.css
│         ├──📄 index.tsx
│         └──📄 package.json
└──📄faststore.json
```

#### Project structure

The `src/index.tsx` file at the root of your project is the entry point for all VTEX Sales App extensions you create. It looks like this:

```tsx
import { defineExtensions } from '@vtex/sales-app'
import { Example } from './components/Example'

export default defineExtensions({
  'cart.cart-list.after': Example,
})
```

The `defineExtensions` function connects the extensions you create to the extension point where they should appear. You can create your extensions in separate files and then import them into `index.tsx` to keep your project organized.

This function also helps during development by showing available extension points with autocomplete and type-checking, making the setup easier and less error-prone. To build your extension, use the hooks, types, and helper functions available in the `@vtex/sales-app` package. For more information, see the [VTEX Sales App extension points](#LINK) guide.

The `src/components/Example.tsx` file includes a sample extension point. You can import CSS files, such as `Example.css`, to define classes and make them available globally. Organize your code however best fits your project, either by separating implementation and styling into different files or by keeping everything in a single file.

The `faststore.json` file should include a `sales-app` entry like the following:

```json
{
  "store-a": {
    "sales-app": {
      "path": "./store-a/sales-app",
      "port": 3002
    }
  }
}
```

> ℹ️ The `fsp create` command updates `faststore.json` automatically. Review the generated values to make sure the account name, `path`, and `port` match your project.

### Step 3 - Configuring the project as a workspace

Now, you need to register the new project as a `workspace` in the root `package.json` file so the package manager can discover it and install dependencies correctly.

For example, if you're using Yarn, your `package.json` should include:

```json
{
  "workspaces": [
    "store-a/sales-app"
  ]
}
```

> ℹ️ For more information, see your package manager's documentation on workspaces, such as the [Yarn](https://classic.yarnpkg.com/lang/en/docs/workspaces/) or [npm](https://docs.npmjs.com/cli/v7/using-npm/workspaces) documentation.

After a workspace is declared, run the install command at the root of the monorepo:

```yarn
yarn install
```

```npm
npm install
```

### Step 4 - Previewing extensions in development

After installing the dependencies, start your storefront development environment with the CLI:

```yarn
yarn fsp dev store-a
```

```npx
npx fsp dev store-a
```

The VTEX Sales App is available at the `/sales-app/checkout/cart` path on the URL provided by the FastStore CLI. You should see a screen similar to this:

![Sales App Extensions tab listing available apps with name, description, and enable toggles](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-17928-sales-app-extension-setting-up/images/sales-app-extensions-1.webp)

You can also access the VTEX Sales App locally using the `path` and `port` values defined in `faststore.json`. For example, if the file specifies port `3002`, open `http://localhost:3002/sales-app/checkout/cart`.
