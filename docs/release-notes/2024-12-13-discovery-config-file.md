---
title: "FastStore: `faststore.config.js` file is now `discovery.config.js`"
slug: "2024-12-13-discovery-config-file"
type: "added"
excerpt: ""
createdAt: "2024-12-13T10:10:15.623Z"
---

To improve your FastStore development experience, we've updated the configuration file name from `faststore.config.js` to `discovery.config.js`. By making this change, we aim to enhance the flexibility and maintainability of your FastStore projects with ongoing efforts to evolve FastStore.

## What needs to be done?

To rename the file to `discovery.config.js` follow these steps:

1. Open your store project in the code editor of your preference.
2. Open the terminal and run the following to update the `@faststore/cli` package to the latest version.
3. Go to `faststore.config.js` and rename it to `discovery.config.js`.
Update any references pointing to `faststore.config.js` to use `discovery.config.js` instead.
4. Run `yarn dev` to sync the updates you made in the `@faststore/cli` package and the new filename.
