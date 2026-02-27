---
title: 'Issues during extending the FastStore API schema'
slug: "issues-during-extending-the-faststore-api-schema"
hidden: false
createdAt: "2024-11-13T00:00:00.000Z"
updatedAt: "2026-02-25T13:00:00.000Z"
excerpt: "Development and deployment challenges may arise while extending FastStore API schema with GraphQL."
tags:
    - FastStore
---

Keywords: FastStore | API extension | GraphQL | schema extensions | yarn generate | deploy preview

Although the FastStore API provides a GraphQL schema for ecommerce, you can extend it to access other or more specific information from your store. During this implementation, you may face issues such as local GraphQL changes not appearing, schema differences between environments, or generation errors.

## Solutions

## GraphQL changes not visible or inconsistent across environments

If your GraphQL changes are not visible during development, or if your deploy preview or production schema differs from your development schema, the GraphQL layer likely needs optimization. This process ensures your latest code changes are reflected in the generated schema and types.

1. Run `yarn generate` (recommended) or `yarn run faststore generate-graphql` in the project root.

> ⚠️ You can run `yarn generate` while the development server is running.

2. If changes are still not visible, or if differences between development and deploy preview/production persist, stop `yarn dev` and start it again.

### GraphQL changes not visible in production or deploy preview

If changes are visible in development but not in deploy preview or production, verify deployment inputs and build context.

1. Confirm all API Extensions changes are committed to the deployed branch.
2. Confirm the deploy preview/production build was triggered from the same branch and latest commit.
3. Re-run `yarn generate` (or `yarn run faststore generate-graphql`) locally and compare local behavior with the deployed result.

### Type generation errors and warnings

If you see errors or warnings during generation, use the table below to identify the issue and the required action.

Issue | Description | Solutions
--- | --- | ---
`error Failed to run 'yarn generate:schema'. Please check your setup.` | Schema generation failed, usually because of invalid schema extension files. | Review `.graphql` files in `src/graphql/vtex/typeDefs` and `src/graphql/thirdParty/typeDefs` for syntax and schema definition issues.
`error GraphQL was not optimized and TS files were not updated. Changes in the GraphQL layer did not take effect` | GraphQL optimization failed, usually due to invalid schema, resolvers, queries, or fragments. | Validate schema files, resolver files in `src/graphql/(vtex or thirdParty)/resolvers`, and query or fragment declarations in `.ts` and `.tsx` files.
`warn Failed to format generated files. 'yarn format:generated' threw errors` | Formatting step failed after generation. | This is a warning, not an error. Your GraphQL layer will still function correctly. If you want to investigate and resolve the formatting issue, follow these steps: <ol><li>1. Retry formatting: Run the `yarn format:generated` command again.</li> <li>2. Check formatting configuration: Ensure the formatting rules are correct and compatible with the generated files.</li><li>3. Inspect error logs: Look for specific error messages that might provide more clues about the issue.</li></ol>

### Error details

If the issue is not clear from the messages above, run the generation command with debug output to identify exactly where the failure occurs.

1. Run `yarn generate --debug`.
2. Use the verbose output to identify the failing file or operation.
