---
title: "Search Result"
slug: "oggimexico-search-result-space"
excerpt: "oggimexico.search-result-space@5.0.2"
hidden: true
createdAt: "2022-07-14T17:48:49.002Z"
updatedAt: "2022-07-15T01:46:54.480Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

VTEX Search Result app is responsible for handling the result fetched by the [VTEX Search API](https://developers.vtex.com/vtex-developer-docs/reference/search-api-overview) and displaying it to users.

The app exports all store blocks expected in a search results page, such as the filters and the product gallery.

![search-result](https://user-images.githubusercontent.com/52087100/77557721-d96b6580-6e98-11ea-9178-77c8c4a6408e.png)

## Configuration

To configure the VTEX Search Result, check the sections below.

### Adding the Search Result app to your theme's dependencies 

In your theme's `manifest.json`, add the Search Result app as a dependency: 

```json
  "dependencies": {
    "vtex.search-result": "3.x"
  }
```

Now, you can use all the blocks exported by the `search-result` app. Check out the full list below:

#### `search-result` blocks
| Block name   | Description  |
| -------- | ------------------------ |
| `search-result-layout`     |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Enables you to build the search result page using its three children blocks: `search-result-layout desktop`, `search-result-layout.mobile`, and `search-not-found-layout` . It must be used in the `store.search` template since it uses the context provided by the VTEX Search API.                                                                                 |
| `search-result-layout.customQuery` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Used instead of `search-result-layout` in scenarios in which the search result will be declared in a template that doesn't fetch Search context, such as Home. It accepts a `querySchema` prop that executes search custom queries. It also supports three children blocks: `search-result-layout.desktop`, `search-result-layout.mobile` and `search-not-found-layout` .
| `search-result-layout.desktop`   | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Builds the search result page structure for desktop mode.                                                                                                             |
| `search-result-layout.mobile`   | Builds the search result page structure for mobile mode.  If the `search-result-layout.mobile` is not provided, the `search-result-layout.desktop` will be used instead.                                                                                                            |
| `search-layout-switcher`       | Enables mobile users to switch between the available layout modes.                                                                                              |
| `search-not-found-layout`   | Builds the whole search result page structure for scenarios in which no result was fetched. It is rendered whenever users search for a term that doesn't return a product. |                                                      |
| `gallery`  | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Displays the gallery with all the products found in the search.  |                    |                                         
| `gallery-layout-switcher` | Logical block that allows users to switch between the available `gallery`'s layouts. To know how to build your search results with multiple layouts, access the [documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts).  |                           |                                     
| `gallery-layout-option` | Defines how each layout option should be rendered for users. To know how to build your search results with multiple layouts, access the [documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts).  | 
| `not-found` | Contains a text and a description for the page that was not found in the search. It must be declared as a child of `search-not-found-layout`.  | 
| `search-content`          | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Decides, behind the scenes, which block will be displayed: either the `gallery` block (if products are found) or the `not-found` block (if the selected filters lead to an empty search results page). This means that both `gallery` and `not-found` must be declared as `search-content` children.                    |
| `store.not-found#search`    | When configured, it displays a `404` error message whenever the server cannot return what the browser request was or when it is configured not to handle that request.  |  
| `search-products-count-per-page` | Displays the total number of products being displayed on the search results page. | 
| `search-products-progress-bar` | Displays a progress bar of products being displayed on the search results page. |
| `order-by.v2`            | Allows users to choose the product ordination on the search results page.  | 
| `filter-navigator.v3`        | Allows users to apply different filters to the search. On mobile, renders a button that, when clicked on, displays all available filters in a sidebar. | 
| `total-products.v2`        | Displays the total amount of products found for that search. | 
| `search-title.v2`         | Displays a title for the search that was done. |                                                                                              |
| `search-fetch-more`         | Displays the **Show More** button. This button is not rendered when the user is on the last page. |                                                                                              |
| `search-fetch-previous`         | Displays the **Show Previous** button. This button is not rendered when the user is on the first page. |                                                                                              |
| `search-products-count-per-page`         | Displays the number of products currently on the page. |                                                                                              |
| `sidebar-close-button`         | Displays an `X` button on the filter sidebar on mobile. |                                                                                       


### Adding the Search Result to page templates

The Search Result app data usually is displayed on search pages (`store.search`), but it can also be added on any other page. 

When added to the search page, the block used must be the `search-result-layout`, since it fetches data provided by the template's current search context. If you want to add the app to another page, use the [`search-result-layout.customQuery` block](#search-result-blocks).

On the desired store page, add the `search-result-layout` block or the `search-result-layout.customQuery` to the correct template blocks list. Check both codes below as  examples:

On search pages

```json
"store.search": {
  "blocks": ["search-result-layout"]
} 
```

On other pages

```diff
 "store.home": {
   "blocks": [
     "carousel#home",
     "shelf#home",
+    "search-result-layout.customQuery#home"
   ]
 }
 ```

### Defining how the search query data should be fetched

You need to define how the search results will be fetched before declaring the blocks into the search result layout.

You should define these results through a custom query on the home page. On the search template, you must use the already provided context.

If you use `search-result-layout`, the blocks will define the fetched data from the `context`. If what you are using is `search-result-layout.customQuery`, the props should be sent through the `querySchema` to configure the custom query. 

Using `search-result-layout`

```json
{
  "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
      "context": {
        "skusFilter": "FIRST_AVAILABLE",
        "simulationBehavior": "default"
      }
    }
  }
}
```

Using `search-result-layout.customQuery`

```json
{
  "store.home": {
    "blocks": [
      "carousel#home",
      "shelf#home",
      "search-result-layout.customQuery#home"
    ]
  },
  "search-result-layout.customQuery#home": {
    "props": {
      "querySchema": {
        "skusFilter": "FIRST_AVAILABLE",
        "simulationBehavior": "default"
      }
    }
  }
}
```
Check all props to configure your search data int the table below:

### The `context` and `querySchema` props
| Prop name              | Type             | Description                                                                                                                                                                                           | Default value     |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `queryField` | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Search URL's query string to define which results should be fetched in the custom query. For example: `Blue`. This prop only works if the `mapField` prop is declared as well.  | `undefined` | 
| `mapField` | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Search URL's `map` parameter to define which results should be fetched in the custom query, for example `specificationFilter_100`. This prop only works if the `queryField` prop is declared as well. | `undefined` | 
| `maxItemsPerPage`      | `number`         | Maximum number of items per search page. The maximum value of this prop is `50`. If a larger number is added, the query will fail.                 | `10`                |
| `orderByField`         | `enum`           | Decides which order products must follow when displayed. The possible values are named after the order type: `OrderByTopSaleDESC` (it considers the number of sold units of the product), `OrderByReleaseDateDESC`, `OrderByBestDiscountDESC`, `OrderByPriceDESC`, `OrderByPriceASC`, `OrderByNameASC`, `OrderByNameDESC` or `OrderByScoreDESC` ([relevance Score](https://help.vtex.com/en/tutorial/how-does-the-score-field-work--1BUZC0mBYEEIUgeQYAKcae)). `ASC` and `DESC` stand for ascending order and descending order, respectively.  | `OrderByScoreDESC`    |
| `hideUnavailableItems` | `boolean`     | Whether the search result should hide unavailable items (`true`) or not (`false`).     | `false`           |
| `facetsBehavior` |  `string`        | Defines the filter's behavior. When set to `Dynamic`, it restricts the results according to the filters that the user has already selected. If set to `Static`, all filters will continue to be displayed to the user, even if no results exist.       | `Static`           |
| `skusFilter`           | `enum` | Refines the SKUs returned for each product in the query. The fewer returned SKUs, the more performant your shelf query will be. Available value options: `FIRST_AVAILABLE` (returns only the first available SKU), `ALL_AVAILABLE` (returns all available SKUs), and `ALL` (returns all product's SKUs).                                     | `ALL_AVAILABLE` |
| `simulationBehavior`     | `enum` | Defines whether the search data will be up-to-date (`default`) or fetched using the Cache (`skip`). You should only use the last option if you prefer faster queries than the most up-to-date prices or inventory.                                                               | `default` |
| `installmentCriteria`               | `enum`                 | Defines which price should be displayed when different installments are available for it. Possible values are: `MAX_WITHOUT_INTEREST` (displays the maximum installment option with no interest attached to it) or `MAX_WITH_INTEREST` (displays the maximum installment option whether it has interest attached to it or not).                                 | `"MAX_WITHOUT_INTEREST"` |
| `excludedPaymentSystems`               | `string`                 | List of payment systems that should not be considered when displaying the installment options to users. This prop configuration only works if the `installmentCriteria` prop was also declared. In case it was not, all available payment systems will be displayed regardless.   | `undefined` |
| `includedPaymentSystems`               | `string`                 | List of payment systems that should be considered when displaying the installment options to users. This prop configuration only works if the `installmentCriteria` prop was also declared. In case it was not, all available payment systems will be displayed regardless.                                  | `undefined` |

> ℹ️ Pagination does not display results after the page 50. You can configure it to display more products per page using the prop `maxItemsPerPage` by increasing the quantity of products on each page.

> ⚠️ When the `simulationBehavior` prop is set as `skip`, it defines that the search data should only be fetched using the store's cache. This may impact the content displayed on store pages since the cache storage changes according to user interaction in each page.

You must define the query for the following search pages:

- Brand
- Department
- Category
- Subcategory 

This allows you to define custom behaviors for each of your store's search pages. For example:

```json
{
  "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "default"
        }
     }
  },
 "store.search#category": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "default"
        }
     }
  },
  "store.search#brand": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "default"
        }
     }
  },
  "store.search#department": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "default"
        }
     }
  },
  "store.search#subcategory": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "default"
        }
     }
  }
}
```



### Defining your search results page layouts and behavior

Now you can structure the `search-result-layout` or the `search-result-layout.customQuery` blocks. They both necessarily require the `search-result-layout.desktop` as a child. But you can also provide others, such as the `search-result-layout.mobile` and the `search-not-found-layout` props. 
 
According to your store's scenario, structure the `search-result-layout` or the `search-result-layout.customQuery`, by declaring their children and then configuring them using the [Flex Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-flex-layout) blocks and their props. For example:

```json
{
  "search-result-layout": {
    "blocks": [
      "search-result-layout.desktop",
      "search-result-layout.mobile",
      "search-not-found-layout"
    ]
  },
  "search-result-layout.desktop": {
    "children": [
      "flex-layout.row#searchbread",
      "flex-layout.row#searchtitle",
      "flex-layout.row#result"
    ],
    "props": {
      "preventRouteChange": true
    }
  }
}
```

#### The `search-result-layout.desktop`, `search-result-layout.mobile`, and `search-not-found-layout` props

| Prop name           | Type           | Description                                                                                                                          | Default value     |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| `hiddenFacets`      | `object` | Indicates which filters should be hidden. The possible values are in [this table](#the-hiddenfacets-object).                | `undefined`              
| `showFacetQuantity` | `boolean`      | Whether the resulting amount in each filter should appear beside its name on the `filter-navigator.v3` block as (`true`) or (`false`)      | `false`           |
| `blockClass`        | `string`       | Unique block ID to be used in [CSS customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization#using-the-blockclass-property)                                                                                    | `undefined`              |
| `trackingId` | `string` | ID to be used in Google Analytics to track store metrics based on the Search Result block. |  `Search result` | 
| `mobileLayout`      | `object` | Controls how the search results page will be displayed to users using the mobile layout. The possible values are in [this table](#the-mobilelayout-object).                                                                                                               | `undefined`              |
| `defaultGalleryLayout` | `string` | Name of the gallery layout to be used by default in the search results page. This prop is required when several layouts are explicitly defined by the `gallery` block. This prop's value must match the layout name defined in the `name` prop from `layouts` object. |  `undefined` | 
| `thresholdForFacetSearch` | `number` | The minimum number of facets must be displayed on the interface for a search bar to be displayed. If you declare `0`, the search bar will always be displayed. |  `undefined` | 
| `preventRouteChange` | `boolean` | Keeps page customizations even when the user applies new filters on it. This prop will merely change the URL’s query string instead of the entire URL; therefore, it prevents a full page reload whenever filters are applied. |  `false` | 


#### The `mobileLayout` object

| Prop name | Type   | Description                                                           | Default value |
| --------- | ------ | --------------------------------------------------------------------- | ------------- |
| `mode1`   | `enum` | Defines the default layout for the mobile search results page. Possible values are: `normal`, `small` or `inline`.  | `normal`      |
| `mode2`   | `enum` | Defines which layout will be set for the mobile search results page when users click on the layout selector button. Possible values also are `normal`, `small`, or `inline`. | `small`       |


#### The `hiddenFacets` object

| Prop name              | Type                   | Description                 | Default value |
| ---------------------- | ---------------------- | --------------------------- | ------------- |
| `brands`            | `boolean`      | Whether Brand filters should be hidden (`true`) or not (`false`).       | `false`         |
| `categories`           | `boolean`       | Whether Category filters should be hidden (`true`) or not (`false`). | `false`         |
| `priceRange`           | `boolean`              | Whether Price filters should be hidden (`true`) or not (`false`). | `false`         |
| `specificationFilters` | `object` | Indicates which Specification filters should be hidden. The possible values are in [this table](#the-specificationfilters-object).              | `undefined`    |

#### The `specificationFilters` object

| Prop name       | Type                      | Description                                           | Default value |
| --------------- | ------------------------- | ----------------------------------------------------- | ------------- |
| `hideAll`       | `boolean`      | Whether specification filters should be hidden (`true`) or not (`false`).    | `false`         |
| `hiddenFilters` | `object` | Object array of specification filters that should be hidden. The possible values are in [this table](#the-hiddenfilters-object).  | `undefined`       |

#### The `hiddenFilters` object

| Prop name | Type    | Description                         | Default value |
| --------- | ------- | ----------------------------------- | ------------- |
| `name`      | `string` | Name of the specification filter that you want to hide. | `undefined`            |

### Using the Flex Layout to build your search results page

With the [Flex Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-flex-layout) app and the other blocks also exported by the Search Results app, such as the `gallery`, it's time for you to build your search results page!

Find below the available blocks to build your store's search results page and their existing props as well. 

#### The `gallery` block

The `gallery` block defines how fetched items should be displayed on the store's search results page.

When declared with no props, it expects the [`product-summary.shelf`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary) as a child and consequently the block structure inherited from it. 

However, it is possible to use the `layouts` prop to provide several layouts to the page, allowing your store to have different arrangements of items according to what best fits your users' needs.

In a scenario where multiple layouts are provided, your store users will be able to shift between them according to their needs using the `gallery-layout-switcher` block, described in [the table below](#the-gallery-layout-switcher-props). The `gallery` will then render the component provided by the currently selected layout.

To understand how to build your search results with multiple layouts using the `layouts` prop, access the [**documentation**](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts).

##### The `gallery-layout-switcher` props

| Prop name | Type                      | Description                                                    | Default value   |
| :---------: | :---------------------: | :--------------------------------------------------------------| :-------------: |
| `layouts`  | `object` | List of layouts used to arrange and display the items on the search results page. If no value is provided, the `gallery` block must receive a `product-summary-shelf` block instead as a child. Check [this table](#the-layouts-object) for props of this block. | `undefined`  |
| `undefined` | `block` | Defines which blocks should be rendered per layout. The prop name is not `undefined`, you must include the value passed on the `component` prop. This prop's value must match the block name of your choosing to be rendered in that specific layout. | `undefined` | 
| `customSummaryInterval` | `number` |  Defines the item interval at which the **Gallery** should render a custom `product-summary` block. For example, declaring `5` would render a custom block at every four items rendered, as shown [on this image](https://user-images.githubusercontent.com/1207017/101687291-0cff1780-3a49-11eb-9c00-678b70001c8a.jpg). It is important to know that this prop doesn't support `layouts` yet. | `undefined` | 
| `CustomSummary` | `block` |  Defines a block to be rendered according to the interval defined by the `customSummaryInterval` prop. | `undefined` | 

##### The `layouts` object 

| Prop name   | Type     | Description                                                             | Default value   |
| :---------: | :------: | :---------------------------------------------------------------------: | :-------------: |
| `name`   | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Layout name. This value must be unique i.e. not equal to other layout names declared in the `gallery` block. | `undefined` |
| `component`   | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Names the `undefined` prop from the `gallery` block, which is responsible for declaring the block to be rendered in this layout. This prop's value can be any of your choosing as long as it is PascalCased i.e. has the first letter of each word in its name capitalized. **Caution**: For this to work, the chosen value must name afterwards the `gallery` block' `undefined` prop - *Do not use the `component` prop's value to directly pass the desired block name itself*. Check out the example below in order to understand the underlying logic behind this prop. | `undefined` |
| `itemsPerRow`   | `number` / `object` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Number of items to be displayed in each row of this layout. This prop works with [responsive values](https://vtex.io/docs/app/vtex.responsive-values/), therefore it also accepts an object with different numbers for desktop, tablet or phone screen sizes (*see the table below*). | `undefined` |
|     `preferredSKU`      | `PreferredSKUEnum` | Controls which SKU will be initially selected in the product summary                                                                                                                                                                                                                                                                                                                                 | `"FIRST_AVAILABLE"` |

For `PreferredSKUEnum`:

| Name            | Value             | Description                                        |
| --------------- | ----------------- | -------------------------------------------------- |
| First Available | `FIRST_AVAILABLE` | First available SKU in stock found or first SKU without stock. |
| Last Available  | `LAST_AVAILABLE`  | Last available SKU in stock found or last SKU without stock.  |
| Cheapest        | `PRICE_ASC`       | Cheapest SKU in stock found or first SKU without stock.        |
| Most Expensive  | `PRICE_DESC`      | Most expensive SKU in stock found or first SKU without stock.  |

⚠️ There's a way to select which SKU should take preference over this prop. You can create a Product (field) specification and per product assign the value of the desired SKU to be initially selected. Keep in mind that If the specification doesn't exist or if the value is empty, it will use the `preferredSKU` prop as fallback. You can read more about it, and how to implement it in [Recipes](https://vtex.io/docs/recipes/all)


##### The `itemsPerRow` object
  
| Prop name | Type     | Description | Default value   |
| :-------: | :------: | :--------:  | :-------------: | 
| `desktop` | `number` | Number of slides to be shown on desktop devices. |  `undefined` | 
| `tablet` | `number` | Number of slides to be shown on tablet devices. | `undefined` | 
| `phone` | `number` |  Number of slides to be shown on phone devices.   | `undefined` | 

##### Example of a `gallery` block

```json
{
  "gallery": {
    "props": {
      "layouts": [
        {
          "name": "whole",
          "component": "OneOrTwoLineSummary",
          "itemsPerRow": 1
        },
        {
          "name": "two",
          "component": "OneOrTwoLineSummary",
          "itemsPerRow": 2
        },
        {
          "name": "many",
          "component": "ManyByLineSummary",
          "itemsPerRow": {
            "desktop": 5,
            "mobile": 1
          }
        }
      ],
      "OneOrTwoLineSummary": "product-summary.shelf",
      "ManyByLineSummary": "product-summary.shelf"
    }
  }
}
```

#### The `gallery-layout-switcher` block

The `gallery-layout-switcher` block is a logical block that allows users to switch between the available `gallery`'s layouts. 

It receives no props and expects [the `gallery-layout-option` block](#the-gallery-layout-option-block) as a child. It's essential to define the options in the same order as the layouts so that the accessibility features can work properly.

#### The `gallery-layout-option` block

This block defines how each layout option should be rendered for users.

| Prop name   | Type           | Description                                                         | Default value   |
| :---------: | :------------: | :-----------------------------------------------------------------: | :-------------: |
| `name`  | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Name of the layout option. This prop's value must match the one passed to the [`name` prop](#the-layouts-object).  | `undefined`  |

##### Example of the `gallery-layout-switcher` and the `gallery-layout-option` blocks

```jsonc
{
  "gallery-layout-switcher": {
    "children": [
      //It follows the same whole -> two -> many order
      "gallery-layout-option#whole",
      "gallery-layout-option#two",
      "gallery-layout-option#many"
    ]
  },
  "gallery-layout-option#whole": {
    "props": {
      "name": "whole"
    },
    "children": [
      "icon-single-grid",
      "rich-text#option-whole"
    ]
  },
  "gallery-layout-option#two": {
    "props": {
      "name": "two"
    },
    "children": [
      "icon-inline-grid",
      "rich-text#option-two"
    ]
  },
  "gallery-layout-option#many": {
    "props": {
      "name": "many"
    },
    "children": [
      "icon-menu",
      "rich-text#option-many"
    ]
  }
}
```

#### `filter-navigator.v3` block

This block renders a filter selector for the fetched results.

| Prop name | Type                      | Description                                                                                       | Default value |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------- | ------------- |
| `categoryFiltersMode`  | `enum` | Whether the category filters should use the `href` attribute with the category pages' URLs (`href`) or not (`default`). By default, the filters use HTML divs with `role="link"`. You may change this behavior by setting this prop's value to `href`, thereby creating a link building to improve the SEO ranking of your category pages. | `default`  |
| `layout`  | `enum` | Whether the **Filter Navigator** layout should be responsive (`responsive`) or not (`desktop`). You may use `desktop` when the **Filter Navigator** is configured to display in a [drawer](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-drawer). | `responsive`  |
| `maxItemsDepartment` | `number`                 | Maximum number of departments to be displayed before the **See More** button is triggered.          | `8`             |
| `maxItemsCategory`   | `number`                 | Maximum number of category items to be displayed before the **See More** button is triggered.     | `8`             |
| `initiallyCollapsed` | `boolean` | Makes the search filters start out collapsed (`true`) or open (`false`). | `false` |
| `openFiltersMode`    | `enum` | Defines how many filters can be opened simultaneously on the **Filter Navigator** component. The possible values are `many` (more than one filter can be opened simultaneously) and `one` (only one filter can be opened). Notice that if `one` is declared, all filters will collapse before user interaction, regardless of what is passed to the `initiallyCollapsed` prop. | `many` |
| `filtersTitleHtmlTag` | `string` | HTML tag for the filter's title. | `h5` |
| `scrollToTop` | `enum` | Scrolls the page to the top (`auto` or `smooth`) or not (`none`) when selecting a facet. | `none` |
| `truncateFilters` | `boolean` | Whether a filter selector with more than 10 filters options should shorten the list and display a `See more` button (`true`) or not (`false`). | `false` |
| `closeOnOutsideClick` | `boolean` | Whether the **Filter Navigator** component should be closed when users click outside of it (`true`) or not (`false`). This prop only works if the `openFiltersMode` prop is set as `one`.  | `false` |
| `appliedFiltersOverview` | `enum` | Whether an overview of the applied filters should be displayed (`"show"`) or not (`"hide"`). | `"hide"` |
| `totalProductsOnMobile` | `enum` | Whether the Filter Navigator should display the total number of products on mobile devices  (`show`) or not (`hide`). | `hide` |
| `fullWidthOnMobile`      | `boolean` | Whether the `filter-navigator.v3` will be rendered on mobile using the full screen width (`true`) or not (`false`).     | `false`       |
| `navigationTypeOnMobile` | `enum`    | Defines how mobile users should navigate on the filter selector component. The possible values are `page` (only one list of options can be seen at a time) or `collapsible` (all lists of options can be seen simultaneously).                                    | `page`        |
| `updateOnFilterSelectionOnMobile` | `boolean` | Whether the search results on mobile should be updated according to filter selection (`true`) or not (`false`). This prop only works if the `preventRouteChange` prop is declared as `true`.         | `false`       |
| `drawerDirectionMobile` | `Enum` | Whether the search filters on mobile opens to the left (`drawerLeft`) or to the right (`drawerRight`) | `drawerLeft` |
| `showClearByFilter`       | `boolean` | Whether a clear button (responsible for erasing all filter options selected by the user) should be displayed alongside the filter name (`true`) or not (`false`).   | `false`       |
| `showClearAllFiltersOnDesktop`       | `boolean` |  Whether a clear button should be displayed (`true`) or not (`false`). This button will reset all selected filters.   | `false`       |
| `priceRangeLayout` | `enum` | Whether a text field enters the desired price range should be displayed  (`inputAndSlider`) or not (`slider`). | `slider` |
| `facetOrdering` | `array` | Array of objects (see below) that applies custom sorting rules for filters. The default behavior sorts descending the items by quantity. | `undefined` |
| `showQuantityBadgeOnMobile` | `boolean` | Displays a badge for mobile users indicating how many active filters there are. | `false` |

- **`facetOrdering` object:** 
  
| Prop name | Type     | Description | Default value   |
| :-------: | :------: | :--------:  | :-------------: | 
| `key` | `string` | Facets key that will be sorted. Possible values are `category-1`, `category-2`, `category-3` (for department, category and subcategory), `brand` or a product specification name. |  `undefined` | 
| `orderBy` | `enum` | Field from facets that should be used when sorting the entries. Possible values are `name` and `quantity`. | `undefined` | 
| `order` | `enum` | Whether the filter should be sorted by ascending (`ASC`) or descending (`DESC`) order. | `ASC` |

For example:

```jsonc
{
  "filter-navigator.v3": {
    "props": {
      "facetOrdering": [
        {
          "key": "brand",
          "orderBy": "name",
          "order": "ASC"
        }
      ]
    },
  }
}
```

> ⚠️ The `facetOrdering` prop will conflict with the `enableFiltersFetchOptimization` flag on `vtex.store`, since it returns only the top filter values ordered by count. In order to achieve the desired outcome with `facetOrdering`, it is necessary to set `enableFiltersFetchOptimization` as `false` on `vtex.store` Admin settings.


#### The `order-by` block

The `order-by` block renders a dropdown button with [sorting options](#the-sorting-options-for-the-order-by-block) to display the fetched results. Check the block props in the table below.

##### The `order-by` props
| Prop name       | Type            | Description                 | Default value |
| --------------- | --------------- | --------------------------- | ------------- |
| `specificationOptions` | `[object]` | Indicates which sorting options by specification will be displayed. This only works for stores using `vtex.search-resolver@1.x` | `undefined` |
| `hiddenOptions` | `[string]` | Indicates which sorting options will be hidden. (e.g. `["OrderByNameASC", "OrderByNameDESC"]`) | `undefined`      |
| `showOrderTitle` | `boolean` | Whether the selected order value (e.g. `Relevance`) will be displayed (`true`) or not (`false`).  | `true`           |

##### The sorting options for the `order-by` block

| Sorting option           | Value                       |
| ------------------------ | --------------------------- |
| Relevance                | `""`        |
| Top Sales Descending     | `"OrderByTopSaleDESC"`      |
| Release Date Descending  | `"OrderByReleaseDateDESC"`  |
| Best Discount Descending | `"OrderByBestDiscountDESC"` |
| Price Descending         | `"OrderByPriceDESC"`        |
| Price Ascending          | `"OrderByPriceASC"`         |
| Name Ascending           | `"OrderByNameASC"`          |
| Name Descending          | `"OrderByNameDESC"`         |
| Collection               | `"OrderByCollection"`         |


#### The `search-fetch-more` block

- **`specificationOptions` Object:**

| Prop name  | Type      | Description                             | Default value |
| ---------- | --------- | --------------------------------------- | ------------- |
| value      | string | Value that will be sent for ordering in the API. It must be in the format `{specification key}:{asc|desc}`. For example: `"size:desc"` or `"priceByUnit:asc"`. | `undefined` |
| label      | string | Label that will be displayed in the sorting options. E.g.: `"Price by unit, ascending"` | `undefined` |

The `search-fetch-more` block renders a **Show More** button used to load the results of the next search results page. Check the block props in the table below.

>ℹ️ This block is not rendered if there is no next page.

##### The `search-fetch-more` prop
| Prop name       | Type            | Description                           | Default value |
| --------------- | --------------- | ------------------------------------- | ------------- |
| `htmlElementForButton` | `enum` | Which HTML element will be displayed for `Show more` button component. Possible values are: `a` (displays a `<a>` element with `href` and `rel` attributes)  or `button` (displays a `<button>` element without `href` and `rel` attributes). | `button` |

#### The `search-fetch-previous` block

The `search-fetch-previous` block renders a `Show Previous` button used to load the results of the previous search results page. 

>ℹ️ This block is not rendered if there is no previous page.

##### The `search-fetch-previous` prop
| Prop name       | Type            | Description        | Default value |
| --------------- | --------------- | ------------------ | ------------- |
| `htmlElementForButton` | `enum` | Which HTML element will be displayed for `Show previous` button component. Possible values are: `a` (displays a `<a>` element with `href` and `rel` attributes)  or `button` (displays a `<button>` element without `href` and `rel` attributes). | `button` |

#### The `search-products-count-per-page` block

The `search-products-count-per-page` block shows the product count per search page. This block does not need any prop when declared.

#### The `search-products-progress-bar` block

The `search-products-progress-bar` block shows a progress bar of search results. This block does not need any prop when declared.

#### The `sidebar-close-button` block

The `sidebar-close-button` block is the `Close` button rendered on the top right of the mobile filter sidebar.

##### The `sidebar-close-button` props
| Prop name       | Type            | Description      | Default value |
| --------------- | --------------- | ---------------- | ------------- |
| `size` | `number` | Size of the button icon. | `30`       |
| `type` | `string` | Type of the button icon. | `line`       |

## Customization

To apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-search-results-page-with-multiple-layouts).

| CSS handles                           |
| ------------------------------------- |
| `accordionFilter`                     |
| `accordionFilterContainer`            |
| `accordionFilterContent`              |
| `accordionFilterItemActive`           |
| `accordionFilterItemBox`              |
| `accordionFilterItemHidden`           |
| `accordionFilterItemIcon`             |
| `accordionFilterItemOptions`          |
| `accordionFilterItemTitle`            |
| `accordionFilterItem`                 |
| `accordionFilterOpen`                 |
| `accordionSelectedFilters`            |
| `border`                              |
| `breadcrumb`                          |
| `buttonShowMore`                      |
| `categoriesContainer`                 |
| `categoryGroup`                       |
| `categoryParent`                      |
| `clearAllFilters`                     |
| `container`                           |
| `dropdownMobile`                      |
| `filter`                              |
| `filterAccordionBreadcrumbs`          |
| `filterBreadcrumbsContent`            |
| `filterBreadcrumbsText`               |
| `filterBreadcrumbsItem`               |
| `filterBreadcrumbsItemName`           |
| `filterAccordionItemBox--{facetValue}`|
| `filterApplyButtonWrapper`            |
| `filterAvailable`                     |
| `filterIsOpen`                        |
| `filterButtonsBox`                    |
| `filterClearButtonWrapper`            |
| `filterContainer--{facetType}`        |
| `filterContainer--b`                  |
| `filterContainer--c`                  |
| `filterContainer--priceRange`         |
| `filterContainer--{selectedFilters}`  |
| `filterContainer--{title}`            |
| `filterContainer`                     |
| `filterIcon`                          |
| `filterItem--{facetValue}`            |
| `filterItem--selected`                |
| `filterItem`                          |
| `filterMessage`                       |
| `filterPopup`                         |
| `filterPopupArrowIcon`                |
| `filterPopupButton`                   |
| `filterPopupContent`                  |
| `filterPopupContentContainer`         |
| `filterPopupContentContainerOpen`     |
| `filterPopupFooter`                   |
| `filterPopupOpen`                     |
| `filterPopupTitle`                    |
| `filterSelected`                      |
| `filterSelectedFilters`               |
| `filterTotalProducts`                 |
| `filtersWrapper`                      |
| `filtersWrapperMobile`                |
| `filterTemplateOverflow`              |
| `filterTitle`                         |
| `filterTitleSpan`                     |
| `footerButton`                        |
| `galleryItem`                         |
| `galleryItem--custom`                 |
| `galleryItem--{displayMode}`          |
| `galleryTitle`                        |
| `gallery`                             |
| `galleryLayoutSwitcher`               |
| `galleryLayoutOptionButton`           |
| `layoutSwitcher`                      |
| `loadingOverlay`                      |
| `loadingSpinnerInnerContainer`        |
| `loadingSpinnerOuterContainer`        |
| `orderByButton`                       |
| `orderByDropdown`                     |
| `orderByOptionItem`                   |
| `orderByOptionItem--selected`         |
| `orderByOptionsContainer`             |
| `orderByText`                         |
| `orderBy`                             |
| `productCount`                        |
| `progressBarContainer`                |
| `progressBar`                         |
| `progressBarFiller`                   |
| `resultGallery`                       |
| `searchNotFoundInfo`                  |
| `searchNotFoundOops`                  |
| `searchNotFoundTerm`                  |
| `searchNotFoundTextListLine`          |
| `searchNotFoundWhatDoIDo`             |
| `searchNotFoundWhatToDoDotsContainer` |
| `searchNotFoundWhatToDoDots`          |
| `searchNotFound`                      |
| `searchResultContainer`               |
| `seeMoreButton`                       |
| `selectedFilterItem`                  |
| `showingProductsContainer`            |
| `showingProductsCount`                |
| `showingProducts`                     |
| `switch`                              |
| `totalProductsMessage`                |
| `totalProducts`                       |

## Contributors ✨

Thanks goes out to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/grupo-exito-ecommerce"><img src="https://avatars2.githubusercontent.com/u/46934781?v=4?s=100" width="100px;" alt=""/><br /><sub><b>grupo-exito-ecommerce</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=grupo-exito-ecommerce" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ygorneves10"><img src="https://avatars1.githubusercontent.com/u/39542011?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ygor Neves</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=ygorneves10" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/marcosewbank"><img src="https://avatars3.githubusercontent.com/u/27689698?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marcos André Suarez Ewbank</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=marcosewbank" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/BeatrizMiranda"><img src="https://avatars2.githubusercontent.com/u/28959326?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Beatriz Miranda</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=BeatrizMiranda" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/felipeireslan"><img src="https://avatars3.githubusercontent.com/u/47363947?v=4?s=100" width="100px;" alt=""/><br /><sub><b>felipeireslan</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=felipeireslan" title="Code">💻</a></td>
    <td align="center"><a href="https://juliomoreira.pro"><img src="https://avatars2.githubusercontent.com/u/1207017?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Julio Moreira</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=juliomoreira" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/anto90fg"><img src="https://avatars.githubusercontent.com/u/73878310?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Antonio Cervelione</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=anto90fg" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

----