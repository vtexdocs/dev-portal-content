---
title: "Glossary"
slug: "store-framework-glossary"
hidden: false
createdAt: "2025-04-17T18:11:56.877Z"
updatedAt: ""
category: "Storefront Development"
---

## A
### Analytics
Tools and practices for examining data to gain insights or track performance. In the [Store Framework](#store-framework) context, analytics help store owners understand customer behavior and optimize their operations. Learn more in [Analytics](https://developers.vtex.com/docs/guides/storefront-analytics).

---

## B
### Bindings
Process of linking a website, a store name, and a [trade policy](#trade-policy) to create a unique identifier for each store, allowing multiple storefronts to operate within the same VTEX account. Learn more in [What is binding?](https://help.vtex.com/en/tutorial/what-is-binding--4NcN3NJd0IeYccgWCI8O2W).

### Blocks
Fundamental building units of a storefront’s layout used to structure and customize pages in [Store Framework](#store-framework). They are declared in the `blocks` section of the [Store Theme](#store-theme)’s app JSON files, allowing for a modular and reusable approach to storefront development. Learn more in [Blocks](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition#blocks).

### Builders
Modules defined in the `manifest.json` file that specify the functionality of an app. They categorize the app’s features, such as [`store`](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder) for storefront elements, [`react`](https://developers.vtex.com/docs/guides/vtex-io-documentation-react-builder) for UI components, and [`node`](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder) for backend app development, among others. Learn more in [Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders).

---

## C
### Children
A [composition](#composition) type that allows flexible ordering of child [blocks](#blocks). Child blocks are listed in a `children` array, and their sequence determines their positioning on the page, enabling dynamic layout control for store themes. Learn more in [Children](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition#children).

### Content Management System (CMS)
A tool that allows you to create, manage, and publish digital content easily, without needing advanced technical skills. In Store Framework, [Site Editor](#site-editor) functions as a Content Management System (CMS), reflecting the blocks defined in the [Store Theme](#store-theme) of the VTEX account. Learn more in [CMS Overview](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/6OCY6S9tqBXPD5mgpbBInC).

### Components
Building [blocks](#blocks) used to create storefronts and admin apps. These blocks accept [properties](#properties-props) and return React elements to define what is displayed in the user interface. They range from basic elements (such as buttons and forms) to complex features (such as product carousels and navigation bars). Learn more in [Using components](https://developers.vtex.com/docs/guides/store-framework-using-components).

### Composition
A property in the `interfaces.json` file that defines how [React](https://react.dev/) components are organized and structured within a parent-child hierarchy in a [Store Theme](#store-theme). There are three types of composition: [blocks](#blocks), [children](#children), and [slots](#slots). Learn more in [Composition](https://developers.vtex.com/docs/guides/vtex-io-documentation-composition).

### CSS Handles
A CSS class that maps to an HTML element. It serves as a layout-building assistant for your store, allowing you to customize any block by applying CSS classes within the [Store Theme](#store-theme) code. Learn more in [Using CSS handles for store customizations](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

---

## D
### Dependencies
A property (#properties-props) in the `manifest.json` file that specifies other [VTEX IO apps](#vtex-io-apps) that an app requires to function. Dependencies ensure that required apps are automatically installed when your app is installed. Learn more in [Dependencies](https://developers.vtex.com/docs/guides/vtex-io-documentation-dependencies).

---

## I
### Interfaces
Rules defined in the `interfaces.json` file that link a [block](#blocks) to a [component](#components), enabling storefront development. These rules define the block's behavior, available [properties](#properties-props), and methods used during rendering. Learn more in [Interfaces](https://developers.vtex.com/docs/guides/vtex-io-documentation-interface).

---

## J
### JSON Schema
A declarative format for defining the structure, constraints, and default values of JSON data. Used in [Store Framework](#store-framework), it ensures consistency and validation in app configurations, such as [blocks](#blocks) or [components](#components), by specifying data types, required fields, and allowed values. Learn more in [JSON Schema](https://json-schema.org/).

---

## M
### Manifest
A document containing metadata that defines and shapes the core attributes and features of a [VTEX IO app](#vtex-io-app). Learn more in [Manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

---

## P

### Peer dependencies
Declared in the ´manifest.json` file under the `peerDependencies` field, these specify other [VTEX IO apps](#vtex-io-apps) required for an app to function. Unlike regular [dependencies](#dependencies), peer dependencies aren’t automatically installed when the app is installed. Instead, users must manually ensure their installation. They are often used in scenarios where an app relies on specific major versions of other apps, or when it depends on paid apps that may not be included by default. Learn more in [Peer dependencies](https://developers.vtex.com/docs/guides/vtex-io-documentation-peerdependencies).

### Properties (props)
Key-value pairs used to define the behavior and appearance of [components](#components) in the [Store Framework](#store-framework). They provide flexibility and customization, allowing developers to configure various aspects of a component, such as layout, functionality, and styling, within the storefront. Learn more in [Properties](https://developers.vtex.com/docs/guides/vtex-io-documentation-properties).

---

## R
### Routes
Routes are configurations that map URL patterns and HTTP methods to specific actions, determining how an application handles incoming client requests. In the context of [Store Framework](#store-framework), routing is managed by the [Rewriter app[(https://developers.vtex.com/docs/apps/vtex.rewriter) and [Store Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-builder), enabling developers to focus on defining route paths and designing page templates without managing low-level routing logic directly. Learn more in [Routing](https://developers.vtex.com/docs/guides/store-framework-routing).

---

## S
### Search Engine Optimization (SEO)
Practices and techniques to improve a website’s visibility and ranking on search engines. Learn more in [SEO](https://developers.vtex.com/docs/guides/storefront-seo).

### Site Editor
A [Content Management System (CMS)](#content-management-system-cms) for stores built with [Store Framework](#store-framework). It reflects [blocks](#blocks) defined in the [Store Theme](#store-theme), allowing non-technical users to edit content, modify components, and update storefronts via a user-friendly interface. Learn more in [Working with Site Editor](https://developers.vtex.com/docs/guides/store-framework-working-with-site-editor).

### Sitemap
File listing all pages of a website, typically used for [SEO](#search-engine-optimization-seo) purposes, ensuring search engines can index pages effectively.

### Slots
A [composition](#composition) type that allows developers to pass [components](#components) as [props](#properties-props) directly, offering an alternative to [blocks](#blocks) composition in [Store Framework](#store-framework). Learn more in [Slots](https://developers.vtex.com/docs/guides/vtex-io-documentation-slots).

### Store Framework
VTEX framework for creating ecommerce storefronts, leveraging [React](https://react.dev/) and [VTEX IO](#vtex-io) development platform. It offers native storefront [components](#components) to develop scalable and efficient online stores. Learn more in [Store Framework](https://developers.vtex.com/docs/guides/store-framework).

### Store Theme
A [VTEX IO app](#vtex-io-app) that defines a storefront’s appearance and functionality. Learn more in [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme).

---

## T
### Trade policy
A set of configurations on the VTEX platform that define catalog, pricing, promotions, logistics, and payments for specific sales strategies. Trade policies are used to segment sales conditions across different channels (for example, B2B, marketplaces), adapting store navigation and offerings based on the user type. Learn more in [How trade policies work](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV).

---

## V
### VTEX App Store
A marketplace for [VTEX IO](#vtex-io) plug-and-play solutions, where both first-party and third-party apps can be published and downloaded by clients and partners. Learn more in [VTEX App Store](https://developers.vtex.com/docs/guides/vtex-app-store).

### VTEX IO
A cloud-based development platform designed to enhance the agility and autonomy of creating and managing online stores. It allows for the streamlined and independent development of applications and new software, supporting multiple environments known as [workspaces](#workspaces). Learn more in [What is VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io).

### VTEX IO apps
Modular applications developed to extend or customize the VTEX platform. Developed using VTEX IO's framework, these apps can range from frontend components for Store Framework to backend services, like payment gateways and integrations with third-party tools. VTEX IO apps can also be distributed through the VTEX App Store, offering a straightforward way to install, update, and maintain functionality across VTEX stores. Learn more in [What is a VTEX App](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-a-vtex-app).

### VTEX IO CLI
A command-line interface for developers to interact with the [VTEX IO](#vtex-io) platform. It enables linking local files, managing [workspaces](#workspaces), releasing app versions, and performing essential development tasks. The CLI is central to the VTEX IO development workflow. Learn more in [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

---

## W
### Workspaces
Isolated environments within a VTEX account that act as separate versions for app development in VTEX IO. Similar to branches in [Git](https://git-scm.com/), workspaces enable safe testing, development, and deployment of new features and updates. Learn more in [Workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace).

---
