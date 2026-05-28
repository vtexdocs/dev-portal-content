---
title: "VTEX Sales App Extensibility"
slug: "vtex-sales-app-extensibility"
excerpt: "Learn about Sales App extensions, how to build and style them, and how to access the data layer."
hidden: false
createdAt: "2026-05-27T17:17:40.610Z"
updatedAt: "2026-05-27T17:32:46.010Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

[VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility) lets you extend the default assisted-sales journey with capabilities aligned to your business model, such as external integrations and VTEX data.

The technical aspects of Sales App extensions are covered in the following articles:

- [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill) — AI skill with Sales App and FastStore knowledge (`sales-app-extensibility`) to scaffold, validate, and deploy extensions across the full development lifecycle.

- [Sales App extensions implementation](https://developers.vtex.com/docs/guides/sales-app-extensions-implementation) — Set up your FastStore monorepo, build and deploy extensions with WebOps, and consult extension points and the API reference. Contains the following articles:
  - [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points) — Explore predefined slots in the Sales App UI (cart, PDP, menu), the hooks available at each point, and layout-shift guidance.
  - [Setting up extensions for VTEX Sales App](https://developers.vtex.com/docs/guides/setting-up-extensions-for-vtex-sales-app) — Add `@vtex/sales-app` to your FastStore monorepo, create a `sales-app` project with the FSP CLI, register the workspace, and preview locally.
  - [Installing WebOps for Sales App extensions](https://developers.vtex.com/docs/guides/installing-webops-for-sales-app-extensions) — Install and configure FastStore WebOps in your VTEX account and GitHub repository so the `sales-app` module can be built and deployed.
  - [Creating a VTEX Sales App extension](https://developers.vtex.com/docs/guides/creating-a-vtex-sales-app-extension) — Build a React component, register it with `defineExtensions`, and optionally style it with CSS and `useSettings`.
  - [Deploying VTEX Sales App extensions](https://developers.vtex.com/docs/guides/deploying-vtex-sales-app-extensions) — Push to your production branch to trigger a WebOps build of the `sales-app` module, and troubleshoot failures with GitHub Checks or `fsp build`.
  - [Sales App extension hooks and types](https://developers.vtex.com/docs/guides/sales-app-extension-hooks-and-types) — Consult hooks and types to interact with the Sales App data layer.

- [CSS styling in VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/css-styling-in-vtex-sales-app-extensibility) — Style extensions with CSS Modules (recommended) or plain CSS imports; limit styles to your extension and avoid overriding core Sales App UI

- [Data layer and data fetching in VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/data-layer-and-data-fetching-in-vtex-sales-app-extensibility) — Read Sales App state through `@vtex/sales-app` hooks, or fetch data from VTEX and external APIs when needed.

> ℹ️ For business context, extension point locations, and use case examples, see [VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility) on Help Center.
