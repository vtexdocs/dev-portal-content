---
title: "Pricing Hub - Overview"
slug: "pricing-hub-overview"
hidden: true
createdAt: "2021-10-25T18:44:02.713Z"
updatedAt: "2022-06-13T16:06:15.138Z"
---

[block:callout]
{
  "type": "info",
  "body": "This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests)."
}
[/block]
In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.

In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.
![Pricing hub protocal diagram](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/pricing-hub-overview-0.png)

## Implementation

To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:

- [C# template](https://github.com/vtex-apps/external-prices-app)
- [Node template](https://github.com/vtex-apps/external-prices-node)

Read the documentation on each repository to learn more about the required steps to use and customize the app.

## Specifications

See below all the specifications of the request and the response expected when communicating with Pricing Hub.

### Price calculation request

The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/vtex-rest-api/reference/post_api-pricing-hub-prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.
[block:callout]
{
  "type": "warning",
  "title": "Warning",
  "body": "Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds."
}
[/block]
In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.

#### Request body example

```json
{
    "item": 
        {
            "index": 0,
            "skuId": "880011",
            "quantity": 1
        },
    "context":{
        "email": "john@email.com"
    }
}
```

The request body should have the following properties:

| **Attribute** | **Type** | **Description**                                                                                                                                                                                          |
|---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |
| ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |
| ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |
| ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |
| `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |
| ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |

### External prices provider response

In response to the request sent by Pricing Hub, we expect an outcome in the following format:

```json
{
    "item": {
        "price": 54035,
        "priceTables": "special",
        "index": 0,
        "skuId": "880011",
        "listPrice": 54035,
        "costPrice": 50000,
        "sellingPrice": 54035,
        "priceValidUntil": "2023-01-27T20:29:57Z",
        "tradePolicyId": "special"
    }
}
```

The response should have the following properties:

| **Attribute**       | **Type** | **Description**                                                                                                                                        |
|---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `item`              | object   | The object that contains the price data.                                                                                                               |
| ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |
| ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |
| ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |
| ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |
| ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |
| ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |
| ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |
| ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |
| ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |

## Index - Pricing Hub API

<span class="APIMethod APIMethod_fixedWidth APIMethod_post" data-testid="http-method">post</span> [Get Prices](https://developers.vtex.com/vtex-rest-api/reference/post_api-pricing-hub-prices)
<span class="APIMethod APIMethod_fixedWidth APIMethod_put" data-testid="http-method">put</span> [Configure External Price Source](https://developers.vtex.com/vtex-rest-api/reference/configexternalpricesource)
