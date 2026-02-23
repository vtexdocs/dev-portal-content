---
title: "CMS overview"
hidden: false
slug: "cms-overview"
createdAt: "2026-01-26T12:50:00.813Z"
updatedAt: "2026-02-19T11:48:00.813Z"
---

> ⚠️ For information about the legacy version of this CMS, see the [Headless CMS (legacy)](https://developers.vtex.com/docs/guides/faststore/headless-cms-overview) track.

The CMS is a VTEX content management system for defining, storing, and delivering storefront content. It currently supports FastStore storefronts, with planned support for headless storefronts. It provides a structured approach to content modeling, collaborative editing, and reliable distribution, supporting both editorial teams and developers working on large-scale commerce experiences.

The system follows a decoupled architecture that separates content authoring from content consumption. This separation allows content management workflows and content delivery workloads to evolve and scale independently.

> ⚠️ The CMS is currently available only for FastStore storefronts.

## Technical overview

| Aspect | Description |
| :---- | :---- |
| **Performance** | Read-optimized data access for content consumption during storefront builds. |
| **Reliability** | Event-driven architecture with message queues ensuring no content updates are lost. |
| **Scalability** | Independent scaling of content authoring (write) and content delivery (read) workloads, enabled by a command-query separation (CQRS) model. |
| **Developer experience** | Schema-first configuration, CLI-based operations, and compatibility with source control systems. |
| **Collaboration** | Git-like branching workflows, multi-user awareness, and content approval processes. |
| **Localization** | Built-in support for multiple locales with automatic language fallback rules. |

## Main features

### Content modeling

Define content structures using [JSON Schema](https://json-schema.org/) with support for:

- **Content Types**: Page structures like `home`, `pdp`, `plp`, and `landingPage`.
- **Components**: Reusable building blocks with metadata like `$componentKey` and `$componentTitle`.
- **Content referencing**: Reference entries across multiple pages without duplication.
- **Schema extension**: Inherit properties from base schemas using the `$extends` keyword.

### Content editing

Manage content through the VTEX Admin with:

- **AI content generation**: Generate and improve content with integrated AI services.
- **Branching workflow**: Create isolated branches, preview changes, and merge to publish.
- **Version history**: Track changes, compare versions, and restore previous content.
- **Multi-user awareness**: See when others are editing the same content.
- **Scheduled publishing**: Schedule content to go live at specific dates and times.

### Media management

Organize and reuse media assets with:

- **Media Gallery**: Central repository for images and video references.
- **Image formats**: PNG, JPG, JPEG, GIF, SVG, and WebP.
- **Video embedding**: Reference videos from YouTube, Vimeo, and other services.

### Developer tools

Build and manage schemas with:

- [**VTEX Content CLI**](/TBD): Commands for schema generation, splitting, and uploading (`@vtex/cli-plugin-content`).
- **Modular schemas**: Individual `.jsonc` files for components and Content Types.
- **Role-based permissions**: Granular access control for editors, reviewers, and administrators.

## Next steps

<Flex>

<WhatsNextCard
  linkTo="/TBD"
  title="FastStore integration"
  description="Learn how to connect the CMS with FastStore"
  linkTitle="See more"
/>

<WhatsNextCard
  linkTo="/TBD"
  title="Upgrading from Headless CMS (legacy) to CMS"
  description="Learn about the architectural and code-level changes when migrating from Headless CMS (legacy) to the CMS."
  linkTitle="See more"
/>

</Flex>
