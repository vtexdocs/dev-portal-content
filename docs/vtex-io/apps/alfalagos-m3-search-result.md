---
title: "Search Result"
slug: "alfalagos-m3-search-result"
excerpt: "alfalagos.m3-search-result@0.0.8"
hidden: true
createdAt: "2022-08-05T12:48:55.555Z"
updatedAt: "2022-08-05T13:51:22.255Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

VTEX Search Result app is responsible for handling the result fetched by the [VTEX Search API](https://developers.vtex.com/vtex-developer-docs/reference/search-api-overview) and displaying it to users.

The app therefore exports all store blocks expected in a search results page, such as the filters and the product gallery.

![search-result](https://user-images.githubusercontent.com/52087100/77557721-d96b6580-6e98-11ea-9178-77c8c4a6408e.png)

## Configuration 

### Step 1 - Adding the Search Result app to your theme's dependencies 

In your theme's `manifest.json`, add the Search Result app as a dependency: 

```json
  "dependencies": {
    "vtex.search-result": "3.x"
  }
```

Now, you are able to use all the blocks exported by the `search-result` app. Check out the full list below:

| Block name   | Description  |
| -------- | ------------------------ |
| `search-result-layout`     |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red)  Layout block that enables you to build the search result page using its 3 children blocks: `search-result-layout.desktop`, `search-result-layout.mobile` and `search-not-found-layout` . It must be used in the `store.search` template since it uses the context provided by the VTEX Search API.                                                                                 |
| `search-result-layout.customQuery` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Used instead of `search-result-layout` in scenarios in which the search result will be declared in a template that doesn't fetch Search context, such as Home. It accepts a `querySchema` prop that executes search custom queries. It also supports three children blocks: `search-result-layout.desktop`, `search-result-layout.mobile` and `search-not-found-layout` .
| `search-result-layout.desktop`   | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Builds the search result page structure for desktop mode.                                                                                                             |
| `search-result-layout.mobile`   | Builds the search result page structure for mobile mode.  If the `search-result-layout.mobile` is not provided, the `search-result-layout.desktop` will be used instead.                                                                                                            |
| `search-layout-switcher`       | Enables mobile users to switch between the available layout modes.                                                                                              |
| `search-not-found-layout`   | Builds the whole search result page structure for scenarios in which no result was fetched. It is rendered whenever users search for a term that doesn't return a product. |                                                      |
| `gallery`  | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Displays the gallery with all the products found in the search.  |                    |                                         
| `gallery-layout-switcher` | Logical block that allows users to switch between the available `gallery`'s layouts.  |                           |                                     
| `gallery-layout-option` | Defines how each layout option should be rendered for users.  | 
| `not-found` | Block containing a text and a description for the page that was not found in the search. It must be declared as a child of `search-not-found-layout`.  | 
| `search-content`          | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Decides, behind the scenes, which block will be displayed: either the `gallery` block (if products are found) or the `not-found` block (if the selected filters lead to an empty search results page). This means that both `gallery` and `not-found` must be declared as `search-content` children.                    |
| `store.not-found#search`    | When configured, it displays a 404 error message whenever the server is not able to return what the browser request was or when it is configured to not handle that request.  |  
| `search-products-count-per-page` | Displays the total number of products being displayed in the search results page. | 
| `search-products-progress-bar` | Displays a progress bar of products being displayed in the search results page. |
| `order-by.v2`            | Allows users to choose the product ordination in the search results page.  | 
| `filter-navigator.v3`        | Allows users to apply different filters to the search. On mobile, renders a button that, when clicked on, displays all available filters in a sidebar. | 
| `total-products.v2`        | Displays the total amount of products found for that search. | 
| `search-title.v2`         | Displays a title for the search that was done. |                                                                                              |
| `search-fetch-more`         | Displays the "Show More" button. This button isn't rendered when the user is on the last page. |                                                                                              |
| `search-fetch-previous`         | Displays the "Show Previous" button. This button isn't rendered when the user is on the first page. |                                                                                              |
| `search-products-count-per-page`         | Displays the quantity of products currently on the page. |                                                                                              |
| `sidebar-close-button`         | Displays an `X` button on the filter sidebar on mobile. |                                                                                              |
| `search-title.v2`         | Displays a title for the search that was done. |         

:information_source: The Search Result app data may be displayed on **search pages** (`store.search`) or any other desired page. When added to the search page, the block that is used must be the `search-result-layout`, since it fetches data provided by the template's current search context. If you want to add the app to another page, the block that must be used is the `search-result-layout.customQuery`. 

### Step 2 - Adding the Search Result to page templates

According to the desired store page, add the `search-result-layout` block or the `search-result-layout.customQuery` to the correct template blocks list. For example:

```json
"store.search": {
  "blocks": ["search-result-layout"]
} 
```

*or* 

```diff
 "store.home": {
   "blocks": [
     "carousel#home",
     "shelf#home",
+    "search-result-layout.customQuery#home"
   ]
 }
 ```

Now, before declaring all desired blocks for your search result layout, your first need to define how you want the search results to be fetched. 

:warning: *Remember: on the home page, you define these results through a custom query. On the search template, you just need to use the already provided context.* 

### Step 3 - Defining how the search query data should be fetched

According to your store's scenario, define how the search query data should be fetched using props. 

If you are using a `search-result-layout`, the blocks will define the data that is fetched from the `context`. If what you are using is a `search-result-layout.customQuery`, the props should be sent through the `querySchema` to configure the custom query. 

For example: 

```json
{
  "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
      "context": {
        "skusFilter": "FIRST_AVAILABLE",
        "simulationBehavior": "skip"
      }
    }
  }
}
```

or 

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
        "simulationBehavior": "skip"
      }
    }
  }
}
```

> ⚠️ *When set as `skip`, the `simulationBehavior` prop defines that the search data should only be fetched using the store's Cache. Caution: In practice, **this may impact the content displayed on store pages, since the cache storage changes according to user interaction in each page**. In order to understand this prop behavior, take a look at the table below!

:warning: **You must define the query for the following search pages: brand, department, category and subcategory**. This will allow you to define custom behaviors for each of your store's possible search pages. For example:

```json
{
  "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "skip"
        }
     }
  },
 "store.search#category": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "skip"
        }
     }
  },
  "store.search#brand": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "skip"
        }
     }
  },
  "store.search#department": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "skip"
        }
     }
  },
  "store.search#subcategory": {
    "blocks": ["search-result-layout"],
    "props": {
        "context": {
            "skusFilter": "FIRST_AVAILABLE",
            "simulationBehavior": "skip"
        }
     }
  }
}
```

> ⚠️ *When set as `skip`, the `simulationBehavior` prop defines that the search data should only be fetched using the store's Cache. Caution: In practice, **this may impact the content displayed on store pages, since the cache storage changes according to user interaction in each page**. In order to understand this prop behavior, take a look at the table below!

Below you may find all available props to configure your search data (be it by using a context or a custom query through the `querySchema` block):

| Prop name              | Type             | Description                                                                                                                                                                                           | Default value     |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `queryField` | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Search URL's query string to define which results should be fetched in the custom query. For example: `Blue`. Caution: this prop only works if the `mapField` prop is declared as well.  | `undefined` | 
| `mapField` | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Search URL's `map` parameter to define which results should be fetched in the custom query. For example: `specificationFilter_100`. Caution: this prop only works if the `queryField` prop is declared as well. | `undefined` | 
| `maxItemsPerPage`      | `number`         | Maximum number of items per search page. The maximum value of this prop is `50`, if a larger number is passed, the query will fail.                                                                                                                                                               | `10`                |
| `orderByField`         | `enum`           | Decides which order products must follow when displayed. The possible values are named after the order type: `OrderByTopSaleDESC`, `OrderByReleaseDateDESC`, `OrderByBestDiscountDESC`, `OrderByPriceDESC`, `OrderByPriceASC`, `OrderByNameASC`, `OrderByNameDESC` or `OrderByScoreDESC` ([relevance score](https://help.vtex.com/tutorial/como-funciona-o-campo-score--1BUZC0mBYEEIUgeQYAKcae?locale=pt)). `ASC` and `DESC` stand for ascending order and descending order, respectively.  | `OrderByScoreDESC`              |
| `hideUnavailableItems` | `boolean`     | Whether the search result should display unavailable items (`true`) or not (`false`).                                                                                                                                                       | `false`           |
| `facetsBehavior` |  `string`        | Defines the behavior filters will have. When set to `dynamic`, it restricts the results according to the filters that user have already selected. If set to `Static`, all filters will continue to be displayed to the user, even is no results exist.                                                                                                                                                  | `Static`           |
| `skusFilter`           | `enum` | Controls SKUs returned for each product in the query. The less SKUs needed to be returned, the more performant your shelf query will be. Available value options: `FIRST_AVAILABLE` (returns only the first available SKU), `ALL_AVAILABLE` (only returns available SKUs) and `ALL` (returns all product's SKUs).                                                            | `ALL_AVAILABLE` |
| `simulationBehavior`     | `enum` | Defines whether the search data will be up-to-date (`default`) or fetched using the Cache (`skip`). The last option should be used only if you prefer faster queries over no having the most up-to-date prices or inventory.                                                               | `default` |
| `installmentCriteria`               | `enum`                 | Controls which price should be shown when there are different installments options for it. Possible values are: `MAX_WITHOUT_INTEREST` (displays the maximum installment option with no interest attached to it) or `MAX_WITH_INTEREST` (displays the maximum installment option whether it has interest attached to it or not).                                 | `"MAX_WITHOUT_INTEREST"` |
| `excludedPaymentSystems`               | `[string]`                 | List of payment systems that should *not* be taken into account when displaying the installment options to users. Caution: this prop configuration only works in scenarios where the `installmentCriteria` prop was also declared. In case it was not, all available payment systems will be displayed regardless.   | `undefined` |
| `includedPaymentSystems`               | `[string]`                 | List of payment systems that should be taken into account when displaying the installment options to users. Caution: this prop configuration only works in scenarios where the `installmentCriteria` prop was also declared. In case it was not, all available payment systems will be displayed regardless.                                  | `undefined` |

Now it is time to structure the `search-result-layout` block (or the `search-result-layout.customQuery`).  They both necessarily require a child: the `search-result-layout.desktop`. But you can also provide others, such as the `search-result-layout.mobile` and the `search-not-found-layout`. 
 
Since these are layout blocks, you can use [Flex Layout](https://vtex.io/docs/apps/layout-blocks/vtex.flex-layout@0.14.0) blocks to build your search results page.

### Step 4 - Defining your search results page layouts and behavior

Structure the `search-result-layout` or the `search-result-layout.customQuery`, according to your store's scenario, by declaring their children and then configuring them using [Flex Layout](https://vtex.io/docs/apps/layout-blocks/vtex.flex-layout@0.14.0) blocks and their props. For example:

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

#### **Available props for `search-result-layout.desktop`, `search-result-layout.mobile` and `search-not-found-layout`**: 

| Prop name           | Type           | Description                                                                                                                          | Default value     |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| `hiddenFacets`      | `Object` | Indicates which filters should be hidden. Possible props and their respective values can be found below.                                                                                                     | `undefined`.              
| `showFacetQuantity` | `boolean`      | Whether the result amount in each filter should appear besides its name on the `filter-navigator.v3` block as (`true`) or (`false`)      | `false`           |
| `blockClass`        | `string`       | Unique block ID to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property)                                                                                    | `undefined`              |
| `trackingId` | `string` | ID to be used in Google Analytics to track store metrics based on the Search Result block. |  `Search result` | 
| `mobileLayout`      | `Object` | Controls how the search results page will be displayed to users when using the mobile layout. Possible props and their respective values can be found below.                                                                                                                | `undefined`              |
| `defaultGalleryLayout` | `string` | Name of the gallery layout to be used by default in the search results page. This prop is only required when several layouts are explicitly defined by the `gallery` block. Caution: this prop's value must match the layout name defined in the `name` prop from `layouts` object. |  `undefined` | 
| `thresholdForFacetSearch` | `number` | Minimum number of facets that must be displayed on the interface for a search bar to be displayed. If you declare `0`, the search bar will always be displayed. |  `undefined` | 

- **`mobileLayout` Object:** 

| Prop name | Type   | Description                                                           | Default value |
| --------- | ------ | --------------------------------------------------------------------- | ------------- |
| `mode1`   | `Enum` | Defines the default layout for the mobile search results page. Possible values are: `normal`, `small` or `inline`.  | `normal`      |
| `mode2`   | `Enum` | Defines which layout will be set for the mobile search results page when users click on the layout selector button. Possible values also are: `normal`, `small` or `inline`. | `small`       |


- **`HiddenFacets` Object:**

| Prop name              | Type                   | Description                 | Default value |
| ---------------------- | ---------------------- | --------------------------- | ------------- |
| `brands`            | `boolean`      | Whether Brand filters should be hidden (`true`) or not (`false`).       | `false`         |
| `categories`           | `boolean`       | Whether Category filters should be hidden (`true`) or not (`false`). | `false`         |
| `priceRange`           | `boolean`              | Whether Price filters should be hidden (`true`) or not (`false`). | `false`         |
| `specificationFilters` | `Object` | Indicates which Specification filters should be hidden. | `undefined`    |

- **`SpecificationFilters` Object:**

| Prop name       | Type                      | Description                                           | Default value |
| --------------- | ------------------------- | ----------------------------------------------------- | ------------- |
| `hideAll`       | `boolean`      | Whether specification filters should be hidden (`true`) or not (`false`).    | `false`         |
| `hiddenFilters` | `[object]` | Object array of specification filters that should be hidden. | `undefined`       |

-  **`HiddenFilters` object**

| Prop name | Type    | Description                         | Default value |
| --------- | ------- | ----------------------------------- | ------------- |
| `name`      | `string` | Name of the specification filter that you want to hide. | `undefined`            |

### Step 5 - Using the Flex Layout to build your search results page

Using the [Flex Layout](https://vtex.io/docs/apps/layout-blocks/vtex.flex-layout/) app and the other blocks also exported by the Search Results app, such as the `gallery`, it's time for you to build your search results page!

Find below the available blocks to build your store's search results page and their existing props as well. 

#### `gallery` block

The `gallery` block defines how fetched items should be displayed on the store's search results page.

When declared with no props, it expects as child the [`product-summary.shelf`](https://vtex.io/docs/components/content-blocks/vtex.product-summary/) and consequently the block structure inherited from it. 

It is possible, however, to use its `layouts` prop to provide several layouts to the page, allowing your store to have different arrangement of items according to what best fits your users' needs.

In a scenario where several layouts are provided, your store users are able to shift between them according to their needs using the `gallery-layout-switcher` block (described further below). The `gallery` will then render the component provided by the currently selected layout.

:information_source: *It's highly recommended that you set a default layout for your search results page in the `defaultGalleryLayout` prop from the `search-result-layout.desktop` and `search-result-layout.mobile` blocks.*

| Prop name | Type                      | Description                                                    | Default value   |
| :---------: | :---------------------: | :--------------------------------------------------------------| :-------------: |
| `layouts`  | `object` | List of layouts used to arrange and display the items on search results page. Caution: If no value is provided, the `gallery` block must receive instead a `product-summary-shelf` block as child. | `undefined`  |
| `undefined` | `block` | Defines which blocks should be rendered per layout. **Caution**: this prop *name* is not `undefined`. Instead, its name must be the value passed to the `component` prop. This prop's value, in turn, must match the block name of your choosing to be rendered in that specific layout. Check out the example below in order to understand the underlying logic behind this prop. | `undefined` | 

- **`layouts` object:** 

| Prop name   | Type     | Description                                                             | Default value   |
| :---------: | :------: | :---------------------------------------------------------------------: | :-------------: |
| `name`   | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Layout name. This value must be unique i.e. not equal to other layout names declared in the `gallery` block. | `undefined` |
| `component`   | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Names the `undefined` prop from the `gallery` block, which is responsible for declaring the block to be rendered in this layout. This prop's value can be any of your choosing as long as it is PascalCased i.e. has the first letter of each word in its name capitalized. **Caution**: For this to work, the chosen value must name afterwards the `gallery` block' `undefined` prop - *Do not use the `component` prop's value to directly pass the desired block name itself*. Check out the example below in order to understand the underlying logic behind this prop. | `undefined` |
| `itemsPerRow`   | `number` / `object` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Number of items to be displayed in each row of this layout. This prop works with [responsive values](https://vtex.io/docs/app/vtex.responsive-values/), therefore it also accepts an object with different numbers for desktop, tablet or phone screen sizes (*see the table below*). | `undefined` |

- **`itemsPerRow` object:** 
  
| Prop name | Type     | Description | Default value   |
| :-------: | :------: | :--------:  | :-------------: | 
| `desktop` | `number` | Number of slides to be shown on desktop devices. |  `undefined` | 
| `tablet` | `number` | Number of slides to be shown on tablet devices. | `undefined` | 
| `phone` | `number` |  Number of slides to be shown on phone devices.   | `undefined` | 

For example:

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

#### `gallery-layout-switcher` block

Logical block that allows users to switch between the available `gallery`'s layouts. 

It receives no props and expects as child the `gallery-layout-option` block described below. It's important to define the options in the same order as the layouts, so the accessibility features can work properly.

#### `gallery-layout-option` block

Defines how each layout option should be rendered for users.

| Prop name   | Type           | Description                                                         | Default value   |
| :---------: | :------------: | :-----------------------------------------------------------------: | :-------------: |
| `name`  | `string` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Names the layout option. This prop's value must match the one passed to the `name` prop.  | `undefined`  |

For example:

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

Renders a filter selector for the fetched results.

| Prop name | Type                      | Description                                                                                       | Default value |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------- | ------------- |
| `categoryFiltersMode`  | `enum` | Whether the category filters should use the `href` attribute with the category pages' URLs (`href`) or not (`default`). By default, the filters use HTML divs with `role="link"`. You may change this behavior by setting this prop's value to `href`, thereby creating a link building to improve the SEO ranking of your category pages. | `default`  |
| `layout`  | `Enum` | Whether the Filter Navigator layout should be responsive (`responsive`) or not (`desktop`). You may use `desktop` when the Filter Navigator was configured to be displayed in a [drawer](https://vtex.io/docs/components/content-blocks/vtex.store-drawer@0.9.0). | `responsive`  |
| `maxItemsDepartment` | `number`                 | Maximum number of departments to be displayed before the See More button is triggered.          | `8`             |
| `maxItemsCategory`   | `number`                 | Maximum number of category items to be displayed before the See More button is triggered.     | `8`             |
| `initiallyCollapsed` | `Boolean` | Makes the search filters start out collapsed (`true`) or open (`false`). | `false` |
| `openFiltersMode`    | `Enum` | Defines how many filters can be opened at the same time on the Filter Navigator component. Possible values are: `many` (more than one filter can be opened at the same time) and `one` (only one filter can be opened). Notice that if `one` is declared all filters will be collapsed before user interaction, regardless of what is passed to the `initiallyCollapsed` prop. | `many` |
| `filtersTitleHtmlTag` | `string` | HTML tag for the filter's title. | `h5` |
| `scrollToTop` | `enum` | Scrolls the page to the top (`auto` or `smooth`) or not (`none`) when selecting a facet. | `none` |
| `truncateFilters` | `boolean` | Whether a filter selector with more than 10 filter options should shorten the list and display a `See more` button (`true`) or not (`false`). | `false` |
| `closeOnOutsideClick` | `boolean` | Whether the Filter Navigator component should be closed when users click outside of it (`true`) or not (`false`). Caution: This prop only works when the `openFiltersMode` prop is set as `one`.  | `false` |
| `appliedFiltersOverview` | `Enum` | Whether an overview of the applied filters should be displayed (`"show"`) or not (`"hide"`). | `"hide` |
| `totalProductsOnMobile` | `enum` | Whether the Filter Navigator should display the total number of products on mobile devices  (`show`) or not (`hide`). | `hide` |
| `fullWidthOnMobile`      | `boolean` | Whether the `filter-navigator.v3` will be rendered on mobile using the screen full width (`true`) or not (`false`).                                                                                                                                               | `false`       |
| `navigationTypeOnMobile` | `Enum`    | Defines how mobile users should navigate on the filter selector component. Possible values are: `page` (only one list of options can be seen at a time) or `collapsible` (all lists of options can be seen at the same time).                                    | `page`        |

#### `order-by` block

Renders a dropdown button with sorting options to display the fetched results (the list of sorting options can be found in the second table below).

| Prop name       | Type            | Description                 | Default value |
| --------------- | --------------- | --------------------------- | ------------- |
| `hiddenOptions` | `[string]` | Indicates which sorting options will be hidden. (e.g. `["OrderByNameASC", "OrderByNameDESC"]`) | `undefined`      |
| `showOrderTitle` | `boolean` | Whether the selected order value (e.g. `Relevance`) will be displayed (`true`) or not (`false`).  | `true`           |

The sorting options are:

| Sorting option           | Value                       |
| ------------------------ | --------------------------- |
| Relevance                | `"OrderByScoreDESC"`        |
| Top Sales Descending     | `"OrderByTopSaleDESC"`      |
| Release Date Descending  | `"OrderByReleaseDateDESC"`  |
| Best Discount Descending | `"OrderByBestDiscountDESC"` |
| Price Descending         | `"OrderByPriceDESC"`        |
| Price Ascending          | `"OrderByPriceASC"`         |
| Name Ascending           | `"OrderByNameASC"`          |
| Name Descending          | `"OrderByNameDESC"`         |
| Collection          | `"OrderByCollection"`         |

#### `search-fetch-more` block

Renders a `Show More` button used to load the results of the next search results page. 

:information_source: *This block is not rendered if there is no next page.*

| Prop name       | Type            | Description                           | Default value |
| --------------- | --------------- | ------------------------------------- | ------------- |
| `htmlElementForButton` | `enum` | Which HTML element will be displayed for `Show more` button component. Possible values are: `a` (displays a `<a>` element with `href` and `rel` attributes)  or `button` (displays a `<button>` element without `href` and `rel` attributes). | `button` |

#### `search-fetch-previous` block

Renders a `Show Previous` button used to load the results of the previous search results page. 

:information_source: *This block is not rendered if there is no previous page.*

| Prop name       | Type            | Description        | Default value |
| --------------- | --------------- | ------------------ | ------------- |
| `htmlElementForButton` | `enum` | Which HTML element will be displayed for `Show previous` button component. Possible values are: `a` (displays a `<a>` element with `href` and `rel` attributes)  or `button` (displays a `<button>` element without `href` and `rel` attributes). | `button` |

#### `search-products-count-per-page` block

Shows the product count per search page. This block does not need any prop when declared.

#### `search-products-progress-bar` block**

Shows a progress bar of search results. This block does not need any prop when declared.

#### `sidebar-close-button` block

`Close` button rendered on the top right of the mobile filter sidebar.

| Prop name       | Type            | Description      | Default value |
| --------------- | --------------- | ---------------- | ------------- |
| `size` | `number` | Size of the button icon | `30`       |
| `type` | `string` | Type of the button icon | `line`       |

## Customization

In order to apply CSS customization in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

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
| `footerButton`                        |
| `galleryItem`                         |
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
    <td align="center"><a href="https://github.com/grupo-exito-ecommerce"><img src="https://avatars2.githubusercontent.com/u/46934781?v=4" width="100px;" alt=""/><br /><sub><b>grupo-exito-ecommerce</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=grupo-exito-ecommerce" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ygorneves10"><img src="https://avatars1.githubusercontent.com/u/39542011?v=4" width="100px;" alt=""/><br /><sub><b>Ygor Neves</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=ygorneves10" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/marcosewbank"><img src="https://avatars3.githubusercontent.com/u/27689698?v=4" width="100px;" alt=""/><br /><sub><b>Marcos André Suarez Ewbank</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=marcosewbank" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/BeatrizMiranda"><img src="https://avatars2.githubusercontent.com/u/28959326?v=4" width="100px;" alt=""/><br /><sub><b>Beatriz Miranda</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=BeatrizMiranda" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/felipeireslan"><img src="https://avatars3.githubusercontent.com/u/47363947?v=4" width="100px;" alt=""/><br /><sub><b>felipeireslan</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=felipeireslan" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

----