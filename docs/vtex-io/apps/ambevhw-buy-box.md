---
title: "CodeBy Custom Buy Box"
slug: "ambevhw-buy-box"
excerpt: "ambevhw.buy-box@1.0.2"
hidden: true
createdAt: "2022-07-04T22:02:51.786Z"
updatedAt: "2022-07-05T02:19:00.021Z"
---
App for creating a custom buy-box within the product-page. The buy box contains two more sections: **subscriptions** and **pickup points**. The app can be used in portuguese stores, but its admin section can be used in different languages and the app is applied within the Product Page in VTEX IO STORES.

For implementation the app on product page store, follow the steps described below:

## Configuration

1. Import the CodeBy Custom Buy Box app to your theme's `peerDependencies` in the `manifest.json` as shown below:

```json
"peerDependencies": {
  "codeby.custom-buy-box": "1.x"
}
```

Then, run the following line:

```
  vtex install codeby.custom-buy-box@1.x
```

2. Add the `custom-buy-box` block within your `store.product` or within its children elements tree. For example:

```json
{
  "store.product": {
    "children": [
      ...,
      "custom-buy-box",
      ...
    ]
  },
}
```

#### **OBS:** the block `custom-buy-box#desktop` is available, the only difference between it and the default block, is the `isDesktop` property.

## Configuration Admin panel

1. Access the app on vtex admin page:

The first initialization may take a few minutes, in order to create the entity on Masterdata V2. If the entity is already created, it will ignore or be updated, enabling the "Settings" tab.

![Admin page](admin_page.png)

2. In the Settings, you can see all the modules and colors to be customized.

If you disable one module, it will stop bein displayed into the buy box. If you change one color, all the components that use this color will be updated.

At the moment you press **SAVE**, the settings should be applied instantly. Just reload the product page and see the magic happens.

![Buy Box Settings](buybox_settings.png)

## Customization

In order to customize your buy box, it's important to know which modules are present.

First, let's see how the default buy box is created:

```json
"custom-buy-box": {
    "props": {
      "ProductName": "vtex.store-components:product-name",
      "ProductIdentifier": "product-identifier.product",
      "ProductSellingPrice": "product-selling-price",
      "ProductListPrice": "product-list-price",
      "ProductQuantity": "product-quantity",
      "SkuSelector": "sku-selector",
      "AddToCartButton": "add-to-cart-button-wrapper",
      "Subscriptions": "subscriptions-modal-wrapper",
      "PickupPoints": "shipping-custom-provider"
    }
  },
```

The main concept used on this app, is the [VTEX Slots](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-slots). We use vtex blocks and custom components as props to our buy box. In this way, you can pass any component you want, making this app very flexible.

All the properties are shown below:

```ts
interface IBuyBox {
  ProductName: () => JSX.Element
  ProductIdentifier: () => JSX.Element
  ProductSellingPrice: () => JSX.Element
  ProductListPrice: () => JSX.Element
  ProductQuantity: () => JSX.Element
  SkuSelector: () => JSX.Element
  AddToCartButton: () => JSX.Element
  Subscriptions: () => JSX.Element
  PickupPoints: () => JSX.Element
  isDesktop?: boolean
  descriptionScrollerLabel?: string
  buy_btn_query_selector?: string
  sku_selector_query_selector?: string
  subscription_btn_query_selector?: string
  subscription_info_query_selector?: string
}
```