---
title: "GraphQL builder: Update to 2.x, 1.x deprecation"
slug: "2025-09-30-graphql-builder-update-2x"
type: improved
excerpt: "GraphQL builder 2.x enhances security with mandatory authorization directive. Version 1.x will be deprecated."
createdAt: "2025-09-30T11:00:00.000Z"
updatedAt: "2025-09-30T11:00:00.000Z"
hidden: false
---

We are releasing GraphQL builder `2.x` for VTEX IO apps. Version `1.x` will be deprecated. The [GraphQL builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-graphql-builder) handles [GraphQL schemas](https://graphql.org/learn/schema/), used in [API implementations](https://developers.vtex.com/docs/guides/developing-a-graphql-api-in-service-apps) for [service apps](https://developers.vtex.com/docs/guides/vtex-io-documentation-service).

Version `2.x` requires all queries to use the `@auth` directive, enhancing security for apps using GraphQL APIs.

## What has changed?

The `@auth` directive is added to queries and mutations to determine the authorization required for users or apps.

In GraphQL builder `1.x`, the `@auth` directive is optional and defines a [License Manager resource and product](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3). Users or apps need a [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) or [policy](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) that includes the resource or product defined by the directive. Without the `@auth` directive, the query is public by default.

> ⚠️ GraphQL builder `1.x` will be deprecated on January 7, 2026. Existing apps built with version `1.x` will continue to work, but you won't be able to create new apps or major [versions](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version#understanding-app-versioning) of existing apps using version `1.x`. After the deprecation date, apps using builder `1.x` will fail to build via [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) or [publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app).

With builder version `2.x`, the `@auth` directive is mandatory and requires the `scope` argument, which accepts the following values:

- `PUBLIC`: The query is public and doesn't require authorization.
- `PRIVATE`: The query is private and requires authorization for a specific [License Manager resource and product](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3). When using `PRIVATE`, the `productCode` and `resourceCode` arguments are also mandatory.

If an app is built with GraphQL builder version `2.x` and is missing the `@auth` directive, the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) will display an error message in these cases:

- Any query or mutation lacks the `@auth` directive.
- The `scope` argument is missing.
- The `scope` is `PRIVATE`, and `productCode` or `resourceCode` arguments are missing.

![GraphQL auth directive error](../../images/graphql-auth-directive-error.png)

## Why did we make this change?

This change enhances the security and transparency of GraphQL APIs in VTEX IO apps. Developers must now explicitly declare whether queries and mutations are public or require authorization within the schema.

## What needs to be done?

To use the new builder version, developers must update their apps:

1. Update the GraphQL builder version to `2.x` in the [app's manifest](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

    ```json
      "builders": {
        "graphql": "2.x",
        ...
      },
    ```

2. Add the `@auth` directive to every query and mutation in the app's GraphQL schema, and include the `scope` argument. For public queries, use:

    ```graphql
    type Query {
      source(id: ID!): String
      @auth(scope: PUBLIC)
    }
    ```

For private queries, include the authorization requirements:

    ```graphql
    type Query {
      book(id: ID!): Book
      @auth(scope: PRIVATE, productCode: "64", resourceCode: "read_account_config")
    }
    ```

For more information, see [GraphQL builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-graphql-builder) and [GraphQL authorization in IO apps](https://developers.vtex.com/docs/guides/graphql-authorization-in-io-apps).
