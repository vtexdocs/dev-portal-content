---
title: "SKU List"
slug: "vtex-sku-list"
hidden: false
createdAt: "2020-06-03T15:19:30.003Z"
updatedAt: "2022-06-09T16:53:53.438Z"
---

The SKU List app is an essential B2B feature responsible for rendering a SKU list in the product details page.

![sku-list](https://user-images.githubusercontent.com/52087100/85888338-c762d100-b7bf-11ea-9ca0-c808ef9641ea.png)

## Configuration

1. Add the `vtex.sku-list` app to your theme's dependencies in the `manifest.json`, for example:

    ```diff
      "dependencies": {
    +   "vtex.sku-list": "1.x"
      }
    ```

    Now, you are able to use all blocks exported by the `sku-list` app. Check out the full list below:

    | Block name     | Description                                     |
    | -------------- | ----------------------------------------------- |
    | `sku-list` | Top level block in which you will declare as `children` the SKU List layout blocks according to devices (`sku-content.desktop` and the `sku-content.mobile` blocks).   |
    | `sku-content.desktop` | Defines the SKU List layout for desktop devices. |
    | `sku-content.mobile` | Defines the SKU List layout for mobile devices. |
    | `sku-name`  | Renders the SKU name. |
    | `sku-image` | Renders the SKU image. |
    | `sku-seller` | Renders the SKU sellers (if it has any). It uses the `seller-name`, `seller-inventory` and `seller-price` blocks as children in order to display seller data. |
    | `seller-name` | Renders the SKU seller name. |  
    | `seller-inventory` | Renders the SKU inventory per seller. |
    | `seller-price` | Renders the SKU price per seller. |
    | `sku-price` | Renders the SKU price. |
    | `sku-inventory` | Renders the SKU inventory. |
    | `sku-quantity-selector` | Renders a quantity selector. |
    | `item-quantity` | Renders the SKU inventory. |
    | `sku-buy-button` | Renders a Buy Button to add a given SKU to the minicart. |
    | `item-buy-button` | Renders a Buy Button to add a given Product to the minicart. |
    | `sku-specifications` | Renders the SKU specifications. |
    | `sku-highlights` | Renders a highlight disclaimer for a specific SKU. |

2. In the product template (`store.product`), use the following block structure in order to rebuild the Product Details Page now including the `sku-list` blocks:

```diff
{
   "store.product": {
     "children": [
       "flex-layout.row#product-breadcrumb",
-      "flex-layout.row#product-main",
+      "flex-layout.row#images-and-items",
+      "flex-layout.row#buy-button",
       "flex-layout.row#description",
       "shelf.relatedProducts",
       "product-reviews",
       "product-questions-and-answers"
     ]
   },
+  "flex-layout.row#images-and-items": {
+    "children": [
+      "product-images",
+      "flex-layout.col#sku-list"
+    ],
+    "props": {
+      "preventHorizontalStretch": false
+    }
+  },
+  "flex-layout.col#sku-list": {
+    "children": [
+      "flex-layout.row#sku-list-header",
+      "sku-list"
+    ],
+    "props": {
+      "preventVerticalStretch": true,
+      "width": "60%",
+      "blockClass": "skuList"
+    }
+  },
+  "flex-layout.row#sku-list-header": {
+    "props": {
+      "preventHorizontalStretch": false,
+      "blockClass": "skuListHeader"
+    },
+    "children": [
+      "rich-text#certificates",
+      "rich-text#expiry-date",
+      "rich-text#inventory",
+      "rich-text#price",
+      "rich-text#quantity-selector"
+    ]
+  },
+  "rich-text#certificates": {
+    "props": {
+      "text": "**Has Certificates?**",
+      "blockClass": "skuList",
+      "width": "20%"
+    }
+  },
+  "rich-text#expiry-date": {
+    "props": {
+      "text": "**Expires at**",
+      "blockClass": "skuList",
+      "width": "20%"
+    }
+  },
+  "rich-text#inventory": {
+    "props": {
+      "text": "**Stock**",
+      "blockClass": "skuList",
+      "width": "20%"
+    }
+  },
+  "rich-text#price": {
+    "props": {
+      "text": "**Price**",
+      "blockClass": "skuList",
+      "width": "20%"
+    }
+  },
+  "rich-text#quantity-selector": {
+    "props": {
+      "text": "**Quantity**",
+      "blockClass": "skuList",
+      "width": "20%"
+    }
+  },
+  "sku-list": {
+    "blocks": [
+      "sku-content.desktop",
+      "sku-content.mobile"
+    ]
+  },
+  "sku-content.desktop": {
+    "children": [
+      "flex-layout.row#item-main-desktop"
+    ]
+  },
+  "flex-layout.row#item-main-desktop": {
+    "props": {
+      "preventHorizontalStretch": false
+    },
+    "children": [
+      "flex-layout.col#sku-highlight-certificates",
+      "flex-layout.col#sku-highlight-expiry-date",
+      "flex-layout.col#sku-inventory",
+      "flex-layout.col#sku-price",
+      "flex-layout.col#sku-quantity-selector"
+    ]
+  },
+  "flex-layout.col#sku-highlight-certificates": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-highlights#certificates"
+    ]
+  },
+  "sku-highlights#certificates": {
+    "props": {
+      "conditional": {
+        "highlight": "admin/editor.sku-list.highlights.chooseDefaultSpecification",
+        "typeSpecifications": "Has Certificates"
+      },
+      "showLabel": false
+    }
+  },
+  "flex-layout.col#sku-highlight-expiry-date": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-highlights#expiry-date"
+    ]
+  },
+  "sku-highlights#expiry-date": {
+    "props": {
+      "conditional": {
+        "highlight": "admin/editor.sku-list.highlights.chooseDefaultSpecification",
+        "typeSpecifications": "Expiry Date"
+      },
+      "showLabel": false
+    }
+  },
+  "flex-layout.col#sku-inventory": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-inventory#default"
+    ]
+  },
+  "sku-inventory#default": {
+    "props": {
+      "showLabel": false
+    }
+  },
+  "sku-seller#inventory": {
+    "children": [
+      "seller-inventory"
+    ]
+  },
+  "flex-layout.col#sku-price": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-price"
+    ]
+  },
+  "flex-layout.col#sku-quantity-selector": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-quantity-selector"
+    ]
+  },
+  "sku-content.mobile": {
+    "children": [
+      "flex-layout.row#item-main-mobile"
+    ]
+  },
+  "flex-layout.row#item-main-mobile": {
+    "props": {
+      "preventHorizontalStretch": false
+    },
+    "children": [
+      "flex-layout.col#sku-highlight-certificates-mobile",
+      "flex-layout.col#sku-highlight-expiry-date-mobile",
+      "flex-layout.col#sku-inventory-mobile",
+      "flex-layout.col#sku-price-mobile",
+      "flex-layout.col#sku-quantity-selector-mobile"
+    ]
+  },
+  "flex-layout.col#sku-highlight-certificates-mobile": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-highlights#certificates-mobile"
+    ]
+  },
+  "sku-highlights#certificates-mobile": {
+    "props": {
+      "conditional": {
+        "highlight": "admin/editor.sku-list.highlights.chooseDefaultSpecification",
+        "typeSpecifications": "Has Certificates"
+      },
+      "showLabel": true
+    }
+  },
+  "flex-layout.col#sku-highlight-expiry-date-mobile": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-highlights#expiry-date-mobile"
+    ]
+  },
+  "sku-highlights#expiry-date-mobile": {
+    "props": {
+      "conditional": {
+        "highlight": "admin/editor.sku-list.highlights.chooseDefaultSpecification",
+        "typeSpecifications": "Expiry Date"
+      },
+      "showLabel": true
+    }
+  },
+  "flex-layout.col#sku-inventory-mobile": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-inventory#default-mobile"
+    ]
+  },
+  "sku-inventory#default-mobile": {
+    "props": {
+      "showLabel": true
+    }
+  },
+  "sku-seller#inventory-mobile": {
+    "children": [
+      "seller-inventory#mobile"
+    ]
+  },
+  "seller-inventory#mobile": {
+    "props": {
+      "showLabel": true
+    }
+  },
+  "flex-layout.col#sku-price-mobile": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-price#mobile"
+    ]
+  },
+  "sku-price#mobile": {
+    "props": {
+      "showLabel": true
+    }
+  },
+  "flex-layout.col#sku-quantity-selector-mobile": {
+    "props": {
+      "width": "20%"
+    },
+    "children": [
+      "sku-quantity-selector"
+    ]
+  },
+  "sku-quantity-selector#mobile": {
+    "props": {
+      "showLabel": true
+    }
+  },
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ----------------------------------------- |
| `availableQuantityContainer`              |
| `buttonDataContainer`                     |
| `buttonItemsPrice`                        |
| `buyButtonContainer`                      |
| `buyButtonText`                           |
| `buyButtonText`                           |
| `colGroupLeadTime`                        |
| `colGroupQuantityBreak`                   |
| `colGroupUnitPrice`                       |
| `highlightContent`                        |
| `highlightTitle`                          |
| `highlightValue`                          |
| `inventory`                               |
| `inventoryContainer`                      |
| `itemHighlight`                           |
| `priceContainer`                          |
| `productPriceBreaksContainer`             |
| `productPriceBreaksContainer`             |
| `productPriceQuantityDataColumn`          |
| `productPriceTable`                       |
| `productPriceTableFooterMultipleColumn`   |
| `productPriceTableFooterRow`              |
| `productPriceTableHeader`                 |
| `productPriceTableHeaderRow`              |
| `productPriceTableHeaderRowData`          |
| `productPriceTableLeadTimeColumn`         |
| `productPriceTableMainHeader`             |
| `productPriceTablePriceColumn`            |
| `productPriceTableQuantities`             |
| `productPriceTableRow`                    |
| `productPricingTableTitle`                |
| `quantitySelectorContainer`               |
| `quantitySelectorStepper`                 |
| `quantitySelectorTitle`                   |
| `selectedSkuContentWrapper`               |
| `sellerInventory`                         |
| `sellerInventoryWrapper`                  |
| `sellerName`                              |
| `sellerPriceContainer`                    |
| `skuContentWrapper`                       |
| `skuImage`                                |
| `skuName`                                 |
| `specificationItemProperty`               |
| `specificationItemSpecifications`         |
| `specificationsTable`                     |
| `specificationsTableContainer`            |
| `specificationsTablePropertyHeading`      |
| `specificationsTableSpecificationHeading` |
| `specificationsTabsContainer`             |
| `specificationsTitle`                     |
