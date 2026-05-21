---
title: "VTEX Sales App extensions"
slug: "vtex-sales-app-extensions"
excerpt: "Learn how to set up VTEX Sales App extensions in your FastStore project."
hidden: false
createdAt: "2026-05-21T15:59:53.407Z"
---

>> ℹ️ This feature is currently in beta, which means we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/pt/support).

[VTEX Sales App extensibility](https://help.vtex.com/docs/tutorials/extensibility-in-vtex-sales-app) lets you customize the default assisted-sales journey with features that support your business requirements.

By using predefined extension points, you can integrate external APIs, use VTEX data, and add custom experiences to areas such as cart and checkout, the side menu, and the product details page.

In this guide, you'll learn how to set up the VTEX Sales App extension points in your FastStore project.

## Before you begin

* Set up your [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview).

* Install the VTEX Sales App on your account, complete the onboarding in VTEX Admin, and add a sales associate linked to a store. For detailed instructions, see the guide [VTEX Sales App - Basic settings](https://help.vtex.com/docs/tracks/vtex-sales-app-basic-settings).

## Instructions

### Step 1 - Install the VTEX Sales App package

Add the VTEX Sales App modules to your monorepo:

```yarn
yarn add @vtex/sales-app -D -W
```

```npm
npm add @vtex/sales-app -D
```

### Step 2 - Creating a Sales App project

After installation, create a VTEX Sales App project in your monorepo. To do this, you need the following information:

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
📂 Account monorepo
│
├── 📂 store-a
│   └── 📂 sales-app
│      └── 📂 src
│         ├── 📄 index.tsx
│         ├── 📄 HelloWorld.tsx
│         ├── 📄 hello-word.css
│         └── 📄 package.json
│  
```

In the `faststore.json` file, check if your account includes a `sales-app` entry similar to the following:

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

>ℹ️ The `fsp create` command updates `faststore.json` automatically. Review the generated values to make sure the account name, path, and port match your project.

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

![sales-app-ui](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@EDU-17928-sales-app-extension-setting-up/images/sales-app-extensions-1.webp)

You can also access the VTEX Sales App locally using the `path` and `port` values defined in `faststore.json`. For example, if the file specifies port `3002`, open `http://localhost:3002/sales-app/checkout/cart`.

## Next steps

<Flex>

<WhatsNextCard
title=""
description=""
linkTo=""
linkTitle="See more"
/>

<Flex>

<WhatsNextCard
title=""
description=""
linkTo=""
linkTitle="See more"
/>

<Flex>

<WhatsNextCard
title=""
description=""
linkTo=""
linkTitle="See more"
/>
