---
title: "Comparing (legacy) and CMS features"
hidden: false
slug: "comparing-headless-cms-and-cms-features"
createdAt: "2026-01-26T12:50:00.813Z"
updatedAt: "2026-02-02T12:50:00.813Z"
---

Before diving into the technical details, it's important to understand the high-level differences between the CMS and Headless CMS (legacy):

- [Content modeling](#content-modeling): How content schemas are defined and structured, including Content Types, components, and capabilities such as referencing and extension.  
- [Content editing and publishing](#content-editing-and-publishing): The authoring experience for content editors, including the CMS interface in the Admin, search capabilities, and content lifecycle management.  
- [Localization and multi-language support](#localization-and-multi-language-support): Capabilities for content localization, including locale management and language fallback rules.
- [Media and asset management](#media-and-asset-management): Capabilities for media management, including image and video support.
- [Storefront integration](#storefront-integration): Supported frameworks and storefront technologies.
- [Development tools and permissions](#development-tools-and-permissions): CLI tools and access control mechanisms.
- [Technical infrastructure and development tools](#technical-infrastructure-and-development-tools): Architecture and platform dependencies, including APIs, data storage, and build mechanisms.

## Content modeling

Content modeling defines how content is structured and reused across your storefront. Both content management platforms use [JSON Schema](https://json-schema.org/) as the underlying technology, but the CMS introduces schema reusability and content relationships, allowing the same content to be reused across multiple pages or components without duplication.

| Feature | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Content Types** | ✅ | ✅ |
| **Components** | ✅ | ✅ |
| **Schema technology** | JSON Schema | JSON Schema |
| **Content referencing** | ❌ | ✅ |
| **Schema extension** | ❌ | ✅ |

- **Content Types**: Define the page structures in a store (e.g., `home`, `pdp`, `plp`, `landingPage`). Both content management platforms support creating and managing Content Types, but the CMS stores them in individual `.jsonc` files, rather than in a single `content-types.json` file.  

- **Components**: Define the building blocks of pages. Both content management platforms support component definitions, but the CMS uses individual `.jsonc` files with enhanced metadata like `$componentKey` and `$componentTitle`.  

- **Schema technology**: Both content management platforms use [JSON Schema](https://json-schema.org/) as the technology for defining content structure and validation rules. This ensures compatibility and allows you to reuse existing schema knowledge.  

- **Content referencing**: The CMS allows content entries to reference other entries, enabling reusable content blocks across multiple pages. For example, a "Footer" component can be defined once and referenced by multiple pages. In Headless CMS (legacy), each page's content is isolated and must be duplicated if reused.  

- **Schema extension**: While Headless CMS (legacy) supports basic schema definitions, the CMS introduces the `$extends` keyword for schema inheritance. Components can inherit properties from base schemas (e.g., `#/$defs/base-component`). This reduces duplication, makes shared fields easier to maintain, and helps ensure consistent structure across components.

## Content editing and publishing

Content editing capabilities determine how content editors interact with the CMS interface.

| Feature | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Content management (Admin)** | ✅ | ✅ |
| **Content search and filtering** | ✅ | ✅ |
| **Entry (CRUD)** | ✅ | ✅ |
| **AI content generation** | ❌ | ✅ |
| **Versioning** | ✅ | ✅ |
| **Branching workflow** | ❌ | ✅ Git-like branching |
| **Version history** | ❌ | ✅ Git-like branching |
| **Visual preview** | ✅ FastStore | ✅ FastStore |
| **Branch preview** | ❌ | ✅ FastStore |
| **Scheduled publishing** | ✅ | ✅ |
| **Multi-user awareness** | ❌ | ✅ |
| **Content grouping (Projects and Stores)** | ✅ | ✅ |
| **Content approval workflow** | ❌ | ✅ Versioning and Roles |

- **Content management (Admin)**: Both content management platforms provide a full-featured admin interface for creating, editing, and publishing content. The CMS uses a modern React/Next.js stack with improved performance, better accessibility, and a more intuitive user experience. Content editors can manage entries, preview changes, and publish content through a visual interface.  

- **Content search and filtering**: Both content management platforms support searching and filtering content entries by name, Content Type, and other attributes. The CMS enhances this with slug-based indexing, enabling faster lookups when retrieving content by URL path (e.g., `/summer-sale`).  

- **Entry (CRUD)**: Both content management platforms support full Create, Read, Update, and Delete operations for content entries. The CMS adds branching capabilities, allowing changes to be made on separate branches before merging to production.

- **AI content generation**: The CMS integrates with AI services to help content editors generate and improve content directly within the editing interface, such as product descriptions, marketing copy, and other text content.

- **Versioning**: Both platforms support content versioning, allowing editors to track changes over time. The CMS extends versioning capabilities with Git-like branching, providing more granular control over content revisions and the ability to work on multiple versions simultaneously.

- **Branching workflow**: The CMS introduces Git-like branching for content changes. Content editors can create branches in the Admin, make changes, preview them, and merge to publish, similar to how developers work with code. This workflow enables:

  - **Safer content updates**: Changes are isolated on branches until ready to publish.  
  - **Collaboration**: Multiple editors can work on different branches simultaneously.  
  - **Preview before publish (FastStore only)**: Full preview of changes before they go live.  
  - **Rollback capability**: If something goes wrong, previous versions are preserved.

- **Version history**: The CMS maintains a complete history of all content changes through its branching model. Editors can view previous versions, compare changes between branches, and restore earlier versions if needed.

- **Visual preview**: Both platforms support visual preview for FastStore storefront, allowing content editors to see how their changes will appear on the live store before publishing. Preview is available through a configured preview URL that renders content in the actual storefront context.

- **Branch preview**: The CMS supports branch-level preview, enabling editors to preview all content changes within a specific branch as a cohesive experience. This allows testing of multiple related changes together before merging, ensuring consistency across related content updates.

- **Scheduled publishing**: Both platforms support scheduling content to be published at a future date and time. In the CMS, scheduled publishing is modeled as scheduled branch merges, allowing editors to prepare content in advance and automate its release.

- **Multi-user awareness**: The CMS provides features that show when multiple users are editing the same content, helping prevent conflicts and facilitating team collaboration.

- **Content grouping (Projects and Stores)**: Both platforms allow organizing content by projects (Headless CMS) and Stores (CMS), enabling multi-store and multi-brand content management within a single account.

- **Content approval workflow**: The CMS supports content approval workflows through its versioning and role-based permission system. Editors can submit content for review, and approvers can review changes on branches before they are merged and published.

## Localization and multi-language support

Localization capabilities determine how content is adapted for different languages and regions. The CMS provides multi-language support with locale management, fallback rules, and character encoding for international content.

| Feature | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Locales** | ❌ | ✅ |
| **Default and automatic language fallback rules** | ❌ | ✅ |
| **Language character encoding support** | ❌ | ✅ |
| **Language direction support** | ❌ | ✅ |

- **Locales**: The CMS supports defining and managing multiple locales, allowing content to be created and maintained in different language and region combinations (e.g., `en-US`, `pt-BR`, `es-MX`). Content editors can manage translations for each locale directly within the Admin interface.

- **Default and automatic language fallback rules**: The CMS allows configuring fallback rules that determine which content to display when a specific locale's content is not available. For example, if content is missing for `pt-BR`, the system can automatically fall back to `pt` or `en`. This ensures users always see relevant content even when translations are incomplete.

- **Language character encoding support**: The CMS uses UTF-8 encoding, supporting characters from all languages including Latin, Cyrillic, Greek, and other scripts. This ensures proper display of international content, special characters, and symbols across all supported languages.

- **Language direction support**: The CMS currently supports left-to-right (LTR) text direction, which covers most Western languages and many others. This ensures proper text alignment and layout for content in supported languages.

## Media and asset management

Media management capabilities define how images, videos, and other assets are stored, organized, and used across content. Both platforms provide media galleries with support for common image formats and external video embedding.

| Feature | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Media Gallery** | ✅ | ✅ |
| **Image support** | ✅ PNG, JPG, JPEG, GIF, SVG, and WebP | ✅ PNG, JPG, JPEG, GIF, SVG, and WebP |
| **Video support** | ✅ External URL only | ✅ External URL only |

- **Media Gallery**: Both platforms provide media management capabilities through a centralized gallery interface. Content editors can upload, organize, and reuse media assets across multiple entries.

  - **Image and video support**: Upload images (PNG, JPG, JPEG, GIF, SVG, and WebP) or embed videos from YouTube, Vimeo, or cloud services.  
  - **Centralized asset management**: All media assets are stored in a central gallery, making them reusable across multiple entries.

- **Image support**: Both platforms support common image formats including PNG, JPG, JPEG, GIF, SVG, and WebP. Images can be uploaded directly to the media gallery and inserted into content through a visual picker interface.

- **Video support**: Both platforms support embedding videos from external sources such as YouTube, Vimeo, and other video hosting services. Videos are referenced by URL rather than uploaded directly to the CMS.

## Storefront integration

Storefront integration capabilities determine which frontend frameworks and technologies can consume content from the CMS.

| Feature | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Headless** | ✅ | ⚒️ *Coming soon* |
| **Store Framework** | ❌ | ❌ |
| **FastStore v1 and v2** | ✅ | ❌ |
| **FastStore v3 and v4** | ✅ | ✅ |

## Development tools and permissions

Development tools and access controls determine how developers work with the CMS and how user permissions are managed. Both platforms provide CLI tools for schema management and support access permissions, with the CMS adding role-based permission controls.

| Aspect | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **Developer CLI** | ✅ | ✅ |
| **Access permissions** | ✅ | ✅ |
| **Role-based permissions** | ❌ | ✅ |
| **IO workspace compatibility** | Code-only | Code-only |
| **Sub-account inheritance** | ❌ | ❌ |

- **Developer CLI**: Both platforms provide command-line tools for managing content schemas. Headless CMS (legacy) uses the `yarn cms sync` command for syncing schemas, while the CMS introduces the VTEX Content CLI (`@vtex/cli-plugin-content`).

- **Access permissions**: Both platforms support controlling who can access and manage content. Access permissions can be configured to restrict content management capabilities to authorized users.

- **Role-based permissions**: The CMS supports role-based access control (RBAC), allowing administrators to define granular permissions based on user roles. This enables different permission levels for content editors, reviewers, and administrators. Headless CMS (legacy) does not include built-in role-based permission controls.

- **IO workspace compatibility**: Both platforms support code-only workspace compatibility for VTEX IO. Content definitions and schemas are managed through code repositories rather than through IO workspaces.

- **Sub-account inheritance**: Neither platform currently supports automatic inheritance of content or schemas from parent accounts to sub-accounts. Content must be managed separately for each account.

## Technical infrastructure and development tools

Technical infrastructure describes the architectural components and design patterns of the CMS and Headless CMS (legacy), including differences in APIs, event handling, caching, and system architecture.

| Aspect | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **API type** | REST | REST |
| **Build triggers** | Direct webhooks | Event-driven |
| **Caching** | Limited | ETag support |
| **Architecture pattern** | Monolithic | CQRS (Control/Data Plane) |

- **API type**: Both platforms expose REST APIs for content retrieval.

- **Build triggers**: Headless CMS (legacy) triggers builds via direct HTTP webhooks that may fail silently. The CMS uses an event-driven architecture, providing built-in retries and dead-letter queues for reliability. When a branch is merged, the Control Plane emits integration events that downstream systems consume to trigger builds and deployments.

- **Caching**: The CMS Data Plane API supports ETag-based caching, allowing efficient cache validation and reduced bandwidth.

- **Architecture pattern**: The CMS follows CQRS (Command Query Responsibility Segregation), separating content management from content delivery for independent scaling and optimization.
