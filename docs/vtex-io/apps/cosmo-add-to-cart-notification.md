---
title: "ADD TO CART NOTIFICATION/CONFIRMATION MODAL FOR COSMO MUSIC"
slug: "cosmo-add-to-cart-notification"
excerpt: "cosmo.add-to-cart-notification@0.0.3"
hidden: true
createdAt: "2022-07-18T15:27:14.283Z"
updatedAt: "2022-07-18T15:27:14.283Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

This is an application that once the product is added to the cart, a modal is displayed indicating to the user that he/she can continue to checkout or continue shopping.
The app also allows you to increase the number of items you want to buy, remove items & continue to checkout right away from the modal. 

<p align="center">
  <img src="https://user-images.githubusercontent.com/46954736/137529172-2376ce62-3f62-454a-950a-1cb6ecda51d1.gif">
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/46954736/137526517-ff052bda-b0a6-4114-bcee-668a5447c7af.png" >
</p>

## Functionality 

The app uses several functions from the **useOrderForm**, **useOrderItems** & the **useCheckoutURL** hooks. One of the main functionalities is the addItem function, which is responsible of adding new items in the sohopping cart and it's shared in both the [Custom Add to Cart Button](https://github.com/ITGlobers/cosmo-custom-add-to-cart-button) and this Notification Modal 

<p align="center">
  <img width="520" alt="index tsx" src="https://user-images.githubusercontent.com/46954736/137530279-c63a211c-212f-4e5a-9b8b-c7ba0943cf32.png"
</p>
  
## Configuration 

1. Import the `cosmo.add-to-cart-notificaton` to your theme's dependencies in the `manifest.json;`
  <br />
  
  ```
  "dependencies": {
    "cosmo.add-to-cart-notificaton": "0.x"
  }
  ```
  
2. Add the cosmo.add-to-cart-notificaton block in any template from your theme. E.g:
  
  ```
   "flex-layout.row#notification-cart": {
      "title": "Container",
      "props": {
      "blockClass": "notification-add-cart-container"
     },
    "children": ["add-to-cart-notification"]
    },
    "add-to-cart-notification": {
    "children": ["flex-layout.row#product-stock-modal"]
  }
  ```

## Customization

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

  
| CSS Handles |
| ---------------------- | 
|  `product`             | 
|  `message__type`       | 
| `message__icon`        |
|  `notification__banner`| 
| `modal__title`         | 
|  `number__itemsLink`   | 
|  `product__info`       | 
|  `product__image`      | 
|  `product__imageItem`  | 
|  `product__data`       | 
| `product__name`        | 
| `product__sku`         | 
|   `product__qtyInput`  | 
|  `item__optionQty`     | 
|  `product__itemOptions`| 
|  `item__option`        |  
|  `cart__price`         | 
|  `item__input`         | 
|  `item__removeDesk`    | 
|  `item__removePhone`   | 
|  `checkout`            | 
| `checkout__subtotal`     | 
| `checkout__subtotalprice`| 
| `continueCart__buttons`  | 
|  `continueButton`        | 
|  `checkout__button`      | 

<!-- DOCS-IGNORE:start -->

## Contributors ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->

---- 

Check out some documentation models that are already live: 
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)