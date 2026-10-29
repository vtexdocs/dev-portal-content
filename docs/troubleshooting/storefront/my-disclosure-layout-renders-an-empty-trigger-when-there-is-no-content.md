---
title: "My Disclosure Layout renders an empty trigger when there is no content"
slug: "my-disclosure-layout-renders-an-empty-trigger-when-there-is-no-content"
hidden: false
createdAt: "2026-10-29T17:30:00.000Z"
updatedAt: "2026-10-29T17:30:00.000Z"
excerpt: "When the Disclosure Layout has no content defined, an empty trigger button is displayed on the storefront."
domainFilters:
  - Store Framework
symptomFilters:
  - Rendering mismatch
---

**Keywords:** Disclosure Layout | Disclosure Trigger | Disclosure Content | Accordion | Store Framework | Storefront

The [Disclosure Layout](https://developers.vtex.com/docs/apps/vtex.disclosure-layout) app allows you to create layouts based on disclosure indicators, such as accordions. An empty trigger button is displayed on the storefront when a template includes the `disclosure-layout` block but has no content defined for it. This can happen, for example, in a template shared by collection pages where only some pages have accordion content.

This happens because the Disclosure Layout app doesn't check whether the `disclosure-trigger` and `disclosure-content` blocks have content before rendering them. The `disclosure-content` block stays hidden until the user interacts with the trigger, but the `disclosure-trigger` block is rendered as an empty button. This is the expected behavior of the app.

## Solution

Choose one of the following options, depending on your scenario:

- [Adding the Disclosure Layout only where there is content](#adding-the-disclosure-layout-only-where-there-is-content): If you can remove the `disclosure-layout` block from the templates or pages that have no accordion content.
- [Hiding the empty trigger with CSS](#hiding-the-empty-trigger-with-css): If the `disclosure-layout` block needs to stay in a template shared by pages with and without accordion content.

### Adding the Disclosure Layout only where there is content

Use this option if the pages or templates that display the empty trigger have no accordion content to show, and you can edit their structure.

Make sure the `disclosure-layout` block is only part of the templates and pages that have content to display in the accordion. In the pages or templates that have no content, remove the block or use a template that doesn't include it.

To remove the block, edit the template in your store theme. In the `store/blocks` folder, find the template file and remove `disclosure-layout` from the `children` list of the block that contains it. If only some pages have no content, create a template without the block for those pages.

The following example shows a template in which the `disclosure-layout` block is removed from the `children` list of the `flex-layout.col#content` block:

```diff
{
  "flex-layout.col#content": {
    "children": [
      "rich-text#title",
-     "disclosure-layout#simple"
    ]
  }
}
```

After removing the block from the `children` list, you can also delete its definition and the definitions of its child blocks (`disclosure-trigger` and `disclosure-content`) if no other template uses them.

> ℹ️ You can't add or remove blocks in the Site Editor. It only overwrites the configuration of blocks that already exist in the Store Theme app. For more information, see [Managing page and template content](https://help.vtex.com/docs/tutorials/managing-page-and-template-content).

### Hiding the empty trigger with CSS

Use this option if you can't remove the `disclosure-layout` block from the template, for example, because the same template is shared by pages with and without accordion content.

Hide the empty trigger using the `trigger` CSS handle. In your store theme, add the following rule to the `vtex.disclosure-layout.css` file:

```css
.trigger:empty {
  display: none;
}
```

For more information on how to customize the app, see [Using CSS handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

> ⚠️ This rule only hides the trigger when its child blocks render nothing. If a child block renders an empty wrapper element, such as a block with no text defined, the `:empty` selector doesn't match and the trigger remains visible. In this case, follow the first option [Adding the Disclosure Layout only where there is content](#adding-the-disclosure-layout-only-where-there-is-content).
