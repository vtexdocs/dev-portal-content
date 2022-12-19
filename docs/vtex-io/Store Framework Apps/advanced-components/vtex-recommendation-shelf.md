---
title: "Product Recommendation"
slug: "vtex-recommendation-shelf"
excerpt: "vtex.recommendation-shelf@1.7.1"
hidden: true
createdAt: "2020-06-03T15:19:30.034Z"
updatedAt: "2022-07-07T13:16:16.542Z"
---
> ⚠️ **Warning**
>
> This app is on alpha version, which means we are working to improve it and it is not possible to add other accounts for tests. If you have any questions, please contact [our Support](https://support.vtex.com/hc/en-us/requests).

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
 
The Product Recommendation app shows a selection of products using [recommendation strategies](#recommendation-shelf-props). For example, you can use the Product Recommendation to suggest often bought-together products to the one that the user is looking for.
 
![recommendation-shelf-buy-together](https://user-images.githubusercontent.com/52087100/96002543-9c07fe80-0e0f-11eb-94c3-cac778eaf21c.png)
 
## Prerequisites
 
> ℹ️ The Product Recommendation app does not fetch user data for itself. However, most recommendation strategies require user navigation data to provide relevant suggestions to users. Hence, before proceeding any further, make sure you have an app capable of tracking user navigation installed on your VTEX account.
 
Make sure you have the Biggy pixel app installed on your VTEX account or install it by the following steps:
 
1. Open a [Support ticket](https://support.vtex.com/hc/en-us/requests) about your interest in installing the Recommendations Shelf and Biggy Pixel apps. You should expect an App Key as a response. Save it for the 6th step of this tutorial.
2. Using your terminal, install the `biggy.pixel` app by running the following command:
 
```
vtex install biggy.pixel
```
 
3. Access your VTEX account by the Admin.
4. Using the Admin's sidebar, access the **Apps** section and select the **Biggy Pixel** app.
5. Click on **Settings**.
6. In the `apiKey` field, enter the App Key provided by the VTEX team.
7. Save your changes.
 
## Configuration
 
1. Using your terminal, install the `recommendation-resolver` app on your account. This app will solve the recommendation queries of your store shelves.
 
```
vtex install vtex.recommendation-resolver
```
 
2. Add the `recommendation-shelf` app to your theme's dependencies on the `manifest.json`:
 
 
```diff
  "dependencies": {
+   "vtex.recommendation-shelf": "1.x"
  }
```
 
Now, you can use all blocks exported by the `recommendation-shelf` app. Check out the complete list below:
\
&nbsp;


| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `recommendation-shelf` | Displays a list of recommended products on any store page.   |
| `recommendation-buy-together` | Displays a list of recommended products to buy together on the product details page. |
| `recommendation-refresh` | Displays a list of recommended products based on the user history on your store pages. |

\
&nbsp;

`recommendation-shelf`
 
![recommendation-shelf](https://raw.githubusercontent.com/vtex-apps/recommendation-shelf/master/docs/image%20(31).png)
 

`recommendation-buy-together`
 
![recommendation-buy-together](https://raw.githubusercontent.com/vtex-apps/recommendation-shelf/master/docs/image%20(32).png)
 

 
`recommendation-refresh`

![recommendation-refresh](https://raw.githubusercontent.com/vtex-apps/recommendation-shelf/master/docs/Screenshot_3.png)

 
3. Add the `recommendation-shelf` app to your store template. See the example below to know how to add it to a template:
 
```json
  "store.home": {
    "blocks": [
      "flex-layout.row#recommendation-shelf",
    ]
  },
  "flex-layout.row#recommendation-shelf": {
    "children": ["recommendation-shelf"]
  }
```
 
> ℹ️ You can add the `recommendation-shelf` in any store template desired, such as the `store.home` or `store.product`. You can also add the `recommendation-buy-together` and `recommendation-refresh` blocks if desired. For example:
 
```json
  "store.product": {
    "blocks": [
      "flex-layout.row#buy-together",
    ]
  },
  "flex-layout.row#buy-together": {
    "children": ["recommendation-buy-together"]
  }
```
 
```json
  "store.home": {
    "blocks": [
      "flex-layout.row#recommendation-refresh",
    ]
  },
  "flex-layout.row#recommendation-refresh": {
    "children": ["recommendation-refresh"]
  }
```
 
## Setting up the `recommendation-shelf`
 
To configure the `recommendation-shelf` you will need to add props to it. Check the following tables to know what props that the app includes and how to configure them. 
 
### `recommendation-shelf` props
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value      |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ------------------ |
| `strategy`           | `enum`    | Strategy used to fetch and display the recommended products. Check all possible values in the [table](#strategy-and-secondarystrategy-props) below.   | `BEST_SELLERS` |
| `secondaryStrategy`  | `enum`    | Secondary strategy used to fetch and display the recommended products if the initial strategy does not return results. This prop is optional. Check all possible values in the [table](#strategy-and-secondarystrategy-props) below. | `BEST_SELLERS` |
| `recommendation`     | `object`  | Settings for the recommendation shelf component. Here you can define the total and the minimum number of recommendations that should be fetched  | Check the `recommendation` props  |

\
&nbsp;

### `strategy` and `secondaryStrategy` props
\
&nbsp;

| Strategy         | Description                                                                    | 
| ------------------------- | ------------------------------------------------------------------------------ | 
| `BEST_SELLERS`            | Fetches and displays the best seller products.          |
| `MOST_POPULAR`            | Fetches and displays the most popular products. | 
| `PRICE_REDUCTION`         | Fetches and displays products with reduced prices. |
| `NEW_RELEASES`            | Fetches and displays the latest released products.       | 
| `NAVIGATION_HISTORY`      | Fetches and displays products based on the user's navigation history.                        | 
| `SIMILAR_PRODUCTS`        | Fetches and displays recommendations based on the similarity of products on the currently displayed product. This prop only works in the theme template `store.product` and `store.search`. | 
| `BEST_CHOICE`             | Fetches and displays the most visited and ordered products based on the similarity of products on the currently displayed product page. This prop only works in the theme template `store.product` and `store.search`. | 
| `BOUGHT_TOGETHER`         | Fetches and displays recommendations for products often bought together based on the similarity of products on the currently displayed product page. This prop only works in the theme template `store.product` and `store.search`. | 
| `RECOMMENDATION_HISTORY` | Fetches and displays the most relevant products based on a specific customer history.   |
| `CART_HISTORY`           | Fetches and displays products based on the user's cart history.         | 
| `ORDER_HISTORY`          | Fetches and displays products based on the user's order history.        |

\
&nbsp;

See the example below to know how to add it to your template:
 
```json
{
  "store.home": {
    "blocks": ["flex-layout.row#recommendation-shelf"]
  },
  "flex-layout.row#recommendation-shelf": {
    "children": ["recommendation-shelf"]
  },
  "recommendation-shelf": {
    "props": {
      "strategy": "MOST_POPULAR",
      "secondaryStrategy": "NEW_RELEASES",
      "recommendation": {}
    }
  }
}
```
 
 
For each `strategy` and `secondaryStrategy`, you can apply props to specific pages. The possible page types are in the table below:

\
&nbsp;

| Page type        | Description                                                                    |  Available to the `strategy` and `secondaryStrategy`|
| ------------------------- | ------------------------------------------------------------------------------ | ------------|
| `HOME`            |  Recommendations are displayed on the Home page. This context selects the recommended products based on the last categories viewed by the user. If there is no past data from the user, it returns the store data.          | `BEST_SELLERS`, `MOST_POPULAR`, `PRICE_REDUCTION`, `NEW_RELEASES`, `NAVIGATION_HISTORY`, `RECOMMENDATION_HISTORY`, `ORDER_HISTORY` |
| `PLP`            | Recommendations are displayed on the Product List Page. This context uses the category of the first products on the list to select the recommended products.   | `BEST_SELLERS`, `MOST_POPULAR`, `PRICE_REDUCTION`, `NEW_RELEASES`, `NAVIGATION_HISTORY`, `RECOMMENDATION_HISTORY`, `ORDER_HISTORY`, `SIMILAR_PRODUCTS` , `BEST_CHOICE` , `RECOMMENDATION_HISTORY` |
| `PDP`         | Recommendations are displayed on the Product Description Page. This context uses the product information as a param to select the recommended products. | `BEST_SELLERS`, `MOST_POPULAR`, `PRICE_REDUCTION`, `NEW_RELEASES`, `NAVIGATION_HISTORY`, `RECOMMENDATION_HISTORY`, `ORDER_HISTORY`, `SIMILAR_PRODUCTS`, `BEST_CHOICE`, `BOUGHT_TOGETHER`, `RECOMMENDATION_HISTORY`  |
| `CART`            | Recommendations are displayed on the Cart page. This context uses the product category in the cart as a param to select the recommended products.      | `CART_HISTORY`, `SIMILAR_PRODUCTS`|
| `OTHERS`      | Recommendations are displayed on the other store pages, such as My Account. This context will return the store data or user’s navigation history.                        | `BEST_SELLERS`, `MOST_POPULAR`, `PRICE_REDUCTION`, `NEW_RELEASES`, `NAVIGATION_HISTORY`, `RECOMMENDATION_HISTORY`, `ORDER_HISTORY`|
 
\
&nbsp;
  
### `recommendation` props
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ----- |
| `count`              | `object`  | Defines the total and the minimum number of recommendations that should be fetched. | `{"minimum": 5, "recommendations": 20}` |
 
\
&nbsp;

### `count` object
\
&nbsp;

| Prop name         | Type      | Description                                                    | Default value |
| ----------------- | --------- | -------------------------------------------------------------- | ------------- |
| `minimum`         | `number`  | Defines the minimum recommendations that should be fetched.   | `5`             |
| `recommendations` | `number`  | Defines the total number of recommendations that should be fetched. | `20`           |
 
\
&nbsp;

See the example below to know how to add it to your template:
 
```json
{
  "store.home": {
    "blocks": ["flex-layout.row#recommendation-shelf"]
  },
  "flex-layout.row#recommendation-shelf": {
    "children": ["recommendation-shelf"]
  },
  "recommendation-shelf": {
    "props": {
      "strategy": "MOST_POPULAR",
      "secondaryStrategy": "NEW_RELEASES",
      "recommendation": {
        "count": {
          "minimum": 5,
          "recommendations": 20
        }
      }
    }
  }
}
```
## Setting up the `recommendation-buy-together`
 
To configure the `recommendation-buy-together` you will need to add props to it. Check the following tables to know what props that the app allows and how to configure them.
 
### `recommendation-buy-together` props

> ℹ️ The only possible value for `strategy` is `BOUGHT_TOGETHER`.
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value      |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ------------------ |
| `recommendation`     | `object`  | Settings for the recommendation shelf.  | `undefined` |

\
&nbsp;

### `recommendation` object
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ----- |
| `count`              | `object`  | Defines the total and the minimum number of recommendations that should be fetched. | `{minimum: 5, recommendations: 20}` |

\
&nbsp;
 
### `count` object
\
&nbsp;

| Prop name         | Type      | Description                                                    | Default value |
| ----------------- | --------- | -------------------------------------------------------------- | ------------- |
| `minimum`         | `number`  | Defines the minimum recommendations that should be fetched.   | `5`             |
| `recommendations` | `number`  | Defines the total number of recommendations that should be fetched. | `20`            |

\
&nbsp;
 

## Setting up the `recommendation-refresh`
 
To configure the `recommendation-refresh` you will need to add props to it. Check the following tables to know what props that the app allows and how to configure them.
 
### `recommendation-refresh` props
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value      |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ------------------ |
| `strategy`           | `enum`    | Strategy used to fetch and display the recommended products. Possible values can be found in the [table](#strategy-and-secondarystrategy-props-for-recommendation-refresh)  below.   | `RECOMMENDATION_HISTORY` |
| `secondaryStrategy`  | `enum`    | Secondary strategy used to fetch and display the recommended products if the initial strategy does not return results. Possible values can be found in the [table](#strategy-and-secondarystrategy-props-for-recommendation-refresh)  below. | `RECOMMENDATION_HISTORY` |
| `recommendation`     | `object`  | Settings for the recommendation shelf.  | `undefined` |

### `strategy` and `secondaryStrategy` props for `recommendation-refresh`
\
&nbsp;

| Strategy         | Description                                                                    | 
| ------------------------- | ------------------------------------------------------------------------------ | 
| `RECOMMENDATION_HISTORY` | Fetches and displays products based on the user's navigation history.   |
| `CART_HISTORY`           | Fetches and displays products based on the user's cart history.         | 
| `ORDER_HISTORY`          | Fetches and displays products based on the user's order history.        |  

\
&nbsp;

### `recommendation` object
\
&nbsp;

| Prop name            | Type      | Description                                                                      | Default value |
| -------------------- | --------- | -------------------------------------------------------------------------------- | ----- |
| `count`              | `object`  | Defines the total and the minimum number of recommendations that should be fetched. | `{minimum: 5, recommendations: 20}` |

\
&nbsp;

### `count` object:
\
&nbsp;

| Prop name         | Type      | Description                                                    | Default value |
| ----------------- | --------- | -------------------------------------------------------------- | ------------- |
| `minimum`         | `number`  | Defines the minimum recommendations that should be fetched.   | `5`             |
| `recommendations` | `number`  | Defines the total number of recommendations that should be fetched. | `20`            |

\
&nbsp;
 
## Advanced configuration
 
You can customize the blocks `recommendation-shelf`, `recommendation-refresh`, and `recommendation-buy-together`by adding the `shelf-components` app to your theme's dependencies on the `manifest.json` file:
 
```diff
  "dependencies": {
+   "vtex.shelf-components": "0.x"
  }
```
 
Now it is possible to customize these blocks, building their components by using its children blocks `default-shelf`, `refresh-shelf`, and `buy-together`, respectively.
 
Below, you can find an implementation example for each one of them. If needed, use these blocks in your store theme code and make the desired changes according to your needs:
 
```json
  "store.home": {
    "blocks": [
      "flex-layout.row#recommendation-shelf",
    ]
  },
  "flex-layout.row#recommendation-shelf": {
    "children": ["recommendation-shelf"]
  },
  "recommendation-shelf": {
    "blocks": ["default-shelf"]
  },
  "default-shelf": {
    "blocks": ["list-context.product-list", "list-context.product-list-static"]
  },
  "list-context.product-list": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]
  },
  "list-context.product-list-static": {
    "blocks": ["product-summary.shelf#demo1"],
    "children": ["slider-layout#demo-products"]
  },
  "product-summary.shelf#demo1": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-summary-price",
      "product-summary-buy-button"
    ]
  },
  "slider-layout#demo-products": {
    "props": {
      "itemsPerPage": {
        "desktop": 5,
        "tablet": 3,
        "phone": 1
      },
      "infinite": true,
      "fullWidth": false
    }
  }
```
 
```json
  "store.home": {
    "blocks": [
      "flex-layout.row#recommendation-refresh",
    ]
  },
  "flex-layout.row#recommendation-refresh": {
    "children": ["recommendation-refresh"]
  },
  "recommendation-refresh": {
    "blocks": ["refresh-shelf"]
  },
  "refresh-shelf": {
    "blocks": ["product-summary.shelf"]
  },
  "product-summary.shelf": {
    "children": [
      "stack-layout#prodsum",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-space",
      "product-summary-price",
      "add-to-cart-button"
    ]
  }
```
 
```json
  "store.product": {
    "blocks": [
      "flex-layout.row#buy-together",
    ]
  },
  "flex-layout.row#buy-together": {
    "children": ["recommendation-buy-together"]
  },
  "recommendation-buy-together": {
    "blocks": ["buy-together"]
  },
  "buy-together": {
    "blocks": ["product-summary.shelf#buy-together"],
    "props": {
      "BuyButton": "add-to-cart-button"
    }
  },
  "product-summary.shelf#buy-together": {
    "children": [
      "responsive-layout.desktop#product-summary",
      "responsive-layout.tablet#product-summary",
      "responsive-layout.phone#product-summary"
    ]
  },
  "responsive-layout.desktop#product-summary": {
    "children": ["flex-layout.row#product-summary-desktop"]
  },
  "responsive-layout.tablet#product-summary": {
    "children": ["flex-layout.row#product-summary-mobile"]
  },
  "responsive-layout.phone#product-summary": {
    "children": ["flex-layout.row#product-summary-mobile"]
  },
  "flex-layout.row#product-summary-desktop": {
    "children": ["flex-layout.col#product-summary-desktop"]
  },
  "flex-layout.col#product-summary-desktop": {
    "children": [
      "product-summary-image#shelf",
      "product-summary-name",
      "product-summary-space",
      "product-list-price#summary",
      "product-installments#summary",
      "product-summary-sku-selector"
    ]
  },
  "flex-layout.row#product-summary-mobile": {
    "children": [
      "flex-layout.col#product-image",
      "flex-layout.col#product-summary-details"
    ]
  },
  "flex-layout.col#product-image": {
    "children": ["product-summary-image#shelf"]
  },
  "flex-layout.col#product-summary-details": {
    "props": {
      "marginLeft": 4
    },
    "children": [
      "product-summary-name",
      "product-summary-space",
      "product-list-price#summary",
      "product-installments#summary",
      "product-summary-sku-selector"
    ]
  }
```
 
 
## Customization
 
No CSS Handles are available yet for the app customization.
 
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