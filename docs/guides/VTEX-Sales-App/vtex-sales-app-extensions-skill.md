---
title: "VTEX Sales App Extensions Skill"
slug: "vtex-sales-app-extensions-skill"
hidden: false
createdAt: "2026-05-18T19:00:00.000Z"
updatedAt: "2026-05-18T19:00:00.000Z"
excerpt: "Learn about the AI skill that supports you during the development lifecycle of VTEX Sales App extensions."
hidePaginationPrevious: false
hidePaginationNext: false
---

[<i class="fa-brands fa-github"></i> Source code](https://github.com/vtex/skills)

> ℹ️ This feature is in beta, and we are actively working to improve it. If you have any questions, please contact our [Support](https://help.vtex.com/en/support).

[VTEX Sales App Extensibility](https://help.vtex.com/en/tutorial/extensibility-in-vtex-sales-app) is a native capability that lets stores extend the default in-store sales journey. For example, by integrating external APIs, connecting VTEX solutions outside the standard flow, or centralizing seller tasks in one app. Extensions run at seven extension points across the cart and checkout, menu, side drawer, and product detail page (PDP).

The **VTEX Sales App Extensions Skill** is an AI-powered skill with embedded knowledge of [VTEX Sales App](https://help.vtex.com/en/tracks/vtex-sales-app-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc) and [FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore). You can install it before you start an extensibility project so your AI coding assistant can follow Sales App patterns, extension point specifications, and established hooks instead of generic web defaults.

## Full lifecycle coverage

The skill mirrors the implementation workflow for Sales App extensions described in the [extensibility tutorial](https://help.vtex.com/en/tutorial/extensibility-in-vtex-sales-app) and supports every stage from setup to production.

| Phase | What the skill does |
| :--- | :--- |
| **Install** | Sets up your environment, validates dependencies, and resolves setup issues before development. |
| **Define** | Helps delimit project scope—what to build, which extension point to use, and whether the project involves VTEX IO apps, external integrations, or UX changes. |
| **Analysis** | Reviews requirements for gaps or ambiguities in user flows, integrations, or technical details, and prompts for missing information. |
| **Plan** | Produces an implementation plan aligned with Sales App capabilities and validates feasibility against extension point specifications. |
| **Code** | Generates extension code using Sales App hooks and platform patterns, keeping UX consistent with ecommerce when the feature already exists online. |
| **Deploy** | Guides you through local previews, builds, and deployment to production, including validation before release. |

## When to use the skill

Use the Extensions Skill during **definition** and **implementation**, as recommended in the extensibility tutorial:

1. **Plan project scope** — Clarify what the extension should deliver and where it fits in the sales journey.
2. **Map UX and technical requirements** — Detail user flows, UI behavior, and how the extension connects to Checkout, Catalog, Inventory, or external systems.
3. **Check technical feasibility** — Confirm that mapped requirements are supported by the target extension points before coding.
4. **Implement and validate** — Build the extension, test locally, then deploy for store users.

For business context, extension point locations, security goals, and use case examples, see [Extensibility in VTEX Sales App](https://help.vtex.com/en/tutorial/extensibility-in-vtex-sales-app). For technical specifications and API details, follow the [developer extensibility documentation](link).
