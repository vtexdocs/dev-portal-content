---
title: "Modal Layout closes when I click a SKU"
slug: "modal-layout-closes-when-i-click-a-sku"
hidden: false
createdAt: "2024-06-04T11:15:35.508Z"
updatedAt: "2024-06-04T11:15:35.508Z"
excerpt: "When using Product Summary within a storefront modal, the modal closes when you click a SKU."
tags:
    - store-framework
    - catalog

---

**Keywords:** Modal Layout | SKU Selector | Product Summary | SKU | Product | Storefront

The [Modal Layout](https://developers.vtex.com/docs/apps/vtex.modal-layout) component provides blocks to create modals in your storefront. Within a [Product Summary](https://developers.vtex.com/docs/apps/vtex.product-summary) component such as the [Shelf](https://developers.vtex.com/docs/guides/vtex-shelf/) in a search results page, when you define [SKU Selector](https://developers.vtex.com/docs/apps/vtex.store-components/skuselector) as a prop in the `modal-content` block, the component will display all the SKUs available for a given product. However, if you click a SKU option, the modal will close, as shown below.

![sku-selector](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/sku-selector.gif)

This behavior will occur every time you click a SKU from the [SKU Selector](https://developers.vtex.com/docs/apps/vtex.store-components/skuselector) component inside the modal because it expects you to be on the product page with that SKU highlighted. When you pick a size, the URL changes — the SKU ID is added to the end of the URL as a query parameter (e.g., `?skuId=880021`), and the component closes since it is considered a new page.

## Solution

To solve this issue, you must replace the [SKU Selector](https://developers.vtex.com/docs/apps/vtex.store-components/skuselector) component with the [Product Summary SKU Selector](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummaryskuselector), which represents the SKU Selector inside a Product Summary component, such as the Shelf, on a search results page.

1. Add the `product-summary-sku-selector` block to your code, declaring it as a child of the `modal-content` block, as in the example below:

    ```json
    "modal-content#quickview": {
      "children":[
        "product-summary-name",
        "product-images",
        "product-summary-sku-selector",
        "product-summary-quantity",
        "add-to-cart-button"
      ],
      "props":{
        "blockClass": "quickviewContent"
      }
    },
    "product-summary-sku-selector": {
      "props":{
        "showVariations Labels": ["false"]
      }
    },
    ```

2. Run `vtex link` to see your changes reflected in the workspace.

You should then be able to see and interact with the component without the modal closing, as illustrated below:

![product-summary-sku-selector](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/product-summary-sku-selector.gif)
