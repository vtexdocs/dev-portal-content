---
title: "Understanding CMS architecture and schema declarations"
hidden: false
slug: "architecture-schema-declarations"
createdAt: "2026-01-26T12:50:00.813Z"
updatedAt: "2026-02-23T09:00:00.813Z"
excerpt: "Learn how the CMS separates read and write operations with CQRS, defines component schemas using modular files, and organizes project folders differently from the Headless CMS (legacy)."
---

The CMS is built on the **CQRS (Command Query Responsibility Segregation)** architectural pattern, which separates read operations (queries) from write operations (commands) into different models or services.

With CQRS, content editors get a responsive editing experience while your store gets fast content delivery, without either affecting the other, covering the following aspects:

- **Performance under load**: Read and write operations scale independently.  
- **Optimization trade-offs**: Each plane is optimized for its specific purpose.  
- **Reliability**: Failures in one plane don't affect the other.
- **Technology choices**: Best technology for each plane's requirements.

## Data Plane (Content Delivery)

The Data Plane is optimized for high-performance content delivery to storefronts and has the following key characteristics:

- **Read-only**: Only serves published content, no write operations.  
- **ETag caching**: Supports efficient cache validation.  
- **Slug-based lookups**: Retrieve content by URL path.  
- **Context filtering**: Filter content by locale or other contexts.

| Component | Purpose |
| :---- | :---- |
| **Data Plane API** | Read-only RESTful API optimized for fast content retrieval. |
| **Database** | Stores published content in a format optimized for queries. |

## Schema Registry

The Schema Registry manages component schemas and Content Type definitions and has the following key operations:

- Upload and store schema bundles.  
- Validate content against schemas.  
- Provide schema definitions to CMS interface for form rendering.

| Component | Purpose |
| :---- | :---- |
| **CLI Plugin** | Command-line tool for generating and uploading schemas. |
| **Registry API** | Stores and serves schema definitions. |
| **Schema Store** | Persists schema versions and metadata. |

## Content data management through the architecture

1. **Schema upload** (development time):  
   - Developer runs `vtex content upload-schema`.  
   - CLI sends schema to Schema Registry API.  
   - Schema is stored and made available to Control Plane and Data Plane.

2. **Content editing** (authoring time):  
   - Editor creates/edits content in the CMS Admin interface.  
   - CMS interface (Admin UI) calls Control Plane API.  
   - Content is saved to Control Plane database.  
   - Changes are isolated on a branch until merged.

3. **Content publishing** (publish time):  

   - Editor merges branch to main.  
   - Event triggers sync to Data Plane and build webhook.

4. **Content delivery** (runtime):  

   - Content is fetched from the Data Plane API.
   - Data Plane returns published content with ETag headers.

## Schema declarations

Schemas define the structure of content in the CMS. They specify which fields a section exposes, the data types those fields accept, and the validation rules that apply.

When a content editor creates or edits content in the CMS interface in the Admin, schemas are used to:

- **Render the editing form**: Each field in the schema becomes an input field in the interface.  
- **Validate content**: Ensure required fields are filled, and data types are correct.  
- **Define relationships**: Schemas determine which sections can be used within specific Content Types.

Both the Headless CMS (legacy) and the CMS rely on [JSON Schema](https://json-schema.org/) to define schemas. However, they differ in how schemas are organized, authored, and deployed.

### Schema declarations between CMS and Headless CMS (legacy)

The table below summarizes the key differences between schema declarations in the Headless CMS (legacy) and the CMS:

| Aspect | Headless CMS (legacy) | CMS |
| :---- | :---- | :---- |
| **File organization** | Single `sections.json` file. | Individual `.jsonc` files per component. |
| **Section identifier** | `name` field. | `$componentKey` field. |
| **Display name** | `schema.title` | `$componentTitle` field. |
| **Inheritance** | Not supported. | `$extends` for schema inheritance. |
| **Base component** | N/A | Extends `#/$defs/base-component`. |
| **Image widget** | `"ui:widget": "image-uploader"` | `"ui:widget": "media-gallery"` |
| **File extension** | `.json` | `.json` or `.jsonc` |
| **Deployment** | Synced via `vtex cms sync`. | Uploaded via `vtex content upload-schema`. |

### Schema format comparison

To understand the practical differences, let's compare how the same Banner component is defined in the CMS and the Headless CMS (legacy).

#### Headless CMS (legacy) format

In the Headless CMS (legacy), all sections are defined in a single `sections.json` file. Each section has a `name` and a nested `schema` object.

- All components are defined in a single array within one file.  
- Component identified by the `name` field.  
- Display name comes from `schema.title`.  
- No inheritance between components.

```json
// sections.json (single file with all sections)
[
  {
    "name": "Banner",
    "schema": {
      "title": "Banner",
      "description": "A banner component for the storefront",
      "type": "object",
      "required": ["title"],
      "properties": {
        "title": {
          "title": "Title",
          "type": "string"
        },
        "image": {
          "type": "object",
          "title": "Image",
          "properties": {
            "src": {
              "type": "string",
              "title": "Image",
              "widget": {
                "ui:widget": "image-uploader"
              }
            },
            "alt": {
              "type": "string",
              "title": "Alternative Label"
            }
          }
        }
      }
    }
  }
  // ... all other sections in the same file
]
```

#### CMS schema format

In the CMS, each component is defined in its own `.jsonc` file. The schema is flatter and includes additional metadata fields for identification, display, and inheritance.

- Each component in its own file (`cms_component__ComponentName.jsonc`).  
- Component identified by `$componentKey` field.  
- Display name specified by `$componentTitle`.  
- Inherits from base schema via `$extends`.

```jsonc
// cms/components/cms_component__Banner.jsonc
{
  "$extends": ["#/$defs/base-component"],
  "$componentKey": "Banner",
  "$componentTitle": "Banner",
  "type": "object",
  "required": ["title"],
  "properties": {
    "title": {
      "title": "Title",
      "type": "string"
    },
    "image": {
      "type": "object",
      "title": "Image",
      "properties": {
        "src": {
          "type": "string",
          "title": "Image",
          "widget": {
            "ui:widget": "media-gallery"
          }
        },
        "alt": {
          "type": "string",
          "title": "Alternative Label"
        }
      }
    }
  }
}
```

### CMS schema keywords

The CMS introduces additional schema keywords for a more modular, reusable, and maintainable schema definition.

| Keyword | Purpose | Example |
| :---- | :---- | :---- |
| `$extends` | Inherit properties from base schemas. | `"$extends": ["#/$defs/base-component"]` |
| `$componentKey` | Unique identifier for the component. | `"$componentKey": "Banner"` |
| `$componentTitle` | Display name shown in CMS interface. | `"$componentTitle": "Promotional Banner"` |
| [`$ref`](https://json-schema.org/understanding-json-schema/structuring#dollarref) | Reference another schema definition. | `"$ref": "#/components/SEO"` |

> ℹ️ For standard JSON Schema terms, see the [JSON Schema keywords](https://json-schema.org/understanding-json-schema/keywords) reference.

#### Schema inheritance with `$extends`

The `$extends` property allows sections to inherit properties from one or more base schemas, promoting code reuse and consistency. Schema inheritance provides benefits for content modeling, including:

- **Consistency** through a shared base structure across components.  
- **Maintainability** by propagating changes from base schemas.  
- **Reusability** via domain-specific base schemas (for example, promotional or navigational components).  
- **Type safety** through schema-compatibility validation.

**Example: Inheriting from multiple schemas**

```jsonc
{
  "$extends": [
    "#/$defs/base-component",
    "#/components/PromoBase"
  ],
  "$componentKey": "PromoBanner",
  "$componentTitle": "Promotional Banner",
  "properties": {
    // Inherits: id, name, description, data (from base-component)
    // Inherits: startDate, endDate (from PromoBase)
    "discountPercentage": {
      "title": "Discount Percentage",
      "type": "number"
    }
  }
}
```

## Folder structure

The CMS introduces a modular folder structure that aligns with modern development practices. Instead of consolidating all schemas into a single file, the new structure separates components and Content Types into individual files, making it easier to manage, review, and version-control your content definitions.

The shift from monolithic files, as in the Headless CMS (legacy), to individual files addresses the following issues:

- **Version control conflicts**: With a single `sections.json` file, multiple developers editing different components often caused merge conflicts. Individual files mean each component can be edited independently.  
- **Code review clarity**: Reviewing changes to a single component is straightforward when each component has its own file, rather than searching through a large JSON array.  
- **Maintainability**: Finding and updating a specific component is faster when you can navigate directly to `cms_component__Banner.jsonc` instead of scrolling through hundreds of lines in `sections.json`.  
- **Comments and documentation**: The `.jsonc` format allows inline comments, enabling developers to document schema decisions directly in the file.

### Headless CMS (legacy) folder structure

In the Headless CMS (legacy), all schema definitions are consolidated into two main files within a subdirectory, for example, `faststore`:

```sh
your-faststore-project/
├── cms/
│   └── faststore/
│       ├── sections.json       # All component schemas in one file
│       └── content-types.json  # All Content Type definitions
├── src/
│   └── components/
│       ├── Banner/
│       │   └── Banner.tsx
│       └── ProductShelf/
│           └── ProductShelf.tsx
└── ...
```

### CMS folder structure

The CMS organizes schemas into individual files. Below are two common approaches:

**Option 1: Centralized schemas**

Keep component schemas in a dedicated `cms/components/` directory:

```sh
your-store/
├── cms/
│   ├── components/                              # Individual component schemas
│   │   ├── cms_component__Banner.jsonc
│   │   ├── cms_component__MegaMenu.jsonc
│   │   ├── cms_component__ProductShelf.jsonc
│   │   └── cms_component__RecommendationShelf.jsonc
│   └── pages/                                   # Content type definitions
│       ├── cms_content_type__landingPage.jsonc
│       ├── cms_content_type__home.jsonc
│       └── cms_content_type__pdp.jsonc
├── src/
│   └── components/
│       ├── Banner/
│       │   └── Banner.tsx
│       └── ProductShelf/
│           └── ProductShelf.tsx
└── ...
```

**Option 2: Co-located schemas**

Place component schemas alongside their implementation files:

```sh
your-store/
├── cms/
│   └── pages/                                   # Content type definitions
│       ├── cms_content_type__landingPage.jsonc
│       ├── cms_content_type__home.jsonc
│       └── cms_content_type__pdp.jsonc
├── src/
│   └── components/
│       ├── Banner/
│       │   ├── Banner.tsx
│       │   └── cms_component__Banner.jsonc      # Schema co-located with component
│       └── ProductShelf/
│           ├── ProductShelf.tsx
│           └── cms_component__ProductShelf.jsonc # Schema co-located with component
└── ...
```

#### File naming conventions

The CMS uses a consistent naming pattern that makes file purposes immediately clear:

| Item | Headless CMS (legacy) | CMS |
|------|------|---------|
| **Component schemas** | All in `sections.json` | `cms_component__ComponentName.jsonc` |
| **Content types** | All in `content-types.json` | `cms_content_type__typeName.jsonc` |
| **File extension** | `.json` | `.jsonc` (allows comments) |
| **Location** | `cms/faststore/` | `cms/components/` and `cms/pages/`, or co-located with component code |
