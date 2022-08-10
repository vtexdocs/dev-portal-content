---
title: "Change price"
slug: "pricechange"
excerpt: "This request changes the price of a specific item in a cart.\n\r\n\rYou need to inform which cart you are referring to, by sending its `orderFormID`; and what is the item whose price you want to change, by sending its `itemIndex`.\n\r\n\rYou also need to pass the new price value in the body.\n\r\n\rRemember that, to use this endpoint, the feature of *manual price* must be active. To check if it's active, use the [Get orderForm configuration](https://developers.vtex.com/reference#getorderformconfiguration) endpoint. To make it active, use the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) endpoint, making the `allowManualPrice` field `true`."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-02-28T14:34:06.643Z"
---
**Example of request body:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"price\": 10000\n}",
      "language": "json"
    }
  ]
}
[/block]