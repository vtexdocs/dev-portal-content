---
title: "BrainDW IO"
slug: "braindw-braindw-io"
excerpt: "braindw.braindw-io@0.8.13"
hidden: true
createdAt: "2022-07-07T11:07:36.338Z"
updatedAt: "2022-07-27T18:20:23.213Z"
---
The BrainDW App for VTEX IO configures your store to properly interact with BrainDW services.

The installation of the app set up the BrainDW pixel app, the BrainDW recommendation-resolver and allows you to use use the exported front-end components inside the pages of your store theme.

The BrainDW recommendation-resolver an implementation of the VTEX recommendation protocol for recommendation shelves that is defined by the schema GraphQL [recommendation-graphql](https://github.com/vtex-apps/recommendation-graphql).

## Pixel App

The pixel app is responsible from capturing live store events and sending them to BrainDW to feed the recommendation strategies.

## Store blocks

### bdw-recommendation-shelf

The recommendation shelf is component that shows a collection of products using recommendation strategies.

This behavior is defined based on the context page where the shelf is placed. Based on this information, BrainDW evaluates which business rules are being followed on one specific shelf to provide the appropiate recommended products.

### Home

![](https://storage.cdn.braindw.com/braindw_developer/script/files/2021/06/30/dochomeexample.png)
These are a set of rules that you can define for a bdw-recommendation-shelf, regardless of the page where it is.

* Best offers (for a specific category, a specific collection, across the site)
* Most added to the cart (for a specific category, a specific collection, across the site)
* Most viewed by ranking (for a specific category, a specific collection, across the site)
* Last products viewed

### Product page (PDP)

![](https://storage.cdn.braindw.com/braindw_developer/script/files/2021/06/30/docpdpexample.png)
These are a set of specific rules that you can define for bdw-recommendation-shelf that are inside the product page.

* Parent category shelf.
* Category shelf.
* Cross shelf by SKUs. 
* Cross shelf by categories.

Up to 7 cross selling shelves can be incorporated.

### Category page (PLP)

![](https://storage.cdn.braindw.com/braindw_developer/script/files/2021/06/30/docplpexample.png)
These are a set of specific rules that you can define for a bdw-recommendation-shelf that is inside the category page.

* Header category shelf

### Search no result

![](https://storage.cdn.braindw.com/braindw_developer/script/files/2021/06/30/docsnrexample.png)
These are a set of specific rules that you can define for a bdw-recommendation-shelf that is inside the no results page.

* Search result shelf
* Best offer shelf by search query.
* Most viewed shelf
* Last category viewed shelf

## Prerequisites

The front end components and the BrainDW's recommendation algorithms are depending on the pixel app to fetch user data.

In order to have the pixel app and, there by, the BrainDW app working properly, you need to notify the BrainDW team about your insterest in installing the application in your store. For this, you can send a message to soporte@braindw.com. You should expect as response a Client Key (save this key for the configuration steps) and your credentials to access the BrainDW dashboard.

## Configuration

It is possible to install in your store either by using **App Store** or the **VTEX IO Toolbelt**.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the BrainDW IO box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **CLIENT KEY** as is specified in the prerequisites.
4. You don't need to change the default API URL.
5. Click on **Save**.
6. You can now insert the `bdw-recommendation-shelf` blocks into your store theme.

### Using VTEX IO Toolbelt

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `braindw.braindw-io@0.x` app. You can confirm that the app has now been installed by running `vtex ls` again. 
2. Access the **Apps** section in your account's admin page and look for the BrainDW IO box. Once you find it, click on the box.
3. Fill in the "BrainDW IO" field with your **CLIENT KEY** and Google Analytics **TRACKING ID**.
4. You don't need to change the default API URL.
5. Click on **Save**.

### Once installed

You can now insert the `bdw-recommendation-shelf` blocks into your store theme.
You are going to have access to the BrainDW dashboard. From here you will be able to set up the rules for the different blocks inserted into your store theme.

If you do not have access to the BrainDW dashboard yet, you need to request it through the contact email specified in the Prerequisites section of this documentation.

1. Add the `BrainDW IO` app to your theme's peer dependencies on the `manifest.json`, for example:

```json
  "peerDependencies": {
    "braindw.braindw-io": "0.x",
  }
```

2. Add the `bdw-recommendation-shelf` block into your theme (example below).

   ```json
   "store.home": {
     "blocks": [
       "bdw-recommendation-shelf#home-1",
       "bdw-recommendation-shelf#home-2",
       "bdw-recommendation-shelf#home-3",
       "bdw-recommendation-shelf#home-4",
       "bdw-recommendation-shelf#home-5",
       "bdw-recommendation-shelf#home-6",
       "bdw-recommendation-shelf#home-7",
       "bdw-recommendation-shelf#home-8",
       "bdw-recommendation-shelf#home-9",
       "bdw-recommendation-shelf#home-10",
       "bdw-recommendation-shelf#home-11",
       "bdw-recommendation-shelf#home-12",
     ]
   },
   "store.product": {
     "children": [
       "flex-layout.row#store-product",
       "bdw-recommendation-shelf#product-1",
       "bdw-recommendation-shelf#product-2",
       "bdw-recommendation-shelf#product-3",
       "bdw-recommendation-shelf#product-4",
       "bdw-recommendation-shelf#product-5",
     ]
   },
   "search-not-found-layout": {
     "children": [
       "flex-layout.row",
       "flex-layout.row",
       "bdw-recommendation-shelf#noresult-1",
       "bdw-recommendation-shelf#noresult-2",
       "bdw-recommendation-shelf#noresult-3",
       "bdw-recommendation-shelf#noresult-4"
     ]
   },
   "search-result-layout.desktop#category": {
     "children": [
       "flex-layout.row#searchbread",
       "bdw-recommendation-shelf#category",
       "flex-layout.row#searchinfo",
       "flex-layout.row#result"
     ]
   },
   "search-result-layout.customQuery": {
     "blocks":[
       "bdw-recommendation-shelf#collection"
       "search-result-layout.desktop",
       "search-result-layout.mobile"
     ],
     "props": {
       "querySchema": {
         "queryField": "222",
         "mapField": "productClusterIds"
       }
     }
   }
   ```

   **Important:** The order of the shelves will always be determined by this code inside your store-theme.

3. From here, you can link your store theme to a development workspace or deploy it and install it in a production one.

The props of the `bdw-recommendation-shelf` are:

| Prop name           | Type      | Description                                                  | Default value |
| ------------------- | --------- | ------------------------------------------------------------ | ------------- |
| `id`                | `String`  | ID of the shelf, it links the shelf with the BrainDW dashboard. More information in the next section. | `''`          |
| `title`             | `String`  | Title to display above the shelf.                            | `''`          |
| `link`              | `String`  | A link for the title of the shelf. It should be relative for in-store links and absolute for external links. | `''`          |
| `showLazyLoading`   | `boolean` | If the shelf should render a lazy loading skeleton           | `false`       |
| `lazyLoadingHeight` | `number`  | Height in pixels of the lazy loading skeleton.               | `470`         |

Once the `bdw-recommendation-shelf` is on your store theme, it will render the product suggestions provided by BrainDW based on what is configured on your BrainDW dashboard.

### About the bdw-recommendation-shelf id

The id of one bdw-recommendation-shelf block is what defines which rule is going to apply to said shelf. To configure the rule behind an specific ID you need to access the BrainDW dashboard and set it up. 

If you do not have access to the BrainDW dashboard yet, you need to request it through the contact email specified in the Prerequisites section of this documentation.

For now, the IDs are specific and are listed below:

| Shelf ID                | N (number of shelves)              | Section             | Information                                                  |
| ----------------------- | ---------------------------------- | ------------------- | ------------------------------------------------------------ |
| `BDW-Home-Carrusel-{N}` | 1&nbsp;>=&nbsp;`N`&nbsp;>=&nbsp;12 | Home                | General purpose shelfs. <br />Do not need to be within an specific block. |
| `BDW-PDP-Carrusel-{N}`  | 1&nbsp;>=&nbsp;`N`&nbsp;>=&nbsp;7  | PDP                 | Used to make use of specific product rules. <br />Need to be within a `store.product` block. |
| `BDW-PLP-Carrusel`      | - (only one carrusel)              | PLP<br />Collection | Used to make use of specific category or collection rules.<br />Need to be within one of the next blocks:<br />`search-result-layout#department` <br />`search-result-layout#category`<br /><br />For collections, it can also be defined within a<br /> `search-result-layout.customQuery` with a `mapField` <br />equal to `productClusterIds` . |
| `BDW-SNR-Carrusel-{N}`  | 1&nbsp;>=&nbsp;`N`&nbsp;>=&nbsp;4  | Search no result    | Used to make use of specific no result rules. <br />Need to be within a `search-not-found-layout` block. |

Clarification: the range specified by the N column are not strict so you can have more shelves per section than the specified in this table. Here we specified the initial setup for new clients.

### About shelves in the shopping cart page

As of today, the blocks cannot be used within the store's checkout page. If you are interested in providing BrainDW intelligence at your checkout, we invite you to let us know so that we can offer you a service that is beyond the scope of this application.

### bdw-conditional-layout block

You can make use of the bdw-conditional-layout block to prevent UI elements from rendering if an specific shelf does not contain any product. This is a good practice if you are interested in designing specific UI complements around one shelf in your site.

To use it, you need to declare it and define its children as an array of blocks.

```json
"flex-layout.col#main-col": {
  "children": [
    "bdw-condition-layout#1",
  ]
},
"bdw-condition-layout#1": {
  "children": [
    "flex-layout.row#row-1"
  ]
},
"flex-layout.row#row-1": {
  "children": [
    "flex-layout.col#col-image",
    "flex-layout.col#col-bdw"
  ]
},
"flex-layout.col#col-bdw": {
  "children": [
    "bdw-recommendation-shelf#home-1"
  ]
},
```

**In the example:** If the `bdw-recommendation-shelf#home-1` is not displaying any products, the `bdw-conditional-layout` will stop rendering all `flex-layout.row#row-1`, including both image and shelf columns.

### Advanced configuration

The bdw-recommendation-shelf is a fork of the original recommendation-shelf implemented by VTEX. As such it can
be **customized** by building the default-shelf component that the recommendation-shelf render.

To do this, you'll need to add the `shelf-components` app to your theme's dependencies on the `manifest.json` file:

```diff
  "dependencies": {
+   "vtex.shelf-components": "0.x"
  }
````

Below, you can find an implementation example:

```json
  "store.home": {
    "blocks": [
      "flex-layout.row#row-recommendation-shelf",
    ]
  },
  "flex-layout.row#row-recommendation-shelf": {
    "children": ["bdw-recommendation-shelf"]
  },
  "bdw-recommendation-shelf": {
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

## Customization

No CSS Handles are available yet for the app customization.