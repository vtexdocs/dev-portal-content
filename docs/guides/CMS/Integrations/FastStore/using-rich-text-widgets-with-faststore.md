---
title: "Using rich text widgets with FastStore"
slug: "using-rich-text-widgets-with-faststore"
hidden: false
excerpt: "Learn how to configure rich text fields and add images to rich text content in FastStore storefronts."
---

The CMS provides rich text widgets for creating formatted storefront content. To add images to rich text content, configure the field with the `draftjs-rich-text-v2` widget. This widget lets content editors add images from the [Media Gallery](https://help.vtex.com/docs/tutorials/media-overview), resize and align them, and position them among text paragraphs.

## Before you begin

Make sure that:

- Your FastStore project consumes content from the CMS.
- Your project uses the latest FastStore version so the storefront can render images added with `draftjs-rich-text-v2`.
- You can edit and upload the store's CMS schema. See [Content plugin](https://developers.vtex.com/docs/guides/content-plugin).

## Instructions

### Step 1 - Configuring an image-enabled rich text field

1. In the component schema, define the rich text field as a string and set `widget.ui:widget` to `draftjs-rich-text-v2`. For example:

    ```json
    {
    "$componentKey": "RichTextSection",
    "$componentTitle": "Rich text section",
    "type": "object",
    "properties": {
        "content": {
        "title": "Content",
        "type": "string",
        "widget": {
            "ui:widget": "draftjs-rich-text-v2"
        }
        }
    },
    "required": ["content"]
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

> ℹ️ For more information about these commands, see [Content plugin](https://developers.vtex.com/docs/guides/content-plugin).

### Step 2 - Adding and formatting rich text images

1. In the VTEX Admin, go to **Storefront > All Content**.
2. Open an entry containing the image-enabled rich text field.
3. In the rich text toolbar, click the image action.
4. Select an existing image from the Media Gallery or upload a new one. Supported formats are `PNG`, `JPG`, `JPEG`, `GIF`, `WebP`, and `SVG`.
5. Select the inserted image to display its controls. You can:
   - Align the image to the left, center, or right.
   - Resize it by dragging a corner handle.
   - Expand it to the full width of the rich text field.
   - Delete it.
   - Drag it to another position among the text paragraphs.
6. Save the entry and use the branch preview to verify the content on the storefront.
7. When the content is ready, merge the branch to publish it.

> ℹ️ The CMS derives the image alternative text from its filename. Use descriptive filenames before uploading images to improve accessibility.
