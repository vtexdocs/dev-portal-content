---
title: "Building a product details page"
slug: "vtex-io-documentation-building-a-product-details-page"
hidden: false
createdAt: "2020-06-03T16:02:44.244Z"
updatedAt: "2022-12-13T20:17:44.056Z"
---

A product details page (PDP) is the page in an ecommerce website that displays information about a specific product, including dimensions, color, price, reviews, shipping, and other relevant details that consumers may want to check before purchasing.

The PDP is defined within the `store.product` block in the Store Theme app, and it's built with a series of child blocks. The `store.product` block accepts all blocks allowed by the `store` and `flex-layout` blocks as child dependencies, as well as block in the following list:

<details>
  <summary>Blocks accepted by <code>store.product</code></summary>

<ul>
  <li><code>availability-subscriber</code></li>
  <li><code>buy-button</code></li>
  <li><code>blog-related-posts</code></li>
  <li><code>breadcrumb</code></li>
  <li><code>product-add-to-list-button</code></li>
  <li><code>product-assembly-options</code></li>
  <li><code>product-availability</code></li>
  <li><code>product-brand</code></li>
  <li><code>product-details</code></li>
  <li><code>product-description</code></li>
  <li><code>product-highlights</code></li>
  <li><code>product-identifier</code></li>
  <li><code>product-images</code></li>
  <li><code>product-kit</code></li>
  <li><code>product-name</code></li>
  <li><code>product-price</code></li>
  <li><code>product-rating-inline</code></li>
  <li><code>product-rating-summary</code></li>
  <li><code>product-reviews</code></li>
  <li><code>product-teaser.product</code></li>
  <li><code>product-quantity</code></li>
  <li><code>product-questions-and-answers</code></li>
  <li><code>product-separator</code></li>
  <li><code>product-specifications</code></li>
  <li><code>share</code></li>
  <li><code>shipping-simulator</code></li>
  <li><code>sku-selector</code></li>
</ul>

</details>

## Before you start

To build a responsive PDP, you need to use [`flex-layout`](https://developers.vtex.com/docs/apps/vtex.flex-layout). For more information, read [this](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-flex-layout) guide.

## Practical example

Consider the following example of a PDP built using the `store.product` and `flex-layout` blocks:

<details>
  <summary>Click here to see the code sample</summary>

```json
{
  "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "flex-layout.row#product-main",
      "shelf.relatedProducts"
    ]
  },
  "flex-layout.row#product-breadcrumb": {
    "props": {
      "marginTop": 4
    },
    "children": ["breadcrumb"]
  },
  "flex-layout.row#product-main": {
    "props": {
      "colGap": 7,
      "rowGap": 7,
      "marginTop": 4,
      "marginBottom": 7,
      "paddingTop": 7,
      "paddingBottom": 7
    },
    "children": ["flex-layout.col#product-image", "flex-layout.col#right-col"]
  },
  "flex-layout.col#product-image": {
    "props": {
      "width": "60%",
      "rowGap": 0
    },
    "children": ["product-images"]
  },
  "product-images": {
    "props": {
      "displayThumbnailsArrows": true
    }
  },
  "flex-layout.col#right-col": {
    "props": {
      "preventVerticalStretch": true,
      "rowGap": 0
    },
    "children": [
      "product-name",
      "product-rating-summary",
      "product-price#product-details",
      "product-separator",
      "product-quantity",
      "product-identifier.product",
      "sku-selector",
      "flex-layout.row#buy-button",
      "availability-subscriber",
      "shipping-simulator",
      "share#default"
    ]
  },
  "product-price#product-details": {
    "props": {
      "showInstallments": true,
      "showSavings": true
    }
  },
  "flex-layout.row#buy-button": {
    "props": {
      "marginTop": 4,
      "marginBottom": 7
    },
    "children": ["buy-button"]
  },

  "share#default": {
    "props": {
      "social": {
        "Facebook": true,
        "WhatsApp": true,
        "Twitter": false,
        "Pinterest": true
      }
    }
  }
}

```

</details>

![Product details page](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-product-details-page-0.png)

Note that in the code sample, the `store.product` child dependencies define five blocks, the first two being `flex-layout.row`.

> ⚠️ Keep in mind that the `flex-layout` block may be affected if you are using mobile mode. For more information, read the [Flex Layout](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-flex-layout) documentation.

### First row of Flex Layout

In the first row of the `flex-layout` block, the [`breadcrumb`](https://developers.vtex.com/docs/apps/vtex.breadcrumb) block is rendered as follows:

![First row](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-product-details-page-1.png)

```json
"flex-layout.row#product-breadcrumb": {
    "props": {
      "marginTop": 4
    },
    "children": ["breadcrumb"]
  },
```

To customize the breadcrumb, you can declare the `breadcrumb` block and configure its properties based on your preferences. For example:

```json
"breadcrumb": {
    "props": {
        "showOnMobile": true
    }
}
```

### Second row of Flex Layout

The second row of the `flex-layout` block renders the main information about the product.

It renders the product image (`flex-layout.col#product-image`) in the left column and the name, price, SKU selector, and buy button in the right column(`flex-layout.col#right-col`):

```json
 "flex-layout.row#product-main": {
    "props": {
      "colGap": 7,
      "rowGap": 7,
      "marginTop": 4,
      "marginBottom": 7,
      "paddingTop": 7,
      "paddingBottom": 7
    },
    "children": ["flex-layout.col#product-image", "flex-layout.col#right-col"]
  },
```

To customize the `flex-layout.col#product-image` and `flex-layout.col#right-col` sections, you can declare these blocks and configure their properties based on your preferences as below:

```json
"flex-layout.col#product-image": {
    "props": {
      "width": "60%",
      "rowGap": 0
    },
    "children": ["product-images"]
  },
  "product-images": {
    "props": {
      "displayThumbnailsArrows": true
    }
  },
  "flex-layout.col#right-col": {
    "props": {
      "preventVerticalStretch": true,
      "rowGap": 0
    },
    "children": [
      "product-name",
      "product-price#product-details",
      "product-separator",
      "product-quantity",
      "product-identifier.product",
      "sku-selector",
      "flex-layout.row#buy-button",
      "shipping-simulator",
      "share#default"
    ]
  },
```

#### Left column

The left column of the second row contains the [`product-images`](https://developers.vtex.com/docs/apps/vtex.store-components/productimages) block because this was the first `flex-layout.col` block to be declared.

![Left column](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-product-details-page-2.png).

#### Right column

The right column of the second row displays the price, buy button, and other relevant product details. In practice, it's composed of the following blocks:

![Right column](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-product-details-page-3.png)

- [`product-name`](https://developers.vtex.com/docs/apps/vtex.store-components/productname): Displays the product name, along with its SKU name, if desired.
- [`product-price`](https://developers.vtex.com/docs/apps/vtex.product-price): Displays a properly formatted selling price. You can set it to display the list price (if different), installments, etc. Below is an example of a product price displaying both the sale and the list price.
- `product-separator`: Renders a line separator.
- [`product-quantity`](https://developers.vtex.com/docs/apps/vtex.product-quantity): Displays a quantity selector that allows customers to choose how many items they want to add to the cart.
- [`product-identifier`](https://developers.vtex.com/docs/apps/vtex.product-identifier): Displays the product identification number. It accepts different props, such as the label to display before/after the identifier.
- [`sku-selector`](https://developers.vtex.com/docs/apps/vtex.store-components/skuselector): Allows the user to choose a SKU, automatically hiding impossible combinations or indicating combinations that are currently unavailable.
- [`add-to-cart-button`](https://developers.vtex.com/docs/apps/vtex.add-to-cart-button): Adds an item to the cart. You can customize it to display a success message, redirect users to the cart page, etc.
- [`shipping-simulator`](https://developers.vtex.com/docs/apps/vtex.store-components/shippingsimulator): Allows users to enter their postal code to then display the available shipping options and their respective prices for the order.
- [`share`](https://developers.vtex.com/docs/apps/vtex.store-components/share): Allows product sharing on social media. You can customize its props to control which options will be displayed to the user.

### Related products

After the `flex-layout` rows, you need to declare the `shelf.relatedProducts` block in your `store.product` block. This block is a [shelf](https://developers.vtex.com/docs/guides/vtex-shelf/) that displays products related to the one the customer is browsing. These products are defined through Catalog in the Admin.

```json
"shelf.relatedProducts": {
    "props": {
        "recommendation": "view",
        "productList": {
            "titleText": "Who saw also saw",
            "itemsPerPage": 3
        }
    }
}
```

When related products are identified, they are displayed as follows:

![Related products](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-building-a-product-details-page-4.png)

The `shelf.relatedProducts` block accepts different recommendation types, such as `similars`, `view`, `buy`, `accessories`, `viewAndBought`, and `suggestions`.
