---
title: "CMS overview"
hidden: false
slug: "cms-overview"
createdAt: "2026-01-26T12:50:00.813Z"
updatedAt: "2026-01-28T12:50:00.813Z"
---

The CMS is the VTEX content management system designed to provide a set of tools for managing storefront content. It enables teams to create, collaborate on, and distribute content while offering a modern architecture optimized for performance and reliability.

The CMS introduces the following improvements:

| Benefit | Description |
| :---- | :---- |
| **Performance** | Dedicated read-optimized Data Plane for faster content delivery during store builds. |
| **Reliability** | Event-driven architecture with message queues ensuring no content updates are lost. |
| **Scalability** | Independent scaling of content management and content delivery through CQRS architecture. |
| **Developer experience** | Modular schema files, improved CLI tooling, and better alignment with version control workflows. |
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

- **VTEX Content CLI**: Commands for schema generation, splitting, and uploading (`@vtex/cli-plugin-content`).
- **Modular schemas**: Individual `.jsonc` files for components and Content Types.
- **Role-based permissions**: Granular access control for editors, reviewers, and administrators.

## Next steps

<Flex>

<WhatsNextCard
  linkTo="upgrading-from-headless-cms-to-cms"
  title="Upgrading from Headless CMS to CMS"
  description="Learn about the architectural and code-level changes when migrating from Headless CMS to the CMS."
  linkTitle="See more"
/>

<WhatsNextCard
  linkTo="comparing-headless-cms-and-cms-features"
  title="Comparing Headless CMS and CMS features"
  description="Detailed comparison of features between Headless CMS and the CMS."
  linkTitle="See more"
/>

</Flex>
