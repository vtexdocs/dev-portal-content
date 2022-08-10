---
title: "CUSTOM PRODUCT FLAGS"
slug: "micocacola-custom-product-flags"
excerpt: "micocacola.custom-product-flags@0.0.10"
hidden: true
createdAt: "2022-07-29T18:39:19.547Z"
updatedAt: "2022-07-29T18:39:19.547Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

It shows the flags of % discount, "New" and "refill" or "starter" in each of the PLP products.

![Media Placeholder](./custom-products-flags.jpg)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-product-flags",
  .
  .
  .
}
```
2. Login to your vtex account:
```
> vtex login <development-environment>
```
3. Select your workspace and use `vtex link`:
```
> vtex use <workspace>
> vtex link
```

## Block ⚙
1. Adding the app as a theme dependency in the `manifest.json` file:
```
<your-vendor>.custom-product-flags: "0.x"
```
2. Create a new file named `<your-vendor>.custom-product-flags.css` in the css folder and add the following basic styles (optional).
```
.container {
    background-color: white;
  }
  
  .discountContainer {
    width: 10%;
    position: relative;
    z-index: 1;
  }
  
  .refillStarterContainer {
    width: 15%;
    position: relative;
    z-index: 3;
  }
  
  .newContainer {
    width: 10%;
    position: relative;
    z-index: 2;
  }
  
  .flag {
    color: white;
    font-weight: 500;
    line-height: 1rem;
    text-align: right;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    justify-content: flex-end;
    align-items: center;
    -ms-flex-line-pack: stretch;
    align-content: flex-end;
    position: absolute;
    padding: 15px;
    top: 0;
    left: 0;
    height: fit-content;
    width: fit-content;
    border-radius: unset;
    border-bottom-right-radius: 50%;
    margin-top: -24px;
    margin-left: -24px;
  }
  
  .flag--discount {
    font-size: 1rem;
    background-color: #F40009;
  }
  
  .flag--starterkits {
    background-image: url(/arquivos/flag-desktop-si-envase.png); /*URL de img para starterkits*/
    background-size: 100%;
    height: 70px;
    width: 90px;
    background-repeat: no-repeat;
    background-color: #2CAD19;
  }
  
  .flag--refill {
    background-image: url(/arquivos/flag-desktop-n-envase.png); /*URL de img para Refill*/
    background-size: 100%;
    height: 65px;
    width: 80px;
    background-repeat: no-repeat;
    background-color: #F40009;
  }
  
  .flag--new {
    background-color: #F40009;
    width: 65px;
    height: 60px;
    font-size: 0.789rem;
    padding: 20px;
  }  
 
```

3. Declare the main application block at the top of `"product-summary.shelf"`. For example:

```
{
   "product-summary.shelf": {
    "children": [
      "custom-product-flags",
      .
      .
      .
      .
    ]
  },
}
```
## Modus Operandi

The app uses useProduct from 'vtex.product-context' to obtain the data of each of the products listed in the PLP.

In this way we can determine which flag corresponds to each product.

- Discount %: Inspecting the data returned by `useProduct`, we take the `selectedItem` attribute as a base to arrive at `commertialOffer` which contains the current price and the price without discount. In this way the necessary calculations are made and we return a `string` with the corresponding value. If there is no discount, the flag is not shown.

- Refill or Starterkits, NEW: Inspecting the data returned by `useProduct`, we take as a basis the `product` property up to `productClusters` which contains the id of the collections to which that product belongs (It is important to take into account the collections of the CMS to show a flag in certain products and not in others).

### Priority system: 
To determine which flag should be displayed over others, z-index is used.

- Refill or starter: 3.
- New: 2.
- % discount: 1.

** refill or starterkits first, then new and finally the discount. **

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `discountContainer` |
| `refillStarterContainer` |
| `newContainer` |
| `flag` |
| `flag--discount` |
| `flag--starterkits` |
| `flag--refill` |
| `flag--new` |

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**