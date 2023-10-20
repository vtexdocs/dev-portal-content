---
title: "FastStore now supports Node.js 18"
slug: "2023-10-20-faststore-now-supports-node-18"
type: "added"
excerpt: "Stores using FastStore can now take advantage of Node.js 18 capabilities."
createdAt: "2023-10-20T00:00:00.000Z"
---

FastStore has introduced support for [Node.js 18](https://nodejs.org/en/blog/announcements/v18-release-announce), and **by December 13th, 2023, all stores will automatically transition to Node.js 18**. To prepare for this transition, you can enable this feature in your store and conduct initial testing.

> ⚠️ We strongly recommend trying this out before the Black Friday season, ideally by November 13th, 2023, to ensure a seamless experience during the season.

## What has changed?

Previously, the default Node.js version for the FastStore pipeline was Node.js 14, which couldn't leverage the improvements of the latest Node.js versions. With this update, FastStore now fully supports Node.js 18. However, this update will be automatically applied to all stores only on December 13th.

The introduction of Node.js 18 aims to provide greater stability, improved store performance, and reduced latency for the platform and FastStore users. Internal tests have shown approximately 40% less latency and increased efficiency for FastStore stores using Node.js 18.

## What needs to be done?

To try this change beforehand, set the `experimental` flag in your code. To do so, open your FastStore project code and follow the steps below:

1. Create a new branch for testing.
2. Open your store configuration file, which is `store.config.js` for [FastStore v1](https://v1.faststore.dev/) and `faststore.config.js` for [FastStore v2](https://faststore.dev/).
3. Set the experimental flag as follows:

        ```js
        ...
        experimental: {
        nodeVersion: 18,
        },
        ...
        ```

4. In the terminal, run `yarn dev`.
5. Ensure there are no errors in the terminal, and if everything checks out, open a Pull Request.

        > ⚠️ To prevent the build from failing due to compatibility issues during the first build with Node.js 18, some stores may need to turn off the build cache. To do this, set to `FALSE` the following variables in the `vtex.env` file and try again: `USE_BUILD_CACHE=false`, `USE_NODE_MODULES_CACHE=false`, `USE_FRAMEWORK_CACHE=false`.

6. Merge it to the main branch.

Once you have merged to the main branch, your store will be updated with Node.js 18.
