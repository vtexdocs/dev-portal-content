---
title: "Sales App extensions implementation"
slug: "sales-app-extensions-implementation"
excerpt: "Overview of how to implement, deploy, and reference VTEX Sales App extensions."
hidden: false
createdAt: "2026-05-27T17:17:40.610Z"
updatedAt: "2026-05-27T17:32:46.010Z"
---

> ⚠️ This feature is in beta, and we're working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

[VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility) lets you extend the default assisted-sales journey with capabilities aligned to your business model, such as external integrations and VTEX data. Follow the articles below to implement, deploy, and reference VTEX Sales App extensions:

- [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points) — Explore predefined slots in the Sales App UI (cart, PDP, menu), the hooks available at each point, and layout-shift guidance.

- [Setting up extensions for VTEX Sales App](https://developers.vtex.com/docs/guides/setting-up-extensions-for-vtex-sales-app) — Add `@vtex/sales-app` to your FastStore monorepo, create a `sales-app` project with the FSP CLI, register the workspace, and preview locally.

- [Installing WebOps for Sales App extensions](https://developers.vtex.com/docs/guides/installing-webops-for-sales-app-extensions) — Install and configure FastStore WebOps in your VTEX account and GitHub repository so the `sales-app` module can be built and deployed.

- [Creating a VTEX Sales App extension](https://developers.vtex.com/docs/guides/creating-a-vtex-sales-app-extension) — Build a React component, register it with `defineExtensions`, and optionally style it with CSS and `useSettings`.

- [Deploying VTEX Sales App extensions](https://developers.vtex.com/docs/guides/deploying-vtex-sales-app-extensions) — Push to your production branch to trigger a WebOps build of the `sales-app` module, and troubleshoot failures with GitHub Checks or `fsp build`.

- [API Reference](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-api-reference) — Consult hooks, `defineExtensions`, and types from `@vtex/sales-app` (for example, `useCart`, `usePDP`, and `useExtension`) to interact with the Sales App data layer.

> ℹ️ Use the [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill) (`sales-app-extensibility`) with your AI coding assistant when building, customizing, or deploying extensions. Install it from the [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) collection.

## Additional resources

- [CSS styling in VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/css-styling-in-vtex-sales-app-extensibility)
- [Data layer and data fetching in VTEX Sales App Extensibility](https://developers.vtex.com/docs/guides/data-layer-and-data-fetching-in-vtex-sales-app-extensibility)
- [VTEX Sales App Extensions Skill](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill)
- [VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility)
