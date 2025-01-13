---
title: "FastStore: Simplified Lighthouse dependency for projects"
slug: "2025-01-08-simplified-lighthouse-dependency"
hidden: false
type: "improved"
createdAt: "2025-01-08T10:00:00.219Z"
excerpt: "The FastStore CLI now directly includes the '@faststore/lighthouse' package, simplifying project setup"
---

The `@faststore/lighthouse` package is now a core dependency for `@faststore/cli`. This change eliminates the need to manually declare `@faststore/lighthouse` in your project's `package.json` file.

## What needs to be done?

To ensure that the `@faststore/lighthouse` package is included in the final production build, follow these steps:

1. Open your FastStore project.
2. Go to the `package.json` file and remove the `@faststore/lighthouse` from the `devDependencies` section.
3. Open a terminal and update the `@faststore/cli` package to the latest version by running `yarn add @faststore/cli@latest`.
4. Run `yarn dev` to sync the changes to your project.
