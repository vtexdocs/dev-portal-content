---
title: "The promotion highlight flag does not appear on the product."
slug: "the-promotion-highlight-flag-does-not-appear-on-the-product"
hidden: false
createdAt: "2024-08-21T13:43:55.841Z"
updatedAt: ""
excerpt: "When creating a promotion and enabling the highlight function, the product does not display the highlight flag in the store."
tags:
    - store-framework
    - product-highlights
    - promotions
---

In stores developed with VTEX IO Store Framework, when creating a promotion and [enabling the highlight function](https://help.vtex.com/en/tutorial/configurando-promocao-com-destaque-flag--tutorials_2295#configuring-the-promotion), the corresponding flag may not appear on the product.

This behavior may occur due to the absence of the [`product-highlights`](https://developers.vtex.com/docs/apps/vtex.product-highlights) component on the corresponding page.

## Solution

To display the promotion highlight on a product, follow the steps below.

### Check the promotion setup

Ensure your promotion is configured properly, with the highlight function enabled. You can check it directly in the VTEX Admin or using a VTEX API.

#### **VTEX Admin**

1. In the VTEX Admin, go to **Promotions > Promotions**.
2. Open the promotion you configured.
3. Ensure the promotion is highlighted.

![is-featured](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/is-featured-en.png)

#### **VTEX API**

Using the [Get promotion or tax by ID](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/calculatorconfiguration/-idCalculatorConfiguration-) API, check if the `isFeatured` field is set as **true**.

### Verify the `product-highlights` component

1. Open the Store Theme app using the code editor of your choice, such as Visual Studio Code.
2. Go to the page’s template where the product should appear with the highlight flag. 
3. Check if the template has a product highlight block declared.

  >⚠ The Product Highlights blocks require a product context to function properly. Therefore, when declaring these blocks, ensure that they are placed in a theme template or block where this context is available, such as the `store.product` and `product-summary.shelf`.

4. If a product highlight block is not declared, follow the [Product Highlights](https://developers.vtex.com/docs/apps/vtex.product-highlights) documentation to set it up.

If the problem continues, open a ticket to [VTEX Support](https://help.vtex.com/en/support).
