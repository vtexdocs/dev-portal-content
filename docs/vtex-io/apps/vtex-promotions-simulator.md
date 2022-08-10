---
title: "Promotions Simulator"
slug: "vtex-promotions-simulator"
excerpt: "vtex.promotions-simulator@0.0.5"
hidden: true
createdAt: "2022-07-13T14:33:09.694Z"
updatedAt: "2022-07-13T14:33:09.694Z"
---
The Promotion Simulator is an application focused on the ecommerce operation, one that brings peace of mind to customers about the changes in prices resulting from promotions. It guarantees that the promotion performs as expected, considering all other active promotions.

It offers a detailed promotion cause-analysis in a specific shopping cart. Therefore, users have more visibility about the logic for the selection made by the Promotions module, considering all active promotions that could potentially be applied.

To leverage the Promotion Simulator, one should:

1. Initially, set up Cartman - following the step by step on this documentation.
2. Build the scenario in which they want to perform the evaluation of a promotions' applicability. This is done by including specific SKUs on a shopping cart.
3. Initiate Cartman > Visualize promotion details > Open Promotion Analyzer > Tã-dã 🎉🎉.
4. As a result, the Simulator will display:
   - All possible promotions to be applied on each SKU.
   - Whether the promotion was applied or not.
   - The causes that validated the selected promotion (by the Promotions engine).
   - The causes that were not validated, blocking the promotion's applicability.

![Promotions Simulator workflow](https://user-images.githubusercontent.com/5256673/154990967-a95c375a-db4d-4588-88a9-17ec5b466e7f.gif)