---
title: "VTEX Search Result"
slug: "cea-search-result"
excerpt: "cea.search-result@1.49.0"
hidden: true
createdAt: "2022-07-08T12:29:00.854Z"
updatedAt: "2022-07-08T12:29:00.854Z"
---
[![Build Status](https://api.travis-ci.org/vtex-apps/search-result.svg?branch=master)](https://travis-ci.org/vtex-apps/search-result) <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Description

The VTEX Search Result app is a store component that handles with the result of our [_Search API_](https://documenter.getpostman.com/view/845/vtex-search-api/Hs43#8b71745e-00f9-6c98-b776-f4468ecb7a5e), and this app is used by store theme.

:loudspeaker: **Disclaimer:** Don't fork this project; use, contribute, or open issue with your feature request.

### Supported Blocks

This are the current supported blocks in this repository. Blocks not mentioned are deprecated.

| Block name                         | Component                                                            | Description                                                                                                                                         |
| ---------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gallery`                          | [Gallery](react/Gallery)                                             | Gallery that displays found products                                                                                                                |
| `not-found`                        | [NotFoundSearch](react/NotFoundSearch)                               | Block containing text and description that search was not found                                                                                     |
| `search-result-layout`             | [SearchResultLayout](react/SearchResultLayout)                       | Layout block that enables user to build a custom search page                                                                                        |
| `search-result-layout.customQuery` | [SearchResultLayoutCustomQuery](react/SearchResultLayoutCustomQuery) | Just like `search-result-layout` but accepts a `querySchema` prop to execute custom query.                                                          |
| `search-result-layout.desktop`     | [SearchResultFlexible](react/SearchResultFlexible)                   | Block used to build layout for desktop.                                                                                                             |
| `search-result-layout.mobile`      | [SearchResultFlexibleMobile](react/SearchResultFlexibleMobile)       | Block used to build layout for mobile.                                                                                                              |
| `search-not-found-layout`          | [NotFoundLayout](react/NotFoundLayout)                               | Block used to layout when a user searches for a product that does not exist.                                                                        |
| `search-layout-switcher`           | [LayoutModeSwitcherFlexible](react/LayoutModeSwitcherFlexible)       | Enables user to switch between layout modes in mobile                                                                                               |
| `search-content`                   | [SearchContent](react/SearchContent)                                 | Block that chooses to show the `gallery` block if products are found and `not-found` if filters selected lead to an empty search                    |
| `search-fetch-more`                | [FetchMore](react/FetchMore)                                         | Renders the fetch more button if pagination is of type `show-more`. If it is infinite scroll, shows the `Loader` when bottom of the page is reached |
| `search-fetch-previous`            | [FetchPrevious](react/FetchPrevious)                                 | Renders the fetch previous button.                                                                                                                  |
| `search-products-count-per-page`   | [ProductCountPerPage](react/ProductCountPerPage)                     | Shows the total count of products displayed in search at the moment.                                                                                |
| `order-by.v2`                      | [OrderByFlexible](react/OrderByFlexible)                             | Allows user to pick the type of order of the products displayed.                                                                                    |
| `filter-navigator.v3`              | [FilterNavigatorFlexible](react/FilterNavigatorFlexible)             | Allows user to apply different filters to search. On mobile, renders a button that shows the sidebar when pressed.                                  |
| `total-products.v2`                | [TotalProductsFlexible](react/TotalProductsFlexible)                 | Shows the total products count found for that search.                                                                                               |
| `search-title.v2`                  | [SearchTitleFlexible](react/SearchTitleFlexible)                     | Display search title according to the search context.                                                                                               |

### Flexible Layout Update

`search-result` now supports a flexible layout and has all its benefits, specially using the `flex-layout` block.

You now have access to `search-result-layout`, it supports three different blocks: `search-result-layout.desktop`, `search-result-layout.mobile`, `search-not-found-layout`.

`search-result-layout.desktop` is rendered when user is using a desktop. The `.mobile` interface is rendered (if provided), when user is using a mobile device. If the `.mobile` is not provided, the `.desktop` will be used.

The `search-not-found-layout` is used (if provided) when the user searches for a term that returns nothing.

> **Important notice:** if the user lands on a search page and adds filters until it reachs a empty search, this block will not be rendered! Instead, the `not-found` component, **which is currently not flexible**, will.

We also created the `search-result-layout.customQuery`. If you want to display a custom search-result, by passing a custom querySchema, this block should be used. `search-result-layout` does not read the values of a `querySchema` prop!

To pass parameters to the search displayed at `search-result-layout` you should use the `context` props in `store.search`. Example:

```js
"store.search": {
    "blocks": [
      "search-result-layout"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  },
```

If you want to use the `.customQuery`:

```json
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
      "orderByField": "OrderByReleaseDateDESC",
      "hideUnavailableItems": true,
      "facetsBehavior": "Dynamic",
      "maxItemsPerPage": 48,
      "queryField": "clothing",
      "mapField": "c",
      "skusFilter": "FIRST_AVAILABLE"
    }
  },
  "blocks": ["search-result-layout.desktop"]
}
```

In order to be used inside the flexible block, we created: `breadcrumb.search`, `search-fetch-more`, `search-fetch-previous`, `search-content`, `search-products-count-per-page`, `filter-navigator.v3`, `total-products.v2`, `order-by.v2` & `search-title.v2`.

Noticeable notes:

- `search-fetch-more` renders the fetch more button. Infinite-scroll was deprecated.
- `search-content` renders the gallery or the not-found block, depending on the products returned for the specified filters.
- `search-products-count-per-page` renders the current products count displayed.
- All `*.v2` or `.v3` is just a version bump, no changes in behaviour, the changes are that the new components now fetch the data from the search page context and should only be used in the flexible layout. Also changes the wrapper css class, usually by just adding a `--layout` to the previous used class (like `filters` to `filters--layout`).

Read more at the `Max Items Per Page Usage` section.

## Important Note

We ask for users, from now on, to use the `filter-navigator.v2` block if you want to keep updated with the most up to date Filter Navigator in your search-result.

The correct way to use it is setting it in your `blocks.json` like:

```
json
"search-result": {
    "blocks": [
      "filter-navigator.v2",
      "gallery",
      "not-found",
      "breadcrumb",
      "order-by",
      "total-products"
    ],
  }
```

Or via Storefront.

## Max Items Per Page Usage

Disclaimer: this notice is deprecated, please use the `search-result-layout` block.
A `search-result` block may appear in two different contexts, (a) in a search result page (store.search) or (b) as a block in your home page (store.home).

In case of (a) we can configure the search parameters in a search context in the following way:

```json
  "store.search": {
    "blocks": [
      "search-result"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  },
 "store.search#category": {
    "blocks": [
      "search-result"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  },
  "store.search#brand": {
    "blocks": [
      "search-result"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  },
  "store.search#department": {
    "blocks": [
      "search-result"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  },
  "store.search#subcategory": {
    "blocks": [
      "search-result"
    ],
    "props": {
        "context": {
           "orderByField": "OrderByReleaseDateDESC",
            "hideUnavailableItems": true,
            "facetsBehavior": "Dynamic",
            "maxItemsPerPage": 48,
            "skusFilter": "FIRST_AVAILABLE"
        }
     }
  }
```

Note that only in this case, the parameters must be passed in the `context` prop of the `store.search` block. Also remember that we have different `store.search` blocks and you may configure them in different ways.
You may configure a brand search (ended with /b), have 6 items per page, while a department search page, that number may be 12.

Search examples:
Free search: https://storetheme.vtex.com/shirt?map=ft. Falls on: `store.search`.
Departament: https://storetheme.vtex.com/decoration/d. Falls on: `store.search#department`.
Category: https://storetheme.vtex.com/bags/necessaire. Falls on: `store.search#category Subcategory: https://storetheme.vtex.com/decoration/smartphones/bateria. Falls on:`store.search#subcategory`. Brand: https://storetheme.vtex.com/kawasaki/b. Falls on:`store.search#brand`.

Now for option (b), when we want to show the `search-result` block outside of a search page, like in the home page, the same parameters must be passed on a different way.

At our example, we want to show a `search-result` inside a `store.home`. We put this inside our blocks.json:

```json
"store.home": {
  "blocks": [
    "carousel#home",
    "shelf#home",
    "search-result#home"
  ]
}
```

Now, to change the search done by this block, we must pass its parameters directly to it, thorugh the `querySchema` prop:

```json
"store.home": {
  "blocks": [
    "carousel#home",
     "shelf#home",
    "search-result#home"
  ]
},
"search-result#home": {
  "props": {
    "querySchema": {
      "orderByField": "OrderByReleaseDateDESC",
      "hideUnavailableItems": true,
      "facetsBehavior": "Dynamic",
      "maxItemsPerPage": 48,
      "skusFilter": "FIRST_AVAILABLE"
    }
  }
}
```

## Release schedule

| Release |       Status        | Initial Release | Maintenance LTS Start | End-of-life | Store Compatibility |
| :-----: | :-----------------: | :-------------: | :-------------------: | :---------: | :-----------------: |
|  [3.x]  | **Current Release** |   2018-12-01    |                       |             |         2.x         |
|  [2.x]  | **Maintenance LTS** |   2018-10-02    |      2018-12-01       | March 2019  |         1.x         |

See our [LTS policy](https://github.com/vtex-apps/awesome-io#lts-policy) for more information.

## Table of Contents

- [Usage](#usage)
  - [Blocks API](#blocks-api)
    - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS namespaces](#css-namespaces)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Tests](#tests)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder [click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

We add the search-result as a block in our [Store](https://github.com/vtex-apps/store/blob/master/store/interfaces.json).

To configure or customize this app, you need to import it in your dependencies in `manifest.json`.

```json
  dependencies: {
    "vtex.search-result": "3.x"
  }
```

Then, add `search-result` block into your app theme as we do in our [Store theme app](https://github.com/vtex-apps/store-theme/blob/master/store/blocks.json).

Now, you can change the behavior of the search result block that is in the store header. See an example of how to configure:

```json
  "search-result#department": {
    "blocks": [
      "filter-navigator.v2",
      "gallery",
      "not-found",
      "breadcrumb",
      "order-by",
      "total-products",
      "search-title"
    ],
    "props": {
      "context": {
        "maxItemsPerPage": 48,
        "orderByField": "OrderByReleaseDateDESC"
      },
      "hiddenFacets": {
        "layoutMode1": "normal",
        "layoutMode2": "small",
        "specificationFilters": {
          "hiddenFilters": []
        }
      },
      "pagination": "show-more"
    }
  },
```

### Blocks API

When implementing this app as a block, various inner blocks may be available. The following interface lists the available blocks within search result and describes if they are required or optional.

```json
"search-result": {
    "allowed": [
      "not-found",
      "breadcrumb",
      "filter-navigator",
      "total-products",
      "order-by",
      "search-title"
    ],
    "required": [
      "gallery"
    ],
    "component": "index"
  },
```

The search-result has as a required block the `gallery`. So, any search-result block implementation created must add a gallery as a block that is inside of search-result. Similarly, `gallery` has its own inner block structure that can be configured that you can see below.

```json
 "gallery": {
    "required": [
      "product-summary"
    ],
    "component": "Gallery"
  }
```

The gallery has as a required block the `product-summary`. So, any gallery block implementation created must add a product-summary as a block that is inside of gallery. (Similarly, `product-summary` has its own inner block structure that can be configured. There is a link to its API in the next section.)

### Configuration

#### Layout API

These properties can be changed in the `blocks.json` file of your theme.

| Prop name           | Type           | Description                                                                                                                          | Default value     |
| ------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| `querySchema`       | `QuerySchema`  | Query made when there's no context                                                                                                   | N/A               |
| `hiddenFacets`      | `HiddenFacets` | Indicates which facets will be hidden                                                                                                | N/A               |
| `pagination`        | `Enum`         | Pagination type (values: 'show-more' or 'infinite-scroll')                                                                           | `infinity-scroll` |
| `mobileLayout`      | `MobileLayout` | Control mobile layout                                                                                                                | N/A               |
| `showFacetQuantity` | `Boolean`      | If quantity of items filtered by facet should appear besides its name on `filter-navigator`                                          | `false`           |
| `blockClass`        | `String`       | Unique class name to be appended to block classes                                                                                    | `""`              |
| `showProductsCount` | `Boolean`      | controls if the quantity of loaded products and total number of items of a search result are displayed under the `show more` button. | `false`           |

##### QuerySchema

| Prop name              | Type             | Description                                                                                                                                                                                           | Default value     |
| ---------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `maxItemsPerPage`      | `Number`         | Maximum number of items per search page. The maximum value of this prop is `50`, if a number bigger than this one is passed, the query will fail.                                                                                                                                                               | 10                |
| `queryField`           | `String`         | Query field                                                                                                                                                                                           | N/A               |
| `mapField`             | `String`         | Map field                                                                                                                                                                                             | N/A               |
| `restField`            | `String`         | Other Query Strings                                                                                                                                                                                   | N/A               |
| `orderByField`         | `Enum`           | Order by field (values: `OrderByTopSaleDESC`, `OrderByReleaseDateDESC`, `OrderByBestDiscountDESC`, `OrderByPriceDESC`, `OrderByPriceASC`, `OrderByNameASC`, `OrderByNameDESC` or `OrderByScoreDESC` (by relevance)) | `OrderByScoreDESC`              |
| `hideUnavailableItems` | `Boolean`        | Set if unavailable items should show on search                                                                                                                                                        | `false`           |
| `facetsBehavior` | `String`        | Set if specificationFilters will be ignored when getting the facets. If set to `Static`, you will be able to filter your search result with facets of the same specification filters, making it possible to make an `or` filter. If set to `Dynamic`, you won't be able to filter by `or` but the facets will be smarter and will only show the facets that will have at least one result.                                                                                                                                                        | `Static`           |
| `skusFilter`           | `SkusFilterEnum` | Control SKUs returned for each product in the query. The less SKUs needed to be returned, the more performant your shelf query will be.                                                               | `"ALL_AVAILABLE"` |
| `simulationBehavior`           | `SimulationBehaviorEnum` | Set to "skip" value if you want faster queries and do not care about most up to date prices or stock.                                                               | `"default"` |

`SkusFilterEnum`:
| Name | Value | Description |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| First Available | `FIRST_AVAILABLE` | Most performant, ideal if you do not have a SKU selector in your shelf. Will return only the first available SKU for that product in your shelf query. |
| All Available | `ALL_AVAILABLE` | A bit better performace, will only return SKUs that are available, ideal if you have a SKU selector but still want a better performance. |
| All | `ALL` | Returns all SKUs related to that product, least performant option. |

`SimulationBehaviorEnum`:
| Name | Value | Description |
| --------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Default | `default` | Does not change anything, catalog will simulate all skus and deliver most up to date prices and stock. |
| Skip Simulation | `skip` | Catalog will not simulate any sku making the query faster but prices and stock will have the value of the last indexation. |

##### HiddenFacets

| Prop name              | Type                   | Description                 | Default value |
| ---------------------- | ---------------------- | --------------------------- | ------------- |
| `brands`               | `Boolean`              | Hide Brands filter          | false         |
| `categories`           | `Boolean`              | Hide Categories filter      | false         |
| `priceRange`           | `Boolean`              | Hide Price filter           | false         |
| `specificationFilters` | `SpecificationFilters` | Hide Specifications filters | N/A           |

##### SpecificationFilters

| Prop name       | Type                      | Description                                           | Default value |
| --------------- | ------------------------- | ----------------------------------------------------- | ------------- |
| `hideAll`       | `Boolean`                 | Hide specifications filters                           | false         |
| `hiddenFilters` | `Array(HiddenFilterUnit)` | Array of specifications filters that should be hidden | N/A           |

##### HiddenFilterUnit

| Prop name | Type    | Description                         | Default value |
| --------- | ------- | ----------------------------------- | ------------- |
| name      | String! | Name of Hidden specification filter | ""            |

##### MobileLayout

This prop controls the way search results are displayed on mobile. The default values are shown below.

Notice that the default behavior for your store will be the one defined by the `mode1`. If you want the user to be able to switch between two modes, you must specify the `mode2` prop. If only the `mode1` is provided, the layout switcher will not be shown and search results will always be rendered according to `mode1`.

| Prop name | Type   | Description                                                           | Default value |
| --------- | ------ | --------------------------------------------------------------------- | ------------- |
| `mode1`   | `Enum` | Layout mode of the switcher (values: 'normal', 'small' or 'inline')   | `normal`      |
| `mode2`   | `Enum` | Layout mode of the switcher 2 (values: 'normal', 'small' or 'inline') | `small`       |

##### `filter-navigator` block

| Prop name            | Type      | Description                                                                                                                                                    | Default value |
| -------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `preventRouteChange` | `Boolean` | Prevents route change when selecting filters, using the query string instead. Intended for `search-result` blocks inserted on custom pages with static routes. | `false`       |
| `initiallyCollapsed` | `Boolean` | Makes the search filters start out collapsed.                                                                                                                  | `false`       |

##### `filter-navigator.v2` block

| Prop name             | Type      | Description                                                                                                                                                    | Default value |
| --------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `preventRouteChange`  | `Boolean` | Prevents route change when selecting filters, using the query string instead. Intended for `search-result` blocks inserted on custom pages with static routes. | `false`       |
| `initiallyCollapsed`  | `Boolean` | Makes the search filters start out collapsed.                                                                                                                  | `false`       |
| `alwaysOnDesktopView` | `Boolean` | Block filter's layout mode on Desktop.                                                                                                                         | `false`       |

##### `filter-navigator.v3` block

| Prop name | Type                      | Description                                                                                       | Default value |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------- | ------------- |
| `layout`  | `responsive` or `desktop` | Which layout should it use. One might use `desktop` when adding filter-navigator inside a drawer. | `responsive`  |

Also, you can configure the product summary that is defined on search-result. See [here](https://github.com/vtex-apps/product-summary/blob/master/README.md#configuration) the Product Summary API.

##### `order-by` block

| Prop name       | Type            | Description                                                                                                  | Default value |
| --------------- | --------------- | ------------------------------------------------------------------------------------------------------------ | ------------- |
| `hiddenOptions` | `Array(String)` | Indicates which [sort options](#sort_options) will be hidden. (e.g. `["OrderByNameASC", "OrderByNameDESC"]`) | `[]`          |

###### `SORT_OPTIONS`

| Option                   | Value                       |
| ------------------------ | --------------------------- |
| Relevance                | `"OrderByScoreDESC"`        |
| Top Sales Descending     | `"OrderByTopSaleDESC"`      |
| Release Date Descending  | `"OrderByReleaseDateDESC"`  |
| Best Discount Descending | `"OrderByBestDiscountDESC"` |
| Price Descending         | `"OrderByPriceDESC"`        |
| Price Ascending          | `"OrderByPriceASC"`         |
| Name Ascending           | `"OrderByNameASC"`          |
| Name Descending          | `"OrderByNameDESC"`         |

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `vtex.searchResult.css` inside the `styles/css` folder. Add your custom styles:

```css
.container {
  margin-top: 10px;
}
```

#### Customization

| CSS handles                           |
| ------------------------------------- |
| `container`                           |
| `buttonShowMore`                      |
| `showingProducts`                     |
| `showingProductsCount`                |
| `switch`                              |
| `breadcrumb`                          |
| `filter`                              |
| `resultGallery`                       |
| `border`                              |
| `gallery`                             |
| `filterPopupButton`                   |
| `accordionFilter`                     |
| `filterAccordionItemBox`              |
| `filterAccordionBreadcrumbs`          |
| `filterButtonsBox`                    |
| `filterPopupFooter`                   |
| `accordionFilterItemOptions`          |
| `dropdownMobile`                      |
| `accordionFilterItemActive`           |
| `totalProducts`                       |
| `totalProductsMessage`                |
| `orderBy`                             |
| `orderByText`                         |
| `accordionFilterItemHidden`           |
| `accordionFilterItem`                 |
| `accordionFilterItemBox`              |
| `accordionFilterItemTitle`            |
| `accordionFilterItemIcon`             |
| `filterAvailable`                     |
| `filterSelected`                      |
| `filterPopupTitle`                    |
| `filterPopupArrowIcon`                |
| `filterMessage`                       |
| `footerButton`                        |
| `layoutSwitcher`                      |
| `filterPopup`                         |
| `filterPopupOpen`                     |
| `filterPopupContent`                  |
| `filterPopupContentContainer`         |
| `filterPopupContentContainerOpen`     |
| `galleryItem`                         |
| `searchNotFound`                      |
| `filterContainer`                     |
| `filterContainer--title`              |
| `filterContainer--selectedFilters`    |
| `filterContainer--c`                  |
| `filterContainer--b`                  |
| `filterContainer--priceRange`         |
| `filterContainer--` + FACET_TYPE      |
| `filterTitle`                         |
| `filterIcon`                          |
| `filterTemplateOverflow`              |
| `galleryTitle`                        |
| `filterItem`                          |
| `filterItem--` + FACET_VALUE          |
| `filterItem--selected`                |
| `selectedFilterItem`                  |
| `orderByButton`                       |
| `orderByDropdown`                     |
| `orderByOptionsContainer`             |
| `orderByOptionItem`                   |
| `categoriesContainer`                 |
| `categoryGroup`                       |
| `categoryParent`                      |
| `searchNotFoundOops`                  |
| `searchNotFoundInfo`                  |
| `searchNotFoundWhatDoIDo`             |
| `searchNotFoundWhatToDoDots`          |
| `searchNotFoundWhatToDoDotsContainer` |
| `searchNotFoundTerm`                  |
| `searchNotFoundTextListLine`          |
| `loadingOverlay`                      |
| `searchResultContainer`               |
| `loadingSpinnerOuterContainer`        |
| `loadingSpinnerInnerContainer`        |

## Troubleshooting

You can check if others are experiencing similar issues [here](https://github.com/vtex-apps/search-result/issues). Also feel free to [open issues](https://github.com/vtex-apps/search-result/issues/new).

## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project.

## Tests

To execute our tests go to `react/` folder and run `npm test`

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/grupo-exito-ecommerce"><img src="https://avatars2.githubusercontent.com/u/46934781?v=4" width="100px;" alt="grupo-exito-ecommerce"/><br /><sub><b>grupo-exito-ecommerce</b></sub></a><br /><a href="https://github.com/vtex-apps/search-result/commits?author=grupo-exito-ecommerce" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!