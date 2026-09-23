---
title: "Media gallery"
hidden: false
slug: "cms-media-gallery"
createdAt: "2026-09-21T12:00:00.000Z"
updatedAt: "2026-09-21T12:00:00.000Z"
excerpt: "Declare the media-gallery widget in a component schema so editors can pick images and reference videos from the CMS Media Gallery."
---

The Media Gallery is the CMS's central repository for images and video references. As a developer, you expose it to editors by using the `media-gallery` widget on a field in your component schema.

## Supported media

| Media type | Supported formats or sources |
| :---- | :---- |
| **Images** | PNG, JPG, JPEG, GIF, SVG, and WebP |
| **Videos** | Referenced by URL from YouTube, Vimeo, and other video hosting services (not uploaded directly) |

## Declaring the widget in a schema

To let editors pick an image from the Media Gallery for a given field, use the `media-gallery` widget:

```jsonc
{
  "src": {
    "type": "string",
    "title": "Image",
    "widget": {
      "ui:widget": "media-gallery",
      "restrictMediaTypes": {
        "video": true,
        "image": ["png", "jpg", "jpeg", "webp"]
      }
    }
  }
}
```

The `restrictMediaTypes` property lets you limit which formats editors can pick for that specific field, for example, allowing video references but only a subset of image formats.

For how editors upload, organize, and reuse assets in the Admin, see the Help Center's [Media overview](https://help.vtex.com/en/docs/tutorials/media-overview).

## Next steps

<Flex>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/understanding-components-and-sections"
  title="Understanding components and sections"
  description="Learn how components declare fields, including media fields, that editors complete in the Admin."
  linkTitle="See more"
/>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/getting-started-with-cms#creating-and-publishing-content"
  title="Creating and publishing content"
  description="Find the Help Center resources for creating, previewing, and publishing content."
  linkTitle="See more"
/>

</Flex>
