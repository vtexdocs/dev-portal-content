---
title: "Creating a new custom page"
slug: "vtex-io-documentation-creating-a-new-custom-page"
hidden: false
createdAt: "2020-06-03T16:02:44.295Z"
updatedAt: "2026-03-23T16:41:35.064Z"
category: "Storefront Development"
---

Stores consist of several pages, each with a unique layout and content. When you create a store in VTEX IO, several default pages with predefined URLs are available, such as:

- `store.home` - Homepage
- `store.product` - Product page
- `store.search` - Search results page
- `store.account` - Client account page
- `store.login` - Login page
- `store.orderplaced` - Order placed page

> ℹ️ You can manage the title and template of each page in the Pages section of the CMS in the VTEX Admin.

You can also develop custom pages to meet your store's specific needs, such as landing pages for special campaigns or institutional pages.

In this guide, you'll learn how to create a new custom page for your Store Framework store.

## Instructions

As an example, consider that you want to create a custom **About us** page for your store with an image in the left column and a title and text in the right column:

![store-product-exp](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-creating-a-new-custom-page-0.png)

### Step 1 - Creating the new template

First, define the template the new page will use. There are three template types:

- **Product:** For pages that display content for a single product, like a product detail page. When a new product is added, a product page is automatically generated.
- **Product collections:** For pages containing a group of products, such as the search result page.
- **Standard:** For pages with no specific product content, such as the homepage.

> ℹ️ Even though `Standard` pages aren't directly linked to a specific product, they can display shelves or lists for any chosen group of products. The main difference is that the group of products shown on a standard page depend on the shelf settings, not on the URL query.

Then follow the steps below:

1. In your Store Theme's code, declare a new template within your `blocks` folder or `blocks.jsonc` file as follows:

```json
{
 "store.custom#about-us": {
     "blocks": [  
     ]
  }
}
```

2. Complete it with the blocks that will set the desired layout. For example:

```json
{
 "store.custom#about-us": {
   "blocks": [
     "flex-layout.row#about-us"
   ]
 },
 "flex-layout.row#about-us": {
   "children": [
     "image#about-us",
     "flex-layout.col#text-about-us"
   ]
 },
 "flex-layout.col#text-about-us": {
   "children": [
     "rich-text#about-title",
     "rich-text#about-content"
   ],
       "props": {
     "preventVerticalStretch": true
   }
 },
"rich-text#about-title": {
   "props": {
     "text":
     "# About us Title"
   }
 },
 "rich-text#about-content": {
   "props": {
     "text":
     " About us content - Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
   }
 },
 "image#about-us": {
   "props": {
     "src": "https://storecomponents.vteximg.com.br/arquivos/mobile-phone.png",
     "maxHeight": "600px"
   }
 }
}
```

For more information, see the [Flex Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-flex-layout) documentation.

### Step 2 - Creating the new page's path

To make the new page accessible in your store, you must declare its path. You can do it by [updating the Store Theme code](#updating-the-store-theme-code) or [using the VTEX Admin](#using-the-vtex-admin).

#### Updating the Store Theme code

1. In your theme's source code, access the `routes.json` file. You can find it in the `store` folder.
2. In that file, add the path to the JSON file for the template you recently created:

```json
"store.custom#{templatename}": {
  "path": "/{URL}"
}
```

3. Save your files.
4. [Link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) the theme to a Development workspace. You'll be able to access and see your new page live through your workspace using the following format: `{workspaceName}--{accountName}.myvtex.com/{pathName}`.

#### Using the VTEX Admin

To set the new page path using VTEX Admin, you must first [release](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version) the changes you made to create the template and [install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the new version of your Store Theme in a [production workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-production-workspace).

Once your changes are set up in a production workspace, you can use the CMS in the Admin to create the page path:

1. In the VTEX Admin, go to **Storefront > Pages**.
2. Click `Create new`.
3. Choose the desired URL and one of the templates you created, such as the **About Us** page template previously created.

A template only defines the page layout. Therefore, you can apply any new template to any page that accepts templates of the same type.

> ℹ️ When editing any content using the CMS section, When editing content in the CMS, we recommend making your changes in a production workspace. Make sure you do not create your new custom page in the store's master workspace.

### Step 3 - Adding the content

You can define your page content either by making changes directly in the [Store Theme](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) app or by using [Site Editor](https://help.vtex.com/docs/tutorials/site-editor-overview) in the VTEX Admin.

When editing directly in the Store Theme app, you can visualize your changes by linking the theme to your development workspace.

To edit the page in Site Editor, you can browse to your custom page or enter its URL in the `Page URL` field.

![custom-pages-siteeditor](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/custom-page-site-editor.png)

### Step 4 - Making your theme content publicly available

If you're satisfied with the changes to your Store Theme, make your new page publicly available. For detailed instructions, see the guide [Making your theme content public](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).
