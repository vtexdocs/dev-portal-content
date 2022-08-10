---
title: "Tokstok PDP Components"
slug: "tokstoksponsorio-pdp-components"
excerpt: "tokstoksponsorio.pdp-components@0.67.0"
hidden: true
createdAt: "2022-07-08T06:39:59.659Z"
updatedAt: "2022-07-29T11:51:56.585Z"
---
> Tokstok components for the PDP page.

## Configuration

Add `"tokstokio.pdp-components": "0.x"` on manifest.json of store theme

```tsx
"dependencies": {
  "tokstokio.pdp-components": "0.x"
}
```

## Usage

There are several components inside this `app` that you can use declaring their `interfaces` in your `blocks` structure

### Components

**Use the `technical-information` interfaces declared [here](../store/interfaces.json)**

```tsx
  "technical-information": {
    "title": "Technical Information"
  }
```

Renders a brief technical description and observations, alongside product's measurements related information.
It must be used inside a ProductContext.

---

**Use the `assembly-information` interfaces declared [here](../store/interfaces.json)**

```tsx
  "assembly-information": {
    "title": "Assembly Information",
    "children": [...]
  }
```

Renders product assembly related information. The children field was introduced in order to be possible to inject a modal trigger to open the 'modal-layout#mount' block.
It must be used inside a ProductContext.

---

**Use the `buy-together` interfaces declared [here](../store/interfaces.json)**

```tsx
  "buy-together#pdp": {
    "title": "Frequently Bought Together - PDP"
  }
```

It renders a section showing three products, whereas the first is the main product, and the two other are distinct product recommendations frequently bought together.
It must be used inside a ProductContext.

---

**Use the `product-images-slider` interfaces declared [here](../store/interfaces.json)**

```tsx
  "product-images-slider": {
    "title": "Product Images Slider"
  }
```

Renders a slider containing the product images

---

**Use the `shipping-simulator-tokstok` interfaces declared [here](../store/interfaces.json)**

```tsx
  "shipping-simulator-tokstok": {
    "title": "Product Shipping Simulator"
  }
```

It will render an input where you can put your postal code and get the delivery options available.

---

**Use the `add-to-cart-button-modal` interfaces declared [here](../store/interfaces.json)**

```tsx
  "store.product": {
    "children": [
      "add-to-cart-button-modal",
      "flex-layout.row#product-breadcrumb",
      "responsive-layout.desktop#pdp",
      "responsive-layout.tablet#pdp",
      "responsive-layout.phone#pdp"
    ]
  }
```

This component works from a custom event on the add to cart button, providing a modal with information on accessories or lines according to the context of the product.

**Add the custom event on `add-to-cart-button`**

```tsx
   "add-to-cart-button#pdp": {
    "props": {
      "blockClass": "buyButtomProductPage",
      "text": "Comprar",
      "isOneClickBuy": false,
      "customPixelEventId": "openModalProductPage",
      "addToCartFeedback": "customEvent"
    }
  },
```

In this case the event must be added as described in this documentation.

---

**Use the `store-price` interfaces declared [here](../store/interfaces.json)**

```tsx
   "store-price": {
    "children": ["modal-trigger#see-conditions"]
  }
```

This component shows the price for pickup in the store according to sales chanel.

---