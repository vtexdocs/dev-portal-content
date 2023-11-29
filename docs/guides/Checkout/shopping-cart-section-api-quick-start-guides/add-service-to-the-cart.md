---
title: "Add a service (offering) to a shopping cart"
slug: "add-service-to-the-cart"
hidden: false
createdAt: ""
updatedAt: ""
excerpt: "{Insert a synopsis of your article here}"
seeAlso:
 - ""
hidePaginationPrevious: false
hidePaginationNext: false
---
## Add a service (offering) to a shopping cart

A service, also known as offering, is an item that may come with a product, optionally and with an additional cost. It is used to assign a value of an additional service to an SKU, as a gift packaging. 

You can add a service (offering) to a shopping cart by using the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api). To do so, follow the sections below.

### Checking if a cart product has a service attached to it

First, you must check if a product has a service available attached to it. This way, you know the options of service you can add to the item in the shopping cart.

You must use the [Cart simulation](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation?endpoint=post-/api/checkout/pub/orderForms/simulation) endpoint and send the `skuId`, `seller` and `quantity` in the request body, as the code example below.

```json
    "items": [
        {
            "id": "30",
            "quantity": 1,
            "seller": "1"
        }
    ]
```

In the response body, you must check if the `offerings` object presents the following information:

```json
    "offerings": [
        {
            "type": "Removal of additional old appliance",
            "id": "1",
            "name": "Removal of additional old appliance",
            "allowGiftMessage": false,
            "attachmentOfferings": ["Name", "Info"],
            "price": 2999
        }
    ]
```

If the `offerings` array presents this information, the product has a service associated with it. You will use the `id` value in the next step.

>ℹ️ If you have multiple services associated with the product, all of them will be returned in the `offerings` array. 

### Adding a service to a product

You can add a service to an item in the shopping cart by using the checkout [`orderForm`](https://developers.vtex.com/docs/guides/orderform-fields).

To do so, you must add the item to the cart using the [Add cart items](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/items) endpoint. 

Then, you must send the service `id` from the previous step in the desired `item` by using the request body of the 
`POST` `https://{accountName}.{enviroument}.com/api/checkout/pub/orderForm/{orderFormId}/items/{itemPosition}/offerings` request:

```json
{
    "id": "1"
}
```

The expected response is the `orderForm` structure with the `offerings` array with the service information inside it, as the code below:

```json
    "offerings": [
        {
            "type": "Removal of additional old appliance",
            "id": "1",
            "name": "Removal of additional old appliance",
            "allowGiftMessage": false,
            "attachmentOfferings": ["Name", "Info"],
            "price": 2999
        }
    ]
```

### Removing a service (offering) from a shopping cart

In order to remove a service (offering), you must use the `POST` `https://{accountName}.{enviroument}.com/api/checkout/pub/orderForm/{orderFormId}/items/{itemPosition}/offerings/remove` endpoint with the service `id` in the request body:

```json
    {
    "id": "1" 
    }
```

The expected response is the `orderForm` structure with the `offerings` array empty, like the example below:

```json
    "offerings": []
```

