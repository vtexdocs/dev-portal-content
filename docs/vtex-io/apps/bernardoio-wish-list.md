---
title: "Wishlist"
slug: "bernardoio-wish-list"
excerpt: "bernardoio.wish-list@2.14.0"
hidden: true
createdAt: "2022-07-07T11:45:48.209Z"
updatedAt: "2022-07-07T11:50:40.088Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Wishlist app, designed for **B2C** stores, adds a heart icon to shelves and product detail pages, so users can add the desired products to a Wishlist.

![wishlist-list](https://user-images.githubusercontent.com/52087100/94687168-40fbe500-0302-11eb-8239-135d773324dd.png)
_Example of heart icons on a shelf._

![wish-list-pdp](https://user-images.githubusercontent.com/52087100/94687148-393c4080-0302-11eb-8ab4-e5bd44e642ec.png)
_Example of a heart icon on a product details page._

In addition to that, a brand new route called `/wishlist` is generated under the My Account menu, creating a page responsible for listing all wishlisted items for your users.

![wishlist-my-account](https://user-images.githubusercontent.com/52087100/101348528-87257580-386a-11eb-84e3-0ffda3ce0fb5.png)
_Example of a wishlist page._

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the Wishlist app in the desired VTEX account by running `vtex install vtex.wish-list` in your terminal.
2. Open your store's Store Theme app directory in your code editor.
3. Add the Wishlist app to your theme's `manifest.json` file inside **peerDependencies** as shown below:

```diff
 "peerDependencies": {
+  "vtex.wish-list": "1.x"
 }
```

> ℹ️ _The Wishlist app can export two theme blocks when added as a dependency: `add-to-list-btn` and `list-context.wishlist`. They are responsible, respectively, for adding the heart icon to other theme blocks and for providing product data to build the `/wishlist` also shared with the My Account page._

4. Add the `add-to-list-btn` block into the `store.product` template's children block list. For example:

```diff
{
  "store.product": {
    "children": [
      "product-name",
      "product-reviews",
+      "add-to-list-btn"
    ]
  },
```

5. Declare the `add-to-list-btn` block as a child of the [`product-summary.shelf` blocks](https://vtex.io/docs/components/all/vtex.product-summary/) in your theme. For example:

```diff
  "product-summary.shelf": {
    "children": [
+     "add-to-list-btn",
      "product-summary-name",
      "product-rating-inline",
      "product-summary-price",
      "add-to-cart-button"
    ]
  }
```

> ℹ️ _The new route called `/wishlist`, responsible for creating the Wishlist custom page that displays wishlisted product items, already contains a default template, it is already rendered under the My Account menu and no further actions are required from you. However, you can **customize the Wishlist page, overwriting the template by creating a brand new one as you wish**. To do so, check the **Advanced configurations** section below._

## Uages

There are couple URLs to read, search and modify data for the app:

To read the schema of the wishlist app: 
`````
curl --request GET \ 
     --url 'https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/wishlist/schemas/wishlist' \
     --header 'VtexIdClientAutCookie: {authToken}' \
`````

To GET all the wishlist data: 
`````
curl --request GET \
     --url 'https://{environment}--{accountName}.myvtex.com/_v/wishlist/export-lists' \
     --header 'VtexIdClientAutCookie: {authToken}' \
`````

To search wishlist by user email: 
`````
curl --request GET \
     --url 'https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/wishlist/search?' \
     --header 'VtexIdClientAutCookie: {authToken}' \
`````

To PATCH a wishlist to the MasterData: 
`````
curl --request PATCH \
     --url 'https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/wishlist/documents' \
     --header 'VtexIdClientAutCookie: {authToken}' \
     --data '
        [
            "Email",
            "Name",
            .
            .
            .
            "IsPublic",
        ]
     '
`````

To DELETE a wishlist from the MasterData:: 
`````
curl --request DELETE \
     --url 'https://{{accountName}}.vtexcommercestable.com.br/api/dataentities/wishlist/documents/{documentId}' \
     --header 'VtexIdClientAutCookie: {authToken}' \
`````

## Advanced configurations

According to the Wishlist app composition, the `/wishlist` page can be highly customizable using other blocks. Currently, its default implementation is as follows:

`store.wishlist` interface for the route `/wishlist` and `my-account-page.wishlist-page` along with `my-account-link.wishlist-link` for the Wishlist section under My Account

**wishlist.jsonc**

```json
{
  "my-account-link.wishlist-link": {
    "props": {
      "label": "My Wishlist"
    }
  },
  "my-account-page.wishlist-page": {
    "props": {
      "title": "Wishlist"
    },
    "children": ["list-context.wishlist"]
  },
  "store.wishlist": {
    "blocks": ["flex-layout.row#top", "list-context.wishlist"]
  },
  "flex-layout.row#top": {
    "children": ["flex-layout.col#title"]
  },
  "flex-layout.col#title": {
    "children": ["rich-text#title"],
    "props": {
      "blockClass": "titleWishlist",
      "preventVerticalStretch": true
    }
  },
  "rich-text#title": {
    "props": {
      "text": "### Wishlist"
    }
  },
  "list-context.wishlist": {
    "blocks": ["product-summary.shelf#wishlist"],
    "children": ["slider-layout#wishlist"]
  },
  "product-summary.shelf#wishlist": {
    "children": [
      "add-to-list-btn",
      "product-summary-image",
      "product-summary-name",
      "product-summary-space",
      "product-summary-price",
      "add-to-cart-button"
    ]
  },
  "slider-layout#wishlist": {
    "props": {
      "itemsPerPage": {
        "desktop": 5,
        "tablet": 3,
        "phone": 1
      },
      "showNavigationArrows": "desktopOnly",
      "showPaginationDots": "always",
      "infinite": false,
      "fullWidth": true,
      "blockClass": "shelf"
    }
  }
}
```

Add the `plugins.json` file to your theme's `/store/` folder, this will add the Wishlist to the "My Account"

**plugins.json**

```json
{
  "my-account-pages > my-account-page": "my-account-page.wishlist-page",
  "my-account-menu > my-account-link": "my-account-link.wishlist-link"
}
```

By "default implementation" we mean that, by installing the Wishlist app in your store, you're actually using the `json` above behind the scenes to build the new page template (`/wishlist`), as shown in the third image displayed above.

Therefore, in order to customize the `/wishlist` page configuration, you should:

1. Create a `wishlist.jsonc` file under `store/blocks`.
2. Create a `plugins.json` file under `store/`.
3. Copy the code above, paste it in the new file and change it as you wish.
4. Deploy your changes.

If you want to configure the layout without the `slider-layout` dependency, you can use the `list-context-renderer` to wrap the `product-summary.shelf`, more information [here](https://github.com/vtex-apps/list-context#list-context-renderer)

#### `my-account-link.wishlist-link` props

| Prop name |   Type   |                         Description                         | Default value |
| :-------: | :------: | :---------------------------------------------------------: | :-----------: |
|  `label`  | `string` | Change the label for the section menu under My Account page |  `Wishlist`   |


## Custom toast URL
Change the link of toast message

````` json
{
  "add-to-list-btn#myButton": {
    "props": {
      "toastURL": "/wishlist"
    }
  }
}
`````
| Prop name |   Type   |                         Description                         | Default value |
| :-------: | :------: | :---------------------------------------------------------: | :-----------: |
|  `toastURL`  | `string` | Change the link of toast message |  `/account/#wishlist'`   |

## Custom View Wishlist Empty
Show custom view in case there are no added products.

`````diff
{
  "list-context.wishlist": {
+    "blocks": ["wishlist-empty-list", "product-summary.shelf#wishlist"],
    "children": ["slider-layout#wishlist"],
    "props": {
      "showViewEmptyList": true
    }
  },
  "wishlist-empty-list": {
    "children": [
      "rich-text#description"
    ]
  },
  "rich-text#description": {
    "props": {
      "text": "### There are no products",
      "textAlignment": "CENTER",
      "textPosition": "CENTER",
      "font": "t-heading-2"
    }
  },
}
`````

#### `list-context.wishlist` props
| Prop name |   Type   |                         Description                         | Default value |
| :-------: | :------: | :---------------------------------------------------------: | :-----------: |
|  `showViewEmptyList`  | `boolean` | Show custom view in case there are no added products. |  `false`   |

## Customization

In order to apply CSS customizations to this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `columnText`            |
| `columnThumb`           |
| `linkText`              |
| `linkThumb`             |
| `listItemsContainer`    |
| `listName`              |
| `listTab`               |
| `productDescription`    |
| `productItemRow`        |
| `productTitle`          |
| `thumb`                 |
| `wishlistContainer`     |
| `wishlistIcon`          |
| `wishlistIconContainer` |
| `emptyMessage`          |

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