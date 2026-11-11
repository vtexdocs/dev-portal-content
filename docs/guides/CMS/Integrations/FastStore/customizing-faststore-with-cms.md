---
title: "Customizing FastStore storefronts with the CMS"
hidden: false
slug: "customizing-faststore-storefronts-with-cms"
createdAt: "2026-09-28T12:00:00.000Z"
updatedAt: "2026-09-28T12:00:00.000Z"
---

FastStore and the CMS support different levels of storefront customization. The right approach depends on whether you only need to change content, adapt an existing FastStore component, or build a new section.

## Edit a native section's content

Use the CMS when the native FastStore section already supports the layout and behavior you need. Content editors can change the fields exposed by the section's schema, such as text, images, and links, without changing storefront code.

In the VTEX Admin, go to **Storefront > Content**, open the page that contains the section, edit its fields, and save your changes. To learn how the CMS represents sections and their fields, see [Understanding components and sections](https://developers.vtex.com/docs/guides/understanding-components-and-sections).

## Override a native FastStore component

Use an override when a native section already provides the required data fetching and most of the desired behavior, but part of its rendered interface needs to change.

This approach involves FastStore code and, when editors need to control new properties, a CMS schema declaration. For an end-to-end example, see [Overriding a native component in the CMS](https://developers.vtex.com/docs/guides/faststore/developing-and-customizing-components-overriding-a-native-component-cms).

## Create a new section

Create a section when no native FastStore section provides the layout or behavior you need. This approach involves creating a React component, declaring its CMS schema, registering it in FastStore, and syncing the schema so editors can add the section to pages.

For the complete procedure, see [Creating a new section in the CMS](https://developers.vtex.com/docs/guides/faststore/developing-and-customizing-components-creating-a-new-section-cms).

## Change the content model

Change the CMS schema when you need to define or reorganize the structures editors use, including Content Types, sections, components, and their fields. Start with [Understanding CMS architecture and schema declarations](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations), then use the [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) to generate and upload the schema.

## Customize storefront styling

Use FastStore themes and design tokens when the component structure and behavior are already suitable and only its visual presentation needs to change. See [Styling a component](https://developers.vtex.com/docs/guides/faststore/using-themes-components).
