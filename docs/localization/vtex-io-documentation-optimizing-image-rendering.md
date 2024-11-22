---
title: "Optimizing image rendering"
slug: "vtex-io-documentation-optimizing-image-rendering"
hidden: false
createdAt: "2020-06-03T16:02:44.306Z"
updatedAt: "2024-11-08T13:25:53.180Z"
excerpt: "Learn how to optimize image rendering for faster load times."
---

This guide outlines best practices for using images in your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) to maintain consistency and performance.

Images are crucial for creating a strong brand identity, but if not managed properly, they may slow down your store. To address this, Store Framework offers several image blocks tailored for different purposes, minimizing performance loss and allowing you to display images effectively. Additionally, there are best practices to follow when uploading images in your Store Theme.

This guide presents the following sections:

- [List of image blocks](#list-of-image-blocks): Presents the VTEX native components available in Store Framework that you can use to optimize image rendering on your store.
- [Best practices for uploading images](#best-practices-for-uploading-images): Describes best practices to maintain performance and visual consistency when updating images.

## List of image blocks

Store Framework offers several image blocks for different use cases. Selecting the right block helps to maintain performance and visual consistency.

- [**Logo**](https://developers.vtex.com/docs/apps/vtex.store-components/logo): Renders your brand logo, typically in the header or footer.
- [**Infocard**](https://developers.vtex.com/docs/apps/vtex.store-components/infocard): Renders images with links and call-to-action (CTA) buttons when you want to guide users with image-based CTAs.
- [**Rich Text**](https://developers.vtex.com/docs/apps/vtex.rich-text): Renders markdown text when you need to combine text and images in a single block.
- [**Product Summary Image**](https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryimage): Renders the product image attached to the product summary information, such as the product name and price. It's commonly used within other store components, like the [Shelf](https://developers.vtex.com/docs/apps/vtex.shelf), to display products with their key details.

  When using the Product Summary block, configure at least one of the following props:
  - `aspectRatio`
  - `width`
  - `height`
  - `maxHeight`

  These props define image dimensions, ensuring that product summary images are displayed at a consistent size, even if the images uploaded in the catalog have different dimensions. By declaring these props, your store shelf will replicate image consistency across all products being displayed, differently from the shelf example below:

  ![beat-practices-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-rendering-images-0.png)

  > ℹ️ You don't need to define all four properties in your Product Summary Image block at the same time. Each property has a unique purpose and can be configured based on your needs.

- [**Image**](https://developers.vtex.com/docs/apps/vtex.store-components/image): Renders standalone images without additional elements such as links or text, for when you just need to display an image.

## Best practices for uploading images

Follow these guidelines to upload images efficiently and avoid performance issues:

- To upload images, use the [Assets Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-assets-builder) or [Site Editor](https://developers.vtex.com/docs/guides/working-with-site-editor). These tools handle cropping automatically, ensuring a consistent user experience across your store.
- Avoid hardcoding image URLs in the `blocks.json` file, as this can lead to image deformation.
- Don't use images with large dimensions, as they may not crop correctly in Site Editor, leading to display issues.
