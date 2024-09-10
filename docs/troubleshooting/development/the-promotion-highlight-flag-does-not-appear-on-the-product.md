---
title: "The promotion highlight flag does not appear on the product."
slug: "the-promotion-highlight-flag-does-not-appear-on-the-product"
hidden: false
createdAt: "2024-09-10T12:08:37.773Z"
updatedAt: ""
excerpt: "When creating a promotion and enabling the highlight option, the product does not display the highlight flag in the store."
tags:
    - store-framework
    - product-highlights
    - promotions
---

In stores developed with VTEX IO Store Framework, when creating a promotion and [enabling the highlight option](https://help.vtex.com/en/tutorial/configurando-promocao-com-destaque-flag--tutorials_2295#configuring-the-promotion), the corresponding flag may not appear on the product.

This behavior may occur due to the absence of the [`product-highlights`](https://developers.vtex.com/docs/apps/vtex.product-highlights) component on the corresponding page.

## Solution

To display the promotion highlight on a product, follow the steps below.

### Check the promotion setup

Make sure your promotion is configured properly and has the highlight option enabled. You can check this directly in the VTEX Admin or using a VTEX API.

#### VTEX Admin

1. In the VTEX Admin, go to **Promotions > Promotions**.
2. Open the promotion you configured.
3. Confirm the promotion is highlighted.

![is-featured](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/is-featured-en.png)

#### VTEX API

Using the [Get promotion or tax by ID](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/calculatorconfiguration/-idCalculatorConfiguration-) API, check if the `isFeatured` field is set as **true**.

### Check the `product-highlights` component

1. Open the Store Theme app using any code editor, such as Visual Studio Code.
2. Go to the page template where the product should be displayed with the highlight flag.
3. Check if the template has a product highlight block declared.

  >⚠ The Product Highlights blocks require a product context to work properly. Therefore, when declaring these blocks, ensure that they are placed in a theme template or a block where this context is available, such as `store.product` and `product-summary.shelf`.

4. If a product highlight block is not declared, follow the [Product Highlights](https://developers.vtex.com/docs/apps/vtex.product-highlights) documentation to set it up.

If the problem continues, open a ticket with [VTEX Support](https://help.vtex.com/en/support).
