---
title: "Change seller"
slug: "change-seller"
hidden: false
createdAt: "2021-07-29T19:25:33.532Z"
updatedAt: "2022-08-30T18:13:03.813Z"
---
Marketplaces have the autonomy to change a seller that has been designated to fulfill an order. This can only be done under specific circumstances described in this [article on the Change seller feature](https://help.vtex.com/en/tutorial/how-to-use-the-change-seller--5TBAwO2kOAMw44uyaaQMQO#).

There are a few different APIs that can be useful to execute a seller change. Here we will see which are they and how to use them to perform this task.

>❗ Make sure you are aware of the limitations for using this, as described in this [article on the Change Seller feature](https://help.vtex.com/en/tutorial/como-utilizar-change-seller--5TBAwO2kOAMw44uyaaQMQO#). Also, note that this can only be done while the order's status is `window-to-change-seller`, `payment-pending` or `waiting-for-authorization` as seen on the API.

## Seller listing

In the case of a seller change, the marketplace is responsible for choosing the new seller. VTEX does not have any automated system to make this choice, but we do suggest you use the [Get seller list API request](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/sellers) to see the list of sellers associated with your marketplace. It is also possible to filter sellers returned by this call using query params.


## Cart simulation

With the information of the sellers in hand, you can simulate carts to check the availability of the products. To do this, you may use our [Fulfillment simulation endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation?endpoint=post-/api/checkout/pub/orderForms/simulation).


## Window to change seller

When a seller cancels an order, the marketplace has a limited period of time to choose a new seller to fulfill that order. This period of time is the window to change seller, and the default is of two days.

This value can be checked using the [Get window to change seller request](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/checkout/pvt/configuration/window-to-change-seller) and configured with the [Update window to change seller endpoint](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/checkout/pvt/configuration/window-to-change-seller).


## Change seller

Once you have all the information you need and are ready to actually change the seller responsible for shipping a given order, you can make a `PUT` call to this endpoint:
`{marketplace_host}/api/checkout/pvt/orders/{marketplace_order_id}/sellers`

This is an example of what the body of this request should look like:
```json
{
  "marketplacePaymentValue": 1000,
  "newSellerId":"{id_do_seller_no_mkt}",
  "shippingData":
  {
    "logisticsInfo":
    [
      {
        "itemIndex": 0,
        "selectedSla": "PAC",
        "selectedDeliveryChannel": "delivery"
      }
    ]
  }
}
```

>❗ When a change of seller is successfully completed, the marketplace order loses courier information, since the array in `shippingData.logisticsInfo.deliveryIds` is now empty. In order to get the updated information, it is necessary to make a [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) request to the new seller's endpoint, such as `https://{newSeller}.{environment}.com.br/api/oms/pvt/orders/{orderId}`.