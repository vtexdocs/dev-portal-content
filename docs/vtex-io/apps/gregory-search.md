---
title: "Search"
slug: "gregory-search"
excerpt: "gregory.search@2.9.1"
hidden: true
createdAt: "2022-08-05T14:49:20.003Z"
updatedAt: "2022-08-05T14:49:20.003Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

The VTEX Search app is responsible for handling the new [**VTEX Intelligent Search**](https://help.vtex.com/tracks/vtex-intelligent-search) solution in IO stores by providing new UI components that enhance the search experience, such as the autocomplete feature.

![search-app-gif](https://user-images.githubusercontent.com/52087100/82367576-6d196800-99ea-11ea-9672-77fa2b90a581.gif)

## Configuration

:warning: The proper functioning of the Search app components relies on having already installed apps `vtex.admin-search@1.x` and `vtex.search-resolver@1.x` in your store. For more on this, access our Help Center track on [**VTEX Intelligent Search**](https://help.vtex.com/tracks/vtex-intelligent-search).

### Step 1 - Adding the Search app to your theme's dependencies

Add the `search` app to your theme's dependencies in the `manifest.json` as showed below:

```diff
  "dependencies": {
+   "vtex.search": "2.x"
  }
```

You are now able to use all of the blocks exported by the `search` app. Check the full list below:

| Block name                    | Description                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `autocomplete-result-list.v2` | Provides customized autocomplete features in the search bar component, such as top searches, search history, product suggestions or term suggestions. You can read more about the Intelligent Search [autocomplete feature](https://help.vtex.com/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4gXFsEWjF7QF7UtI2GAvhL) on VTEX Help Center. |
| `search-banner`               | Renders a customized banner according to the search query performed.                                                                                                                                                                                                                                                                                  |
| `did-you-mean`                | Helps users with possible misspelling corrections for the current search query.                                                                                                                                                                                                                                                                       |
| `search-suggestions`          | Renders a list of similar search terms for the current search query.                                                                                                                                                                                                                                                                                  |

>:warning: The blocks `search-banner`, `did-you-mean` and `search-suggestions` require you to have [Search Results app](https://vtex.io/docs/components/all/vtex.search-result@3.59.0/) version 3.x or higher installed in your theme.

### Step 2 - Adding the Search's blocks into the theme

First, declare the `autocomplete-result-list.v2` block as a child block of the [`search-bar` block](https://vtex.io/docs/components/all/vtex.store-components/searchbar), exported by the Store Components app. For example:

```json
{
  "search-bar": {
    "blocks": ["autocomplete-result-list.v2"],
    "props": {
      "openAutocompleteOnFocus": true
    }
  }
}
```

#### `autocomplete-result-list.v2` props

| Prop name                     | Type                    | Description                                                                | Default value |
| ----------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `maxTopSearches`              | `number`                | Maximum number of items in the top searches list.                | `10`          |
| `maxHistory`                  | `number`                | Maximum number of items in the search history list.                                                            | `5`           |
| `maxSuggestedProducts`        | `number`                | Maximum number of items in the suggested products list.                                                      | `3`           |
| `maxSuggestedTerms`           | `number`                | Maximum number of items in the suggested terms list.                                                                 | `3`           |
| `autocompleteWidth`           | `number`                | Autocomplete list width (in percent). The value must be between `0` and `100`                                | `undefined`   |
| `productLayout`               | `enum`                  | Defines the suggested products list layout when rendered. Possible values are `HORIZONTAL` and `VERTICAL`.     | `undefined`   |
| `hideTitles`                  | `boolean`               | Defines whether all component titles are hidden when rendered (`true`) or not (`false`).              | `false`       |
| `hideUnavailableItems`                  | `boolean`               | Defines whether the autocomplete should hide unavailable items (`true`) or not (`false`).             | `false`       |
| `historyFirst`                | `boolean`               | Defines whether the search history list should be prioritized over the other lists (`true`) or not (`false`).                                                          | `false`       |
| `customBreakpoints`           | `object`                | Defines a maximum number of suggested products by breakpoints. Possible values are `md`, `lg` or `xlg`.                                                           | -             |
| `simulationBehavior`          | `"skip"` or `"default"` | If you want faster searches and do not care about most up to date prices and promotions, use `"skip"` value.                                                                                                                                                                                                                                                                                                                                                                                    | `default`     |
| `HorizontalProductSummary`          | `product-summary` block | By default, the mobile autocomplete uses the `CustomListItem` component to render the suggested products with a horizontal layout. But if you send a `product-summary` block here, it will render your customized Product Summary component. You can see how to build a horizontal Product Summary component [here](https://vtex.io/docs/recipes/templates/building-a-horizontal-product-summary/)                            | `undefined`     |

- `customBreakpoints` object:

| Prop name | Type     | Description                                                                    | Default value |
| --------- | -------- | ------------------------------------------------------------------------------ | ------------- |
| `md`      | `object` | Defines the maximum number of suggested products for the `md` breakpoint.      | `undefined`   |
| `lg`      | `object` | Defines the the maximum number of suggested products for the `lg` breakpoint.  | `undefined`   |
| `xlg`     | `object` | Defines the the maximum number of suggested products for the `xlg` breakpoint. | `undefined`   |

- `md`, `lg` and `xlg` objects:

| Prop name              | Type     | Description                           | Default value |
| ---------------------- | -------- | ------------------------------------- | ------------- |
| `width`                | `number` | Breakpoint minimum width.             | `undefined`   |
| `maxSuggestedProducts` | `number` | Maximum number of suggested products. | `undefined`   |

The `autocomplete-result-list.v2` block also allows you to add a list of child blocks onto it.

This means that you can declare a theme block of your choosing and have it rendered among the autocomplete features. For example:

```json
{
  "autocomplete-result-list.v2": {
    "blocks": ["product-summary"]
  }
}
```

Now, the time has come to add the last 3 search blocks: `search-banner`, `did-you-mean` and `search-suggestions`.

Those blocks, differently from `autocomplete-result-list.v2`, need to be added under the `search-result-layout.desktop` or the `search-result-layout.mobile` blocks, according to the Search Results block hierarchy.

Once added, these can be declared using their respective props for their configuration. For example:

```json
{
  "search-result-layout.desktop": {
    "children": [
      "flex-layout.row#did-you-mean",
      "flex-layout.row#suggestion",
      "flex-layout.row#banner-one",
      "flex-layout.row#result"
    ],
    "props": {
      "pagination": "show-more",
      "preventRouteChange": true,
      "mobileLayout": {
        "mode1": "small",
        "mode2": "normal"
      }
    }
  },

  "flex-layout.row#did-you-mean": {
    "children": ["did-you-mean"]
  },
  "flex-layout.row#suggestion": {
    "children": ["search-suggestions"]
  },
  "flex-layout.row#banner-one": {
    "children": ["search-banner#one"]
  },

  "search-banner#one": {
    "props": {
      "area": "one",
      "blockClass": "myBanner",
      "horizontalAlignment": "center"
    }
  }
}
```

#### `search-banner` props

| Prop name             | Type     | Description                                                                                                                      | Default value |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `area`                | `string` | Area of ​​the store where the banner will be displayed. It needs to match the predefined area value in the banner setup.         | `undefined`   |
| `blockClass`          | `string` | Unique block ID to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization/) | `undefined`   |
| `horizontalAlignment` | `string` | Defines the banner horizontal alignment. Possible values are `left`, `center` or `right`.                                        | `center`      |

## Modus Operandi

The Search app is merely responsible for offering blocks that when rendered as components will improve the user's search experience in stores where the VTEX Intelligent Search engine is already supported.

These components use `_q` as the query-string for the search term, meaning that if you wish to **track the searches** of your users in these components you'll need to add the `_q` query-string to the store's Google Analytics.

Find out how to do this by accessing our [Google Analytics search tracking](https://vtex.io/docs/recipes/store-management/setting-up-google-analytics-search-tracking/) documentation.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `searchBanner`          |
| `didYouMeanPrefix`      |
| `didYouMeanTerm`        |
| `suggestionsList`       |
| `suggestionsListItem`   |
| `suggestionsListLink`   |
| `itemListSubItemLink`   |
| `itemListLink`          |
| `itemListLinkTitle`     |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes out to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->