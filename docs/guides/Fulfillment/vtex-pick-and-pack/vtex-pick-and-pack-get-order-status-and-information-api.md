---
title: "VTEX Pick and Pack Get order status and information API"
slug: "vtex-pick-and-pack-get-order-status-and-information-api"
hidden: false
createdAt: "2023-04-05T17:08:52.219Z"
updatedAt: "2023-04-05T17:08:52.219Z"
excerpt: "Learn how to create webhooks and get order status and information from VTEX Pick and Pack API"
seeAlso:
 - "vtex-pick-and-pack"
hidePaginationPrevious: false
hidePaginationNext: false
---

# VTEX Pick and Pack Get order status and information API

[VTEX Pick and Pack](link) is a solution to streamline stores’ fulfillment processes by optimizing orders’ picking and packing, and the last-mile delivery. The solution is composed of the [VTEX Fulfillment](http://link) and the [Last Mile](link) modules.

This documentation explains how to make a request to the **Get order status and information** REST API to retrieve the status and details of an order in the **VTEX Pick and Pack** context. If you use this API to retrieve orders from other contexts, you will receive 404 error messages.

>⚠️The [order statuses in VTEX Pick and Pack](#order-status-in-pick-and-pack) do not correspond to the [order flow and status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) of the Order Management System (OMS).

## Before you start

Before making the request, you will need the following:



* [Basic authentication](#basic-authentication)
* [JSON Web Token (JWT)](#json-web-token-jwt)


### Basic authentication

Basic Authentication is a method for an HTTP user agent to provide a username and password when making a request. The system doesn't store API keys, they need  to be generated every time there's a new request.

Below, you will find an Api-Key for the Development environment that you can use. To find the Api-Key of the environment in Production, Admin users can generate an API Key in the users section of their Pick and Pack settings.

**Production (Prod)**

```
{{alphanumericSequence}}
```



### JSON Web Token (JWT)

JSON Web Token (JWT) is an open standard ([RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)) that defines a compact and self-contained way for securely transmitting information as a JSON object between parties. 

In order to authorize the [API request](#get-order-status-and-information-api), you will have to generate a JWT. For that, you will use the Api-Key from the previous section.

The first step is to create a token of authentication with the endpoint below. No authentication is required:


#### Endpoint


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL</strong>
   </td>
  </tr>
  <tr>
   <td>POST
   </td>
   <td>`<code>https://auth.pickingnpacking.com/prod/token</code>`
   </td>
  </tr>
</table>



#### Request body example


```
{
    "apiKey": 
"db5a3cecfef9cb0a9815af7c2eb8f7d6:c400460c165cc9beb146ad4d757e3bb1a24ff15228c424a0bd7c37f0ac356c0f6230568705d93dd6ff68190c0eafe5a74cbb14229748f20d3e53cbcc790ba372"
}
```



#### Response body example


```
{
    "message": "success",
    "data": 
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ2.eyJob4N0bmFtZSI6Im5ld2J1c2luZXNzMDEiLCJpYXQiOjE2MzM3MjE1NzksImV4cCI6MTYzMzcyMjQ3OX0.7QRZpElg1HYgyJpE6QTNgE2IN3vXbzIfulBS0Bvyzds"
}
```



#### Status codes


<table>
  <tr>
   <td><strong>Status code</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>200
   </td>
   <td>OK
   </td>
  </tr>
  <tr>
   <td>401
   </td>
   <td>Requires authentication
   </td>
  </tr>
  <tr>
   <td>400
   </td>
   <td>Bad request
   </td>
  </tr>
  <tr>
   <td>404
   </td>
   <td>Resource not found
   </td>
  </tr>
  <tr>
   <td>500
   </td>
   <td>Internal error
   </td>
  </tr>
</table>

#### Headers

After you have created the token of authentication, make the request to the endpoint once again, this time sending in the headers the following object:


```
// Headers
{
  "Authorization": "{{JWT}}"
} 
```



## Get order status and information API

In order to get the **VTEX Pick and Pack** status and details of a given order, use the endpoint below:


### Endpoint


<table>
  <tr>
   <td><strong>Method</strong>
   </td>
   <td><strong>URL</strong>
   </td>
  </tr>
  <tr>
   <td><strong>GET</strong>
   </td>
   <td><code>`https://legacy.pickingnpacking.com/prod/picking-tracking/{orderId}`</code>
   </td>
  </tr>
</table>



```
The `orderId` is the order's unique code and is the same used in OMS and all VTEX modules.
```



### Authorization

Use the authorization retrieved from the steps listed in [Before you start](#before-you-start) and insert it in the call's header. 



### Response body example


```
{
    "message": "string",
    "data": {
        "hostname": "string",
        "orderId": "string",
        "fulfillmentStatus": "string",
        "pickedItems": [
            {
            "image": "string",
            "sellingPrice": "float",
            "ean": "string",
            "quantity": "number",
            "name": "string",
            "id": "string",
            "refId": "string",
            "categories": [
                {
                "name": "string",
                "id": "string"
                }
            ]
            }
        ]
        "shipping"?: {
            "trackingId": "string",
            "trackingStatus": "string",
            "services"?: [
                {
                    "serviceId": "string",
                    "agent"?: "string",
                    "vehicle"?: "string",
                    "courier": "string",
                    "trackingUrl"?: "string",
                    "serviceStatus": "string",
                    "evidences"?: "string",
                    "createdAt": "string"
                }
            ]
        }
    }
}
```



### Status codes


<table>
  <tr>
   <td><strong>Status code</strong>
   </td>
   <td><strong>Internal response Code</strong>
   </td>
   <td><strong>Message</strong>
   </td>
  </tr>
  <tr>
   <td>200
   </td>
   <td>OK 
   </td>
   <td>OK
   </td>
  </tr>
  <tr>
   <td>401
   </td>
   <td>1000
   </td>
   <td>* | Internal server
   </td>
  </tr>
  <tr>
   <td>404
   </td>
   <td>1001
   </td>
   <td>Resource not found
   </td>
  </tr>
  <tr>
   <td>400
   </td>
   <td>1002
   </td>
   <td>OrderId is not found | Order not found by {orderId}
   </td>
  </tr>
  <tr>
   <td>500
   </td>
   <td>1003
   </td>
   <td>* | Internal error
   </td>
  </tr>
</table>



## Webhook

You will need to create a webhook to receive the response of the request, used for receiving notifications for invoicing purposes, for example. 

Your webhook may have your desired setting for URL, path, method, and authentication, it is flexible. 

The order’s information and status change notifications received will be an object like the following example:

**Example**


```
{
  "orderId": "XDE-1253881550433-01",
  "oldStatus": "PENDING",
  "newStatus": "READY_FOR_PICKING",
  "hostname": "picknpackstore"
}
```



## Order status in Pick and Pack

In the table below, you will find the possible order statuses in the **VTEX Pick and Pack** context:


<table>
  <tr>
   <td><strong>Status</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>READY_FOR_HANDLING
   </td>
   <td>An order imported from the Order Management System (OMS) that is ready to be fulfilled.
   </td>
  </tr>
  <tr>
   <td>IDLE (Inactive)
   </td>
   <td>The order was an external fulfillment, and <em>VTEX Pick and Pack</em> will not be able to process it. If the order is invoiced in OMS in a status different from `Ready for invoicing`, the system will also consider it an external fulfillment and change the order status to ` Idle`.
   </td>
  </tr>
  <tr>
   <td>READY_FOR_PICKING
   </td>
   <td>The order was assigned to a picker and is depending on the picker’s confirmation to move to the next status.
   </td>
  </tr>
  <tr>
   <td>PICKING
   </td>
   <td>The picker is collecting the order items.
   </td>
  </tr>
  <tr>
   <td>READY_FOR_PACKING
   </td>
   <td>The picker has finished the picking process and the order is ready to be packed.
   </td>
  </tr>
  <tr>
   <td>PACKING
   </td>
   <td>The order’s items are being packed.
   </td>
  </tr>
  <tr>
   <td>READY_FOR_INVOICING
   </td>
   <td>The order can be invoiced. <strong>VTEX Pick and Pack </strong>solution does not invoice orders.
   </td>
  </tr>
  <tr>
   <td>INVOICING
   </td>
   <td>The invoice is being processed.
   </td>
  </tr>
  <tr>
   <td>INVOICED
   </td>
   <td>The order was invoiced.
   </td>
  </tr>
  <tr>
   <td>PREPARING_SHIPPING
   </td>
   <td>Shipping services are being created for the order.
   </td>
  </tr>
  <tr>
   <td>READY_FOR_SHIPPING
   </td>
   <td>Once Shipping Services are created, service is awaiting carrier pickup. 
   </td>
  </tr>
  <tr>
   <td>WAITING_FOR_DELIVERY_COMPANY
   </td>
   <td>The order is packed and the shipping service was successfully created.
   </td>
  </tr>
  <tr>
   <td>ON_ROUTE
   </td>
   <td>The courier (driver) has collected the package in the physical store or <a href="https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb">warehouse</a>, for example.
   </td>
  </tr>
  <tr>
   <td>DELIVERED
   </td>
   <td>The order was delivered to the customer.
   </td>
  </tr>
  <tr>
   <td>RETURNED
   </td>
   <td>The customer couldn’t be reached or refused to receive the package, so the order was returned.
   </td>
  </tr>
  <tr>
   <td>WAITING_FOR_PICKUP
   </td>
   <td>The package is ready to be picked up by the customer at the physical store or at another <a href="https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R">pickup point</a>.
   </td>
  </tr>
  <tr>
   <td>CANCELED
   </td>
   <td>The order was canceled.
   </td>
  </tr>
</table>




>⚠️The statuses above are related to VTEX Pick and Pack only, and do not correspond to the order flow and status of the Order Management System (OMS).


