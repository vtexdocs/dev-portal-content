---
title: "Dependencies"
slug: "vtex-io-documentation-dependencies"
hidden: false
createdAt: "2020-07-21T13:18:17.212Z"
updatedAt: "2022-12-13T20:17:44.566Z"
category: "App Development"
excerpt: "Learn how to declare and manage app dependencies in VTEX IO through the manifest.json file, ensuring all required apps are automatically installed and available."
---

The `dependencies` property is a JSON object field (`dependencies`) in the app's `manifest.json` file.

This field specifies which VTEX IO apps your app relies on to function. Its semantics resemble the [`dependencies` property in `package.json`](https://docs.npmjs.com/files/package.json#dependencies) for JavaScript applications.

When an app is installed on a VTEX account, every app listed in its `dependencies` field is automatically installed on that account.

Therefore, if your app needs to interact with another IO app—such as a VTEX API or a Store Framework block—you must declare it in the `manifest.json` file under `dependencies`, following this structure: `"{account}.{appName}": "{majorVersion}.x"`.

An example of the `dependencies` object in an app's `manifest.json` file is shown below:

```json manifest.json
"dependencies": {
  "vtex.blog-interfaces": "0.x",
  "vtex.store": "2.x",
  "vtex.styleguide": "9.x",
  "vtex.store-components": "3.x",
  "vtex.shelf": "1.x",
  "vtex.product-summary": "2.x",
  "vtex.search-graphql": "0.x",
  "vtex.search-page-context": "0.x",
  "vtex.css-handles": "0.x"
}
```

## Common use cases

Declaring dependencies is necessary for many common development scenarios, including:

- Using blocks from the [VTEX Store Framework](https://developers.vtex.com/docs/guides/vtex-store-framework).
- Importing React components from another app.
- Importing TypeScript types from a service app.
- Consuming [GraphQL](https://developers.vtex.com/docs/guides/graphql-ide) or [REST](https://developers.vtex.com/docs/api-reference) definitions declared in another app.
- Implementing a GraphQL schema interface from another app.

>⚠️ When you install a VTEX IO app, its dependencies are also installed on the account, but they are treated as indirect dependencies. This means they cannot declare public [routes](https://developers.vtex.com/docs/guides/vtex-io-documentation-routes) or receive public traffic directly.
