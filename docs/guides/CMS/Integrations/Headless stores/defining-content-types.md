---
title: "Defining Content Types for Headless stores"
hidden: false
slug: "defining-content-types"
createdAt: "2026-07-24T12:00:00.813Z"
updatedAt: "2026-07-24T12:00:00.813Z"
---

A **Content Type** is the schema template to create page **entries**. In a headless project, you declare each Content Type as an individual `.jsonc` file, combine them into a schema bundle with the [Content plugin](https://developers.vtex.com/docs/guides/content-plugin), and upload the bundle to the Schema Registry.

This guide covers how to define Content Types: where files live, which properties are required, and two annotated examples (minimal and full).

> ℹ️ For modeling concepts (Content Type vs. Component, singleton patterns, recommended page structures), see [Understanding content modeling and architecture for headless stores](https://developers.vtex.com/docs/guides/content-modeling-and-architecture-for-headless-stores).

## Before you begin

* [Understanding content modeling and architecture for headless stores](https://developers.vtex.com/docs/guides/content-modeling-and-architecture-for-headless-stores)  
* [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) installed  
* Component schemas your Content Types reference (for example, `SEO`, `PromoBanner`) are defined under `cms/components/`

## Organizing Content Type files

Each Content Type lives in its own file. The [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) discovers files by prefix and merges them into the `content-types` key of your schema bundle.

### Structuring directories

For headless storefronts, keep Content Type files separate from component schemas:

```md
your-headless-project/
├── cms/
│   ├── components/
│   │   ├── cms_component__SEO.jsonc
│   │   └── cms_component__PromoBanner.jsonc
│   └── pages/
│       ├── cms_content_type__home.jsonc
│       ├── cms_content_type__landingPage.jsonc
│       └── cms_content_type__aboutPage.jsonc
└── src/
    └── …                          # Your storefront implementation
```

You can co-locate Content Type files under `cms/pages/` (shown above) or use another directory; the CLI accepts custom paths as arguments. What matters is the **file prefix**, not the folder name.

### Naming Content Type files

| Rule | Example | Result in schema bundle |
| :---- | :---- | :---- |
| File prefix | `cms_content_type__` | Required. Files without this prefix are ignored. |
| Content Type ID | `cms_content_type__landingPage.jsonc` | Becomes the key `landingPage` under `content-types`. |
| Casing | Use camelCase for the ID segment | `landingPage`, `blogPost`, `globalHeader` |
| Extension | `.jsonc` (recommended) or `.json` | `.jsonc` allows inline comments for documentation. |

> ⚠️ The Content Type ID (the segment after `cms_content_type__`) is what editors see in the CMS Admin and what your storefront uses in Data Plane URLs: `…/{storeId}/landingPage/entries/slug/{slug}`.

### Uploading the schema bundle

> ⚠️ Remember, this step applies only to headless stores. Do not use the \`vtex.headless\` base schema for FastStore stores, as it may remove the default FastStore content types and components from the store schema.

Before uploading the schema, open the generated `schema.json` file and review its contents. Make sure it includes the expected content types, components, and pages for your headless store.

Uploading a schema replaces the current schema configuration for the selected store. Reviewing the file first helps prevent accidentally removing existing content types or components.

Generate and upload the bundle with the headless base schema:

```shell
vtex content generate-schema cms/components cms/pages
  --out schema.json
  --base vtex.headless

vtex content upload-schema schema.json
```

Replace `{storeId}` with your headless store ID when prompted, or pass it with the store flag documented in the [Content plugin](https://developers.vtex.com/docs/guides/content-plugin).

## Declaring required and optional properties

A Content Type schema is a JSON Schema `object` with CMS-specific metadata. The table below lists every property you are likely to use.

### CMS-specific properties

| Property | Required | Description |
| :---- | :---- | :---- |
| `type` | ✅ | Must be `"object"`. |
| `title` | ✅ | Display name in the CMS Admin (for example, `"Landing Page"`). |
| `$singleton` | ✅ | `true` if only one entry is allowed store-wide (`home`); `false` if editors can create many entries. |
| `identifierKeys` | ✅ | Array of field names that identify an entry. Use `[]` for singletons; `["slug"]` for multi-instance pages. |
| `properties` | ✅ | Field and relation definitions for the Content Type. |
| `$extends` | Optional | Inherits structure from a base template (for example, `#/$defs/base-page-template`). |
| `description` | Optional | Help text shown to editors in the Admin. |
| `required` | Optional | Lists top-level fields editors must fill before saving. |

### Common fields inside `properties`

| Field | Typical use | Notes |
| :---- | :---- | :---- |
| `slug` | Multi-instance pages | Use `"ui:widget": "slug"`. Add `"slug"` to `identifierKeys`. |
| `seo` | Fixed SEO block on every entry | Embed with `"$ref": "#/components/SEO"`. |
| `sections` | Dynamic page blocks | Reference `"#/$defs/$ALLOW_ALL_COMPONENTS"` or a restricted `anyOf`. |

> ℹ️ `$ALLOW_ALL_COMPONENTS` is **generated** when you run `vtex content generate-schema`. Reference it in Content Types — do not create it manually in individual files.

### `identifierKeys` and `$singleton`

These two properties work together to control how entries are created and fetched:

| Pattern | `$singleton` | `identifierKeys` | Editor experience | Data Plane lookup |
| :---- | :---- | :---- | :---- | :---- |
| Single page (Home) | `true` | `[]` | One entry, edited in place | By Content Type name |
| Multi-instance page | `false` | `["slug"]` | Many entries, each with a slug | By slug |
| Multi-key identity | `false` | `["slug", "locale"]` | Rare. Only when multiple keys identify an entry | By composite key |

For most headless pages, use either a **singleton with empty `identifierKeys`** or **`identifierKeys: ["slug"]`**.

## Defining a minimal Content Type

The example below defines a singleton **About** page. It has a `sections` array only. No slug, no embedded components. Editors add sections from the components you registered in the bundle.

**File:** `cms/pages/cms_content_type__aboutPage.jsonc`

```jsonc
{
  // Display name in the CMS Admin
  "title": "About Page",

  // Every Content Type must be an object
  "type": "object",

  // Only one About entry for the entire store
  "$singleton": true,

  // No identifier fields — singletons use an empty array
  "identifierKeys": [],

  "properties": {
    "sections": {
      "title": "Page sections",
      // Generated by `generate-schema` — lists all your components
      "$ref": "#/$defs/$ALLOW_ALL_COMPONENTS"
    }
  }
}
```

**What editors get:** a single About entry where they add and reorder sections such as `PromoBanner` or `RichTextBlock`.

**What your storefront does:** fetch the about entry by Content Type name and render each section by `componentKey`.

## Defining a full Content Type with relations and media

The example below defines a multi-instance **Landing Page** Content Type with:

* A **slug** field for routing.
* An embedded **SEO** component (relation via `$ref`).
* A **hero image** field using the media gallery widget.
* A **sections** array for dynamic page blocks

**Prerequisite component**: `cms/components/cms_component__SEO.jsonc`:

```jsonc
{
  "$componentKey": "SEO",
  "$componentTitle": "SEO",
  "type": "object",
  "required": ["title", "description"],
  "properties": {
    "title": {
      "title": "Page title",
      "type": "string"
    },
    "description": {
      "title": "Meta description",
      "type": "string"
    },
    "canonical": {
      "title": "Canonical URL",
      "type": "string"
    }
  }
}
```

**Content Type file**: `cms/pages/cms_content_type__landingPage.jsonc`:

```jsonc
{
  "title": "Landing Page",
  "type": "object",
  "description": "Marketing landing pages with a unique URL slug.",

  // Many landing pages allowed
  "$singleton": false,

  // Slug uniquely identifies each entry
  "identifierKeys": ["slug"],

  // Top-level fields editors must complete
  "required": ["slug"],

  "properties": {
    "slug": {
      "title": "Slug",
      "description": "URL path segment for this page (for example, summer-sale).",
      "type": "string",
      "minLength": 3,
      "widget": {
        "ui:widget": "slug"       // Slug input with / prefix normalization
      }
    },

    "seo": {
      "title": "SEO",
      // Relation: embeds the SEO component on every landing page entry
      "$ref": "#/components/SEO"
    },

    "heroImage": {
      "title": "Hero image",
      "description": "Optional full-width image above the page sections.",
      "type": "string",
      "widget": {
        "ui:widget": "media-gallery",
        "restrictMediaTypes": {
          "image": ["png", "jpeg", "webp"],
          "video": false
        }
      }
    },

    "sections": {
      "title": "Page sections",
      "$ref": "#/$defs/$ALLOW_ALL_COMPONENTS"
    }
  }
}
```

### Understanding relations in this example

| Property | Mechanism | Behavior |
| :---- | :---- | :---- |
| `seo` | `$ref` to `#/components/SEO` | Every entry includes one SEO block with `title`, `description`, and `canonical`. Editors fill it as part of the landing page form. |
| `sections` | `$ref` to `$ALLOW_ALL_COMPONENTS` | Editors add any registered component. Each item in the array includes a `componentKey` at publish time. |
| `heroImage` | `media-gallery` widget | Stores a Media Gallery asset URL as a string. Your storefront renders it in the page layout outside the section loop. |

### Reviewing the published entry shape

After editors save and publish, the Data Plane returns content shaped by this schema:

```json
{
  "componentKey": "landingPage",
  "slug": "summer-sale",
  "seo": {
    "componentKey": "SEO",
    "title": "Summer Sale",
    "description": "Our biggest sale of the season.",
    "canonical": "/summer-sale"
  },
  "heroImage": "https://content.vtexassets.com/assets/…",
  "sections": [
    {
      "componentKey": "PromoBanner",
      "title": "Up to 50% off"
    }
  ]
}
```

Your storefront maps `landingPage` to its page template, reads `slug` for routing, and renders `seo`, `heroImage`, and each item in `sections`.

## Related resources

<Flex\>

<WhatsNextCard  
  linkTo="https://developers.vtex.com/docs/guides/content-modeling-and-architecture-for-headless-stores"  
  title="Understanding content modeling and architecture for headless stores"  
  description="Review modeling concepts, design principles, and recommended page patterns."  
  linkTitle="See more"  
\>

<WhatsNextCard  
  linkTo="https://developers.vtex.com/docs/guides/content-plugin"  
  title="Content plugin"  
  description="Generate and upload schema bundles for your headless store."  
  linkTitle="See more"  
\>

</Flex\>
