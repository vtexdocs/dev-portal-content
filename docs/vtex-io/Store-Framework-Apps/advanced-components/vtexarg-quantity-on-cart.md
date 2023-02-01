---
title: "Quantity On Cart"
slug: "vtexarg-quantity-on-cart"
hidden: false
createdAt: "2022-04-25T13:13:25.281Z"
updatedAt: "2022-04-25T13:13:25.281Z"
---

The **Quantity on Cart** app allows you to display a message to your customers informing how many units of a product they have added to the cart. This message can be displayed in a [Shelf](https://developers.vtex.com/docs/guides/vtex-io-documentation-building-a-shelf) or in a product page.

![app-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtexarg-quantity-on-cart-0.gif)

> ⚠️ The Quantity On Cart app does not work with promotions scenarios such as [Buy Together](https://help.vtex.com/en/tutorial/buy-together--tutorials_323) and [Buy One Get One](https://help.vtex.com/en/tutorial/buy-one-get-one--tutorials_322).

## Configuration

1. Open the terminal and use the [VTEX IO CLI](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference) to log into the desired VTEX account.
2. Run the following command to install the Quantity On Cart app:

```
vtex install vtexarg.quantity-on-cart
```  

3. Open your store’s Store Theme app directory in your code editor.
4. Open your app's `manifest.json` file and add the Quantity On Cart app under the `peerDependencies` field.

```json
"peerDependencies": {
  "vtexarg.quantity-on-cart": "2.x"
}
```

5. Add the `quantity-on-cart` block to other theme block using a product context since the `quantity-on-cart` block handles product data, such as the `store.product`or the [`product-summary.shelf`](https://developers.vtex.com/docs/guides/vtex-product-summary-productsummaryshelf#configuration). For the example below, we have added to the `product-summary.shelf`:

```json
  {
  "product-summary.shelf": {
    "children": [
    + "quantity-on-cart"
    ]
  },
...
```

After step 5, no further configuration is needed, and the app is ready to use in your store.

> ℹ️
>
> The displayed message in the Quantity On Cart app is available in three languages: English (EN), Spanish (ES), and Portuguese (PT), and follows the pattern below, which cannot be changed: EN - `You have x units in your shopping cart.` | ES - `Tienes x unidades en el carrito.` | PT - `Você tem x unidades no carrinho.`

---

## Customization

To apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `quantityOnCart` |
