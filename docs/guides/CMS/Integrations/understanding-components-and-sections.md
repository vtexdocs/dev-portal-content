---
title: "Understanding components and sections"
hidden: false
slug: "understanding-components-and-sections"
createdAt: "2026-05-04T12:00:00.813Z"
updatedAt: "2026-05-05T18:00:00.813Z"
excerpt: "Understand what components and sections are in the CMS, how they differ, and how they work together to build pages in storefronts integrated with the CMS."
---

**Components** and **Sections** are the building blocks that editors and developers use to assemble storefront pages through the CMS. Understanding the difference between them is key to deciding what to create when you want to expose new content for editing in the VTEX Admin and where it should live in your project.

This guide explains both concepts, shows how they relate to [Content Types](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations), and lists common Section examples shipped with FastStore.

## Content hierarchy

In the CMS, content is organized hierarchically: a **Content Type** specifies which **Sections** are available on a page, and each Section consists of one or more **Components** (groups of fields).

```mermaid
flowchart TD
  ContentType["Content Type (e.g. landingPage)"]
  SectionA["Section (dynamic container, e.g. CallToAction)"]
  SectionB["Section (dynamic container, e.g. Hero)"]
  ComponentA["Component (group of fields, e.g. Link)"]
  ComponentB["Component (group of fields, e.g. Image)"]
  ComponentC["Component (group of fields, e.g. Title)"]

  ContentType --> SectionA
  ContentType --> SectionB
  SectionA --> ComponentA
  SectionA --> ComponentC
  SectionB --> ComponentB
  SectionB --> ComponentC
```

At runtime, your storefront (FastStore or another headless storefront) maps this hierarchy, Content Types, Sections, and Components, into actual UI components and HTML.

## Components

A **Component** is a **group of fields** declared with [JSON Schema](https://json-schema.org/). It defines the data structure, such as a title, an image, or a link, that editors complete in the CMS Admin form.

Regardless of the storefront technology you use, a Component:

- Declares which fields exist and their data types.
- Controls how fields appear in the Admin (labels, descriptions, validation).
- Can be reused across different sections and content types.

### Schema files for components

Each component resides in its own `.jsonc` file, named following the convention `cms_component__ComponentName.jsonc`. The schema relies on a few CMS-specific keywords:

| Keyword | Purpose |
| :---- | :---- |
| `$componentKey` | Unique identifier for the component. |
| `$componentTitle` | Display name displayed in the CMS interface. |
| `$extends` | Inherits properties from base schemas (for example, `#/$defs/base-component`). |

For more details on schema declarations, see [Understanding CMS architecture and schema declarations](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations).

### `Link` component example

The schema below defines a reusable `Link` Component with two fields (`text` and `url`) in a [FastStore project](https://developers.vtex.com/docs/guides/cms-for-faststore-storefronts).

```jsonc
{
  "$extends": ["#/$defs/base-component"],
  "$componentKey": "Link",
  "$componentTitle": "Link",
  "type": "object",
  "required": ["text", "url"],
  "properties": {
    "text": {
      "title": "Text",
      "type": "string"
    },
    "url": {
      "title": "URL",
      "type": "string"
    }
  }
}
```

> ℹ️ A plain component can't be placed directly on a page. It's designed for reuse inside a section or as a field nested within another component.

## Sections

A **section** is a type of component that functions as a dynamic container for other components. Sections are the units that editors drag, reorder, and configure on a page in the CMS Admin. They group other components to create specific parts of a storefront page, such as a hero banner, a product shelf, or a call-to-action block.

Conceptually, a section:

- Uses the same JSON Schema mechanics as a regular component.
- Is referenced from a **content type**, so it becomes available in the page editor.
- Encapsulates a part of the page (for example, "Hero", "Footer", "Product shelf").

### Rendering sections in storefronts

How a section is rendered depends on the storefront:

- In **FastStore projects**, each section corresponds to a React component located in `src/components/`. These components are exported via `src/components/index.tsx` to render the data that editors configure in the Admin.
- In **other headless storefronts**, you can map section identifiers (for example, `$componentKey: "Hero"`) to your own Vue, React, or server-side templates, following the same principle.

### `CallToAction` section example

The schema below declares a `CallToAction` section in a FastStore project, composed of a `title` field and a nested `link` object, which mirrors the `Link` component shape:

```jsonc
{
  "$extends": ["#/$defs/base-component"],
  "$componentKey": "CallToAction",
  "$componentTitle": "Call To Action",
  "title": "Call To Action",
  "description": "Get your 20% off on the first purchase!",
  "type": "object",
  "required": ["title", "link"],
  "properties": {
    "title": {
      "title": "Title",
      "type": "string"
    },
    "link": {
      "title": "Link Path",
      "type": "object",
      "required": ["text", "url"],
      "properties": {
        "text": {
          "title": "Text",
          "type": "string"
        },
        "url": {
          "title": "URL",
          "type": "string"
        }
      }
    }
  }
}
```

<!-- Add the following callout once we have the following guide published
> ℹ️ To see a Section being created end-to-end in a FastStore project, follow the [Extending a component](https://developers.vtex.com/docs/guides/cms-extending-a-component) guide.-->

## Differences between components and sections

| Criteria | Component | Section |
| :---- | :---- | :---- |
| **Purpose** | Defines a reusable data shape (for example, a link, badge, or media block). | Page-placeable container of components that represents a full page block (for example, hero, shelf, footer). |
| **Scope** | Reused inside sections or other components. | Exposed in the CMS page editor for editors to add to a page. |
| **Schema file** | Stored as a component schema file (for example, `cms_component__*.jsonc` in FastStore projects). | Also stored as a component schema file; sections are distinguished by their usage, referenced by Content Types, and rendered as page blocks. |
| **Referenced from a content type** | Typically **no**. Used as nested objects or arrays inside sections and other components. | **Yes.** Listed in one or more content type schemas so editors can add them to pages. |
| **Rendering** | Data is consumed by a parent component or template. | Maps directly to a storefront component or template that renders an entire page block. |

## Relationship with content types

A **content type**, such as `home`, `pdp`, `plp`, or `landingPage`, defines a page structure and declares which sections editors can add to that page. When you create a new section, you make it available to editors by referencing it from one or more content type schemas.

In any storefront integration:

- Components and sections define **what** can be edited.
- Content types define **where** those sections can appear and how the page is structured.
- Your storefront code fetches content type entries and renders the referenced sections and components.

For a deeper dive into how schemas are organized, validated, and deployed, see [Understanding CMS architecture and schema declarations](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations).

## Native sections in FastStore

FastStore ships with several native sections you can reuse or override before creating new ones. These examples apply specifically to FastStore projects, but the underlying concepts (page-placeable Sections composed of Components) apply to any storefront.

Some examples:

- [`Hero`](https://developers.vtex.com/docs/guides/faststore/organisms-hero): Full-width banner used above the fold.
- [`ProductGrid`](https://developers.vtex.com/docs/guides/faststore/organisms-product-grid): Product list typically used on PLP pages.
- [`Navbar`](https://developers.vtex.com/docs/guides/faststore/organisms-navbar): Top navigation bar.

## Next steps

<Flex>

<WhatsNextCard
 linkTo="https://developers.vtex.com/docs/guides/cms-extending-a-component"
 title="Extending a component"
 description="Learn how to extend an existing component, such as the CallToAction Section, in your FastStore project."
 linkTitle="See more"
/>

<WhatsNextCard
 linkTo="https://developers.vtex.com/docs/guides/content-plugin"
 title="Content plugin"
 description="Manage CMS schemas, organize components, and define Content Types from the terminal using the Content plugin."
 linkTitle="See more"
/>

</Flex>
