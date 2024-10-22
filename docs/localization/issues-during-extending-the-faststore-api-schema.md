---
title: 'Issues during extending the FastStore API schema'
slug: "issues-during-extending-the-faststore-api-schema"
excerpt: "Updating EANs in VTEX can lead to catalog sync issues affecting inventory."
tags:
    - faststore
    - api
---

**Keywords:** FastStore | API extension

Although the FastStore API provides a GraphQL schema for ecommerce, you can extend the FastStore API schema to access other or more specific information from your store. During this implementation, you encounter issues such as not having the GraphQL changes you performed aren’t visible during development or in the store production.

Below are different troubleshooting checks and instructions you can use to solve API extension issues:

- [GraphQL changes not visible during development](#graphql-changes-not-visible-during-development)
- [Deploy preview/production GraphQL schema different from development](#deploy-previewproduction-graphql-schema-different-from-development)
- [Type generation errors and warnings](#type-generation-errors-and-warnings)
  - [Error details](#error-details)
- [GraphQL changes not visible in production/deploy preview](#graphql-changes-not-visible-in-productiondeploy-preview)

## GraphQL changes not visible during development

If your GraphQL changes aren't visible during development, the changes you have made since you started the development server (`yarn dev`) are probably not optimized.

To trigger the optimization, run `yarn generate` (recommended) or `yarn run faststore generate-graphql`. Alternatively, you can stop and restart the development server using `yarn dev`.

    > ℹ️ This optimization can also be performed while the development server is running.

## Deploy preview/production GraphQL schema different from development

If you notice differences between the GraphQL schema in your deploy preview or production environment and your development setup, it may be because the schema has not been optimized since the development server's initiation. The build process optimizes the schema before deployment to accurately reflect the schema declared in the store's code.

To fix the issue, refer to the [GraphQL changes not visible during development](#graphql-changes-not-visible-during-development) topic.

## Type generation errors and warnings

Some errors can occur during GraphQL optimizations and type generation. Here's how to troubleshoot them:

| **Error message** | **Possible cause** | **Solution** |
| ----------------- | ------------------ | ------------ |
| `error Failed to run 'yarn generate:schema'. Please check your setup.` | Malformed files in your GraphQL Schema Extensions definitions. | Check the graphql files inside the `src/graphql/(vtex or thirdParty)/typeDefs` folders for syntax or definition errors. |
| `error GraphQL was not optimized and TS files were not updated. Changes in the GraphQL layer did not take effect` | Malformed files or GraphQL types within your GraphQL layer, including errors in GraphQL Schema Extensions, declared queries, and fragments. | Check the graphql files inside the `src/graphql/(vtex or thirdParty)/typeDefs` folders and component (`.ts`, `tsx`) files declaring queries and fragments in your project for syntax or definition errors. |
| `warn: Failed to format generated files. 'yarn format:generated' thrown errors` | An issue occurred during the formatting process for the generated GraphQL optimization and types files. | This is a warning, not an error. Your GraphQL layer will still function correctly. If you want to investigate and resolve the formatting issue, follow these steps: <ol><li>1. Retry formatting: Run the `yarn format:generated` command again.</li> <li>2. Check formatting configuration: Ensure the formatting rules are correct and compatible with the generated files.</li><li>3. Inspect error logs: Look for specific error messages that might provide more clues about the issue.</li></ol> |

### Error details

To access more detailed error information, use the `--debug` flag when manually running the `yarn generate` command to see detailed errors on why the generation has failed.

## GraphQL changes not visible in production/deploy preview

During the build step, the GraphQL optimization and type files are always generated fresh, reflecting the most recent changes in the code.

If your changes are not visible in production, this means you must not have committed them to the branch you're currently working on. If you see different GraphQL schema, queries, or data during development, refer to the [GraphQL changes not visible during development](#graphql-changes-not-visible-during-development) topic.
