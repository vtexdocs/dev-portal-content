---
title: "FastStore: New @faststore/core package version"
slug: "2024-08-19-faststore-core-new-version"
type: "added"
excerpt: "Upgrade your `@faststore/core` package version to leverage enhanced API extensions, customizable error pages, and support for Next.js 13."
createdAt: "2024-08-19T10:30:00.000Z"
updateAt: "2024-08-20T10:30:00.000Z"
tags:
    - FastStore
---

FastStore v2 users can now update the `@faststore/core` package version and benefit from enhanced API extensions, streamlined error page customization in the Headless CMS, and support for Next.js 13.

> ℹ️ For more information on this update, check out [FastStore GitHub releases](https://github.com/vtex/faststore/releases/tag/v3.0.0).

## What has changed?

### Enhanced API extensions

To reduce bundle sizes, align with GraphQL community standards, and get up to date with the latest bundling and compilation tools,`@faststore/core` 3.x deprecates the `@faststore/graphql-utils` package in favor of the [`client-preset`](https://the-guild.dev/graphql/codegen/plugins/presets/preset-client) plugin.

### Streamlined error page customization in the Headless CMS

Before, FastStore had a more limited scope for customizing content on pages such as Login, 404 Error, and 500 Error within the Headless CMS. Customizing these pages was only possible through code, which limited users’ ability to tailor these pages to their specific needs within the Headless CMS.

These content types are now part of `@faststore/core` 3.x, and users can customize them within the Headless CMS.

![gif](https://vtexhelp.vtexassets.com/assets/docs/src/release-note-hcms___480683289080e473473504654c4e4697.gif)

### Support for Next.js 13

FastStore v2 now supports [Next.js version](https://nextjs.org/blog/next-13) 13, bringing performance and stability improvements.

Next.js 13 simplifies app directories, introduces Server Components for optimal performance, and incorporates [Turbopack](https://nextjs.org/blog/next-13#introducing-turbopack-alpha), a faster, Rust-based alternative to Webpack. This version also includes improvements to [`next/image`](https://nextjs.org/blog/next-13#nextimage) and [`@next/font`](https://nextjs.org/blog/next-13#nextimage).

## What needs to be done?

To benefit from these changes, you first need to update your store’s `@faststore/core` version:

1. In your local FastStore project, install the latest version of `@faststore/core`:

   ```bash
   yarn add @faststore/core@ˆ3.0.0
   ```

2. Run the project locally with `yarn dev`.

After running `yarn dev`, update each topic mentioned before as follows:

<details>
<summary>Migrating to Next.js 13</summary>

1. Open your store’s `package.json` file and, in `dependencies`, edit the `next` entry:

   ```bash
   "dependencies": {
      ...
      "next": "^13.5.6",
      ...
   },
   ```

2. After updating the `next` dependency, refer to the [Upgrading from 12 to 13](https://nextjs.org/docs/pages/building-your-application/upgrading/version-13#upgrading-from-12-to-13) official Next.js documentation for more information on how to migrate to version 13.

</details>

<details>
<summary>Error page customization in the Headless CMS</summary>

1. To sync the updated version, open a new terminal and run `faststore cms-sync`.
2. Access the VTEX Admin and go to **Headless CMS > FastStore**. You should be able to see the three new content types listed there.
3. Click one of the content types, and then`Add section` ( `+`).
4. Choose the [`EmptyState`](https://developers.vtex.com/docs/guides/faststore/organisms-empty-state) section and update its fields according to your store's requirements.

</details>

<details>
<summary>Enhanced API extensions</summary>

Follow the [Best practices for API extensions](https://developers.vtex.com/docs/guides/faststore/api-extensions-best-practices) guide for more information.

</details>
