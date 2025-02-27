---
title: "FastStore"
slug: "faststore"
hidden: false
updatedAt: "2024-06-06T12:50:00.813Z"
excerpt: "The ultimate toolkit for building blazing-fast storefronts."
---

[FastStore](https://github.com/vtex/faststore) is a toolkit based on [Jamstack](https://jamstack.org/) that helps developers build high-performance stores.

It supports integration with [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview), offers analytics functionalities to inform storefront decision-making, and gives developers the flexibility to customize the store based on the brand’s vision, creating a unique shopping experience for users.

| Aspect | Description |
| ------ | ----------- |
| **Performance** | Ensures fast-loading stores and provides a good user experience, focusing on achieving high scores in tests like [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) and [Web Vitals](https://web.dev/articles/vitals#core-web-vitals).  |
| **Stability** | Built to be stable and avoid crashes, so your store doesn't lose sales due to provider issues.  |
| **Analytics/SEO** | Works with analytics tools to understand store customers and with SEO tools to improve store visibility in search results. |

## FastStore architecture

  ```mermaid
  flowchart LR

  style InvisibleSubgraph fill:#FFFFFF,stroke-width:0px;
  style InvisibleSubgraph2 fill:#FFFFFF,stroke-width:0px;
  style InvisibleSubgraph3 fill:#FFFFFF,stroke-width:0px;

  subgraph InvisibleSubgraph[" "]
  subgraph Developer_Tools[Developer Tools]
  direction TB
  subgraph InvisibleSubgraph3 [" "]
  direction TB
  M(GitHub pipeline)
  N(Releases)
  O(Preview mode for Headless CMS)
  P(FastStore CLI)
  Q(Localhost preview)
  R(VTEX IO CLI)
  P ~~~ M
  R ~~~ N
  Q ~~~ O
  P ~~~ N
  end
  end

  subgraph Package layer
  direction TB
  S(Core)
  T(Components)
  U(SDK)
  V(API)
  X(CLI)
  S ~~~ X
  T ~~~ X
  U ~~~ X
  end


  subgraph Technologies[Technologies]
  React ~~~ Next.js ~~~ Typescript
  GraphQL ~~~ Node
  end
  end

  subgraph InvisibleSubgraph2[" "]
  direction LR
  subgraph " "
  A(Codebase)
  F(Versioning - GitHub)
  end

  subgraph " "
  A --> B(Build process)
  H(FastStore WebOps)
  end

  subgraph " "
  B --> C(Deployment)
  I(FastStore WebOps)
  J(VTEX GitHub bot)
  end

  subgraph " "
  C --> D(Customer touchpoint)
  K(Webstore)
  end

  subgraph " "
  C --> E(User touchpoint)
  L(VTEX Headless CMS)
  end
  end
  ```

The diagram above shows a FastStore architectural flow, which includes the following components:

- **Codebase:** Source code of the FastStore project hosted on GitHub.
- **Build process:** Process of converting the source code into a deployable project through [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview).
- **Deployment:** Process of deploying the project to a production environment through [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) and quality assurance bots.
- **Business user touchpoint:** Environment where admin users interact with storefront settings on VTEX Headless CMS.
- **Customer touchpoint:** Environment where customers interact with the storefront, in this case, the store website.

## Developer tools

These are the tools that developers use to build and deploy FastStore projects. They include:

- [FastStore CLI](https://developers.vtex.com/docs/guides/faststore/getting-started-3-faststore-cli): Command-line interface (CLI) that can be used to interact with FastStore.
- [VTEX IO CLI:](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) CLI used when the project needs to interact with the VTEX platform.
- Localhost preview: Tool that allows developers to preview their FastStore projects locally.

## Package layer

FastStore consists of five main packages that enable the store to work:

- [Core](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson): Provides the starter source code to get your store up and running. It contains four sub-packages: Components, SDK, UI, and API packages.

- [SDK](https://developers.vtex.com/docs/guides/faststore/project-structure-overview#packagejson): Provides developers with a set of tools that handle all meaningful states an ecommerce store might have, such as Session, Cart, Component, and Search. The SDKs also provide GA4-compatible analytics functions to help you create powerful analytics capabilities in your ecommerce store.

- [UI](https://developers.vtex.com/docs/guides/faststore/components-index): Gathers the design system based on FastStore components, using [Sass](https://sass-lang.com/) for styling.

- [API](https://developers.vtex.com/docs/guides/faststore/faststore-api-overview): Connects your project to your favorite ecommerce provider by creating interfaces for querying products, collections, and handling carts.

- [CLI](https://developers.vtex.com/docs/guides/faststore/getting-started-3-faststore-cli): Unifies the VTEX source code in `@faststore/core` with the customizations and extensions the store will create in the `/src` folder.

## Technologies

To work with FastStore, you should be familiar with the following technologies:

- [TypeScript](https://www.typescriptlang.org/)
- [React](https://react.dev/)
- [Next.js](https://nextjs.org/)
- [GraphQL](https://graphql.org/)
- [Node.js](https://nodejs.org/en)

## Quickstart

Follow the steps below to start building and deploying a FastStore storefront.

### 1. Initial settings

Before starting the project, make sure you have the necessary tools and apps installed in your account or your local development environment. See the [Requirements](https://developers.vtex.com/docs/guides/faststore/getting-started-requirements) guide for more information.

### 2.  Starting the project

After you have prepared your machine with the initial settings, you can start your project by following the steps below:

  1. [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview): Start the onboarding of your project with the FastStore WebOps app. This app streamlines the process, saving you the trouble of complex configurations and getting your project up and running quickly.

  2. [Local Development](https://developers.vtex.com/docs/guides/faststore/getting-started-2-setting-up-the-project): After onboarding, start working on your store locally, making the initial changes and adjustments to your storefront.

## Next steps

Now that you have your FastStore project running extend your store functionalities by working with FastStore customization tools:

<Flex>

<WhatsNextCard
title="UI components"
description="Enhance your store's features with these components designed to help you quickly implement and customize features in your store."
linkTo="https://developers.vtex.com/docs/guides/faststore/components-index"
linkTitle="See more"
/>

<WhatsNextCard
title="Using themes"
description="Explore the look-and-feel of your store by using Themes, FastStore CSS stylesheets."
linkTo="https://developers.vtex.com/docs/guides/faststore/using-themes-overview"
linkTitle="See more"
/>

<WhatsNextCard
title="Customizing sections and components"
description="Explore new ways to customize your store components with overriding."
linkTo="https://developers.vtex.com/docs/guides/faststore/building-sections-overview"
linkTitle="See more"
/>

<WhatsNextCard
title="Extending the FastStore API"
description="Extend the FastStore API schema by adding new data to the existing queries"
linkTo="https://developers.vtex.com/docs/guides/faststore/api-extensions-overview"
linkTitle="See more"
/>

</Flex>
