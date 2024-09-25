---
title: "Rendering images"
slug: "vtex-io-documentation-best-practices-for-rendering-images"
hidden: false
createdAt: "2020-06-03T16:02:44.306Z"
updatedAt: "2022-12-13T20:17:44.629Z"
---

Images play a vital role in building your brand’s visual identity, but they can also impact your store's performance. To balance aesthetics and speed, Store Framework provides several image blocks, each designed for specific use cases. 

This guide outlines best practices for handling images in your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) to maintain both performance and consistency.

## Best practices for uploading images

Follow these guidelines to upload images efficiently and avoid performance issues:

- Use the [Assets Builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-the-assets-builder) or [Site Editor](https://help.vtex.com/en/tutorial/site-editor-overview) to upload images. These tools handle cropping automatically, ensuring a consistent user experience.
- Avoid hardcoding image URLs in the `blocks.json` file. Doing so may cause image deformation.
- Do not use images with large dimensions. Images with large dimensions might not crop correctly in the Site Editor, leading to display issues.

## List of image blocks

The Store Framework offers several image blocks, each suited to different use cases. Selecting the appropriate block will help maintain performance and visual consistency:

- [**Logo:**](https://developers.vtex.com/docs/apps/vtex.store-components/logo) Use this block to render your brand’s logo, typically in the header or footer.
- [**Infocard:**](https://developers.vtex.com/docs/apps/vtex.store-components/infocard) Ideal for displaying images with links and call-to-action buttons. Use this block when you want to guide users with image-based CTAs.
- [**Rich Text:**](https://developers.vtex.com/docs/apps/vtex.rich-text) A versatile block for rendering markdown text, which can also include images. Use this when text and images are combined.
- [**Product Summary Image:**](https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryimage) Renders the product image attached to a product summary information (e.g., name, price). It is often used within other store components like the Shelf.
- [**Image:**](https://developers.vtex.com/docs/apps/vtex.store-components/image)  A simple block for rendering standalone images without additional elements like links or text. Use this block when you just need to display an image.

### Configuring the Product Summary Image Block

When using the Product Summary block, configure at least one of the following props:
- `aspectRatio`
- `width`
- `height`
- `maxHeight`

These props define image dimensions and enable you to let product summary images be of identical size when rendered, even if the images submitted in the Admin's Catalog are of a different size.

These props define the image's dimensions and allow product summary images to be presented with the same size, regardless of the dimensions of the images uploaded via the admin's Catalog.

> ℹ️ You do not need to define all four properties in your Product Summary Image block at the same time. Each property has a unique purpose and can be configured based on your specific needs. For more information, refer to the [**Product Summary Image**](https://developers.vtex.com/docs/apps/vtex.product-summary/productsummaryimage) documentation.

For example, by declaring these props, your store's Shelf will have image consistency across all products being displayed, differently from the Shelf example below:

![beat-practices-images](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-best-practices-for-rendering-images-0.png)
