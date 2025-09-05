---
title: "GraphQL builder"
slug: "vtex-io-documentation-graphql-builder"
excerpt: "Learn how to use the GraphQL builder."
hidden: false
createdAt: "2025-05-05T12:00:00.000Z"
updatedAt: "2025-05-05T12:00:00.000Z"
category: "App Development"
---

The `graphql` builder handles the GraphQL app [schema](https://graphql.org/learn/schema/) and serves as an interface between frontend applications and backend [services](https://developers.vtex.com/docs/guides/vtex-io-documentation-service). This guide provides a comprehensive overview of how to use this builder effectively. For more information, check [Using GraphQL to retrieve data from Master Data](https://developers.vtex.com/docs/guides/services-6-graphql-retrieving-data-from-master-data) and the [official GraphQL documentation](https://graphql.com/learn/what-is-graphql/).

> ℹ️ The `graphql` builder is used only when developing an app's GraphQL API. You don't need this builder to consume GraphQL APIs in IO apps.

## Versioning

The `graphql` builder is available in these versions:

| Builder version | Mandatory `@auth` directive\* | Status |
| :-    | :-  | :- |
| `1.x` | No  | Unavailable for new apps and new major versions of existing apps. Available for linking apps and publishing new minor and patch [versions](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version#understanding-app-versioning) of existing apps until January 7, 2025. |
| `2.x` | Yes | Active |

\* The `@auth` directive adds an authorization step to GraphQL queries and mutations. For more details, see [GraphQL authorization in IO apps](https://developers.vtex.com/docs/guides/graphql-authorization-in-io-appshttps://developers.vtex.com/docs/guides/graphql-authorization-in-io-apps).

> ⚠️ Apps using deprecated builder versions can still run on the VTEX platform, but developers can't build or create new app versions using these builder versions.

## Folder structure

The `graphql` builder uses a `graphql` folder in the app’s root folder. This folder contains `.graphql` files with the schema definitions. Developers can structure the whole schema in a single file or split it into multiple files and subfolders.

Our recommendation is to:

- Define only the endpoints ([queries](https://graphql.org/learn/queries/), [mutations](https://graphql.org/learn/mutations/), and [subscriptions](https://graphql.org/learn/subscriptions/)) in `schema.graphql`.
- Handle [directives](https://graphql.org/learn/schema/#directives) separately in `directives.graphql`.
- Define additional types in separate files inside the `types` subfolder.

```txt
graphql
┣ 📂 types
    ┣ 📄 a_type.graphql
    ┗ 📄 b_type.graphql
┣ 📄 directives.graphql
┗ 📄 schema.graphql
```

## Usage

To develop an app using the `graphql` builder, follow the steps below:

1. **Start with a template:** Download an app template such as [`graphql-example`](https://github.com/vtex-apps/graphql-example) or create a new project using the [`vtex init` CLI command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#starting-a-new-project) and select the `graphql-example` option.
2. **Add the schema files**: Add the `.graphql` files with the schema definitions, including the endpoints (queries, mutations, and subscriptions), directives, and other types you want to define.
3. **Add the API implementation logic**: Add the code that implements and instantiates the resolver functions.
    1. **Create the resolvers**: Create the resolver functions that will run when your GraphQL endpoints are called. The functions must have the same names as the endpoints defined in the schema. If you're developing a Node service, you should add the TypeScript code (`.ts` files) in the `node/resolvers` folder.
    2. **Instantiate the resolvers**: Add the code to instantiate the resolvers. If you're developing a Node service, in the `Service` class of the `node/index.ts` file, you should add a `graphql` field with the resolvers for each endpoint implemented along with the directives.
4. **Testing**: [Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace for testing. Test the endpoints with the [GraphQL IDE](https://developers.vtex.com/docs/guides/graphql-ide).

For a more detailed tutorial on implementing an app with this builder, see [Developing a GraphQL API in service apps](https://developers.vtex.com/docs/guides/developing-a-graphql-api-in-service-apps).

## Use case examples

Below are some app examples that use the `graphql` builder:

- [b2b-organizations-graphql](https://github.com/vtex-apps/b2b-organizations-graphql)
- [b2b-quotes-graphql](https://github.com/vtex-apps/b2b-quotes-graphql)
- [my-account](https://github.com/vtex-apps/my-account)
- [session-client](https://github.com/vtex-apps/session-client)
