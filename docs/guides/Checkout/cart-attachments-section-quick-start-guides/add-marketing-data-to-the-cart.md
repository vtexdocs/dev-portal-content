---
title: "Add marketing data to the cart"
slug: "add-marketing-data-to-the-cart"
hidden: true
createdAt: "2022-11-23T19:24:49.778Z"
updatedAt: "2022-11-28T18:28:17.413Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to add marketing data information to the shopping cart by the API. For more information about UTMs, access [What are utm_source, utm_campaign, and utm_medium](https://help.vtex.com/tutorial/what-are-utm-source-utm-campaign-and-utm-medium).

## Getting shopping cart information

The first step is to get the `orderFormId` of the shopping cart you want to add the marketing data information to. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

## Adding marketing data to the shopping cart

To add marketing data to the shopping cart, you need to use the [Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata) endpoint. In this request, you must send the `orderFormId` through the URL address, as shown in the example below:

`https://{accountName}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/attachments/marketingData`

Additionally, you need to send the request body containing the following marketing data information:

- `coupon`: coupon code to be applied to the cart. Use the [cart simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation) request to check which coupons can be applied before placing the order.
- `marketingTags`: marketing tags.
- `utmSource`: source of the traffic (e.g. Facebook, Google).
- `utmMedium`: advertising or marketing media (e.g. banner, cpc).
- `utmCampaign`: campaign name (e.g. Christmas, launch, promo01).
- `utmiPage`: utmi_page (internal utm).
- `utmiPart`: utmi_part (internal utm).
- `utmiCampaign`: utmi_campaign (internal utm).

See a request body example below:

```json
{
     "coupon": "free-shipping",
     "marketingTags": [
          "tag1",
          "tag2"
     ],
     "utmSource": "Facebook",
     "utmMedium": "CPC",
     "utmCampaign": "Black friday",
     "utmiPage": "utmi_page-example",
     "utmiPart": "utmi_part-example",
     "utmiCampaign": "utmi_campaign-example"
}
```

After sending the request, the endpoint will return the response body containing the client preferences information in the shopping cart, as shown in the example below:

```json
...
"marketingData": {
        "utmSource": "Facebook",
        "utmMedium": "CPC",
        "utmCampaign": "Black friday",
        "utmipage": "utmi_page-example",
        "utmiPart": "utmi_part-exmaple",
        "utmiCampaign": "utmi_campaign-example",
        "coupon": "free-shipping",
        "marketingTags": [
            "tag1",
            "tag2"
        ]
    }
...
```

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if the item `coupon` code sent is incorrect or unavailable, the following message will appear.

```json
...
"messages": [
        {
            "code": "couponNotFound",
            "text": "Coupon 34324 invalid",
            "status": "warning",
            "fields": {}
        }
    ]
...
```

### 400 - Bad Request

- `Message error example (code ORD002): "Invalid order form"`. The `orderFormId` information is not valid.

```json
{
    "fields": {},
    "error": {
        "code": "ORD002",
        "message": "Invalid order form",
        "exception": null
    },
    "operationId": "5d9f54e6-7db4-46d6-bca9-deeb278b8b98"
}
```

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: check that the URL data is correct.

```html
<body>
	<h1>404 Not Found</h1>
	<p>The requested URL was not found on this server.</p>
</body>
```
