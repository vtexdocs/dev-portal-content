---
title: "GraphQL in VTEX IO"
slug: "graphql-in-vtex-io"
hidden: false
createdAt: "2025-04-28T11:00:00.000Z"
updatedAt: "2025-04-28T11:00:00.000Z"
---
[GraphQL](https://graphql.org/) is a query language for APIs that allows clients to request specific data from a server. Unlike REST APIs, which return fixed data structures, GraphQL allows developers to retrieve only the data they need, preventing over- and under-fetching.

GraphQL has the advantage of being self-documenting, making it easier for developers to explore and consume APIs. With [introspection queries](https://graphql.org/learn/introspection/) and GraphQL IDEs such as [GraphiQL](https://github.com/graphql/graphiql), consumers can inspect the schema to view available endpoints, arguments, and fields.

In VTEX IO, there are specific ways to interact with GraphQL APIs. They include authenticating endpoints, implementing an API in an app, making GraphQL requests in an app, and more. For example, you need to use the [GraphQL builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-graphql-builder) to define the schema when creating an API in an app, and you also need to use [IO clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients) to make GraphQL requests in an app.

## Essential concepts

To effectively work with GraphQL APIs in VTEX IO, it's important to understand the following core concepts:

- **Schema**: The GraphQL schema defines the structure of the API, including types, queries, and mutations. It serves as the blueprint for both the server and the client.
- **Queries** and **mutations**: Queries are used to fetch data, while mutations are used to modify data. Understanding how to craft these is crucial for interacting with GraphQL APIs.
- **Introspection**: GraphQL allows for introspection, meaning you can query the API to understand its structure. This is particularly useful for exploring available queries, mutations, and types.

## Guides in this section

In this section, we will cover the following topics:

<Flex>

<WhatsNextCard
title="List of GraphQL APIs"
description="See how to use GraphQL APIs of VTEX Apps."
linkTo="https://developers.vtex.com/docs/guides/vtex-io-graphql-api-list"
linkTitle="See more"
/>

</Flex>
