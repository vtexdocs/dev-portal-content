---
title: "Node builder"
slug: "vtex-io-documentation-node-builder"
excerpt: "Learn how to use the VTEX IO Node builder."
hidden: false
createdAt: "2024-03-26T11:00:00.000Z"
updatedAt: "2024-06-05T17:53:00.000Z"
category: "App Development"
---

The `node` builder is used to develop [backend apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-service) with TypeScript code executed by the [Node.js runtime](https://nodejs.org/en). This guide aims to provide a comprehensive understanding of how to utilize this builder effectively. For further insights, refer to [Developing services on VTEX IO](https://developers.vtex.com/docs/guides/developing-services-on-vtex-io).

## Versioning

The Node builder has its versions defined in the table below. Each builder version works with a specific version of the Node.js engine, [`@types/node` package](https://www.npmjs.com/package/@types/node) (TypeScript definitions for Node), and TypeScript. You can choose the builder version in your app’s `manifest.json` file.

|Builder version|Node.js|@types/node|TypeScript|Status|
|-|-|-|-|-|
|4.x|[12.x](https://nodejs.org/en/blog/release/v12.0.0)|-|[3.9.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html)|Active until March 2025|
|6.x|[16.x](https://nodejs.org/en/blog/release/v16.0.0)|[12.0.0](https://www.npmjs.com/package/@types/node/v/12.0.0)|[3.9.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html)|Active until June 2025|
|7.x|[20.x](https://nodejs.org/en/blog/release/v20.0.0)|[20.0.0](https://www.npmjs.com/package/@types/node/v/20.0.0)|[5.5.3](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html)|Active|

>⚠️ Apps using deprecated builder versions will not link and build. For details about updating the Node builder version, see our [migration guide](https://developers.vtex.com/docs/guides/node-builder-7x-migration-guide).

## Folder structure

An app that uses the `node` builder has a `node` folder on its root, where are located the following files and directories:

```txt
node
  ┣ 📂 clients
      ┗ 📄 {ClientCodeFileName}.ts
  ┣ 📂 middlewares
      ┗ 📄 {MiddlewareCodeFileName}.ts
  ┣ 📂 event
      ┗ 📄 {EventCodeFileName}.ts
  ┣ 📄 {TypeScriptCodeFileName}.ts
  ┣ 📄 index.ts
  ┣ 📄 package.json
  ┣ 📄 services.json
  ┗ 📄 tsconfig.json
```

- TypeScript code files (`.ts` extension) containing the core logic of the app, organized within various directories, such as:
  - `clients`: Directory with the code files of [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients).
  - `middlewares`: Directory with the code files of middlewares.
  - `event`: Directory with the code files of event functions.
- `index.ts`: Main TyepScript code file, where the execution begins. This file contains the main class of the service.
- `package.json`: JSON file describing the dependencies, script commands for building, and version details.
- `services.json`: Service configuration file used for defining the app parameters such as routes, events, time-to-live, etc. For more details, see [Service configuration parameters](https://developers.vtex.com/docs/guides/vtex-io-documentation-service#service-configuration-parameters).
- `tsconfig.json`: JSON file containing build configuration options.

## Usage

To develop an app using the `node` builder, refer to the following steps:

- **Start with a template**: Download the [`service-example` template](https://github.com/vtex-apps/service-example) or create a new project using the [`vtex init` CLI command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#starting-a-new-project) and choose the `service-example` option.
- **Configure the `service.json` file**: Edit the `service.json` configuration file. For more information, see [Service configuration parameters](https://developers.vtex.com/docs/guides/vtex-io-documentation-service#service-configuration-parameters).
- **Configure permissions**: If you want to access external resources, add the necessary [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) to get permission for each resource in the [`manifest.json`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) and the corresponding [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients) in the code to access the resources.
- **Implement the app's logic**: Add the necessary TypeScript files containing the app logic.
- **Testing**: [Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace for testing.

>ℹ️ Refer to [Engineering guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-engineering-guidelines) for further information on scalability, performance optimization, data privacy best practices, and versioning.

## Use case examples

Consider the following scenarios when using the `node` builder:

- **Backend service development**: If you are building backend services using Node.js, the `node` builder provides a streamlined development experience with native functions and clients for integrating with the VTEX ecosystem.
- **Event-driven applications**: For applications that rely heavily on event-driven architecture, where actions trigger responses asynchronously, the `node` builder allows developers to implement event handlers and listeners.
- **Integration with external systems**: When your application needs to integrate with external systems or APIs, such as payment gateways, databases, or third-party services, the `node` builder facilitates the development of client modules for interacting with these systems.
- **Custom middleware**: If your application requires custom middleware for tasks like authentication, logging, or request processing, the `node` builder supports the creation and integration of middleware components.

Here are some app examples that use the `node` builder:

- [orders-feed-example](https://github.com/vtex-apps/orders-feed-example)
- [external-seller-example](https://github.com/vtex-apps/external-seller-example)
- [adyen-platforms](https://github.com/vtex-apps/adyen-platforms)
- [mega-menu](https://github.com/vtex-apps/mega-menu)
