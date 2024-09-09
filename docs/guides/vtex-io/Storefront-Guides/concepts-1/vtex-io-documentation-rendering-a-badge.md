---
title: "Rendering a badge on top of a product"
slug: "vtex-io-documentation-rendering-a-badge"
hidden: false
createdAt: "2021-12-29T19:51:43.371Z"
updatedAt: "2022-12-13T20:17:44.260Z"
category: "Storefront Development"
seeAlso:
 - "/docs/guides/vtex-product-summary"
 - "/docs/guides/vtex-product-highlights"
 - "/docs/guides/vtex-stack-layout"
 - "/docs/guides/vtex-io-documentation-linking-an-app"
 - "/docs/guides/vtex-io-documentation-workspace"
---

To render a badge on top of a [Product Summary](/docs/guides/vtex-product-summary) component, for example, product collection on a [Shelf](/docs/guides/vtex-shelf) block, you combine the [Product Highlights app](/docs/guides/vtex-product-highlights/) and [Stack Layout](/docs/guides/vtex-stack-layout).

![badge](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-rendering-a-badge-0.png)

## Before you begin

1. Knowledge of how the Product Summary, Product Highlights, Stack Layout, and Product collections work is required for this recipe. If you have any doubts regarding them, we strongly recommend you access their technical documentation: [Product Summary](/docs/guides/vtex-product-summary), [Product Highlights](/docs/guides/vtex-product-highlights/), [Stack Layout](/docs/guides/vtex-stack-layout) and [Collections](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye).

2. Ensure you have already installed [VTEX IO CLI](/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) on your machine.

3. Also, make sure you have as a dependency `"vtex.product-summary": "2.x"` in your theme’s `manifest.json`.

## Instructions

1. In your theme’s `manifest.json` file, add the Product Highlights app and Stack Layout as a dependency:

   ```json
   “dependencies” : {
     "vtex.product-highlights": "2.x",
     "vtex.stack-layout": "0.x”,

   }

   ```

2. Open a product template you desire.

3. Then, add the `stack-layout` component to the `blocks` list of the desired template, for example:

   ```json
   {
   "product-summary.shelf": {
     "children": [
       "stack-layout#prodsum",
       ]
     },
   ...
   ```

4. In the theme’s template, declare the `stack-layout` component, and add the `"product-summary-image#shelf"` and `"vtex.product-highlights@2.x:product-highlights#collection"` as its `children`  to render the image and the badge, respectivetly.

   ```json
   "stack-layout#prodsum": {
       "children": [
         "product-summary-image#shelf",
         "vtex.product-highlights@2.x:product-highlights#collection"
       ]
     },
   ```

5. Then declare the props of the children. The first is `"product-summary-image#shelf"` props, responsible for rendering the product's image.

   ```json

   "product-summary-image#shelf": {
       "props": {
         "showBadge": true,
         "aspectRatio": "1:1",
         "maxHeight": 300
       }
     },
   ```

6. After declare the props and the children of `vtex.product-highlights@2.x:product-highlights#collection`: `product-highlight-wrapper` and `product-highlight-text`.

   > ℹ️ The `product-highlight-text` only renders the text already defined in the **Collection** page in a store’s Admin.  For more information about it, refer to [Collections articles](https://help.vtex.com/en/tutorial/creating-collections-beta--yJBHqNMViOAnnnq4fyOye) and the [Product Highlights app](/docs/guides/vtex-product-highlights#configuration)

   ```json

   "vtex.product-highlights@2.x:product-highlights#collection": {
       "props": {
         "type": "collection"
       },
       "children": ["product-highlight-wrapper"]
     },
     "product-highlight-wrapper": {
       "props": {
         "blockClass": "collection"
       },
       "children": ["product-highlight-text"]
     },
     "product-highlight-text": {
       "props": {
         "message": "{highlightName}"
       }
                },
     ...
   ```

Once you have declared the blocks’ props, [link the app](/docs/guides/vtex-io-documentation-linking-an-app) and see the changes live at the [Development workspace](/docs/guides/vtex-io-documentation-workspace) you are working.
