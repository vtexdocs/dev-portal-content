---
title: "Getting started with storefront solutions"
slug: "getting-started-with-storefront-solutions"
hidden: false
excerpt: "Learn about the main differences between VTEX storefront solutions"
createdAt: "2024-05-20t12:59:27.687z"
updatedAt: "2024-06-03t10:49:27.000z"
---

The VTEX platform offers three options for storefront development, each with distinct characteristics to meet the needs of our clients:

- **FastStore**: Innovative technology that prioritizes performance and stability, offering development teams an easily maintainable solution for editing store pages.
- **Store Framework**: Emphasizes a composable commerce model, allowing integration of VTEX IO apps for dynamic storefronts.
- **Legacy CMS Portal**: VTEX’s inaugural storefront technology, that relies on HTML, CSS, and JavaScript, with code management exclusively through the VTEX Admin.

The following table outlines the main differences between VTEX’s Legacy CMS Portal, Store Framework, and FastStore.

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | --- | --- | --- |
| **Storefront development** | FastStore is built with a **performance** focus based on the [Jamstack](https://jamstack.org/) (JavaScript, API, and Markup) architecture.<br><br>The development is carried out through the integration of `npm` packages provided by VTEX and customizations via the extensibility of VTEX API core services. | Store Framework is based on **composability**, as its development is based on VTEX IO apps, allowing the combination of different content, services, and data. | The development is carried out through the Admin, using the [Legacy Content Management System (CMS)](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC). |
| **Tech stack** | <ul><li>[React](https://react.dev/)</li><li>[Typescript](https://www.typescriptlang.org/)</li><li>[Node.js](https://nodejs.org/)</li><li>[Next.js](https://nextjs.org/)</li><li>[GraphQL](https://graphql.org/)</li><li>VTEX WebOps</li></ul> | <ul><li>[React](https://react.dev/)</li><li>[TypeScript](https://www.typescriptlang.org/)</li><li>[Node.js](https://nodejs.org/)</li><li>[.NET](https://learn.microsoft.com/pt-pt/dotnet/)</li><li>[GraphQL](https://graphql.org/)</li><li>[VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io)</li></ul> | <ul><li>[CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS/)</li><li>HTML</li><li>JavaScript</li></ul> |
| **Starter (initial template)** | After completing the [FastStore Onboarding](https://www.faststore.dev/docs/getting-started-overview), you can access the [FastStore Starter](https://starter.vtex.app/). This allows you to kick off the project with a base template focused on performance. | The [Store Theme](https://github.com/vtex-apps/store-theme) is the initial template you can use to launch the storefront project. | The [Layout](https://help.vtex.com/es/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj) section allows you to create your storefront with HTML and CSS.<br><br>Inside it, you can find the standard [templates](https://help.vtex.com/en/tutorial/what-are-templates--4l7BQBYO9ycumsqua2CU88), which are files that contain the code of your website pages. |
| **CMS solution** | Integrates with the [Headless CMS](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview). | Integrates with the [Site Editor](https://developers.vtex.com/docs/guides/vtex-io-documentation-site-editor). | The [Layout](https://help.vtex.com/en/tutorial/what-is-cms-layout--EmO8u2WBj2W4MUQCS8262) feature allows you to create your storefront with HTML and CSS. |
| **Apps Admin (Extension Hub)** | There is no integration with the VTEX app platform. | Allows installation and use. | Allows installation and use of some apps. |
| **Customizations** | Performance-focused: Easier to add customizations without degrading performance. | Composability-focused: Flexible and customizable through VTEX IO apps. | Customizations are limited and can be managed by creating, organizing, and editing the structure of folders, files, and components within the Layout feature. |
| **Performance** | Maximum performance possible, as it uses [Jamstack](https://jamstack.org/), which serves pre-rendered content to a CDN. It is made dynamic through APIs and serverless functions. | SSR (Server Side Rendering) features generate the complete HTML of a page on the server as a response to a page request, while SPA (Single Page Application) loads elements such as the header only once the page is loaded. | Outdated technologies make it challenging to maintain optimal performance, especially in scenarios demanding multiple customizations. |
| **Availability** | Generally available for LATAM, Brazil, and North America; limited access for other regions. For information on unavailable features, refer to the [Features and Functionalities](#features-and-functionalities) topic. | General availability. | No longer available to new stores starting with VTEX. |
| **Support**<br><br>_To learn more about our support, see our documentation [Responsibilities within the VTEX ecosystem](https://help.vtex.com/en/tutorial/responsibilities-in-the-vtex-ecosystem--3vL9aWICDr3WR64DYi1fJ3)._ | Available for VTEX core commerce services, [FastStore packages](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore), and troubleshooting code issues. | Available for VTEX core commerce services, VTEX IO native apps or components, and troubleshooting code issues. | Available for [VTEX core commerce services](https://developers.vtex.com/docs/guides/getting-started) and VTEX native [Controls](https://developers.vtex.com/docs/guides/list-of-controls-for-templates) and [Templates](https://help.vtex.com/en/tutorial/what-are-templates--4l7BQBYO9ycumsqua2CU88). |

## Features and functionalities

The VTEX platform is both composable and complete, as it delivers a set of services that can be integrated to empower your ecommerce operation and enables customizations and integrations with third-party services.

Each storefront solution offers varying levels of composability and extensibility. Below, you can explore the features and functionalities available for each storefront technology.

|     | FastStore | Store Framework | Legacy CMS Portal |
| --- | :---: | :---: | :---: |
| **GitHub WebOps workflow** | ✅   | ❌  | ❌   |
| **Support to VTEX IO frontend apps** | ❌   | ✅   | ❌   |
| **Native support to cross-border and multi-language stores** | ❌   | ✅   | ❌   |
| **Native support to B2B capabilities** | ❌   | ✅   | ❌   |
| **Native support to marketplace capabilities** | ✅   | ✅   | ✅   |
| **[Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search) integration** | ✅   | ✅   | ❌   |
