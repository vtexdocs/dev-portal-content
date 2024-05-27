---
title: "FastStore: New @faststore/core package version"
slug: "2024-05-24-faststore-core-new-version"
type: "new"
excerpt: "Upgrade your `@faststore/core` package version to leverage enhanced API extensions, customizable error pages, and support for Next.js 13."
createdAt: "2024-05-23T10:30:00.000Z"
---

FastStore v2 users can now update their`@faststore/core` package version and benefit from enhanced API extensions, streamlined error page customization in the Headless CMS, and support for Next.js 13.

> For more information on this update, check out [FastStore GitHub releases](https://github.com/vtex/faststore/releases/tag/v3.0.0).

## What has changed?

### Enhanced API extensions

To reduce bundle sizes, align with GraphQL community standards, and get up to date with the latest bundling and compilation tools, the latest `@faststore/core` package version 3.0.0 deprecates the `@faststore/graphql-utils` package in favor of the [`client-preset`](https://the-guild.dev/graphql/codegen/plugins/presets/preset-client) plugin.

### Streamlined error page customization in the Headless CMS

Before, FastStore had a more limited scope for customizing content on pages such as Login, 404 Error, and 500 Error within the Headless CMS. Customizing these pages was only possible through code, which limited users’ ability to tailor these pages to their specific needs within the Headless CMS.

Now, these new content types are part of the latest `@faststore/core` package version 3.0, and users can customize them within the Headless CMS.

[gif](/)

### Support for Next.js 13

FastStore v2 now supports [Next.js version](https://nextjs.org/blog/next-13) 13, bringing performance and stability improvements.

Next.js 13 simplifies app directories, introduces Server Components for optimal performance, and incorporates [Turbopack](https://nextjs.org/blog/next-13#introducing-turbopack-alpha), a faster, Rust-based alternative to Webpack. This version also includes improvements to [`next/image`](https://nextjs.org/blog/next-13#nextimage) and  [`@next/font`](https://nextjs.org/blog/next-13#nextimage).

## What needs to be done?

To benefit from these changes, you first need to update your store’s `@faststore/core` version:
In your local FastStore project, install the latest version of `@faststore/core`:
 ```bash
yarn add @faststore/core@ˆ3.0.0

```

Run the project locally with `yarn dev`.

After running `yarn dev`, update each topic mentioned before as follows:
