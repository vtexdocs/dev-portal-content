---
title: "Kit Look"
slug: "vtexbr-kitlook"
excerpt: "vtexbr.kitlook@5.3.0"
hidden: false
createdAt: "2021-10-07T18:46:15.904Z"
updatedAt: "2022-07-25T20:06:31.514Z"
---
The Kit Look app displays relevant products to the shopper at the time of purchase, increasing the store's product selling. 

The customer can choose the items from the kit they want to buy or add the complete kit to the cart if they are interested in the combinations highlighted automatically by the store.


![Kitlook](https://user-images.githubusercontent.com/1207017/64264890-6902f400-cf08-11e9-8916-2f281e7c2f51.jpg)

In the following sections, learn how to add the app to your store and configure it.
## Before you start

Set up the Kit with all the products that will be displayed. To do so, refer to the tutorial [Kit registration](https://help.vtex.com/tutorial/kit-registration--tutorials_215).  

## Step-by-step
### Step 1 - Installing the app

1. Go to the [VTEX App Store](https://apps.vtex.com/vtexbr-kitlook/p) and after logging into your account, click on `GET APP`.

2. You will be redirected to the checkout and choose a payment method since **the Kit Look is a paid app.**

> ℹ️
>
> As the Kit look is a paid app, you will be charged a US$0.01 fee to validate your credit card information. This will be refunded as soon as the payment is approved.

Once you have paid for the app, it is installed in your account.

3. To finish this step, import it in your store's `peerDependencies` in `manifest.json`.

```json
{
  "peerDependencies": {
    "vtexbr.kitlook": "5.x"
  }
}
```

### Step 2 - Configuration

The Kit Look order by default is sorted by the productId in ascending order, but it is possible to configure it to respect the Kit order registration through the settings in the Kit Look app inside my applications.

![KitOrder](https://user-images.githubusercontent.com/67066494/179033651-29ebcb47-6ce1-4de4-9a71-c61232047b50.png)

The `kitlook-layout` interface works by alternating the blocks if it detects that the product is a kit. 

Therefore, you have to add its interface in your app store theme code. There are two ways to achieve this: Adding the `kitlook-layout` interface in the `interfaces.json` or `product.jsonc`. 

Check out the following sections to add the `kitlook-layout` interface.

### Adding `kitlook-layout` in the `interfaces.json`

1. Allow the Kit look interfaces by adding the Kit Look in the `store.product` in `interfaces.json` of your app theme.

```json
// interfaces.json
{
  "store.product.kitlook": {
    "allowed": ["kitlook-layout", "kitlook"]
  }
}
```

2. Then, add the `kit look-layout` interface to the page you want to display a different block when the product is a kit.

```json
// product.json
{
  "store.product.kitlook": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "kitlook-layout", // <--- Here's our new block
      "flex-layout.row#description",
      "shelf.relatedProducts"
    ]
  },
  "kitlook-layout": {
    "children": [
      "flex-layout.row#product-main", // <--- The first child is for regular product
      "flex-layout.row#kitlook" // <--- The second one will show when a product is a kit
    ]
  }
}
```

> ℹ️
>
> Keep in mind that the first block specified will always be for regular products, and the second one is for your custom product page that you want to display if the product is a kit.

3. In your second block, you can use the `kitlook` block to display the kit items. For example:

```json
// product.json
{
  "flex-layout.row#kitlook": {
    "props": {
      "colGap": 7,
      "rowGap": 7,
      "marginTop": 4,
      "marginBottom": 7,
      "paddingTop": 7,
      "paddingBottom": 7
    },
    "children": ["flex-layout.col#kitlook", "flex-layout.col#stack"]
  },
  "flex-layout.col#kitlook": {
    "props": {
      "colGap": 7,
      "rowGap": 7,
      "marginTop": 4,
      "marginBottom": 7,
      "paddingTop": 7,
      "paddingBottom": 7
    },
    "children": ["kitlook"]
  }
}
```

In the example above, we are reusing the `flex-layout.col#stack` block shared with your regular product blocks.

### Adding `kitlook-layout` in the `product.jsonc`

1. Add `product-details.kitlook` as a child in your `store.product` in `store/blocks/product.jsonc`.

```json
{
  "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "product-details.kitlook",
      "shelf.relatedProducts",
      "product-reviews",
      "product-questions-and-answers"
    ]
  },
  ...
}
```

2. In your `product-details.kitlook` add `kitlook` as a block.

```json
{
  "product-details.kitlook": {
    "blocks": [
      "kitlook",
      "product-images",
      "product-description",
      "product-specifications",
      "buy-button",
      "sku-selector",
      "shipping-simulator",
      "product-highlights",
      "availability-subscriber",
      "product-price",
      "product-name",
      "share#default"
    ],
    "props": {
      "displayVertically": true
    }
  }
}
```

### Product Summary

If you have any shelves which may display kits you need to replace the `product-summary` or `product-summary.shelf` interface with `product-summary.kitlook-layout` in those shelves in `store/blocks/home/home.jsonc`

```json
{
  "shelf#home": {
    "blocks": ["product-summary.kitlook-layout"],
    "props": {
      "orderBy": "OrderByTopSaleDESC",
      "paginationDotsVisibility": "desktopOnly",
      "skusFilter": "FIRST_AVAILABLE",
      "productList": {
        "maxItems": 10,
        "itemsPerPage": 5,
        "minItemsPerPage": 1.5,
        "scroll": "BY_PAGE",
        "arrows": true,
        "titleText": "Top sellers"
      }
    }
  }
}
```

> ⚠️
>
> We recommend you do the same for your `gallery` block, so the new layout is used in search results and categories pages.

```json
{
  "gallery": {
    "blocks": ["product-summary.kitlook-layout"]
  }
}
```

Now that you're using `product-summary.kitlook-layout`, you may want to specify a custom block for your regular products and another for kitlook, so let's do that.

To do that, somewhere in your `blocks.json` add the block `product-summary.kitlook-layout`.

You can specify two children's blocks. The first will be displayed for regular products and the second for kitlooks.

```json
{
  "product-summary.kitlook-layout": {
    "children": ["product-summary.shelf", "product-summary.kitlook"]
  }
}
```

### Advanced

By default `product-summary.kitlook` displays a list with the name and price of the items in the kit.

However, it is possible to achieve a wide range of customizations using `product-summary-kitlook` ( different from the `product-summary.kitlook`)

You can specify any interface that a regular `product-summary` accepts, e.g., `product-summary-image`, `product-summary-buy-button`, to name a few.

You can also use `flex-layout` and `stack-layout` to achieve the maximum level of control.

Take a look at how to do that.

1. Create a new custom `product-summary.kitlook` so you can modify `product-summary-kitlook` and `product-summary-buy-button#kitlook` later on. For example:

```json
{
  "product-summary.kitlook#custom": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-space",
      "product-summary-kitlook",
      "product-summary-buy-button#kitlook"
    ]
  }
}
```

2. Then, create a `flex-layout.row` and `flex-layout.col` columns to go inside it. In one column put the product image using `product-summary-image` and in the other `product-summary-name` and `product-summary-price`.

```json
{
  "product-summary-kitlook": {
    "children": ["flex-layout.row#product-summary-kitlook"]
  },
  "flex-layout.row#product-summary-kitlook": {
    "children": [
      "flex-layout.col#kit-item-image",
      "flex-layout.col#mini-summary"
    ],
    "props": {
      "colGap": 3,
      "border": ["top"],
      "borderWidth": 1,
      "borderColor": "silver",
      "paddingTop": 5
    }
  },
  "flex-layout.col#kit-item-image": {
    "children": ["product-summary-image"],
    "props": {
      "width": "33%"
    }
  },
  "flex-layout.col#mini-summary": {
    "children": ["product-summary-name", "product-summary-price#mini"],
    "props": {
      "horizontalAlign": "left"
    }
  },
  "product-summary-price#mini": {
    "props": {
      "showLabels": false,
      "showInstallments": false,
      "showListPrice": false
    }
  }
}
```

Everything put together:

```json
{
  "product-summary.kitlook-layout": {
    "children": ["product-summary.shelf", "product-summary.kitlook#custom"]
  },
  "product-summary.kitlook#custom": {
    "children": [
      "product-summary-image",
      "product-summary-name",
      "product-summary-space",
      "product-summary-kitlook",
      "product-summary-buy-button#kitlook"
    ]
  },
  "product-summary-kitlook": {
    "children": ["flex-layout.row#product-summary-kitlook"]
  },
  "flex-layout.row#product-summary-kitlook": {
    "children": [
      "flex-layout.col#kit-item-image",
      "flex-layout.col#mini-summary"
    ],
    "props": {
      "colGap": 3,
      "border": ["top"],
      "borderWidth": 1,
      "borderColor": "silver",
      "paddingTop": 5
    }
  },
  "flex-layout.col#kit-item-image": {
    "children": ["product-summary-image"],
    "props": {
      "width": "33%"
    }
  },
  "flex-layout.col#mini-summary": {
    "children": ["product-summary-name", "product-summary-price#mini"],
    "props": {
      "horizontalAlign": "left"
    }
  },
  "product-summary-price#mini": {
    "props": {
      "showLabels": false,
      "showInstallments": false,
      "showListPrice": false
    }
  },
  "product-summary-buy-button#kitlook": {
    "props": {
      "buyButtonBehavior": "alwaysGoToProduct"
    }
  }
}
```

After that, do not forget to change the default product page interface on **CMS > Pages** to use the `store.product.kitlook interface`.

You can expect to have a similar result as the following:

![kitlook-advanced-preview](https://i.imgur.com/BopgrCF.png)