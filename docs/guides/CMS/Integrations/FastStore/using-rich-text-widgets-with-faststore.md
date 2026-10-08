---
title: "Using rich text widgets with FastStore"
slug: "using-rich-text-widgets-with-faststore"
hidden: false
excerpt: "Learn how to configure rich text fields and render CMS images in a FastStore storefront."
---

The CMS provides rich text widgets for formatted storefront content. To let editors insert images, set the field widget to `draftjs-rich-text-v2`. Render that field with `RichText` from `@faststore/core`.

## Before you begin

Make sure that:

- The store uses the CMS. In `discovery.config.js`, set `contentSource.type` to `CP`.
- Your project uses the latest FastStore version so the storefront can render images added with `draftjs-rich-text-v2`.
- You can edit and upload the store's CMS schema. See [Content plugin](https://developers.vtex.com/docs/guides/content-plugin).

## Instructions

### Step 1 - Configuring an image-enabled rich text field

1. In `cms/faststore/components/`, define the rich text field as a string and set `widget.ui:widget` to `draftjs-rich-text-v2`. For example, `cms_component__richtextsection.jsonc`:

    ```json
    {
      "$extends": ["#/$defs/base-component"],
      "$componentKey": "RichTextSection",
      "$componentTitle": "Rich text section",
      "title": "Rich text section",
      "type": "object",
      "required": ["content"],
      "properties": {
        "content": {
          "title": "Content",
          "type": "string",
          "widget": {
            "ui:widget": "draftjs-rich-text-v2"
          }
        }
      }
    }
    ```

2. After changing the schema, open a terminal and run the following command to generate the consolidated schema:

    ```shell
    vtex content generate-schema
    ```

3. Upload the schema to the CMS:

    ```shell
    vtex content upload-schema
    ```

In a FastStore project, you can run both steps with a single command from the store root:

```shell
yarn cms-sync
```

> ℹ️ For more information about these commands, see [Content plugin](https://developers.vtex.com/docs/guides/content-plugin).

### Step 2 - Rendering the field

1. In `src/components`, create `RichTextSection.tsx` and pass the CMS field to `RichText` from `@faststore/core`. Set `$componentKey` to the same value used in the schema:

    ```tsx
    import { RichText } from '@faststore/core'

    export interface RichTextSectionProps {
      content: string
    }

    export default function RichTextSection({ content }: RichTextSectionProps) {
      return <RichText content={content} />
    }

    RichTextSection.$componentKey = 'RichTextSection'
    ```

    > ℹ️ `RichText` from `@faststore/core` is the ready-to-use way to render this field, including images. You can also render the field with your own component, but it must handle the image content stored by the CMS.

2. Export the section in `src/components/index.tsx`:

    ```tsx
    import RichTextSection from './RichTextSection'

    export default {
      RichTextSection,
    }
    ```

> ℹ️ For more information about creating and registering sections, see [Creating a new section in the CMS](https://developers.vtex.com/docs/guides/faststore/developing-and-customizing-components-creating-a-new-section-cms).

### Step 3 - Adding and formatting rich text images

1. In the VTEX Admin, go to **Storefront > All Content**.
2. Open an entry containing the image-enabled rich text field.
3. In the rich text toolbar, click the image action.
4. Select an existing image from the [Media Gallery](https://help.vtex.com/docs/tutorials/media-overview) or upload a new one. Supported formats are `PNG`, `JPG`, `JPEG`, `GIF`, `WebP`, and `SVG`.
5. Select the inserted image to display its controls. You can:
   - Align the image to the left, center, or right.
   - Resize it by dragging a corner handle.
   - Expand it to the full width of the rich text field.
   - Delete it.
   - Drag it to another position among the text paragraphs.
6. Save the entry and use the branch preview to verify the content on the storefront.
7. When the content is ready, merge the branch to publish it.

> ℹ️ The CMS derives the image alternative text from its filename. Use a descriptive filename before uploading the image.
