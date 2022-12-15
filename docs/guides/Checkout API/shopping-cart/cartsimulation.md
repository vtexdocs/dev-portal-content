---
title: "Cart simulation"
slug: "cartsimulation"
excerpt: "This endpoint is used to simulate a cart in VTEX Checkout.\r\n\r\nIt receives an **SKU ID**, the **quantity** of items in the cart and the ID of the **Seller**.\r\n\r\nIt sends back all information about the cart, such as the selling price of each item, rates and benefits data, payment and logistics info.\r\n\r\nThis is useful whenever you need to know the availability of fulfilling an order for a specific cart setting, since the API response will let you know the updated price, inventory and shipping data.\r\n\r\n**Important**: The fields (`sku id`, `quantity`, `seller`, `country`, `postalCode` and `geoCoordinates`) are just examples of content that you can simulate in your cart. You can add more fields to the request as per your need. Access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/checkout-api-overview) guide to check the available fields."
hidden: false
createdAt: "2022-03-23T14:22:14.645Z"
updatedAt: "2022-10-26T17:09:36.097Z"
---
