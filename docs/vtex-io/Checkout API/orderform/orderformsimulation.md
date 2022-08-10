---
title: "Do OrderForm Simulation"
slug: "orderformsimulation"
excerpt: "The orderForm simulation endpoint is used to simulate a cart in VTEX Checkout.\r\n\r\nIt receives an **SKU ID**, the **quantity** of items in the cart, the ID of the **Seller** and the **country** in ISO ALPHA-3 Code (eg. BRA, USA, ARG).\r\n\r\nIt sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.\r\n\r\nThis is useful whenever you need to know the avaiability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data."
hidden: false
createdAt: "2020-02-05T23:27:53.590Z"
updatedAt: "2020-02-28T14:34:06.275Z"
---
**Example of request body:** 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"items\":[\n        {\n            \"id\": \"8965\",\n            \"quantity\": 3,\n            \"seller\": \"1\"\n        }\n    ],\n    \"country\": \"USA\"\n}",
      "language": "json"
    }
  ]
}
[/block]