---
title: "Store Framework: Improved image dimension control with Store Image"
slug: "2025-03-11-store-image-component-improved-image-dimension-handling"
type: improved
excerpt: "Store Image app has been updated to allow a more flexible management of image dimensions."
createdAt: "2025-03-11T20:18:58.347Z"
updatedAt: ""
hidden: false
---

The [Store Image](https://developers.vtex.com/docs/apps/vtex.store-image) app has been updated to improve image dimension management. This release enhances flexibility and ensures better control over user-defined image sizes, resolving previous issues with dimension handling.

## What has changed?

- **Inline style adjustments:** The `height` attribute has been removed from the inline `style` rule and conditions for applying dimensions have been added to control when dimensions are applied.
- **Enhanced height control:** The `specificHeight` field has been introduced, which allows for more precise control over image heights.
- **Priority order for heights:** A new hierarchy for height settings has been established as follows.
  - `specificHeight`: Height of the image component. If set, it overrides other height values.
  - `genericHeight`: Fallback height value used when `specificHeight` is not set. Previously, it was the default field.
  - `maxHeight`: Maximum image height, inherited from the parent component.

- **Conditional dimension application:** Added checks to prevent incorrect dimension applications when heights are specified as percentages.

## Why did we make this change?

Previously, using the `imageDimensions` attribute directly in the `<img>` tag could overwrite CSS properties, causing layout inconsistencies. This update prevents such issues by providing more control and flexibility to create a consistent layout, especially when using percentage-based height.

## What needs to be done?

To benefit from the new functionality:
1. Update your Store Theme to use the latest version of the Store Image app.
2. Set the `experimentalSetExplicitDimensions` attribute to `true`
3. Update the desired image dimensions by referring to the [Store Image](https://developers.vtex.com/docs/apps/vtex.store-image) documentation.
