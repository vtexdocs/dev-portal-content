---
title: "Listrak"
slug: "vtex-listrak-pixel"
excerpt: "vtex.listrak-pixel@2.3.0"
hidden: false
createdAt: "2020-06-03T15:20:18.786Z"
updatedAt: "2022-10-03T18:26:48.050Z"
---
This app provides pixel integration for Listrak metrics and cart abandonment functionality, and provides related routes and blocks for use in an account's store-theme.

Additionally, if you would like the app to send Order, Product, and Customer data to Listrak, you can create a [Listrak Data Integration](#Listrak-Data-Integration).

## Configuration

1. [Install](https://vtex.io/docs/recipes/store/installing-an-app) the `listrak-pixel` app in the desired account;
2. In the account's admin, access **Apps > My Apps** and then select the **Listrak** box;
3. Once in the app's page, define the app’s configurations in the **Setup** section:

- **Merchant ID**: Input your Listrak Merchant ID here.

- **Subscription Point ID**: Input your `Subscribe ID` of the email Subscription Point from your Listrak account.

- **Subscription Form IDs**: To capture a shoppers opt-in to an email subscription, enter the field IDs associated with the subscription form email input and submit button. Enter both IDs separated with commas and no spaces like `emailInputId,submitButtonId`. **If the Newsletter block from the `vtex.store-component` is used, no entry is necessary**.

- **Email Input Field IDs**: Listrak's cart abandonment feature works in part by capturing email addresses when shoppers type them into certain fields. These field IDs can be specified here, separated with commas and no spaces like `emailField1,emailField2`.

- **Preference Center Name**: This app creates a new store route with the path `/preference-center` which displays the Listrak Preference Center. Referencing your Listrak Preference Center integration instructions, input the value for the `data-ltk-prefcenter` attribute of the Preference Center div here.

The settings below are only needed if you have created a [Listrak Data Integration](#Listrak-Data-Integration).

- **Client ID**: Your Listrak Data Integration Client ID.

- **Client Secret**: Your Listrak Data Integration Client Secret.

- **Full Catalog Import**: Send your entire product catalog to Listrak. This will happen on the first SKU update after enabling the option.

- **Use SKU Reference ID**: Send Listrak SKU reference IDs instead of VTEX SKU IDs.

- **Image Size (in pixels)**: Set dimensions for images imported to Listrak. If left blank, the default size for your store's thumbnail images wil be used, usually 100x100 pixels.

**Listrak Fields and Values (Optional)**

The following optional settings allow you to map VTEX product specifications to specific Listrak fields. If left blank, they will be filled according to the default behavior explained below:

- **Category**: Input the name of the product specification field containing the product's main category. If left blank, this will be automatically set as the first category that the product belongs to.

- **Sub Category**: Input the name of the product specification field containing the product's secondary category. If left blank, this will be automatically set as "Type/Silhouette".

- **Meta 1**: Input the name of the product specification field containing any additional data you wish to send. If left blank, this will be automatically set as a pipe-separated list of the item's unique SKU specifications.

- **Meta 2**: Input the name of the product specification field containing any additional data you wish to send. If left blank, this will be automatically set with a placeholder value of "meta_2".

- **Meta 3**: Input the name of the product specification field containing any additional data you wish to send. If left blank, this will be automatically set with a placeholder value of "meta_3".

## (Optional) On-Site Recommendation Integration Block

To use this optional block in your `store-theme`, you must add the Listrak app to your `store-theme`'s peer dependencies in `manifest.json`:

```json
"peerDependencies": {
    "vtex.listrak-pixel": "1.x"
  }
```

Then you may use this block in your layouts:

- `"listrak-recommendations"`: The Listrak app provides this block which is designed to be added to the product page (`store.product`). It renders Listrak's On-Site Recommendations product shelf. The block takes two props:

| Prop name            | Type     | Description                                                               |
| -------------------- | -------- | ------------------------------------------------------------------------- |
| `merchandiseBlockId` | `String` | The Merchandise Block ID from Listrak's admin. Default: `''`              |
| `templateHTML`       | `String` | The HTML template for the recommender from Listrak's admin. Default: `''` |

:warning: Both props must be filled for the component to render.

Example - Listrak provides sample template code that looks like this:

```html
<div
  data-ltk-merchandiseblock="sample-merchandise-block-id"
  style="width:100%; padding:40px 0;"
>
  <script type="text/html">
    <div style="box-sizing:border-box; vertical-align:top; display:inline-block; width:25%; padding:20px;">
        <a href="@Recommendation.LinkUrl"><img src="@Recommendation.ImageUrl" title="@Recommendation.Title" style="display:block; width:auto; height: 100%; max-height:200px; margin:auto;"/></a>
        <a href="@Recommendation.LinkUrl" title="@Recommendation.Title" style="display:block; width:100%; font-family:Segoe UI,Roboto,Helvetica Neue,sans-serif; font-size: 15px; font-weight: 500; color:#333;text-decoration:none; text-align:center; padding-top:8px;">@Recommendation.Title</a>
        <a href="@Recommendation.LinkUrl" title="@Recommendation.Title" style="display:block; width:100%; font-family:Segoe UI,Roboto,Helvetica Neue,sans-serif; font-size: 13px; font-weight: 700; color:#d43e3e; text-decoration:none; text-align:center; padding-top:8px;">$@Recommendation.Price</a>
    </div>
  </script>
</div>
```

In this case, your block's props would look like this:

```json
"listrak-recommendations#example": {
    "props": {
        "merchandiseBlockId": "sample-merchandise-block-id",
        "templateHTML": "<div style='box-sizing:border-box; vertical-align:top; display:inline-block; width:25%; padding:20px;'><a href='@(window.location.origin + Recommendation.LinkUrl)'><img src='@Recommendation.ImageUrl' title='@Recommendation.Title' style='display:block; width:auto; height: 100%; max-height:200px; margin:auto;'/></a><a href='@(window.location.origin + Recommendation.LinkUrl)' title='@Recommendation.Title' style='display:block; width:100%; font-family:Segoe UI,Roboto,Helvetica Neue,sans-serif; font-size: 15px; font-weight: 500; color:#333;text-decoration:none; text-align:center; padding-top:8px;'>@Recommendation.Title</a><a href='@(window.location.origin + Recommendation.LinkUrl)' title='@Recommendation.Title' style='display:block; width:100%; font-family:Segoe UI,Roboto,Helvetica Neue,sans-serif; font-size: 13px; font-weight: 700; color:#d43e3e; text-decoration:none; text-align:center; padding-top:8px;'>$@Recommendation.Price</a></div>"
    }
},
```

:warning: Note that the HTML has all been combined into a single line, and double quotes `"` replaced with single quotes `'`.

:warning: Also note that each `@Recommendation.LinkUrl` has been replaced with `@(window.location.origin + Recommendation.LinkUrl)`. This is because the `LinkUrl` stored for each product in Listrak is a relative URL. `ImageUrl` does NOT need this same treatment because each `ImageUrl` is already an absolute URL.

## Checkout Integration

To finalize a Listrak integration, custom JS code must be added to checkout in the `checkout6-custom.js` file:

```js
// Listrak
$(document).ready(function() {
  var prevItems = []
  $(window).on('orderFormUpdated.vtex', function(evt, orderForm) {
    ;(function() {
      if (typeof _ltk == 'object') {
        ltkCode()
      } else {
        ;(function(d) {
          if (document.addEventListener)
            document.addEventListener('ltkAsyncListener', d)
          else {
            e = document.documentElement
            e.ltkAsyncProperty = 0
            e.attachEvent('onpropertychange', function(e) {
              if (e.propertyName == 'ltkAsyncProperty') {
                d()
              }
            })
          }
        })(function() {
          ltkCode()
        })
      }
      function ltkCode() {
        _ltk_util.ready(function() {
          _ltk.SCA.CaptureEmail('client-pre-email')
          if (JSON.stringify(orderForm.items) != JSON.stringify(prevItems)) {
            if (orderForm.items.length > 0) {
              orderForm.items.forEach(item => {
                _ltk.SCA.AddItemWithLinks(
                  item.id,
                  item.quantity,
                  (item.price / 100).toString(),
                  item.name,
                  item.imageUrl,
                  item.detailUrl
                )
              })
              _ltk.SCA.Submit()
            } else {
              _ltk.SCA.ClearCart()
            }
            prevItems = orderForm.items
          }
        })
      }
    })()
  })
})
var biJsHost = 'https:' == document.location.protocol ? 'https://' : 'http://'
;(function(d, s, id, tid, vid) {
  var js,
    ljs = d.getElementsByTagName(s)[0]
  if (d.getElementById(id)) return
  js = d.createElement(s)
  js.id = id
  js.src =
    biJsHost + 'cdn.listrakbi.com/scripts/script.js?m=' + tid + '&v=' + vid
  ljs.parentNode.insertBefore(js, ljs)
})(document, 'script', 'ltkSDK', 'LISTRAK-MERCHANT-ID', '1')
// end Listrak
```

:warning: Make sure to replace `'LISTRAK-MERCHANT-ID'` in the second-to-last line with your Listrak Merchant ID. No other customizations are needed.

## Listrak Data Integration

Enabling this feature will send additional Order, Customer, and Product data to listrak.

- Orders data is sent when an order has been invoiced and/or updated if canceled.
- Customer data is sent when the order is invoiced.
- Product data is sent when a SKU has been created or updated.

To provide additional data to Listrak, you will need to create a new integration from the Listrak application and allow access to the Listrak API. Listrak provides some instructions [here](https://api.listrak.com/data#section/INTEGRATION-SETUP).

**Access Levels**

The app supports sending Order, Customer, and Product data and will need these access levels selected.

**IP Address Whitelist**

There are three possible IPs the app may use to send data to the Listrak API, these will need to be added to the integration's whitelist.

- 34.199.112.14
- 107.23.210.212
- 52.73.206.45

## Customization

In order to apply CSS customizations to this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles       |
| ----------------- |
| `recommendations` |