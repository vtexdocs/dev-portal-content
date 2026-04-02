---
title: "Setting up FastCheckout"
slug: "fastcheckout-setting-up"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: ""
---

> ⚠️ This feature is only available for stores using B2B Buyer Portal, which is currently available to selected accounts.

After setting up your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview), you can create a Checkout extensions project. First, add the VTEX Checkout modules to your monorepo:

```yarn
yarn add @vtex/checkout -D -W
```

```npm
npm add @vtex/checkout -D
```

## Creating a project

After installation, create a Checkout project in your monorepo. To do this, you need the following information:

* The store account name for which you are creating extensions
* The module for which you want to initialize a project (in this case, `checkout`)
* The path where you want to initialize the project

Run the following commands in your terminal:

```yarn
yarn fsp create
```

```npx
npx fsp create
```

In this example, use the account `store-a` and the path `./store-a/checkout`. Fill in the prompts according to your project requirements:

```text
> ? What's the account name? store-a
> ? Which module do you want to initialize? checkout
> ? What should be the path to initialize checkout? ./store-a/checkout
```

After running the command, the folder is created at the root of your monorepo based on the path you provided. The project has the following structure:

![dir](/docs/guides/Checkout/monorepo-dir.png)

## Updating or creating your monorepo configuration

FastStore is compatible with different monorepo tools, from simple workspace setups with [npm](https://www.npmjs.com/) or [Yarn](https://yarnpkg.com/) to more advanced tools such as [Turborepo](https://turborepo.dev/) and [Nx](https://nx.dev/). You are responsible for managing your monorepo and workspace configuration.

Whenever you create a new project or change your workspace configuration, update the `workspaces` field in the root `package.json`.

For example, if you are using Yarn, your `package.json` should include:

```json
{
  "workspaces": [
    "store-a/checkout"
  ]
}
```

> ℹ️ For more information, see your package manager’s documentation on workspaces and monorepos, such as the [Yarn](https://classic.yarnpkg.com/lang/en/docs/workspaces/) or [npm](https://docs.npmjs.com/cli/v7/using-npm/workspaces) documentation.

After updating the configuration, run the install command again at the root of the monorepo:

```yarn
yarn install
```

```npm
npm install
```

## Connecting Checkout to Discovery

If Discovery is running locally, you can connect your local Checkout instance to it as part of your development environment. This lets you use the same Checkout instance that renders your extensions together with Discovery, so you can add products to the cart and validate the end-to-end flow locally.

To do this, update the `checkoutUrl` entry in the store’s `discovery.config.js` file (formerly `faststore.config.js`):

```js
{
  ...
  storeUrl: "https://vtexfaststore.com",
  secureSubdomain: "https://secure.vtexfaststore.com",
  checkoutUrl: process.env.NODE_ENV === 'development'
    ? "http://localhost:3000/checkout/cart"
    : "https://secure.vtexfaststore.com/checkout/cart",
  loginUrl: "https://secure.vtexfaststore.com/api/io/login",
  ...
}
```

This configuration points Discovery’s `checkoutUrl` to the Checkout instance running locally.

> ℹ️ Port `3000` is the default used by the FastStore CLI. This ensures that redirects to Checkout work correctly and also allows direct access through `http://localhost:3000/checkout/cart`. If you are using a custom port with the `--proxy-port` flag, update this value accordingly.

## Previewing extensions in development

After installing the dependencies, start your storefront development environment with the CLI:

```yarn
yarn fsp dev store-a
```

```npx
npx fsp dev store-a
```

Checkout is available at the `/checkout/cart` path on the URL provided by the FastStore CLI. To access it, open your store’s homepage, add products to the cart, and proceed to the cart. You should see a screen similar to this:

![cart](/docs/guides/Checkout/fastcheckout-cart.png)

You can also access Checkout directly by using the local URL and port defined in `faststore.json`. To find it, check the `port` value in the store and project configuration that was added when you ran `yarn fsp create`:

```json
{
  "store-a": {
    "checkout": {
      "path": "./store-a/checkout",
      "port": 3002
    }
  }
}
```

Based on this configuration, you can access Checkout directly at `http://localhost:3002/checkout/cart`.
