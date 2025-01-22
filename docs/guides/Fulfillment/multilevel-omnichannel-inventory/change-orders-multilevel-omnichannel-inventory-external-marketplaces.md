---
title: "Change chain orders in external marketplaces"
slug: "change-orders-multilevel-omnichannel-inventory-external-marketplaces"
hidden: false
createdAt: "2022-11-18T18:48:14.043Z"
updatedAt: "2022-11-18T18:53:14.127Z"
---

>⚠️ The [Multilevel Omnichannel Inventory (MOI)](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory) feature has been discontinued for integrations with external marketplaces. Now, MOI is available only for integrations between VTEX marketplaces and sellers. We recommend reviewing your integration strategies to align with the currently supported functionalities. For more information, please contact [VTEX support](https://help.vtex.com/en/support).

[Multilevel Omnichannel Inventory](https://developers.vtex.com/vtex-rest-api/docs/multilevel-omnichannel-inventory) is the VTEX setting that allows franchise accounts or white label sellers' inventory to be sold in marketplaces connected to the main account. This article explains how to use the [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order) while performing Multilevel Omnichannel Inventory operations in [external marketplaces](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).

By configuring this feature, your VTEX store will be able to have orders' items or prices changed when selling products that belong to a franchise account in orders made in external marketplaces. This happens due to a new endpoint is created to receive change order’s notifications sent by a VTEX seller in a Multilevel Omnichannel Inventory operation.

The image below shows how the process occurs, in more detail:

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Integration-Guides/change%20chain%20orders%20in%20multilevel%20omnichannel%20inventory%20%20marketplace.jpg)

## Implementators

The integration can be implemented by:

- **Integration partner** with the technical ability to implement integrations.
- **External marketplace** who develops an integration with a VTEX store.

This article is suitable for both cases.

>❗ The external marketplace must be responsible for the payment process, otherwise the change order in Multilevel Omnichannel Inventory chain orders in external marketplaces operations will be blocked by the Order Management System (OMS).

## Implementation steps

The feature is implemented as follows:

1. The external marketplace or partner creates an endpoint to receive notifications of order changes in Multilevel Omnichannel Inventory operations in external marketplaces, as specified in [Expected payloads](#expected-payloads). The endpoint must have a base URL followed by `/pvt/orders/{orderGroup}/changes` .

    > For example: `https://www.{{storeName}}.com.br/pvt/orders/orderGroup/changes`.

2. The external marketplace informs the base URL to VTEX's Order Management System (OMS) when a new order is placed in the external marketplace, by using the `marketplaceServicesEndpoint` field in the [Order placement](https://developers.vtex.com/vtex-rest-api/reference/order-placement) API.
3. When an order is changed in the external marketplace, the OMS uses the base URL informed through `marketplaceServicesEndpoint` and concatenates it with `/pvt/orders/{orderGroup}/changes`, so that the endpoint created in step 1 receives notifications about order changes.

>⚠️ We have considered the `OrderGroup` to build the endpoint because it follows the [Multilevel Omnichannel Inventory](https://developers.vtex.com/vtex-rest-api/docs/multilevel-omnichannel-inventory) communication standards.

## Expected payloads

The endpoint created will have a request body and a response body, as shown in the next sections.

### Request body

The payload sent to the external marketplace follows the same structure used in the [Register change on order](https://developers.vtex.com/vtex-rest-api/reference/registerchange) API. You have an example below:

```json
{
    "reason": "Some text about the change. E.g: Add item XPTO",
    "discountValue": 0,
    "incrementValue": 0,
    "itemsRemoved": [], 
    "itemsAdded": [
        {
            "sellerItemId": "8",
            "quantity": 1,
            "price": 12,
            "unitMultiplier": 1.0000,
            "measurementUnit": "un"
        }
    ]
}
```

| **Field** | **Type** | **Description** |
|:----------:|:----------:|:----------|
| `reason` | string | Text explaining why there was a change in the order. This information may be shown to the shopper in the storefront or transactional emails. |
| `discountValue` | integer | This field can be used to apply a discount to the total value of the order. Value in cents. |
| `incrementValue` | integer | This field can be used to increment the total value of the order. Value in cents. |
| `itemsAdded` | array of objects | List of items that should be added to the order. |
| `sellerItemId` | string | SKU ID of the item to be added to the order. |
| `quantity` | integer | Quantity of items to be added to the order. |
| `price` | integer | Total amount in cents of the item to be added to the order.  |
| `unitMultiplier` | integer | Unit multiplier of the item to be added to the order. |
| `measurementUnit` | string | Item's measurement unit. |
| `itemsRemoved` | array of objects | List of items that should be removed from the order. Has the same fields of `itemsAdded`. |

### Response body

The request returns two types of responses:

- **Response 200 OK:** confirmation and payload as the following example:

```json
{
"orderId": "SLR-v20918230965-01",
"receipt": "61d49ff5-eee4-4093-aba1-1560435dedb0"
}
```

| Field | Type | Description |
|---|---|---|
| `orderId` | `string` | Order ID is a unique code that identifies an order. |
| `receipt` | `string` | Hash for transaction identification or any string that uniquely identifies the transaction. |

- **Response 500 error:** message of failure and there is no payload.
