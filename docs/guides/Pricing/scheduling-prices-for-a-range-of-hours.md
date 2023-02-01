---
title: "Scheduling prices for a range of hours"
slug: "scheduling-prices-for-a-range-of-hours"
hidden: false
createdAt: "2022-08-01T20:20:15.152Z"
updatedAt: "2022-08-01T20:21:34.453Z"
---
One of the most important actions in massive events such as Black Friday is establishing prices during a limited period of time. Scheduling a price for a specific time range allows you to temporarily optimize a product’s profitability during promotional actions and switch back to the regular price automatically given an end date.

This is possible using [Pricing API](https://developers.vtex.com/docs/api-reference/pricing-api#overview), more specifically by making a request to `PUT` [Create or Update Base Price or Fixed Prices](https://developers.vtex.com/vtex-rest-api/reference/createupdatepriceorfixedprice).

In the request body, you should include the `fixedPrices` object containing a `dateRange` object, with `from` and `to` properties. Make sure to check out the [request body example](#request-body-example) and include all properties as specified in the `PUT`  [Create or Update Base Price or Fixed Prices](https://developers.vtex.com/vtex-rest-api/reference/createupdatepriceorfixedprice) documentation.  

By default, dates are in Coordinated Universal Time (UTC) and they must follow the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format. Example: `"2017-06-23T03:00:00Z"`.

[block:callout]
{
  "type": "warning",
  "body": "In case a price is changed through the VTEX Admin, the scheduled hour will be lost and only the date will be considered."
}
[/block]

## Request body example


```json
{
    "markup": 30,
    "basePrice": 100,
    "listPrice": 35,
    "fixedPrices": [
        {
            "tradePolicyId": "1",
            "value": 31,
            "listPrice": 32,
            "minQuantity": 1,
            "dateRange": {
                "from": "2022-05-21T22:00:00Z",
                "to": "2022-05-21T23:00:00Z"
            }
        },
        {
            "tradePolicyId": "1",
            "value": 31.5,
            "listPrice": 33,
            "minQuantity": 2
        }
    ]
}
```