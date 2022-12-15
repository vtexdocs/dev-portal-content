---
title: "Quantity On Cart"
slug: "vtexarg-quantity-on-cart"
excerpt: "vtexarg.quantity-on-cart@2.2.8"
hidden: false
createdAt: "2022-04-25T13:13:25.281Z"
updatedAt: "2022-04-25T13:13:25.281Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The **Quantity on Cart** app allows you to display a message to your customers informing how many units of a product they have added to the cart. This message can be displayed in a [Shelf](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-building-a-shelf) or in a product page.

![app-example](https://user-images.githubusercontent.com/67270558/162291375-e469fb78-ef87-4eeb-bd8b-f228a4579a52.gif)

> ⚠️
> 
> The Quantity On Cart app does not work with promotions scenarios such as [Buy Together](https://help.vtex.com/en/tutorial/buy-together--tutorials_323) and [Buy One Get One](https://help.vtex.com/en/tutorial/buy-one-get-one--tutorials_322).

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
5. Add the `quantity-on-cart` block to other theme block using a product context since the `quantity-on-cart` block handles product data, such as the `store.product`or the [`product-summary.shelf`](https://developers.vtex.com/vtex-developer-docs/docs/vtex-product-summary-productsummaryshelf#configuration). For the example below, we have added to the `product-summary.shelf`:

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

To apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ----------- | 
| `quantityOnCart` | 

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:
<table>
  <tr>
    <td align="center"><a href="https://github.com/germanBonacchi"><img src="https://avatars.githubusercontent.com/u/55905671?v=4" width="100px;" alt=""/><br /><sub><strong>Germán Bonacchi</strong></sub></a><br /><a href="https://github.com/vtex-apps/quantity-on-cart/commits?author=germanBonacchi" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/tomymehdi"><img src="https://avatars.githubusercontent.com/u/774112?v=4" width="100px;" alt=""/><br /><sub><strong>Tomás Alfredo Mehdi</strong></sub></a><br /><a href="https://github.com/vtex-apps/quantity-on-cart/commits?author=tomymehdi" title="Code">💻</a></td>
  </tr>
</table>
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->