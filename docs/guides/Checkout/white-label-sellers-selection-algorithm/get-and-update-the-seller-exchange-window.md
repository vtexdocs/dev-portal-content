---
title: "Get and update the seller exchange window"
slug: "get-and-update-the-seller-exchange-window"
hidden: true
createdAt: "2022-12-12T21:19:51.360Z"
updatedAt: "2022-12-12T21:36:31.439Z"
---
[Marketplace](https://help.vtex.com/en/tutorial/integrating-with-marketplace) is the platform where products from different sellers can be offered to customers in one place. After the customer completes a purchase and the order is created, there may be scenarios in which the original seller of the product needs to be modified, for example, when their cancels the order due to an internal unavailability of product fulfillment.

In this situation, VTEX allows the marketplace to have a period of time (window), after the customer completes the purchase, to change sellers and thus avoid an order cancellation. For more information on the process of switching sellers, access the guides in the [Help Center](https://help.vtex.com/en/tutorial/change-seller--5TBAwO2kOAMw44uyaaQMQO) and the [Developer Portal](https://developers.vtex.com/vtex-rest-api/docs/change-seller).

>⚠️ The default window for the change seller is **2 days**. However, you can modify the value for up to a maximum period of **30 days**.

This guide describes how to get a seller's current exchange window or update this value in a marketplace on your account.

## Getting the current window to change seller

To get the window to change seller in a marketplace, you need to use the [Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller) endpoint as a **GET** request. In this request, you must send the `accountname` through the URL address, as shown by the example below:

**Method: GET**

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/window-to-change-seller`

After sending the request, the endpoint will return the response body showing the maximum current period of time (days after the customer's purchase) allowed to perform the seller exchange:
[block:code]
{
  "codes": [
    {
      "code": "\"4\"",
      "language": "json"
    }
  ]
}
[/block]
## Updating the window to change seller

To update the seller's exchange window (in days), you need to use a similar request of the **Get window to change seller**, but as a **POST** request ([Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)), as shown by the example below:

**Method: POST**

`https://{accountName}.{environment.com.br}/api/checkout/pvt/configuration/window-to-change-seller`

See a request body example below (10 days):
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"waitingTime\": 10\n    }\n",
      "language": "json"
    }
  ]
}
[/block]
After sending the request, the endpoint will return `code 201 (Created)` and an empty response body. 

To confirm that the new window to change seller have been applied to your account, access the [Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller) endpoint again as a **GET** request.

## Error codes

The following errors may appear as a message in the response body.

### 401 - Unauthorized
- **Message error example (code ORD062)**: `"Unauthorized"`. The credentials (API key and API token) used in this request are incorrect or not authorized to access this type of information.
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD062\",\n        \"message\": \"Unauthorized\",\n        \"exception\": null\n    },\n    \"operationId\": \"8ec4b686-435f-42ab-8cfd-89306f888c3c\"\n}",
      "language": "json"
    }
  ]
}
[/block]
### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.
[block:code]
{
  "codes": [
    {
      "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
      "language": "json"
    }
  ]
}
[/block]