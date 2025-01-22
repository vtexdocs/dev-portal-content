---
title: "Getting started with storefront solutions"
slug: "getting-started-with-storefront-solutions"
hidden: false
excerpt: "Learn about the main differences between VTEX storefront solutions."
createdAt: "2024-05-20t12:59:27.687z"
updatedAt: "2024-09-13T14:32:02.701Z"
---

The VTEX platform provides three options for storefront development, each with distinct characteristics to meet the needs of our clients:

- **FastStore:** Innovative technology that prioritizes performance and stability, offering operational teams an easily maintainable solution for editing store pages.
- **Store Framework:** Emphasizes a composable commerce model, allowing the integration of VTEX IO apps for dynamic storefronts.
- **Legacy CMS Portal:** VTEX’s first storefront technology that relies on HTML, CSS, and JavaScript, with code management exclusively through the VTEX Admin.

The following table outlines the main differences between VTEX FastStore, Store Framework, and Legacy CMS Portal.

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | --- | --- | --- |
| **Storefront development** | FastStore is built with a **performance** focus based on the Jamstack (JavaScript, API, and Markup) architecture.<br><br>Development is done through the integration of `npm` packages provided by VTEX and customizations via the extensibility of VTEX API core services. | Store Framework is based on **composability**, as development is based on VTEX IO apps, allowing the combination of different content, services, and data. | Development is done through the Admin, using the [Legacy Content Management System (CMS)](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC). |
| **Tech stack** | <ul><li>[React](https://react.dev/)</li><li>[Typescript](https://www.typescriptlang.org/)</li><li>[Node.js](https://nodejs.org/)</li><li>[Next.js](https://nextjs.org/)</li><li>[GraphQL](https://graphql.org/)</li></ul> | <ul><li>[React](https://react.dev/)</li><li>[TypeScript](https://www.typescriptlang.org/)</li><li>[Node.js](https://nodejs.org/)</li><li>[.NET](https://learn.microsoft.com/pt-pt/dotnet/)</li><li>[GraphQL](https://graphql.org/)</li></ul> | <ul><li>[CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/)</li><li>HTML</li><li>JavaScript</li></ul> |
| **Starter (initial template)** | After completing the [FastStore Starter](https://starter.vtex.app/), you can access [FastStore Onboarding](https://www.faststore.dev/docs/getting-started-overview). This allows you to kick off the project with a base template focused on performance. | [Store Theme](https://github.com/vtex-apps/store-theme) is the initial template you can use to launch the storefront project or start from scratch. | The [Layout](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj#layout) section allows you to create your storefront with HTML and CSS.<br><br>In it, you can find the standard [templates](https://help.vtex.com/en/tutorial/what-are-templates--4l7BQBYO9ycumsqua2CU88), which are files that contain the code of your website pages. |
| **CMS solution** | Integrated with [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview). | Integrated with [Site Editor](https://developers.vtex.com/docs/guides/vtex-io-documentation-site-editor). | The [Layout](https://help.vtex.com/en/tutorial/what-is-cms-layout--EmO8u2WBj2W4MUQCS8262) feature allows you to create your storefront with HTML and CSS. |
| **Deployment platform** | Store deployment through [FastStore WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) and VTEX GitHub quality assurance bots. | Store deployment through the [VTEX IO platform](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference). | Content updates are done directly through the CMS. |
| **Deployment environment** | Supports running a [local server](https://developers.vtex.com/docs/guides/faststore/getting-started-2-setting-up-the-project#step-2-running-a-local-server), which works as a development environment. Changes made in the local development server do not impact the live store. | Supports creating [development workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) and [production workspaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace), allowing developers to deploy changes confidently, without affecting the live store. | Does not have a separate development environment. |
| **Admin Apps (Extensions Hub)** | The VTEX IO backend apps can work on FastStore through the [API Extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-overview) tool. Frontend apps that manipulate React components are not available. | Allows installation and use. | Allows installation and use of some apps. |
| **Customizations** | Performance-focused: Allows customization through [Theming](https://developers.vtex.com/docs/guides/faststore/using-themes-overview), [Overrides](https://developers.vtex.com/docs/guides/faststore/overrides-overview), [API extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-overview), and [Dynamic Content](https://developers.vtex.com/docs/guides/faststore/dynamic-content-overview) features. | Composability-focused: Flexible and customizable through [VTEX IO apps](https://developers.vtex.com/docs/vtex-io-apps). | Customizations are limited and can be managed by creating, organizing, and editing the structure of folders, files, and components within the [Layout](https://help.vtex.com/es/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj#layout) feature. |
| **Performance** | Maximum performance possible, as it uses [Jamstack](https://jamstack.org/), a framework focused on performance that serves pre-rendered content to a CDN. It is made dynamic through APIs and serverless functions.<br><br>Additionally, FastStore leverages [Partytown](https://partytown.builder.io/) for minimizing performance degradation caused by third-party scripts.<br><br>Built with performance as a core principle, FastStore not only optimizes speed but also provides clear visibility into performance metrics, ensuring transparency. | SSR (Server-Side Rendering) features generate the complete HTML of a page on the server as a response to a page request, while SPA (Single-Page Application) loads elements such as the header only once the page is loaded. | Outdated technologies make it challenging to maintain optimal performance, especially in scenarios demanding multiple customizations. |
| **Availability**<br><br>_You can have both FastStore and Store Framework running simultaneously in your store, as the environments are completely different._ | General availability.<br><br>For information on unavailable features, check the [Business models](#business-models) and [Features and Functionalities](#features-and-funcionalities) sections. | General availability. | No longer available to new stores starting to use VTEX. |
| **Support**<br><br>_To learn more about our support, see our documentation [Responsibilities within the VTEX ecosystem](https://help.vtex.com/en/tutorial/responsabilidades-no-ecossistema-vtex--3vL9aWICDr3WR64DYi1fJ3)._ | Available for VTEX core commerce services, [FastStore packages](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore), and troubleshooting code issues. | Available for VTEX core commerce services, VTEX IO native apps or components, and troubleshooting code issues. | Available for [VTEX core commerce services](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services), and VTEX native [Controls](https://developers.vtex.com/docs/guides/list-of-controls-for-templates) and [Templates](https://help.vtex.com/en/tutorial/what-are-templates--4l7BQBYO9ycumsqua2CU88). |

## Business models

The VTEX platform supports the configuration of different business models, such as business-to-business (B2B), marketplaces, omnichannel, and internationalization. See below the availability for each storefront technology.

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | :---: | :---: | :---: |
| [**B2B capabilities**](https://help.vtex.com/en/tutorial/b2b-overview--5vb9SNXhX2bZnkpAh7ADdC?\&utm_source=autocomplete) | ❌ | ✅ | ❌ |
| [**Bindings**](https://help.vtex.com/en/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W?\&utm_source=autocomplete) | ❌ | ✅ | ✅ |
| [**Cross-border and multi-language stores**](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/5qgXy9Erm7FDP3UB5Ox8Bs) | ❌ | ✅ | ❌ |
| [**Franchise accounts**](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) | ✅ | ✅ | ✅ |
| [**Marketplace capabilities**](https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402) | ✅ | ✅ | ✅ |
| [**Multiple trade policies**](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV) | ✅ | ✅ | ✅ |
| [**Regionalization**](https://developers.vtex.com/docs/guides/faststore/features-regionalization) | ✅ | ✅ | ❌ |

## Features and functionalities

Below, explore the features and functionalities available for each storefront technology. Consider the following legend:

✅ **Available:** An out-of-the-box feature, ready to use.

⚠️ **Limited:** The feature is possible but needs custom implementation.

❌ **Not available:** This feature is currently unavailable, even with customizations.

### Advanced store functionalities

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | :---: | :---: | :---: |
| [**Abandoned Cart**](https://help.vtex.com/en/tutorial/setting-up-abandoned-carts--tutorials_740) | ⚠️ | ✅ | ✅ |
| [**Attachments**](https://help.vtex.com/en/tutorial/what-is-an-attachment--aGICk0RVbqKg6GYmQcWUm) | ✅ | ✅ | ✅ |
| [**Coupons**](https://help.vtex.com/en/tutorial/coupons-beta--1aAEN3ADpz19ss5JCIEBdL) | ✅ | ✅ | ✅ |
| [**Gift Card**](https://developers.vtex.com/docs/guides/gift-card-integration-guide) **integration** | ✅ | ✅ | ✅ |
| [**GTM - Google Analytics 4**](https://help.vtex.com/en/tutorial/how-to-setup-google-analytics-in-vtex-store--G2P0rmSrEiqCcmUMyUUwG) | ✅ | ✅ | ✅ |
| [**Master Data**](https://developers.vtex.com/docs/guides/master-data) **integration** | ⚠️ | ✅ | ✅ |
| [**Newsletter integration with Master Data**](https://developers.vtex.com/docs/guides/implementing-newsletter-opt-in-with-master-data-v1) | ✅ | ✅ | ✅ |
| [**Price table**](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S) | ✅ | ✅ | ✅ |
| [**Promotions**](https://help.vtex.com/en/tutorial/creating-promotions--tutorials_320) | ✅ | ✅ | ✅ |
| [**SmartCheckout**](https://help.vtex.com/en/tutorial/smartcheckout-customer-information-automatic-fill-in--2Nuu3xAFzdhIzJIldAdtan) | ✅ | ✅ | ✅ |
| [**Sitemap**](https://help.vtex.com/en/tutorial/rastreamento-google-search-console-sitemap--tutorials_575) **integration** | ✅ | ✅ | ✅ |
| [**Subscription**](https://help.vtex.com/en/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453) | ✅ | ✅ | ✅ |
| **Support for** [**VTEX IO frontend apps**](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developing-storefront-apps-using-react-and-vtex-io) | ❌ | ✅ | ❌ |

### VTEX IO Apps

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | :---: | :---: | :---: |
| [**Assembly options**](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH?\&utm_source=autocomplete) | ⚠️ | ✅ | ❌ |
| [**Intelligent Search**](https://help.vtex.com/tracks/vtex-intelligent-search) **integration** | ✅ | ✅ | ❌ |
| [**Live Shopping**](https://developers.vtex.com/docs/apps/vtexventures.livestreaming) | ⚠️ | ✅ | ✅ |
| [**Reviews & Ratings**](https://developers.vtex.com/docs/apps/vtex.reviews-and-ratings) | ⚠️ | ✅ | ❌ |
| [**Store Locator**](https://developers.vtex.com/docs/apps/vtex.store-locator) | ⚠️ | ✅ | ❌ |
| [**Wishlist**](https://developers.vtex.com/docs/apps/vtex.wish-list) | ⚠️ | ✅ | ❌ |

### Development experience

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | --- | --- | :---: |
| **API integration** | ✅ [FastStore APIs](https://developers.vtex.com/docs/guides/faststore/faststore-api-overview) | ✅ [API reference](https://developers.vtex.com/docs/api-reference) | ✅ [API reference](https://developers.vtex.com/docs/api-reference) |
| **Automatic storefront updates** | ✅ | ✅ | ❌ |
| **Command Line Interface (CLI)** | ✅ [FastStore CLI](https://developers.vtex.com/docs/guides/faststore/getting-started-3-faststore-cli) | ✅ [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) | ❌ |
| **GitHub [WebOps](https://developers.vtex.com/docs/guides/faststore/1-onboarding-overview) workflow** | ✅ | ❌ | ❌ |

Learn more in [Developer experience](https://developers.vtex.com/docs/guides/developer-experience).
