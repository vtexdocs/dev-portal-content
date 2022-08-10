---
title: "Retail Rocket Tracking"
slug: "retailrocketcl-tracking"
excerpt: "retailrocketcl.tracking@0.0.50"
hidden: true
createdAt: "2022-08-05T20:55:04.536Z"
updatedAt: "2022-08-05T20:55:04.536Z"
---
Retail Rocket Tracking is an app responsible for optimize the entire purchase process of an online store, making available a product recommendation engine. [Retail Rocket](https://retailrocket.es/).

## Installation

It is possible to install the app in your store either by using App Store or the VTEX IO Toolbelt.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the Retail Rocket Tracking box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **PARTNER ID** in the `Retail Rocket Tracking` field.
4. Click on **Save**.

:information_source: Access the [Retail Rocket page](https://retailrocket.es/) and login to you account in order to find out what is your account **PARTNER ID**.

### Using VTEX IO Toolbelt

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `retailrocketcl.tracking@0.x` app. You can confirm that the app has now been installed by running `vtex ls` again.
2. Access the **Apps** section in your account's admin page and look for the Retail Rocket box. Once you find it, click on the box.
3. Fill in the `Retail Rocket` field with your **PARTNER ID**.
4. Click on **Save**.

:information_source: Access the [Retail Rocket page](https://retailrocket.es/) and login to you account in order to find out what is your account **PARTNER ID**.

## Configuration

Import the `retailrocketcl.tracking` app to your theme's dependencies in the `manifest.json`:

```json
  "peerDependencies": {
    "retailrocketcl.tracking": "0.x"
  }
```
## ANNOTATION ABOUT THE VERSIONS
Retail rocket has two ways to connect and show the recommendations but the second way is in experimental phase, we recommend to use the first version.
### FIRST VERSION
Once the application is installed and added the peerDependencie, you can now use all the blocks exported by the `retail-rocket-tracking` application. 

The app export the block `retail-rocket-container` that is responsible for creating the container to display the products.  so it can receive the following props:

| Prop name              | Type                                   | Description                                                                                                                                                                                                                               | Default value |
| ---------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `markupBlock`             | `String`         |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Every time you define this block you need to pass the markupBlock. For this it is necessary that you review the documentation provided by Retail Rocket                                                                                                                                                               |  `undefined`         |
| `type`             | `Enum`         |   This property is responsible for defining the landing page, example product page or home page. Possible values: `GLOBAL`, `HOME`, `PLP`, `SIMILAR_PRODUCT`, `RELATED_PRODUCT`. In a later table it is explained how the types should be defined depending on your needs.                                                                                                                                                             |  `GLOBAL`         |

`Enum type`:

| Value              | Description                                   |
| -------------------| --------------------------------------------- |
| `GLOBAL`           | It is the default value, it does not need to be defined. Blocks with this type can be defined on any page.      | 
| `HOME`             | Blocks with this type should only be used on the home page.    | 
| `PLP`              | Blocks with this type should only be used on pages where products are listed. Which can be: Department, category, subcategory, search results. You can define a only block for the multiples pages mentioned.     | 
| `SIMILAR_PRODUCT`  | Blocks with this type should only be used on the product page. Additionally it serves to show similar products.    | 
| `RELATED_PRODUCT`  | Blocks with this type should only be used on the product page. Additionally it serves to show related products.    | 

## Example

:information_source: The MarkupBlocks utilizied in this examples are of test. For show original values you should consulte the documentation provided by Retail Rocket

### Default Block

```json
{
  "retail-rocket-container#global": {
    "props": {
      "markupBlock": "1621870407701"
    }
  }
}
```

#### Include in the blocks of `store.home`

```json
{
    "store.home": {
        "blocks": [
          "list-context.image-list#demo",
          "__fold__.experimentalLazyAssets",
          "flex-layout.row#deals",
          "retail-rocket-container#global", //Included
          "rich-text#shelf-title",
          "flex-layout.row#shelf",
          "info-card#home",
          "rich-text#question",
          "rich-text#link",
          "newsletter"
        ]
      }
}
```

### Block type PLP

```json
{
 "flex-layout.row#retail-rocket-category": {
    "props": {
      "blockClass": "retail-rocket"
    },
    "children": [
      "retail-rocket-container#category"
    ]
  },
  "retail-rocket-container#category": {
    "props": {
      "type": "PLP",
      "markupBlock": "1621870407701"
    }
  }
}
```

#### Include the block in `search-result-layout`

```json
{
  "store.search#category": {
    "blocks": ["search-result-layout"],
    "props": {
      "context": {
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  },
  "search-result-layout": {
    "blocks": [
      "search-result-layout.desktop",
      "search-result-layout.mobile",
      "search-not-found-layout"
    ]
  },
  "search-result-layout.desktop": {
    "children": [
      "flex-layout.row#retail-rocket-category" //Included,
      "flex-layout.row#searchbread",
      "flex-layout.row#searchtitle",
      "flex-layout.row#result"
    ],
    "props": {
      "pagination": "show-more",
      "preventRouteChange": false,
      "defaultGalleryLayout": "grid"
    }
  }
}
```
## SECOND VERSION (BETA)

This version works through API integration. Don't worry you should not do something additional only it changes the way to implement the carrousels. 

`Enum type`:

| Value              | Description                                   |
| -------------------| --------------------------------------------- |
| `SEARCH`             | Blocks with this type should only be used on the search result page.    | 
| `RECOMMENDATION_PLP`              | Blocks with this type should only be used on pages where products are listed. Which can be: Department, category, subcategory. You can define a only block for the multiples pages mentioned.     | 
| `ALTERNATIVE_PRODUCT`  | Blocks with this type should only be used on the product page. Additionally it serves to show similar products.    | 
| `RELATED_PRODUCT`  | Blocks with this type should only be used on the product page. Additionally it serves to show related products.    | 
| `PERSONALIZED_POPULAR_GLOBAL`, `NEW_PRODUCTS_BY_USER_GLOBAL`, `PERSONAL_RECOMMENDATION_GLOBAL` | Blocks with these types can be used on any view. |

### How to call a carrousel
Each block must have the propertys `type` and `markupBlock`. The next example will show how you must define the block's structure.

```json
{
"retail-rocket-container-v2#pdp": {
    "props": {
      "type": "RELATED_PRODUCT",
      "markupBlock": "MARKUP_BLOCK_TEST"
    },
    "blocks": [
      "default-shelf"
    ]
}
```
The previous code fragment is a block to use on a PDP, it is for the prop `type`. It's important to see that the block `default-shelf` is passed as a block prop. This is to personalize our carrousel as we want, you can do it like this:

```json
{
  "default-shelf": {
    "blocks": ["list-context.product-list", "list-context.product-list-static"]
  },
  "list-context.product-list": {
    "blocks": ["product-summary.shelf"],
    "children": ["slider-layout#demo-products"]
  },
  "list-context.product-list-static": {
    "blocks": ["product-summary.shelf"],
    "children": ["slider-layout#demo-products"]
  },
  "slider-layout#demo-products": {
    "props": {
      "itemsPerPage": {
        "desktop": 3,
        "tablet": 3,
        "phone": 2
      },
      "showPaginationDots":"mobileOnly",
      "infinite": false,
      "fullWidth": true,
      "blockClass": ["shelf", "shelf-department"]
    }
  }
}
```

#### These are some things that you must remember

- If you want to have multiples designs for your carrousel you should create a `default-shelf` for every carrousel. The same for each `product-summary.shelf`.
- It's mandatory you pass one `default-shelf` block.
 
#### Multiple shelfs on a PDP

If you want to display multiples shelfs you must create a `retail-rocket-container-v2` for each shelf. Example:

```json
{
    "store.product": {
        "children": [
          "flex-layout.row#product-breadcrumb",
          "condition-layout.product#availability",
          "flex-layout.row#description",
          "retail-rocket-container-v2#pdp-related", //similar products shelf
          "retail-rocket-container-v2#pdp-similars", //related products shelf
          "flex-layout.row#specifications-title",
          "product-specification-group#table",
          "shelf.relatedProducts"
        ]
      },
    "retail-rocket-container-v2#pdp-related": {
        "props": {
          "type": "RELATED_PRODUCT",
          "markupBlock": "MARKUP_BLOCK_TEST"
        },
        "blocks": [
          "default-shelf"
        ]
    },
    "retail-rocket-container-v2#pdp-similars": {
        "props": {
          "type": "SIMILAR_PRODUCT",
          "markupBlock": "MARKUP_BLOCK_TEST"
        },
        "blocks": [
          "default-shelf"
        ]
    }
}
```

#### To create shelfs for a plp pages (department, category, subcategory and search result)

We will speak about the necessary to have a successful implementation. The first is to have these pages separated like the next code fragment.

```json
{
    "store.search": {
    "blocks": ["search-result-layout"],
    "props": {
      "context": {
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  },
  "store.search#brand": {
    "blocks": ["search-result-layout#plp"],
    "props": {
      "context": {
        "orderByField": "OrderByReleaseDateDESC",
        "hideUnavailableItems": true,
        "maxItemsPerPage": 10,
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  },

  "store.search#department": {
    "blocks": ["search-result-layout#plp"],
    "props": {
      "context": {
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  },

  "store.search#category": {
    "blocks": ["search-result-layout#plp"],
    "props": {
      "context": {
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  },

  "store.search#subcategory": {
    "blocks": ["search-result-layout#plp"],
    "props": {
      "context": {
        "skusFilter": "ALL",
        "simulationBehavior": "skip"
      }
    }
  }
}
```

Here, we can see that the search result page has a `search-result-layout` unique block different to the other pages. The next step is to define the respective block for each page.

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
          "retail-rocket-container-v2#search",
          "flex-layout.row#result"
        ],
        "props": {
          "pagination": "show-more",
          "preventRouteChange": false,
          "defaultGalleryLayout": "grid"
        }
    },
    "retail-rocket-container-v2#search": {
        "props": {
          "type": "SEARCH",
          "markupBlock": "MARKUP_BLOCK_TEST"
        },
        "blocks": [
          "default-shelf"
        ]
    },
    "search-result-layout#plp": {
        "blocks": [
          "search-result-layout.desktop#plp",
          "search-result-layout.mobile#plp",
          "search-not-found-layout"
        ]
    },
    "search-result-layout.desktop#plp": {
        "children": [
          "flex-layout.row#searchbread",
          "flex-layout.row#searchtitle",
          "retail-rocket-container-v2#plp",
          "flex-layout.row#result"
        ],
        "props": {
          "pagination": "show-more",
          "preventRouteChange": false,
          "defaultGalleryLayout": "grid"
        }
    },
    "retail-rocket-container-v2#plp": {
        "props": {
          "type": "PLP",
          "markupBlock": "MARKUP_BLOCK_TEST"
        },
        "blocks": [
          "default-shelf"
        ]
    }
}
```

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<table>
  <tr>
    <td align="center"><a href="https://jumpdigital.co/"><img src="https://avatars.githubusercontent.com/u/86085200?s=200&v=4" width="100px;" alt=""/><br /><sub><b>Jump Digital</b></sub></a><br /><a href="https://vtex.io/docs/app/retailrocketcl.tracking@0.x" title="Project Management">📆</a></td>
    <td align="center"><a href="https://jumpdigital.co/"><img src="https://media-exp1.licdn.com/dms/image/C4E03AQHsWVzs2K_rNw/profile-displayphoto-shrink_800_800/0/1580100025331?e=1634169600&v=beta&t=_cH8psyBqZmqt11aqgWSW4kvV1S7PwZDwWFuQKx_Kes" width="100px;" alt=""/><br /><sub><b>Windsor Ortiz</b></sub></a><br /><a href="https://vtex.io/docs/app/retailrocketcl.tracking@0.x" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/calixfar"><img src="https://avatars.githubusercontent.com/u/26258524?s=400&u=4340771ce3bb51c202d697371073359ebd0b197a&v=4" width="100px;" alt=""/><br /><sub><b>Luis Santiago</b></sub></a><br /><a href="https://vtex.io/docs/app/retailrocketcl.tracking@0.x" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!