---
title: "Dynamic Product"
slug: "lyracons-dynamic-product"
excerpt: "lyracons.dynamic-product@0.0.3"
hidden: true
createdAt: "2022-07-06T18:20:02.587Z"
updatedAt: "2022-08-03T19:22:52.488Z"
---
This customApp will serve as a hub for dynamically render product components. Currently, the only component developed is an extension from `vtex.product-price.installments`. 


# Configuration

1. Add the `dynamic-product` app to your theme's dependencies in the `manifest.json`, for example:

```diff
 "dependencies ": {
+  "lyracons.dynamic-product": "0.x"
 }
```

2. Add the `dynamic-installments` wherever you want. Here's an example:

```diff
  "product-summary-status#shelf": {
    "children": [
      "add-to-list-btn",
      "stack-layout#shelf",
      "flex-layout.row#shelf-highlights",
      "product-summary-name",
      "product-summary-space",
      "flex-layout.row#shelf-unit-price",
      "product-price#price",
      "product-price-savings",
+     "dynamic-installments",
      "add-to-cart-quantity"
    ]
  },
```

3. Save the app's Settings in Admin > Apps > My Apps > Dynamic Product. 

- Installments Criteria: Installments criteria for the product. 

	When set to max-quantity, the block will render the installments plan with the biggest number of installments. When set to max-quantity-without-interest, the block will render the installments plan with the biggest number of installments and zero interest. Notice that, if this prop is set to max-quantity-without-interest, and no installments plan matches the 'without interest' criteria, the component will fallback the default behavior.

- HideFor: The component will be hidden if the product is part of any of the categories inputted in this input