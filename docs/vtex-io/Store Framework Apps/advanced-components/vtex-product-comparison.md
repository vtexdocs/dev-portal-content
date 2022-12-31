---
title: "Product Comparison"
slug: "vtex-product-comparison"
excerpt: "vtex.product-comparison@0.17.0"
hidden: false
createdAt: "2020-11-06T16:27:23.648Z"
updatedAt: "2022-06-15T17:27:43.318Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/vtex-io/Store Framework Apps/advanced-components/#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Product Comparison app compares specifications of pre-selected SKUs, allowing store users to better understand their needs when shopping.

The app exports several blocks, which you can leverage from in order to display a Product Comparison drawer on seach results page and a new Product Comparison page in your store.

![Comparison drawer](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-comparison-0.png)
*Product Comparison drawer on the store's search results page*
![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-comparison-1.png)
*Product Comparison page*

## Configuration

### Step 1 - Adding the Product Comparison app to your theme's dependencies

In your theme's `manifest.json` file, add the `Product Comparison` app as a dependency:

```diff
 "dependencies": {
+  "vtex.product-comparison": "0.x"
 }
```

Now, you are able to use all the blocks exported by the Product Comparison app. Check out the full list below:

| Block name   | Description                |
| :--------:   | :------------------------: |
| `product-comparison-drawer` | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-product-comparison-2.png) Main block responsible for rendering the drawer from the Product Comparison component in which the items will be compared. |
| `list-context.comparison-product-summary-slider` | Extends the `list-context` block to built the Product Comparison component using the [Slider Layout](https://vtex.io/docs/components/layout-blocks/vtex.slider-layout/.) |
| `product-summary.shelf.product-comparison` | Extends the default `product-summary.shelf` block (from the [Product Summary app](https://vtex.io/docs/components/all/vtex.product-summary/)) for the Product Comparison component's features. |
| `product-comparison-block` | Logical block that, once extended (see blocks listed below), is responsible for rendering the Product Comparison component's features. |
| `product-comparison-block.selector` | Renders the selector checkbox on the Product Comparison component. |
| `product-comparison-block.close-button` | Renders the close button on the Product Comparison component. |
| `product-comparison-block.product-summary-row` | Renders the first row to list and compare products on the Product Comparison component. |
| `list-context.comparison-row` | Extends the `list-context` block to built a row in the Product Comparison page using the [Slider Layout](https://vtex.io/docs/components/layout-blocks/vtex.slider-layout/.) |
| `product-comparison-block.grouped-product-specifications` | Renders the section for product specification groups. |
| `product-comparison-block.product-specifications` | Renders the section for product specifications. |
| `product-comparison-block.sku-specifications` | Renders the section for SKU specifications. |

### Step 2 - Adding extended interfaces

In the theme's `interfaces.json` file, add the following extented interfaces:

```diff
+{
+  "store.search.product-comparison": {
+    "around": ["comparison-context-wrapper"]
+  },
+  "search-result-layout.desktop.product-comparison": {
+    "allowed": ["product-comparison-drawer"]
+  },
  "store.product.product-comparison": {
    "around": ["comparison-context-wrapper"],
    "allowed": ["product-comparison-drawer"]
  }
+}
```

### Step 3 - Wraping the search blocks with Product Comparison context

1. In the theme's `search.jsonc` file, replace the default `store.search` blocks with the `store.search.product-comparison` blocks as shown in the example below:

```diff
{
  ...
- "store.search": {
+ "store.search.product-comparison": {
    ...
  },
- "store.search#brand": {
+ "store.search.product-comparison#brand": {
    ...
  },
- "store.search#department": {
+ "store.search.product-comparison#department": {
    ...
  }
- "store.search#category": {
+ "store.search.product-comparison#category": {
    ...
  }
- "store.search#subcategory": {
+ "store.search.product-comparison#subcategory": {
    ...
  }
  ...
```

> ℹ️ *The `store.search.product-comparison` blocks will wraps the `store.search` block with comparison context. The replacement is needed so we can synchronously display the selected products in the Product Comparison drawer.*

2. Replace the `search-result-layout.desktop` blocks with the `search-result-layout.desktop.product-comparison` blocks as shown below:

```diff
{
  ...
"search-result-layout": {
  "blocks": [
-   "search-result-layout.desktop#search"
+   "search-result-layout.desktop.product-comparison#search",
    "search-result-layout.mobile",
    "search-not-found-layout"
  ]
},
```

3. Replace the `product-summary.shelf`, child of the `gallery` block, with the `product-summary.shelf.product-comparison`:

```diff
"gallery": {
-  "blocks": ["product-summary.shelf"]
+  "blocks": ["product-summary.shelf.product-comparison#search"]
}
...
```

### Step 4 - Adding the Product Comparison to the product detail Page

1. In the theme's `product.jsonc` file, replace the default `"store.product"` blocks with the `"store.product.product-comparison"` blocks as shown in the example below:

```diff

- "store.product": {
+ "store.product.product-comparison": {
    ...
  }
```

2. add `"product-comparison-drawer"` to the `"store.product.product-comparison"` children as shown in the example below:

```diff
"store.product.product-comparison": {
  children:[
    ...
+    "product-comparison-drawer"
  ]
  ...
}
```

3. add `"product-comparison-block.selector#pdp"` to the `"store.product.product-comparison"` block as shown in the example below:

```diff
 "store.product.product-comparison": {
   ...
  children:[
    ...
+    "product-comparison-block.selector#pdp"
  ]
  ...
 }
 ```
### Step 4 - Building the Product Comparison component

In any desired template, such as the `store.search`, add the `product-comparison-drawer` block as shown below:

```json
- "search-result-layout.desktop#search": {
+ "search-result-layout.desktop.product-comparison#search": {
  "children": [
    "flex-layout.row#did-you-mean",
    "flex-layout.row#suggestion",
    "flex-layout.row#banner-one",
    "flex-layout.row#searchbread",
    "flex-layout.row#searchtitle",
    "flex-layout.row#result",
+   "product-comparison-drawer"
  ],
  "props": {
    "pagination": "show-more",
    "preventRouteChange": false,
    "mobileLayout": {
      "mode1": "small",
      "mode2": "normal"
    }
  }
}
...
```

> ℹ️ *By adding the `product-comparison-drawer` block as showed above, you will be declaring the following structure behind the scenes:*

```json
"product-comparison-drawer": {
  "blocks": ["list-context.comparison-product-summary-slider#drawer"]
},
"list-context.comparison-product-summary-slider#drawer": {
  "blocks": ["product-summary.shelf.product-comparison#drawer"],
  "children": ["slider-layout#comparison-drawer"]
},
"slider-layout#comparison-drawer": {
  "props": {
    "blockClass": "comparison-drawer",
    "itemsPerPage": {
      "desktop": 4,
      "tablet": 3,
      "phone": 1
    },
    "showPaginationDots": "never",
    "infinite": true,
    "fullWidth": true
  }
},
"product-summary.shelf.product-comparison#drawer": {
  "children": [
    "product-summary-column#drawer-col2",
    "product-comparison-block.close-button"
  ],
  "props": {
    "blockClass": "drawer-summary"
  }
},
"product-summary-column#drawer-col2": {
  "children": ["product-summary-name", "product-summary-price#comparison"],
  "props": {
    "blockClass": "drawer-summary-col2"
  }
},
"product-summary-price#comparison": {
  "props": {
    "showListPrice": false,
    "showSellingPriceRange": false,
    "showLabels": false,
    "showInstallments": false,
    "showDiscountValue": false
  }
}
```

> ℹ️ *The code above is a default implementation of the Product Comparison component. If any changes are desired, declare the code above in your theme and perform the needed updates according to the available blocks.*

### Step 5 - Building the Product Comparison page

1. In the `/store/blocks` folder, create a new file called `product-comparison.json` and add in it the following JSON:

```json
"comparison-page": {
  "children": ["slider-layout-group#comparison-page"]
},

"slider-layout-group#comparison-page": {
  "children": [
    "product-comparison-block.product-summary-row",
    "product-comparison-block.grouped-product-specifications"
  ]
},
"product-comparison-block.product-summary-row": {
  "blocks": ["list-context.comparison-product-summary-slider#comparison-page"]
},
"list-context.comparison-product-summary-slider#comparison-page": {
  "blocks": ["product-summary.shelf.product-comparison#comparison-page"],
  "children": ["slider-layout#comparison-page-product-summary"]
},
"product-summary.shelf.product-comparison#comparison-page": {
  "children": [
    "flex-layout.row",
    "product-summary-image#comparison-page",
    "product-summary-name",
    "product-summary-space",
    "product-summary-price#comparison",
    "product-summary-buy-button"
  ],
  "props": {
    "blockClass": "comparison-page-summary"
  }
},
"flex-layout.row": {
  "children": ["product-comparison-block.close-button"],
  "props": {
    "blockClass": "close",
    "horizontalAlign": "right"
  }
},
"product-summary-image#comparison-page": {
  "props": {
    "width": 200,
    "heightProp": 200
  }
},
"product-comparison-block.grouped-product-specifications": {
  "blocks": ["list-context.comparison-row#comparison-page-row"]
},
"list-context.comparison-row#comparison-page-row": {
  "children": ["slider-layout#comparison-no-arrows"]
},
"slider-layout#comparison-page-product-summary": {
  "props": {
    "blockClass": "comparison-page",
    "itemsPerPage": {
      "desktop": 4,
      "tablet": 3,
      "phone": 1
    },
    "showPaginationDots": "never",
    "infinite": true,
    "fullWidth": true
  }
},
"slider-layout#comparison-no-arrows": {
  "props": {
    "itemsPerPage": {
      "desktop": 4,
      "tablet": 3,
      "phone": 1
    },
    "showPaginationDots": "never",
    "infinite": true,
    "fullWidth": true,
    "blockClass": "comparison-page",
    "showNavigationArrows": "never"
  }
}
```

2. In the theme's `routes.json` file, add a new route for the Product Comparison page:

```diff
+{
+  "store.custom#product-comparison-list": {
+    "path": "/product-comparison"
+  }
+}
```

#### `product-comparison-block.grouped-product-specifications` props

| Prop name      | Type          | Description                    | Default value |
| :------------: | :-----------: | :----------------------------: | :-----------: |
| `productSpecificationsToHide` | `[string]` | List of product fields that should be hidden in the Product Comparison page. The desired product fields must be separated by comma. | `undefined` |
| `productSpecificationGroupsToHide` | `[string]` | List of product specification groups that should be hidden on the Product Comparison page. The desired product specification groups must be separated by comma. | `undefined` |

#### `product-comparison-block.product-specifications` props

| Prop name      | Type          | Description                    | Default value |
| :------------: | :-----------: | :----------------------------: | :--------:    |
| `productSpecificationsToHide` | `[string]` | List of product fields that should be hidden in the Product Comparison page. The desired product fields must be separated by comma. | `undefined` |

#### `product-comparison-block.sku-specifications` props

| Prop name      | Type          | Description                    | Default value |
| :------------: | :-----------: | :----------------------------: | :--------:    |
| `skuSpecificationsToHide` | `[string]` | List of SKU specification fields that should be hidden on the Product Comparison page. The desired SKU specification fields must be separated by comma. | `undefined` |

#### `product-comparison-block.product-summary-row` props

| Prop name      | Type          | Description                    | Default value |
| :------------: | :-----------: | :----------------------------: | :--------:    |
| `isShowDifferenceDefault` | `boolean` | Set the "show only differences" checkbox to true as the default value on the comparison page. | `false` |
=======

### Step 6 - Change the comparison bucket size

This is optional configuration, you can change the maximum number of items in comparison bucket by giving fixed number in app configuration. 
Default value is 10 items, when you exceed maximum limit you will get a notification.

#### Steps

1. Go to `/admin/apps`, you will find `Product Comparison` app under `installed` apps
2. Click on settings 
3. Put the maximum comparison bucket size in your application

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                  |
| :--------------------------: |
| `closeButton`                |
| `closeButtonContainer`       |
| `compareProductsButton`      |
| `comparisonButtons`          |
| `comparisonCol`              |
| `drawer`                     |
| `drawerContainer`            |
| `expandCollapseButton`       |
| `fieldNameCol`               |
| `fieldNameCol`               |
| `productFieldValue`          |
| `productSelectorContainer`   |
| `productSpecificationValue`  |
| `productSpecificationValues` |
| `productSummaryRowContainer` |
| `rowContainer`               |
| `showDifferencesContainer`   |
| `skuFieldValue`              |
| `skuSpecificationValue`      |
| `skuSpecificationValues`     |
| `title`                      |
| `removeAllItemsButtonWrapper`|
| `compareProductButtonWrapper`|
| `removeAllWrapper`           |
| `drawerTitleOuterContainer`  |
| `drawerTitleInnerContainer`  |
| `drawerOpened`               |
| `drawerClosed`               |

<!-- DOCS-IGNORE:start -->
## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->