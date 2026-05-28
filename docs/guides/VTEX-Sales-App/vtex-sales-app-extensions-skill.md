---
title: "VTEX Sales App Extensions Skill"
slug: "vtex-sales-app-extensions-skill"
hidden: false
createdAt: "2026-05-22T19:00:00.000Z"
updatedAt: "2026-05-22T19:00:00.000Z"
excerpt: "Learn about the AI skill that supports you during the development lifecycle of VTEX Sales App extensions."
hidePaginationPrevious: false
hidePaginationNext: false
---

[<i class="fa-brands fa-github"></i> Source code](https://github.com/vtex/skills)

> ℹ️ This feature is in beta, and we're actively working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

VTEX Sales App Extensions Skill is an AI-powered skill with embedded knowledge of [Sales App](https://help.vtex.com/docs/tracks/vtex-sales-app-getting-started-and-setting-up) and [FastStore monorepo](https://developers.vtex.com/docs/guides/faststore/monorepo-overview). It supports you throughout the development lifecycle of extensions, known as [VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility).

In the [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) collection, the VTEX Sales App Extension Skill is identified as `sales-app-extensibility`.

> ℹ️ For business context, extension point locations, and use case examples, see the article [VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/vtex-sales-app-extensibility). For technical information, see our [developer extensibility documentation](link).

The VTEX Sales App Extensions Skill is identified as the `sales-app-extensibility` skill that's part of the [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) collection.

## When Extensions Skill applies

Use this skill when building, customizing, or deploying extensions for Sales App, such as when:

- ✅ Adding features to the cart page (promotions, loyalty, services).
- ✅ Adding features to the Product Detail Pages (badges, recommendations, warranties).
- ✅ Adding features to the menu (user profile, navigation, metrics).
- ✅ Integrating external APIs into Sales App extensions.
- ✅ Generating, scaffolding, or validating extension code for Sales App.

Don't use this skill for:

- ❌ Regular FastStore storefront customization. Use the `faststore-storefront` skill instead.
- ❌ Building VTEX IO apps. Use the `vtex-io-*` skills instead.
- ❌ Sales App core development or framework modifications.

## Skill lifecycle coverage

You can install the Extensions Skill before you start an extensibility project so your AI coding assistant can follow Sales App patterns, and established hooks.

The Extensions Skill supports every stage from setup to production, and follows a seven-step workflow:

| Step | What the skill does |
| :--- | :--- |
| Check prerequisites | Checks whether the project prerequisites defined in the [extensibility technical documentation](link) are satisfied before proceeding with the workflow. If any prerequisite is missing, the workflow provides the required commands for manual execution and waits for confirmation before moving to the next step. |
| Discovery | Understands what you want to build. |
| Requirements & Plan | Maps requirements and generates an implementation plan. Helps delimit project scope—what to build, which extension point to use, and whether the project involves VTEX IO apps, external integrations, or UX changes. |
| Code generation and validation | Generates extension code using Sales App hooks and platform patterns, keeping UX consistent with ecommerce when the feature already exists online. Reviews requirements for gaps or ambiguities in user flows, integrations, or technical details, and prompts for missing information. |
| Documentation | Generates `docs/<ExtensionName>.md` to document the extension. |
| Local testing | Provides development commands and URLs to test the extension locally. |
| Build and deploy | Guides you through local previews, builds, and deployment to production, including validation before release. |

## Extensions Skill installation

Since the `sales-app-extensibility` skill is part of the [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) collection, the complete information about the installation is available in the [VTEX Skills source code](https://github.com/vtex/skills).

> ℹ️ For technical information about VTEX Sales App Extensibility, see our [developer documentation](link).
