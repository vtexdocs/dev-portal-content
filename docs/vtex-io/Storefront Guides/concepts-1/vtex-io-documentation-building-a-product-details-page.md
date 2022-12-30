---
title: "Building a Product Details Page"
slug: "vtex-io-documentation-building-a-product-details-page"
excerpt: "vtex.io-documentation@0.88.24"
hidden: false
createdAt: "2020-06-03T16:02:44.244Z"
updatedAt: "2022-12-13T20:17:44.056Z"
---

A Product Details Page, or PDP, is the web page on an ecommerce website that presents information on a particular product, including the product dimensions, color, price, reviews, shipping information, and other relevant details that shoppers may want to check before making a purchase.

The PDP is defined within the `store.product` block in the Store Theme app, and is composed of a series of child blocks. The `store.product` block accepts all blocks allowed by the `store` and `flex-layout` blocks as child dependencies, as well as the following blocks list:

<details>
  <summary>List of blocks accepted by <code>store.product</code></summary>

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

> ℹ Check out the full and updated list [here](https://github.com/vtex-apps/store/blob/master/store/interfaces.json#L20).

</details>

<h2>Before you start</h2>

To build a responsive PDP, the [`flex-layout`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-flex-layout) will be used. Hence, knowledge of how to use the `flex-layout` block is strongly recommended. For more information, please refer to [this](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-flex-layout) guide.

## Practical example

Consider the following example of a Product Details Page built with the `store.product` and `flex-layout` blocks:

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

![Product Details Page](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-building-a-product-details-page-0.png)

From the code sample, notice that the `store.product` child dependencies define five blocks, the first two being `flex-layout.row`.

> ⚠️ Keep in mind that the `flex-layout` block may suffer modifications if you are on mobile mode. Please refer to the [Flex Layout](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-flex-layout) document for more information.

### Flex layout first row

In the first row of the `flex-layout` block, the [`breadcrumb`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-breadcrumb/) block is rendered as in the following:

![First row](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-building-a-product-details-page-1.png)

```json
"flex-layout.row#product-breadcrumb": {
    "props": {
      "marginTop": 4
    },
    "children": ["breadcrumb"]
  },
```

To customize the breadcrumb, we can then declare the `breadcrumb` block and configure its properties according to our preferences. Consider the following example:

```json
"breadcrumb": {
    "props": {
        "showOnMobile": true
    }
}
```

### Flex layout second row

The second row of the `flex-layout` block is responsible for rendering the main information about the product.

In the left column, it renders the product image (`flex-layout.col#product-image`), while in the right column (`flex-layout.col#right-col`), it renders the name, price, SKU selector, and buy button:

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

To customize the `flex-layout.col#product-image` and `flex-layout.col#right-col` sections, we can declare these blocks and configure their properties according to our preferences as in the following:

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

The left column of the second row contains the [`product-images`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productimages) block since this was the first `flex-layout.col` block to be declared.

![Left column](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-building-a-product-details-page-2.png).

#### Right column

The right column of the second row presents the price, buy button, and other relevant product details. It is, in practice, composed of the following blocks:

![Right column](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-building-a-product-details-page-3.png)

- [`product-name`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productname): displays the product name, along with its SKU name, if desired.
- [`product-price`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-productprice): displays a properly formatted selling price. You can set it to show the list price (if it's different), installments, etc. Check out below an example of a Product Price displaying both the sale and the list price:
- `product-separator`: renders a line separator.
- [`product-quantity`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-quantity): displays a quantity selector that allows shoppers to choose how many items they want to add to the cart.
- [`product-identifier`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-identifier): displays the product identification number. It accepts different props, such as the label to display before/in front of the identifier.
- [`sku-selector`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-skuselector): allows the user to choose his desired SKU, automatically hiding impossible combinations or indicating combinations that are currently unavailable.
- [`buy-button`](https://github.com/vtex-apps/store-components/tree/master/react/components/BuyButton): adds an item to the cart. You can customize it to show a successful message, redirect users to the cart page, etc.
- [`shipping-simulator`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-shippingsimulator): allows users to fill in their postal code to then display the available shipping options and their respective prices for that cart.
- [`share`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-store-components-share): allows product sharing on social media. You can customize its props to control which options will be shown to the user.

### Related products

After the `flex-layout` rows, we declared the `shelf.relatedProducts` block in our `store.product` block. This block is a [Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-shelf/) that displays products related to the one shoppers are browsing. These products are defined through the Catalog in the Admin.

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

When related products are identified, they are presented as in the following:

![Related products](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-io-documentation-building-a-product-details-page-4.png)

The `shelf.relatedProducts` block accepts different recommendation types, such as `similars`, `view`, `buy`, `accessories`, `viewAndBought`, `suggestions`.
