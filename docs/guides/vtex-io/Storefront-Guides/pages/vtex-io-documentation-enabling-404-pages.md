---
title: "Enabling 404 pages"
slug: "vtex-io-documentation-enabling-404-pages"
hidden: false
createdAt: "2020-06-03T16:02:44.190Z"
updatedAt: "2022-12-13T20:17:44.467Z"
---

A 404 error is an HTTP response code indicating that the server cannot find the requested page. This often happens when a user tries to access a page that has been removed or doesn’t exist, such as a deactivated product page.

For ecommerce websites, enabling 404 pages is essential to:
- Prevent search engines like Google from indexing non-existent pages, which can negatively impact SEO.
- Enhance the user experience by guiding visitors to valid content.

In VTEX IO, 404 pages are enabled by default for:
- Non-existent product pages.
- URLs with more than one invalid segment.

In addition, you can also configure 404 pages for URLs with a single invalid segment, as outlined in the instructions below.

> ℹ️ The native 404 functionality does not apply to URLs originating from user searches. These URLs include the `map=ft` parameter and are not considered non-existent. In rare cases where search URLs include the `map=specificationFilter` parameter without `map=ft`, 404 pages might be rendered. 

## Instructions

1. Open the VTEX Admin and navigate to **Apps > App Management**.
2. Find the **Rewriter** app and click the **Settings** button.
3. Select the check button to **Enable 404 for paths with one segment, e.g. `/foo`**. This setting ensures that 404 pages are shown for URLs with a single invalid segment.
4. Save your changes.

    ![404-pages](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-enabling-404-pages-0.png)

### Customizing your 404 Page

To customize 404 pages, you can use blocks in your store’s theme:

1. Open the terminal and [change to a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).
2. Open your [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) using your preferred code editor.
3. In the product or search template (`store.product` or `store.search`), add and configure the `store.not-found#product` or `store.not-found#search` block, respectively. Find below an example of a `store.not-found#product` for a product template:
    
    ```json
    "store.not-found#product": {
      "blocks": ["rich-text#not-found"]
    },
    "rich-text#not-found": {
      "props": {
        "textAlignment": "CENTER",
        "textPosition": "CENTER",
        "text": "**PAGE NOT FOUND**",
        "font": "t-heading-1"
      }
    }
    ```
    
    > ℹ️ The `store.not-found` blocks will only be rendered when the server returns a 404 error. The child block will be displayed to users in such cases.

4. Save your changes and run `vtex link` in your terminal to preview the updated 404 page:

    ![not-found-block](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-enabling-404-pages-1.png)

5. Once you are satisfied with the changes, [make your new theme version publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).
