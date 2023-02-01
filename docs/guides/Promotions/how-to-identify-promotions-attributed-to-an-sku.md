---
title: "How to identify promotions attributed to an SKU"
slug: "how-to-identify-promotions-attributed-to-an-sku"
hidden: true
createdAt: "2021-11-09T17:06:14.573Z"
updatedAt: "2021-11-09T19:59:19.524Z"
---

[block:callout]
{
  "type": "warning",
  "body": "Some of the configurations described in this article use **Google Chrome** as an example for debugging. Since this tool is not part of VTEX, it may be updated without notice."
}
[/block]
This article responds to a frequent query from users of the VTEX platform: what is the reason for a promotion to be applied to an SKU when apparently it should not be?

To determine which promotions are attributed to an SKU, we have to analyze its **priceTags**.

1. Go to the product shopping cart.
2. In Google Chrome, go to **Developer Tools** (`Ctrl+Shift+I`).
3. Select the tab **Network** and press `F5` to record the reload.
   ![network-f5](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-identify-promotions-attributed-to-an-sku-0.png)
4. After loading, press `Ctrl+F` on the **Developer Tools** and search for **orderform**.
   ![Order form](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-identify-promotions-attributed-to-an-sku-1.png)
5. Click on **orderform** and go to `items`. After clicking on `items`, click on the numbers (`0`, `1`, `2`, etc.) to see the details of the product you want. In our example, since there is only one item, it is represented by the number `0` in the array.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-identify-promotions-attributed-to-an-sku-2.png)
6. After clicking on the number, scroll down to **priceTags**. Click on priceTags and then on the numbers (0, 1, 2, etc.) to see the details of the promotion you want. In our example, since there is only one promotion, it is represented by the number `0` in the array. After this, look for the “identifier” of the promotion.
7. Open another tab, and go to URL `https://{nomedaloja}.vtexcommercestable.com.br/admin/pricing/#/benefit/{numero-do-identifier}`. This is the promotion that is being applied to the product in the cart. Check the configurations of the promotion and see whether the conditions apply to the SKU in question.
