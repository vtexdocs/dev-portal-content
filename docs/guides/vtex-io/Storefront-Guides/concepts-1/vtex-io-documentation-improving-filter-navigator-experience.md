---
title: "Improving filter navigator experience"
slug: "vtex-io-documentation-improving-filter-navigator-experience"
hidden: false
createdAt: "2021-04-08T19:44:50.866Z"
updatedAt: "2022-12-13T20:17:44.152Z"
---

The filter navigator is one of the most important components on the search page. This recipe will show you how to set the filter navigator component in a way that has been proven to improve the conversion of your store.

Here is a quick summary of the changes that will be made:

- Add a search input to the filter options list
- Change the filter navigation to use `collapsible` filters
- Add more info about selected filters and product quantity
- Update the search result at the moment that the filter is selected
- Add a show more/less button to the filter options list
- Add a "clear all" button to each filter options list

All props mentioned here are documented on [documentation page](https://developers.vtex.com/docs/guides/vtex-search-result). You will be able to check both the description and the possible values ​​of each prop.

## Instructions

1. Ensure that you have the `vtex.search-result@3.x` as a dependency of your `manifest.json`:

```diff
{
  "dependencies": [
      // other dependencies
+     "vtex.search-result": "3.x"
    }
  ]
}
```

2. Add the following props to the `search-result-layout.desktop` and the `search-result-layout.mobile`:

```diff
"search-result-layout.desktop": {
    "children": [
        // children
    ],
    "props": {
        // props
+       "preventRouteChange": true,
+       "thresholdForFacetSearch": 10,
+       "showProductsCount": true,
+       "showFacetQuantity": true
    }
}
```

```diff
"search-result-layout.mobile": {
    "children": [
        // children
    ],
    "props": {
        // props
+       "preventRouteChange": true,
+       "thresholdForFacetSearch": 10,
+       "showProductsCount": true,
+       "showFacetQuantity": true
    }
}
```

3. Declare the `filter-navigator.v3` block with the following props:

```diff
+ "filter-navigator.v3": {
+     "blocks": ["sidebar-close-button"],
+     "props": {
+         "truncateFilters": true,
+         "showClearByFilter": true,
+         "fullWidthOnMobile": true,
+         "navigationTypeOnMobile": "collapsible",
+         "appliedFiltersOverview": "show",
+         "totalProductsOnMobile": "show",
+         "updateOnFilterSelectionOnMobile": true,
+         "priceRangeLayout": "inputAndSlider"
+     }
+ },
```

4. Your filter-navigator should look like this:

![filter-navigator demo](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-improving-filter-navigator-experience-0.gif)
