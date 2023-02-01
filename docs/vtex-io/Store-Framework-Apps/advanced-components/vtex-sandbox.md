---
title: "VTEX IO Sandbox Component"
slug: "vtex-sandbox"
hidden: false
createdAt: "2020-06-03T15:19:48.424Z"
updatedAt: "2021-05-17T18:10:54.116Z"
---

Allows mounting arbitrary HTML content in extension points from the comfort and safety of an iframe.

### Example block

```json
  "sandbox.product": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<script src='https://unpkg.com/jquery@3.3.1/dist/jquery.min.js'></script><h1 id='test'>initial</h1><script>function render(){ current = window.props.productQuery.product.items.findIndex(function(p){ return p.itemId === window.props.query.skuId }); if (current === -1) {current = 0}; $('#test').html(window.props.productQuery.product.items[current].sellers[0].commertialOffer.ListPrice)}; window.addEventListener('message', function(e){ console.log('got message in product', e.data, window.props); render();});</script>",
      "allowCookies": true
    }
  },
  "sandbox.order": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<script>console.log('Current orderForm: ', window.props.orderForm)</script>",
      "allowCookies": true
    }
  },
  "sandbox#home": {
    "props": {
      "width": "200px",
      "height": "60px",
      "initialContent": "<h1 id='test'>home</h1><script>console.log(props, document.cookie); window.addEventListener('message', function(e){ console.log('got message in home', window.props) });</script>",
      "allowCookies": true
    }
  },
  "store.home": {
    "blocks": ["carousel#home", "shelf#home", "sandbox#home"]
  },
  "store.product": {
    "blocks": [
      "product-details#default",
      "sandbox#product"
    ]
  },
```
