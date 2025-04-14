---
title: "Store Framework: Improved image dimension control with Store Image"
slug: "2025-04-16-store-image-component-improved-image-dimension-handling"
type: improved
excerpt: "Store Image app has been updated to allow a more flexible management of image dimensions."
createdAt: "2025-04-16T08:18:58.347Z"
updatedAt: ""
hidden: false
---

The [Store Image](https://developers.vtex.com/docs/apps/vtex.store-image) app has been updated to improve image dimension management. This release increases flexibility and gives users better control over custom image sizes, addressing previous issues with dimension handling.

## What has changed?

- **Inline style adjustments:** The `height` attribute has been removed from the inline `style` rule, and conditions for applying dimensions have been added to control when dimensions are applied.
- **Enhanced height control:** The `specificHeight` field has been introduced, providing more precise control over image heights.
- **Priority order for heights:** A new hierarchy for height settings has been established as follows.
  - `specificHeight`: Height of the image component. If set, it overrides other height values.
  - `genericHeight`: Fallback height value used when `specificHeight` isn't set. Previously, it was the default field.
  - `maxHeight`: Maximum image height inherited from the parent component.

- **Conditional dimension application:** Added checks to prevent incorrect dimension applications when heights are specified as percentages.

## Why did we make this change?

Previously, using the `imageDimensions` attribute directly in the `<img>` tag could overwrite CSS properties, causing layout inconsistencies. This change gives more control and flexibility to maintain a consistent layout, especially when using percentage-based height.

## What needs to be done?

To benefit from the new functionality:
1. Update your Store Theme to use the latest version of the Store Image app.
2. Set the `experimentalSetExplicitDimensions` attribute to `true`.
3. Update the desired image dimensions following the [Store Image](https://developers.vtex.com/docs/apps/vtex.store-image) documentation.
