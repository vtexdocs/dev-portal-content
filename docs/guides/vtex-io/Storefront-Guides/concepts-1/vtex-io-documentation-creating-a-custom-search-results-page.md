---
title: "Creating a custom search results page"
slug: "vtex-io-documentation-creating-a-custom-search-results-page"
hidden: false
createdAt: "2020-08-11T07:03:17.934Z"
updatedAt: "2022-12-13T20:17:44.158Z"
---
When [creating a new landing page](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-new-custom-page/) for your store's website, you can configure it as a custom search results page to promote specific products.

Although custom pages do not inherently fetch search data, the `search-result-layout.customQuery` block from the [Search Result app](https://developers.vtex.com/docs/guides/vtex-search-result/) allows you to specify the query to render the desired search results for your users.

## Before you begin

To build a custom search results page, familiarize yourself with the [Search Result](https://developers.vtex.com/docs/guides/vtex-search-result) app to understand the blocks exported by this app, including the `search-result-layout.customQuery`.

## Instructions

1. Open your Store Theme app directory using your preferred code editor.
2. In the `routes.json` file, define a new path called `store.custom#landing`. Replace the `path` value as needed for your scenario.
    ```json
    "store.custom#landing": {
      "path": "/landing"
    }
    ```
3. In the `blocks.jsonc` folder, create a new file (e.g., `search-landing.jsonc`) to store the new custom search results page blocks.
4. In the new file, declare the template name, such as `store.custom#landing`. Ensure the name matches the one declared in step 2.
5. In the template's block list, add any theme block you want to build your new custom page. The `search-result-layout.customQuery` block is mandatory to define how the search query should be fetched. For example:
    
    ```json search-landing.jsonc
    {
      "store.custom#landing": { 
        "blocks": [
          "image#landingbanner", 
          "search-result-layout.customQuery"
        ]
      }
    }
    ```
6. Declare the blocks according to the search results custom page you wish to have. Below you can find an example of a custom search results template:
    ```json search-landing.jsonc
    {
      "store.custom#landing": { 
        "blocks": ["image#landing", "search-result-layout.customQuery"]
      },
      "image#landing": { 
        "props": { 
          "minWidth": "100%",
          "src": "https://user-images.githubusercontent.com/18701182/69889938-64b16180-12d2-11ea-8d8a-e3089cbeaffd.png"
        }
      },
      "search-result-layout.customQuery": {
        "props": {
          "querySchema": {
            "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "maxItemsPerPage": 8,
            "queryField": "Blue Top Retro Camera",
            "mapField": "ft"
          }
        },
        "blocks": [
          "search-result-layout.desktop",
          "search-result-layout.mobile",
          "search-not-found-layout"
        ]
      },
      "search-result-layout.desktop": {
        "children": [
          "breadcrumb.search",
          "search-title.v2",
          "flex-layout.row#top",
          "search-fetch-previous",
          "flex-layout.row#results",
          "search-fetch-more"
        ],
        "props": {
          "pagination": "show-more",
          "preventRouteChange": true
        }
      },
      "flex-layout.row#top": { 
        "children": [
          "total-products.v2",
          "order-by.v2"
        ]
      },
      "flex-layout.row#results": { 
        "children": [ 
          "flex-layout.col#filter",
          "flex-layout.col#search"
        ]
      },
      "flex-layout.col#filter": { 
        "props": {
          "width": "20%"
        },
        "children": [
          "filter-navigator.v3"
        ]
      },
      "flex-layout.col#search": { 
        "children": [
          "search-content"
        ]
      },
      "search-content": { 
        "blocks": ["gallery", "not-found"]
      },
      "gallery": {
        "blocks": ["product-summary.shelf"]
      }
    }
    ```
7. Save the changes made in your Store Theme app.
8. Open the terminal, log in to your VTEX Account and [create a new development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace/).
9. Once logged into the desired account and workspace, [link](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app/) your Store Theme app to see your new custom page live.
10. Access your store's website using the following format: `{workspaceName}--{accountName}.myvtex.com/{pathName}` to see your new page live.

Once you are satisfied with the changes to your Store Theme, [make your new theme content publicly available](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-theme-content-public/).
